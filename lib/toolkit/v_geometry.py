"""Geometry checkers of the validation suite.
  interference(P, scope, ...)   GEO-010 a moving node overlaps another node of the same element at rest
                                GEO-020 two element instances occupy the same space (assembly checker / fit checker on real solids)
  motion(P, scope, ...)         MOT-010 a moving node (with what it carries and what follows it) hits something inside its range
  follow_contact(P, scope)      MOT-020 a motion.csv "follow" leader never meets its follower within its range ("linked" + reason)
  screw_stroke(P, scope)        MOT-030 a clamping screw's stroke (turns x lead) closes its clamp's window down to the smallest conductor
  bodies(P, scope)              GEO-070 the element's fixed solids form one connected body (escape group 9)
Declared contacts (lib/contacts.csv: scope, a, b, kind, reason, by) are intended overlaps: a pin in its socket, a clip on its rail.
Followers come from BOM parents (an operator whose parent is door-r swings with door-r) and lib/motion.csv (leader, follower, mode,
stop): the contactor's carrier follows the armature, its poles follow the carrier and stop at 2.0."""
import csv, fnmatch, os
import math
import numpy as np
from .solid import Scene, rotation, node_of
from . import library

VMIN, TMIN = 1.0, 0.2          # an overlap counts above 1 mm3 and 0.2 mm thick (smaller is modelling contact)
MOVING = ("rotate", "translate")
STEPS = [k / 8 for k in range(1, 9)]
TOUCH = 0.25                   # MOT-020: parts this close at rest touch (a pulled follower fixed to its leader); above EPS and H_MIN
BISECT = 6                     # refine the first blocked step to 1/512 of the range

def _csv(name):
    p = os.path.join(library.ROOT, name)
    return [r for r in csv.DictReader(open(p, encoding="utf-8")) if r.get("scope") and not r["scope"].startswith("#")] if os.path.isfile(p) else []

def contacts(scope):
    return [r for r in _csv("contacts.csv") if fnmatch.fnmatch(scope, r["scope"])]

def _declared(rows, a, b):
    """a, b: 'name|material'; a pattern matches either the name or name|material"""
    def m(x, pat): return fnmatch.fnmatch(x, pat) or fnmatch.fnmatch(x.split("|", 1)[0], pat)
    for r in rows:
        if (m(a, r["a"]) and m(b, r["b"])) or (m(b, r["a"]) and m(a, r["b"])): return r
    return None
def _unused(rows, a, b):
    for r in rows:
        if (fnmatch.fnmatch(a, r["a"]) and fnmatch.fnmatch(b, r["b"])) or (fnmatch.fnmatch(b, r["a"]) and fnmatch.fnmatch(a, r["b"])): return r
    return None

def _top(S, i):
    o = S.owner_of[i]; return o.split(".", 1)[0] if o else ""

def _moving_nodes(P):
    return {n for n, pv in P.pivots.items() if pv["kind"] in MOVING and pv["range"][0] != pv["range"][1]}

def _part_nodes(P):
    """nodes that are separate parts (move, or are fixed named parts such as a case or a back panel); ports and lamps sit in their hosts"""
    return _moving_nodes(P) | {n for n, pv in P.pivots.items() if pv["kind"] == "fixed"}

def _fmt(lo, hi): return "x {:.0f}…{:.0f} y {:.0f}…{:.0f} z {:.0f}…{:.0f}".format(lo[0], hi[0], lo[1], hi[1], lo[2], hi[2])

def interference(P, scope, rest=None):
    """findings [(status, rule, where, message)] for overlaps at the pose built; `rest` collects the overlapping pairs (for motion)"""
    S = Scene(P); mv = _part_nodes(P); decl = contacts(scope); agg = {}; accepted = set()
    for i, j in S.candidates(S.idx):
        ti, tj = _top(S, i), _top(S, j)
        if ti != tj: rule = "GEO-020"
        elif ti == "" and S.node(i) != S.node(j) and (S.node(i) in mv or S.node(j) in mv): rule = "GEO-010"
        else: continue
        a, b = sorted((S.name(i), S.name(j)))
        ov = S.overlap(i, j)
        if not ov or ov["volume"] < VMIN or ov["thickness"] < TMIN: continue
        if _declared(decl, f"{a}|{S.material(i) if S.name(i) == a else S.material(j)}", f"{b}|{S.material(j) if S.name(j) == b else S.material(i)}"): accepted.add((a, b)); continue
        if rest is not None: rest.add((i, j)); rest.add((j, i))
        g = agg.setdefault((rule, a, b), dict(volume=0.0, thickness=0.0, lo=ov["lo"], hi=ov["hi"], n=0, step=0.0, mats=set()))
        g["volume"] += ov["volume"]; g["thickness"] = max(g["thickness"], ov["thickness"]); g["n"] += 1; g["step"] = max(g["step"], ov["step"])
        g["lo"] = np.minimum(g["lo"], ov["lo"]); g["hi"] = np.maximum(g["hi"], ov["hi"]); g["mats"] |= {S.material(i), S.material(j)}
    out = []
    for (rule, a, b), g in sorted(agg.items(), key=lambda kv: -kv[1]["volume"]):
        what = "moving node overlaps at rest" if rule == "GEO-010" else "instances overlap"
        out.append(("FAIL", rule, f"{a} × {b}", f"{what}: {g['volume']:.1f} mm³, {g['thickness']:.1f} mm deep at {_fmt(g['lo'], g['hi'])}"
                    + (f" (grid {g['step']:.2f} mm)" if g["step"] else "")))
    if accepted: out.append(("PASS", "GEO-030", scope, f"{len(accepted)} declared contact pair(s) accepted (contacts.csv)"))
    if not agg: out.append(("PASS", "GEO-020", scope, f"no interference among {len(S.idx)} solids"))
    return out

def _followers(P, S, scope, parents):
    """leader node -> list of (selector, mode, stop): selector is ('node', name) or ('owner', tag)"""
    rows = [r for r in _csv("motion.csv") if fnmatch.fnmatch(scope, r["scope"])]
    excl = {(r["leader"], r["follower"]) for r in rows if r["mode"] == "exclude"}
    F = {}
    for tag, parent in parents.items():
        if parent in P.pivots and (parent, tag) not in excl: F.setdefault(parent, []).append(("owner", tag, "follow", None))
    for r in rows:
        if r["mode"] in ("exclude", "requires"): continue           # requires: an interlock, read by _requires, not a follower
        sel = ("node", r["follower"]) if r["follower"] in P.pivots or any(node_of(L) == r["follower"] for L, _, _ in P) else ("owner", r["follower"])
        F.setdefault(r["leader"], []).append((*sel, r["mode"], float(r["stop"]) if r.get("stop") else None))
    return F

def _requires(scope, rows=None):
    """node -> [(leader, value)]: the node moves only while `leader` is held at `value` (motion.csv mode "requires"; request
    elec-6, 2026-11-08: relay-ice-cube-2co's lock-down slider closes only over the pressed test button). MOT-010 sweeps the node with
    each such leader, and what follows it, held there; the leader's own sweep is unchanged."""
    R = {}
    for r in (_csv("motion.csv") if rows is None else rows):
        if r["mode"] == "requires" and fnmatch.fnmatch(scope, r["scope"]): R.setdefault(r["follower"], []).append((r["leader"], float(r["stop"] or 0)))
    return R

def motion(P, scope, parents=None, level="element", rows=None):
    """sweep every moving pivot through its range; at assembly level only hits on other instances count. rows: motion.csv rows
    for the interlocks (the selftest's planted cases); None reads lib/motion.csv."""
    S = Scene(P); rest = set(); interference_pairs = interference(P, scope, rest)   # noqa: overlaps at rest are not motion findings
    F = _followers(P, S, scope, {**getattr(P, "parents", {}), **(parents or {})}); decl = contacts(scope); out = []
    by_node = {}; by_owner = {}
    for i in S.idx:
        n = S.node(i)
        if n: by_node.setdefault(n, []).append(i)
        o = S.owner_of[i]
        while o:
            by_owner.setdefault(o, []).append(i); o = o.rsplit(".", 1)[0] if "." in o else ""
    soft = {n for n, pv in P.pivots.items() if pv["kind"] == "compress"}
    driven = {sel for lst in F.values() for kind, sel, *_ in lst if kind == "node"}      # a follower moves only with its leader
    swept = 0; REQ = _requires(scope, rows); alone = []
    def _group(leader, pv):
        """the moving group of a leader: (solid indices, pivot, how its value follows the leader's), the leader first"""
        group = [(by_node[leader], pv, "lead", None)]; seen = {leader}; queue = [leader]
        while queue:
            ld = queue.pop()
            for kind, sel, mode, stop in F.get(ld, []):
                if sel in seen: continue
                seen.add(sel)
                if kind == "node": idx = by_node.get(sel, []); fpv = P.pivots.get(sel, pv)
                else: idx = by_owner.get(sel) or by_node.get(sel, []); fpv = None   # request mech-6: an own part declared on a moving
                # part (P.parents["roll"] = "arm", the export hierarchy the twin already reads) is carried rigidly; its own pivot
                # is still swept on its own (an "owner" selector is never `driven`), at its carrier's rest pose
                idx = [i for i in idx if S.node(i) not in soft]
                group.append((idx, fpv, mode, stop)); queue.append(sel)
        return group
    def _apply(group, pv, v, f, entry=None):
        """move a group to its leader's value v (fraction f of the way to the range end being swept)"""
        for k_, (idx, fpv, mode, stop) in enumerate(group):
            if entry is not None:
                for i_ in idx: entry.setdefault(i_, k_)
            if fpv is None or fpv is pv or mode == "lead": p_, val = pv, v                       # rigid with the leader
            else:
                p_ = fpv; b0, b1 = (float(x) for x in fpv["range"]); end = b1 if abs(b1) >= abs(b0) else b0
                val = v if (fpv["unit"] == pv["unit"] and mode != "ratio") else f * end      # ratio: the follower's own full range over the leader's
                lim = stop if stop is not None else max(abs(b0), abs(b1)); val = float(np.sign(val) * min(abs(val), lim))
            if p_["kind"] == "rotate":
                R = rotation(p_["axis"], val); o = np.array(p_["origin"]); t = o - R @ o
            else: R = np.eye(3); t = np.array(p_["axis"], float) / np.linalg.norm(p_["axis"]) * val
            S.move(idx, R, t)
    for leader, pv in P.pivots.items():
        if pv["kind"] not in MOVING or pv["range"][0] == pv["range"][1] or leader not in by_node or leader in driven: continue
        r0, r1 = (float(v) for v in pv["range"])
        group = _group(leader, pv)
        # an interlock (motion.csv "requires"): the leaders this node needs, held at their value with what follows them
        held = [(_group(ld, P.pivots[ld]), P.pivots[ld], val) for ld, val in REQ.get(leader, []) if ld in P.pivots and ld in by_node]
        held_idx = {i for g, *_ in held for idx, *_ in g for i in idx}
        movers = {i for idx, *_ in group for i in idx}
        if level == "assembly": tl = _top(S, by_node[leader][0]); static = [i for i in S.idx if i not in movers and _top(S, i) != tl and S.node(i) not in soft]
        else: static = [i for i in S.idx if i not in movers and S.node(i) not in soft]
        swept += 1
        def pose(v, f):
            """move the group to leader value v (fraction f of the way to the range end being swept); first hit or None.
            Movers are checked against everything static, and against movers of another group entry (they move by different amounts)."""
            S.reset(); entry = {}
            for g, hpv, val in held:                                       # the interlock's leaders, where the node needs them
                hb0, hb1 = (float(x) for x in hpv["range"]); hend = hb1 if abs(hb1) >= abs(hb0) else hb0
                _apply(g, hpv, val, val / hend if hend else 0.0)
            _apply(group, pv, v, f, entry)
            M = sorted(movers)
            pairs = S.candidates(M, static) + [(i, j) for i, j in S.candidates(M) if entry.get(i) != entry.get(j)]
            for i, j in pairs:
                if (i, j) in rest: continue
                a, b = S.name(i), S.name(j)
                if _declared(decl, f"{a}|{S.material(i)}", f"{b}|{S.material(j)}"): continue
                ov = S.overlap(i, j)
                if ov and ov["volume"] >= VMIN and ov["thickness"] >= TMIN: return (a, b, ov)
            return None
        for end in [e for e in (r1, r0) if e != 0]:                                              # from the pose as built (0) toward each range end
            hit = None
            for f in STEPS:
                h = pose(f * end, f)
                if h: hit = (f, h); break
            if hit:
                lo_f, hi_f = hit[0] - 1 / 8, hit[0]; best = hit[1]
                for _ in range(BISECT):
                    mid = (lo_f + hi_f) / 2; h = pose(mid * end, mid)
                    if h: hi_f, best = mid, h
                    else: lo_f = mid
                a, b, ov = best; u = pv["unit"]
                out.append(("FAIL", "MOT-010", leader, f"blocked at {hi_f * end:.2f} {u} of {r0:g}…{r1:g} ({hi_f * 100:.0f} % toward {end:g}): {a} hits {b}, "
                            f"{ov['volume']:.1f} mm³ at {_fmt(ov['lo'], ov['hi'])}" + (f" ({len(group) - 1} follower group(s) moved with it)" if len(group) > 1 else "")
                            + (f" (with {', '.join(f'{ld} held at {val:g}' for ld, val in REQ.get(leader, []))})" if held else "")))
        S.reset()
        if level == "element" and not held: alone.append((leader, pv, group, movers, [e for e in (r1, r0) if e != 0]))
    # ESCAPE clamp-angle-1.0 1 (review mech/r124, core watch 2026-11-13): each leader was swept with every other node at rest, so two
    # independent nodes were never posed together: clamp-angle's two pads, each clear alone, meet once both open past 21. Each pair of
    # independent leaders (no interlock between them, no mover in common, neither blocked alone) is posed at its range ends together;
    # a hit is a REVIEW (station 3), since the element may still be right where its behaviour keeps the two apart (then a motion.csv
    # "requires" row says so, and the pair is not posed).
    failed = {w for s, r_, w, *_ in out if s == "FAIL"}; linked = {(a, b) for a, lst in REQ.items() for b, _ in lst}
    paired = 0
    for x in range(len(alone)):
        for y in range(x + 1, len(alone)):
            la, pa, ga, ma, ea = alone[x]; lb, pb, gb, mb, eb = alone[y]
            if la in failed or lb in failed or (la, lb) in linked or (lb, la) in linked or (ma & mb) or not ea or not eb: continue
            paired += 1; hit = None
            for va in ea:
                for vb in eb:
                    S.reset(); _apply(ga, pa, va, 1.0); _apply(gb, pb, vb, 1.0)
                    for i, j in S.candidates(sorted(ma), sorted(mb)):
                        if (i, j) in rest: continue
                        a, b = S.name(i), S.name(j)
                        if _declared(decl, f"{a}|{S.material(i)}", f"{b}|{S.material(j)}"): continue
                        ov = S.overlap(i, j)
                        if ov and ov["volume"] >= VMIN and ov["thickness"] >= TMIN: hit = (va, vb, a, b, ov); break
                    if hit: break
                if hit: break
            S.reset()
            if hit:
                va, vb, a, b, ov = hit
                out.append(("REVIEW", "MOT-010", f"{la}+{lb}", f"posed together, {la} at {va:g} {pa['unit']} and {lb} at {vb:g} {pb['unit']}: {a} hits "
                            f"{b}, {ov['volume']:.1f} mm³ at {_fmt(ov['lo'], ov['hi'])}; each is clear alone. Keep each one's travel out of the "
                            f"other's, or state the interlock in lib/motion.csv (\"requires\") and in behaviour.csv"))
    if not any(s in ("FAIL", "REVIEW") for s, *_ in out):
        out.append(("PASS", "MOT-010", scope, f"{swept} moving node(s) swept through their full range, nothing hit"
                    + (f"; {paired} pair(s) of independent nodes posed together at their ends, clear" if paired else "")))
    return out

def follow_contact(P, scope, rows=None):
    """MOT-020 (escape overload-9a-1no1nc 1.1:1, core watch 2026-11-06): MOT-010 moves a follower with its leader whether or not the leader
    ever reaches it, so a chain that cannot work passed station 3. For each motion.csv row "follow" whose leader and follower are
    both moving nodes of this element: the leader, swept alone toward each end of its range (the follower held at rest), must come
    into contact with the follower (touch it at rest, as a pulled follower fixed to its leader does, or overlap it within the
    range). A pair that moves together without touching (a
    linkage the model doesn't draw) is declared mode "linked", with its reason in note; "linked" with no note is REVIEW too.
    rows: plain motion.csv rows (the selftest's planted cases); None reads lib/motion.csv."""
    rows = [r for r in (_csv("motion.csv") if rows is None else rows) if fnmatch.fnmatch(scope, r["scope"])]
    S = Scene(P); by_node = {}
    for i in S.idx:
        n = S.node(i)
        if n: by_node.setdefault(n, []).append(i)
    out = []; checked = 0
    for r in rows:
        mode = (r.get("mode") or "").strip(); L, F = r["leader"], r["follower"]
        if mode == "linked":
            if not (r.get("note") or "").strip():
                out.append(("REVIEW", "MOT-020", f"{L} → {F}", "declared \"linked\" with no reason in note: say what joins them that the model doesn't draw"))
            continue
        if mode != "follow" or L not in P.pivots or F not in P.pivots or L not in by_node or F not in by_node: continue
        pv = P.pivots[L]
        if pv["kind"] not in MOVING or pv["range"][0] == pv["range"][1]: continue
        r0, r1 = (float(v) for v in pv["range"]); checked += 1

        def meets(v):
            S.reset()
            if pv["kind"] == "rotate": R = rotation(pv["axis"], v); o = np.array(pv["origin"]); t = o - R @ o
            else: R = np.eye(3); t = np.array(pv["axis"], float) / np.linalg.norm(pv["axis"]) * v
            if v: S.move(by_node[L], R, t)
            return any(S.overlap(i, j) for i, j in S.candidates(by_node[L], by_node[F]))

        def touches():
            """at rest, face to face (a carrier the armature pulls, fixed to it): nudged TOUCH along any axis, the leader overlaps"""
            for ax in np.vstack([np.eye(3), -np.eye(3)]):
                S.reset(); S.move(by_node[L], np.eye(3), ax * TOUCH)
                if any(S.overlap(i, j) for i, j in S.candidates(by_node[L], by_node[F])): return True
            return False
        met = meets(0.0) or touches() or any(meets(f * end) for end in (r1, r0) if end != 0 for f in STEPS)
        S.reset()
        if not met:
            u = pv["unit"]
            out.append(("REVIEW", "MOT-020", f"{L} → {F}", f"follow pair never meets: {L} swept alone through {r0:g}…{r1:g} {u} does not reach {F} "
                        "(motion.csv moves it anyway). Place the driver to meet its follower within its travel, or declare the pair "
                        "\"linked\" with its reason"))
    if checked and not out: out.append(("PASS", "MOT-020", scope, f"{checked} follow pair(s): each leader meets its follower within its range"))
    return out

STROKE_TOL = 0.05             # MOT-030: a stroke this much short still closes (modelling contact)

def screw_stroke(P, scope):
    """MOT-030 (escape group 8, review clamp-screw-1.1:4, core watch 2026-11-07): MOT-010 swept the clamp's screw as a rotation and found
    nothing in its way, but at lead 0.5 its 720 degrees drove it 1.0 mm into a 5.0 mm window, so the clamp never closed on any conductor
    it claimed (22 to 10 AWG): the motion data could not do what the element is for. For each of the element's own contact pivots that
    carries a clamp window (window = (across, along the screw), mm) and a size_min (mm2), and each of its own rotate pivots with a lead
    (mm per turn): the screw opens the window fully at the start of its range, so its stroke, (range end - range start) / 360 x lead,
    must reach at least the window along the screw less the smallest conductor's diameter (a round solid conductor of size_min mm2,
    sqrt(4 A / pi)); within STROKE_TOL. A screw with no clamp window is not judged here. Pivots of a placed element (its tag, or
    tag.node) are the placed element's own MOT-030's, never its host's. REVIEW per pair short of it, with the stroke, what it needs
    and the turns that would give it."""
    tags = set(getattr(P, "parents", {}) or {})
    def own(n): return n not in tags and n.split(".")[0] not in tags
    clamps = [(n, pv) for n, pv in P.pivots.items() if own(n) and pv.get("kind") == "contact" and pv.get("window") and pv.get("size_min") is not None]
    screws = [(n, pv) for n, pv in P.pivots.items() if own(n) and pv.get("kind") == "rotate" and pv.get("lead")]
    out = []; checked = 0
    for cn, c in clamps:
        along = float(c["window"][1]); d_min = math.sqrt(4.0 * float(c["size_min"]) / math.pi); need = along - d_min
        for sn, sv in screws:
            r0, r1 = (float(v) for v in sv["range"]); lead = float(sv["lead"])
            turns = abs(r1 - r0) / (360.0 if sv.get("unit", "deg") == "deg" else 2 * math.pi); stroke = turns * lead; checked += 1
            if stroke < need - STROKE_TOL:
                out.append(("REVIEW", "MOT-030", f"{sn} → {cn}", f"the screw's stroke {stroke:.2f} mm ({turns:g} turns x lead {lead:g}) does not close "
                            f"the {along:g} mm window onto the smallest conductor ({c['size_min']:g} mm2, \u00d8{d_min:.2f}): it needs {need:.2f} mm, "
                            f"{need / lead:.1f} turns. Give the screw (or the cage) the travel that closes the clamp over its whole wire range"))
    if checked and not out: out.append(("PASS", "MOT-030", scope, f"{checked} clamping screw(s): each stroke closes its window onto the smallest conductor"))
    return out

JOIN = 0.05                   # GEO-070: solids this close count as touching (modelling contact)

def bodies(P, scope):
    """GEO-070 (escape group 9, review port-m12-a-1.4:1, core watch 2026-11-07): port-m12-a was two groups of solids with nothing in the
    1.9 mm wall between them (its M16 panel-thread body not modelled), and every check passed: nothing asked that an element be one body.
    The element's fixed solids must form one connected body. Two solids join when their bounding boxes meet within JOIN; a bounding box
    holds its solid, so two groups whose boxes stay apart are certainly apart (the check can miss a gap inside a box, never invent one).
    Moving nodes, springs ("compress") and what rides on them join what they touch at rest (a door joins its hinge to the cabinet), but
    a group of them alone is not reported: they ride on their pivots, and MOT-010 / MOT-020 judge how they meet. A placed
    element counts as one solid of its host (its own GEO-070 judges it): the host is judged on how it joins what it places.
    REVIEW per element: each separate group, where it is, and its gap to the main body."""
    S = Scene(P)
    loose = {n for n, pv in P.pivots.items() if (pv["kind"] in MOVING and pv["range"][0] != pv["range"][1]) or pv["kind"] == "compress"}
    parents = getattr(P, "parents", {}); grew = True
    while grew:                                                     # what rides on a moving part (its BOM parent) moves with it
        grew = False
        for tg, pa in parents.items():
            if pa in loose and tg not in loose: loose.add(tg); grew = True
    def is_loose(i): return S.node(i) in loose or _top(S, i) in loose
    idx = list(S.idx); fixed = [i for i in idx if not is_loose(i)]
    if len(fixed) < 2: return [("PASS", "GEO-070", scope, f"{len(fixed)} fixed solid(s): one body")]
    par = {i: i for i in idx}
    def find(a):
        while par[a] != a: par[a] = par[par[a]]; a = par[a]
        return a
    def join(a, b): par[find(a)] = find(b)
    first = {}
    for i in idx:                                                   # a placed element is one solid of its host
        o = _top(S, i)
        if o: join(i, first.setdefault(o, i))
    lo, hi = S.lo, S.hi
    for n_, i in enumerate(idx):                                    # moving parts at rest still join what they touch (a door and its hinge)
        a = S.pos[i]
        for j in idx[n_ + 1:]:
            b = S.pos[j]
            if np.all(lo[a] <= hi[b] + JOIN) and np.all(lo[b] <= hi[a] + JOIN): join(i, j)
    G_ = {}
    for i in fixed: G_.setdefault(find(i), []).append(i)            # a group of moving parts alone is MOT-010 / MOT-020's
    if len(G_) == 1: return [("PASS", "GEO-070", scope, f"{len(fixed)} fixed solids form one body")]
    groups = sorted(G_.values(), key=lambda g: (-len(g), g[0]))
    def box(g): return lo[[S.pos[i] for i in g]].min(axis=0), hi[[S.pos[i] for i in g]].max(axis=0)
    out = []; mlo, mhi = box(groups[0])
    for g in groups[1:]:
        glo, ghi = box(g); gap = float(np.maximum(glo - mhi, mlo - ghi).max())
        names = sorted({f"{S.name(i)}|{S.material(i)}" for i in g})
        where = ", ".join(names[:3]) + (f" (+{len(names) - 3})" if len(names) > 3 else "")
        out.append(("REVIEW", "GEO-070", where, f"{len(g)} solid(s) at {_fmt(glo, ghi)} touch nothing of the main body ({len(groups[0])} solids)"
                    + (f", {gap:.2f} mm from it" if gap > 0 else ", inside its bounds") + ": model what joins them (a body through the wall, "
                    "a stem, a hinge, a spring) or seat them on it; a part that moves gets its pivot"))
    return out

def element_parents(mod):
    return {r["tag"]: r["parent"] for r in library.own_bom(mod)}

def assembly_parents(aid):
    p = os.path.join(library.ROOT, "assemblies", aid, "bom.csv")
    return {r["tag"]: r["parent"] for r in library.read_bom(p)} if os.path.isfile(p) else {}


def _planar_faces(k, q):
    """axis-aligned planar faces of a primitive: (axis, plane value, outward sign, (lo, hi) of the face's other two axes, shape)"""
    out = []
    if k == "box":
        x, y, z, dx, dy, dz = q; lo = np.minimum([x, y, z], [x + dx, y + dy, z + dz]); hi = np.maximum([x, y, z], [x + dx, y + dy, z + dz])
        for a in range(3):
            o = [j for j in range(3) if j != a]
            out.append((a, lo[a], -1, (lo[o], hi[o]), "rect")); out.append((a, hi[a], +1, (lo[o], hi[o]), "rect"))
    elif k == "cyl":
        p1, p2, r = np.array(q[0], float), np.array(q[1], float), float(q[2]); d = p2 - p1; a = int(np.argmax(np.abs(d)))
        if np.allclose(np.delete(d, a), 0, atol=1e-6):
            o = [j for j in range(3) if j != a]; sgn = 1 if d[a] > 0 else -1
            for c, sg in ((p1, -sgn), (p2, sgn)): out.append((a, c[a], sg, (c[o] - r, c[o] + r), "disc"))
    return out

def _shown(P, S, i, cache):
    """does the mesh show i's openings (the writer cut them)? and what are they"""
    if i not in cache:
        from . import csg
        subs = [(P[h][1], P[h][2]) for h in S.holes.get(i, [])]
        cache[i] = subs if subs and csg.cut_solid(P[i][1], P[i][2], subs)[1] in ("extrude", "bsp") else []
    return cache[i]

def zfight(P, scope):
    """GEO-050: two solids with coplanar faces facing the same way overlap on screen, and Godot flickers between them (a cap flush with
    the face it sits on, a decal on the plane of its face). Openings the writer cut (toolkit/csg.py) are not face: a pin flush in its cut
    bore does not flicker. REVIEW per pair of names."""
    from .solid import inside
    S = Scene(P); F = {}; cache = {}
    for i in S.idx:
        for f in _planar_faces(P[i][1], P[i][2]): F.setdefault((f[0], f[2]), []).append((round(float(f[1]), 3), i, f[3], f[4]))
    hits = {}
    for (a, sg), L in F.items():
        L.sort(key=lambda t: t[0])
        o = [j for j in range(3) if j != a]
        for n, (v, i, (lo, hi), shp) in enumerate(L):
            for v2, j, (lo2, hi2), shp2 in L[n + 1:]:
                if v2 - v > 0.005: break
                if j == i or S.node(i) == S.node(j) and S.owner_of[i] == S.owner_of[j] and S.material(i) == S.material(j): continue
                lo_, hi_ = np.maximum(lo, lo2), np.minimum(hi, hi2); ov = hi_ - lo_
                if not (np.all(ov > 0.05) and float(np.prod(ov)) > 0.5): continue
                Hi, Hj = _shown(P, S, i, cache), _shown(P, S, j, cache); area = float(np.prod(ov))
                if Hi or Hj or shp == "disc" or shp2 == "disc":            # sample the shared rectangle: on both faces, in neither's openings
                    st = max(0.02, math.sqrt(area / 6000)); g = [np.arange(lo_[k] + st / 2, hi_[k], st) for k in range(2)]
                    U, W = np.meshgrid(*g, indexing="ij"); X = np.zeros((U.size, 3)); X[:, o[0]] = U.ravel(); X[:, o[1]] = W.ravel(); X[:, a] = v
                    m = np.ones(len(X), bool)
                    for (l_, h_), sh in (((lo, hi), shp), ((lo2, hi2), shp2)):
                        if sh == "disc": c = (l_ + h_) / 2; r = (h_[0] - l_[0]) / 2; m &= ((X[:, o[0]] - c[0]) ** 2 + (X[:, o[1]] - c[1]) ** 2) <= r * r
                    for H in (Hi, Hj):
                        Xin = X.copy(); Xin[:, a] -= sg * 0.01                 # just inside the solid, under its face
                        for hk, hq in H: m &= ~inside(hk, hq, Xin)
                    area = float(m.mean()) * area
                    if area <= 0.5: continue
                key = tuple(sorted((f"{S.name(i)}|{S.material(i)}", f"{S.name(j)}|{S.material(j)}")))
                hits[key] = hits.get(key, 0) + area
    out = [("REVIEW", "GEO-050", f"{a} × {b}", f"coplanar faces facing the same way over {ar:.0f} mm²: Godot flickers between them (offset one by ≥ 0.2 or join them)") for (a, b), ar in sorted(hits.items(), key=lambda kv: -kv[1])]
    if not out: out.append(("PASS", "GEO-050", scope, "no coplanar same-facing faces between different parts"))
    return out

def openings(P, scope):
    """GEO-060: every hole and cut-out shows in the glTF and the previews: the mesh writer (toolkit/csg.py) cut it as AutoCAD does"""
    from . import csg
    S = Scene(P); out = []; how = {}
    for i, H in sorted(S.holes.items()):
        if i >= len(P) or P[i][0].startswith("collider:"): continue
        subs = [(P[h][1], P[h][2]) for h in H]; _, m = csg.cut_solid(P[i][1], P[i][2], subs); how[m] = how.get(m, 0) + 1
        if m is None:
            out.append(("REVIEW", "GEO-060", S.name(i), f"{len(subs)} opening(s) in a {P[i][1]} ({P[i][0]}) not cut in the glTF: the part shows solid where AutoCAD has a hole"
                        + (" (a swept mesh: AutoCAD does not build meshes either; make the target a box, obox or cylinder)" if P[i][1] == "mesh" else "")))
    if not out:
        out.append(("PASS", "GEO-060", scope, f"{sum(how.values())} solid(s) with openings, all cut in the glTF: {how.get('extrude', 0)} as clean extrusions, "
                    f"{how.get('bsp', 0)} by boolean, {how.get('plain', 0)} with nothing visible" if how else "no holes or cut-outs"))
    return out
