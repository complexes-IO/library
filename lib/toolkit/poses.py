"""The pose check: apply each moving node's declared pivot motion (rotate, translate, compress) to the released build and measure what
touches what against the element's states table (behaviour.md). The core's, run by any lane, unattended too:
    python lib/build.py poses <id>      -> prints the checks, writes lib/elements/<id>/gate/<id>-poses.json (station 6 reads it)
Moved here from lib/pose-check.py (the library's file) by core watch 2026-11-07 (request elec-4) with three corrections:
- every moving node is posed by its own pivot's range end (amounts()), never by a fixed number: the flag (0..3.6) was moved the
  card's 1.2, the door-lock (a 0..4 slider since 1.1) 180 mm as if it still turned 180 degrees, the button a fixed 1.5;
- the armature row measures the plate's face where it lies over the core (face_gap()), not its bounding box: the turned plate's
  tip reached the core's face plane, so the box read 0.003 while 0.68 to 0.96 stayed open over the core itself;
- the lanes run it through build.py, which is on their unattended tool list (lib/pose-check.py was not).
Escape group 24 (core watch 2026-11-07, review relay-ice-cube-1.3:1, elec-r14:1): a contact row is bounded on both sides. "The door
holds the button in" passed with the door 1.76 in front of the pressed button (one-sided, door <= button + 0.6), and the manual push
was checked only from below; holds() and push_ok() bound both."""
import os, json, math
import numpy as np
from . import library

def node_of(L): return L[5:].split("|", 1)[0] if L.startswith("node:") else None

def pts_of(q, kind, n=2):
    """a primitive's points: corners (n=2) or an n x n x n lattice through its volume (boxes) / n rings (cylinders)"""
    s = np.linspace(0, 1, n)
    if kind == "box":
        x, y, z, dx, dy, dz = (float(v) for v in q); return [np.array((x + a * dx, y + b * dy, z + c * dz)) for a in s for b in s for c in s]
    if kind == "obox":
        o, ex, ey, ez, l, w, h = q; o, ex, ey, ez = (np.array(v, float) for v in (o, ex, ey, ez))
        return [o + ex * float(l) * a + ey * float(w) * b + ez * float(h) * c for a in s for b in s for c in s]
    if kind == "cyl":
        p1, p2, r = q; p1, p2 = np.array(p1, float), np.array(p2, float); d = (p2 - p1) / np.linalg.norm(p2 - p1)
        a = np.array([1.0, 0, 0]) if abs(d[0]) < 0.9 else np.array([0, 1.0, 0]); u = np.cross(d, a); u /= np.linalg.norm(u); v = np.cross(d, u)
        return [p1 + (p2 - p1) * f + float(r) * (math.cos(t) * u + math.sin(t) * v) for f in s for t in np.linspace(0, 2 * math.pi, 16, endpoint=False)]
    if kind == "mesh": return [np.array(p, float) for t in q[0] for p in t]
    return []

def move(points, pv, amount):
    o = np.array(pv["origin"], float); ax = np.array(pv["axis"], float); ax /= np.linalg.norm(ax)
    if pv["kind"] == "rotate":
        a = math.radians(amount); K = np.array([[0, -ax[2], ax[1]], [ax[2], 0, -ax[0]], [-ax[1], ax[0], 0]]); R = np.eye(3) + math.sin(a) * K + (1 - math.cos(a)) * K @ K
        return [R @ (p - o) + o for p in points]
    if pv["kind"] == "translate": return [p + ax * amount for p in points]
    if pv["kind"] == "compress":     # scale along the axis about the origin by (L - travel) / L; L = the mesh's length along the axis
        s = [float(np.dot(p - o, ax)) for p in points]; Lg = max(s) - min(s) if s else 1.0; f = (Lg - amount) / Lg
        return [o + (p - o) + ax * (np.dot(p - o, ax) * (f - 1)) for p in points]
    return points

MOVING = ("rotate", "translate", "compress")

def amounts(pivots, nodes=None):
    """{node: its pivot's range end} for every moving pivot (or the nodes named): the pose is the element's own declared travel"""
    return {n: float(p["range"][1]) for n, p in pivots.items() if p.get("kind") in MOVING and (nodes is None or n in nodes)}

def posed(P, pose=None, n=2):
    """per primitive: (node, layer, kind, points) after the pose {node: amount}"""
    out = []
    for L, k, q in P:
        if k == "hole" or L.startswith("collider:"): continue
        pts = pts_of(q, k, n); nd = node_of(L)
        if pose and nd in pose and nd in P.pivots: pts = move(pts, P.pivots[nd], pose[nd])
        out.append((nd, L, k, np.array(pts)))
    return out

def boxes(P, pose=None):
    """per primitive: (node, layer, kind, min, max) after the pose"""
    return [(nd, L, k, A.min(axis=0), A.max(axis=0)) for nd, L, k, A in posed(P, pose)]

def gap(a, b, axis):
    """signed clearance between two boxes along an axis where they overlap on the other two (None if they do not face each other)"""
    o = [k for k in range(3) if k != axis]
    if any(a[4][k] < b[3][k] - 1e-6 or b[4][k] < a[3][k] - 1e-6 for k in o): return None
    return round(float(max(b[3][axis] - a[4][axis], a[3][axis] - b[4][axis])), 3)

def face_gap(points, lo, hi, axis):
    """the clearance along an axis between a part's points and a box (lo, hi), counting only the points that lie over the box on the
    other two axes: what a face meets, not what its bounding box reaches. None when no point lies over the box."""
    o = [k for k in range(3) if k != axis]; A = np.asarray(points, float)
    m = np.all([(A[:, k] >= lo[k] - 1e-6) & (A[:, k] <= hi[k] + 1e-6) for k in o], axis=0)
    if not m.any(): return None
    A = A[m]; return round(float(max(lo[axis] - A[:, axis].max(), A[:, axis].min() - hi[axis])), 3)

HOLD_GAP = 0.6     # a holding face may stand this far in front of the face it holds (mm)
HOLD_OVERLAP = 0.05  # and reach this far into it (the check's general 0.05 mm)
PUSH_TOL = 0.05    # a push after contact may fall short of, or run past, the travel it drives by this much (mm)

def holds(holder_back, held_front, gap=HOLD_GAP, overlap=HOLD_OVERLAP):
    """a face that holds another along y (front is −y): its back face at the held part's front face, within gap in front and overlap
    into it. Both sides bounded: a holder any distance in front holds nothing."""
    d = held_front - holder_back          # > 0: the holder stands in front by d; < 0: it reaches into the held part
    return -overlap <= d <= gap

def push_ok(push, travel, tol=PUSH_TOL):
    """a push after contact drives the travel it must: no shorter (the travel isn't reached) and no longer (the driven part would
    overtravel its range end, or the parts overlap), each within tol"""
    return abs(push - travel) <= tol

def relay(mod):
    rep = {"id": mod.ID, "version": mod.VERSION, "checks": []}
    def ck(name, ok, got, want): rep["checks"].append(dict(check=name, ok=bool(ok), got=got, want=want)); print(f"  {'ok  ' if ok else 'DIFF'} {name}: {got}  (want {want})")
    R = mod.build(view="cutaway", socket=False, operated=False); O = mod.build(view="cutaway", socket=False, operated=True)
    piv = R.pivots; amt = amounts(piv, ("armature", "actuator", "spring-return", "pole-1", "pole-2", "flag"))
    print("binder amounts (each pivot's range end):", amt)
    b0 = boxes(R); b1 = boxes(R, amt); bo = boxes(O)
    for n in ["armature", "actuator", "pole-1", "pole-2", "flag", "spring-return"]:
        A = [x for x in b1 if x[0] == n]; B = [x for x in bo if x[0] == n]
        lo1 = np.min([x[3] for x in A], axis=0); hi1 = np.max([x[4] for x in A], axis=0); lo2 = np.min([x[3] for x in B], axis=0); hi2 = np.max([x[4] for x in B], axis=0)
        d = float(max(np.abs(lo1 - lo2).max(), np.abs(hi1 - hi2).max())); ck(f"binder pose of {n} equals build(operated=True)", d <= 0.05, round(d, 3), "<= 0.05 mm")
    for i in range(2):
        pole = f"pole-{i + 1}"; x = piv[pole]["origin"][0]
        riv0 = [b for b in b0 if b[0] == pole and b[2] == "cyl"][0]; riv1 = [b for b in b1 if b[0] == pole and b[2] == "cyl"][0]
        fixed = [b for b in b0 if b[1] == "M-SILVER" and b[0] is None and abs((b[3][0] + b[4][0]) / 2 - x) < 0.01]
        nc = max(fixed, key=lambda b: -b[3][1]) if fixed else None   # the N.C. rivet is the more negative y (above the tip, toward the front)
        no = min(fixed, key=lambda b: -b[3][1]) if fixed else None
        ck(f"released: {pole} tip on N.C.", nc is not None and gap(riv0, nc, 1) is not None and abs(gap(riv0, nc, 1)) < 0.02, gap(riv0, nc, 1) if nc else None, "0 (touching)")
        ck(f"released: {pole} tip clear of N.O.", no is not None and (gap(riv0, no, 1) or 0) > 0.5, gap(riv0, no, 1) if no else None, "the contact gap, 1.2 (Assumption)")
        ck(f"operated: {pole} tip off N.C.", nc is not None and (gap(riv1, nc, 1) or 0) > 0.5, gap(riv1, nc, 1) if nc else None, "open")
        ck(f"operated: {pole} tip on N.O.", no is not None and gap(riv1, no, 1) is not None and abs(gap(riv1, no, 1)) < 0.15, gap(riv1, no, 1) if no else None, "0 (touching; the tilted rivet face may differ by a few hundredths)")
    core = [b for b in b0 if b[1] == "M-STEEL-7035" and b[2] == "cyl"][0]
    arm0 = [b for b in b0 if b[0] == "armature"]; arm1 = [b for b in b1 if b[0] == "armature"]
    pa0 = np.vstack([A for nd, L, k, A in posed(R, None, 21) if nd == "armature"]); pa1 = np.vstack([A for nd, L, k, A in posed(R, amt, 21) if nd == "armature"])
    g0 = face_gap(pa0, core[3], core[4], 1); g1 = face_gap(pa1, core[3], core[4], 1)
    ck("released: armature face to core face (over the core)", g0 is not None and g0 > 0.2, g0, "an air gap")
    ck("operated: armature face on the core face (over the core; states table: 'at the core')", g1 is not None and abs(g1) < 0.1, g1, "0 (closed magnetic gap)")
    card0 = [b for b in b0 if b[0] == "actuator"]; card1 = [b for b in b1 if b[0] == "actuator"]
    gt0 = [gap(a, c, 1) for a in arm0 for c in card0 if gap(a, c, 1) is not None]; gt1 = [gap(a, c, 1) for a in arm1 for c in card1 if gap(a, c, 1) is not None]
    ck("released: armature tip on the card", gt0 and min(abs(g) for g in gt0) < 0.05, min(gt0, key=abs) if gt0 else None, "0")
    ck("operated: armature tip still on the card", gt1 and min(abs(g) for g in gt1) < 0.1, min(gt1, key=abs) if gt1 else None, "0")
    # manual: the button pressed its own travel must push the card through the card's travel
    bt = amounts(piv, ("btn-test",))["btn-test"]
    btn0 = [b for b in b0 if b[0] == "btn-test"][0]; btnp = [b for b in boxes(R, {"btn-test": bt}) if b[0] == "btn-test"][0]
    facing = [g for g in (gap(btn0, c, 1) for c in card0) if g is not None]
    ck("manual: the button faces the card (overlap in x and z)", bool(facing), [round(g, 3) for g in facing] or "no card part in front of the button", "a card part in line with the button")
    if not facing:
        c = min(card0, key=lambda c: np.linalg.norm(((c[3] + c[4]) / 2 - (btn0[3] + btn0[4]) / 2)[[0, 2]]))
        rep["button_vs_card"] = {"button_x": [round(float(btn0[3][0]), 2), round(float(btn0[4][0]), 2)], "button_z": [round(float(btn0[3][2]), 2), round(float(btn0[4][2]), 2)],
                                 "nearest_card_x": [round(float(c[3][0]), 2), round(float(c[4][0]), 2)], "nearest_card_z": [round(float(c[3][2]), 2), round(float(c[4][2]), 2)],
                                 "button_inner_y_pressed": round(float(btnp[4][1]), 2), "card_front_y": round(float(c[3][1]), 2)}
        print("     button vs nearest card part:", rep["button_vs_card"])
    else:
        g = min(facing); ck(f"manual: the button's {bt} travel covers the gap plus the card's {amt['actuator']} travel", push_ok(bt - g, amt["actuator"]), round(bt - g, 3), f"{amt['actuator']} ± {PUSH_TOL} mm of push after contact")
    # locked: the door-lock at its range end lies over the pressed button
    dl = amounts(piv, ("door-lock",))["door-lock"]
    door = [b for b in boxes(R, {"door-lock": dl}) if b[0] == "door-lock"][0]
    over = all(door[3][k] <= btnp[4][k] and door[4][k] >= btnp[3][k] for k in (0, 2))
    ck("locked: the door-lock at its range end covers the pressed button in x and z", over, {"door_x": [round(float(door[3][0]), 2), round(float(door[4][0]), 2)], "door_z": [round(float(door[3][2]), 2), round(float(door[4][2]), 2)]}, "over the button")
    ck("locked: the door sits in front of the pressed button (holds it in)", holds(float(door[4][1]), float(btnp[3][1])), {"door_back_y": round(float(door[4][1]), 2), "button_front_y_pressed": round(float(btnp[3][1]), 2)}, f"door back at the button face: {HOLD_GAP} in front to {HOLD_OVERLAP} into it")
    sp1 = [b for b in b1 if b[0] == "spring-return"][0]; foot1 = min(card1, key=lambda c: abs(c[4][1] - sp1[3][1]))
    ck("operated: spring top meets the card foot", abs(sp1[3][1] - foot1[4][1]) < 0.6, round(float(sp1[3][1] - foot1[4][1]), 3), "about 0 (the wire radius)")
    return rep

CHECKS = {"relay-ice-cube-2co": relay}

def run(eid, write=True):
    """the element's pose check; writes gate/<id>-poses.json (with the version it checked). Refused for an element with none."""
    if eid not in CHECKS: raise ValueError(f"no pose check for {eid} (toolkit/poses.CHECKS: {', '.join(sorted(CHECKS))})")
    mod = library.load(eid); print(f"pose check {eid} v{mod.VERSION}")
    rep = CHECKS[eid](mod); rep["pass"] = all(c["ok"] for c in rep["checks"])
    print(f"{sum(c['ok'] for c in rep['checks'])} of {len(rep['checks'])} checks agree")
    if write:
        out = os.path.join(library.ELEMENTS, eid, "gate", eid + "-poses.json"); os.makedirs(os.path.dirname(out), exist_ok=True)
        json.dump(rep, open(out, "w", encoding="utf-8", newline="\n"), indent=1, default=float); print("->", out)
    return rep
