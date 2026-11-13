"""Feature checkers of the validation suite: holes, GD&T fastener fit, sheet-metal DFM, tolerance stack-ups.
  holes(eid)    HOLE-010 every hole the element cuts matches a standard size (lib/standards/holes.csv) or a declared role
                (features.csv: match Ø, role, kind); a declared role outside its standard window is FAIL
  gdt(eid)      GDT-010 fastener clearance patterns: the positional tolerance the parts can take, floating fastener T = H - F
                (ASME Y14.5 Appendix B, H and F at MMC; H is the modelled nominal = minimum hole), against the pattern's declared
                position tolerance or, failing that, the ISO 2768-m general tolerance of its span (zone Ø = 2√2 · t). Applied to a
                hole-to-hole span that conversion is conservative (up to 2x): it can only add REVIEWs, never hide a FAIL
  dfm(eid)      DFM-010 holes in sheet (steel, galvanised, aluminium ≤ 3 mm): edge distance ≥ 1.5 t and Ø ≥ t (punching guideline)
  stacks()      STK-010 lib/stacks.csv: worst case and RSS of a chain of figures against its requirement
Elements own their holes; holes of a carried element are checked in that element's own run."""
import csv, math, os, re
import numpy as np
from . import library

ROOT = library.ROOT

def _rows(path):
    return [r for r in csv.DictReader(open(path, encoding="utf-8")) if r and list(r.values())[0] and not list(r.values())[0].startswith("#")] if os.path.isfile(path) else []

def table():
    return _rows(os.path.join(ROOT, "standards", "holes.csv"))

def general_tol(L, cls="m"):
    for r in _rows(os.path.join(ROOT, "standards", "general-tolerances.csv")):
        if r["class"] == cls and float(r["over"]) < L <= float(r["up_to"]): return float(r["tol"])
    return 0.1

def own_holes(P):
    """holes cut by the element itself (not by a carried element): (index, Ø, centre, axis, target)"""
    nested = [(s, e) for s, e, *_ in getattr(P, "owners", [])]
    out = []
    for i, (L, k, q) in enumerate(P):
        if k != "hole" or any(s <= i < e for s, e in nested): continue
        p1, p2 = np.array(q[0], float), np.array(q[1], float)
        out.append((i, round(2 * q[2], 3), (p1 + p2) / 2, (p2 - p1) / max(np.linalg.norm(p2 - p1), 1e-9), q[3]))
    return out

def _declared(eid):
    return _rows(os.path.join(library.ELEMENTS, eid, "features.csv"))

def holes(eid, P):
    T = table(); D = _declared(eid); out = []; groups = {}
    for i, d, c, ax, tg in own_holes(P):
        dec = next((r for r in D if r.get("match") and abs(float(r["match"]) - d) < 0.01), None)
        std = [r for r in T if r["kind"] in ("clearance", "cutout", "entry") and float(r["d_min"]) - 1e-6 <= d <= float(r["d_max"]) + 1e-6]
        if dec and dec.get("check") == "review":
            st, msg = "REVIEW", f"Ø{d:g} {dec['role']}: {dec.get('note', '')}"; std = []
        elif dec:
            role = dec["role"]; srow = next((r for r in T if r["role"] == role), None)
            if srow and not (float(srow["d_min"]) - 1e-6 <= d <= float(srow["d_max"]) + 1e-6): st, msg = "FAIL", f"Ø{d:g} declared {role} but the standard window is {srow['d_min']}–{srow['d_max']} ({srow['standard']})"
            else: st, msg = "PASS", f"Ø{d:g} {role} (declared" + (f", {srow['standard']})" if srow else f": {dec.get('kind', 'own')}, {dec.get('source', '')})")
            std = [srow] if srow else []                                                      # a declared role is never re-inferred
        elif std: st, msg = "PASS", f"Ø{d:g} {std[0]['role']} ({std[0]['standard']})"
        else:
            near = min(T, key=lambda r: min(abs(d - float(r["d_min"])), abs(d - float(r["d_max"]))))
            st, msg = "REVIEW", f"Ø{d:g} matches no standard hole (nearest {near['role']} {near['d_min']}–{near['d_max']}): declare its role in features.csv or change it"
        groups.setdefault((st, msg), []).append((i, d, c, ax, tg, std[0] if std else None, dec))
    for (st, msg), g in groups.items(): out.append((st, "HOLE-010", eid, f"{len(g)} × {msg}"))
    return out, groups

def gdt(eid, P, groups):
    """floating-fastener check per pattern of clearance holes (same Ø, same target)"""
    out = []; D = _declared(eid)
    pats = {}
    for (st, msg), g in groups.items():
        for i, d, c, ax, tg, srow, dec in g:
            if not (srow and srow["kind"] == "clearance"): continue
            a = int(np.argmax(np.abs(ax))); key = tuple(round(float(c[j]), 1) for j in range(3) if j != a)       # coaxial holes through several plates are one hole
            L = pats.setdefault((d, a, srow["size"]), {}); L.setdefault(key, c)
    pats = {k: list(v.values()) for k, v in pats.items()}
    for (d, tg, size), C in pats.items():
        F = float(size[1:]); Tallow = d - F
        span = max((np.linalg.norm(a - b) for a in C for b in C), default=0.0)
        dec = next((r for r in D if r.get("match") and abs(float(r["match"]) - d) < 0.01 and r.get("position_tol")), None)
        if dec:
            t = float(dec["position_tol"]); st = "PASS" if t <= Tallow + 1e-9 else "FAIL"
            out.append((st, "GDT-010", eid, f"{len(C)} × Ø{d:g} for {size} (floating): position Ø{t:g} declared {'≤' if st == 'PASS' else '>'} H − F = {Tallow:.2f}"))
        else:
            gt = general_tol(span); zone = 2 * math.sqrt(2) * gt
            st = "PASS" if zone <= Tallow + 1e-9 else "REVIEW"
            out.append((st, "GDT-010", eid, f"{len(C)} × Ø{d:g} for {size} (floating) over {span:.0f} mm: ISO 2768-m ±{gt:g} gives a Ø{zone:.2f} zone {'≤' if st == 'PASS' else '>'} H − F = {Tallow:.2f}"
                        + ("" if st == "PASS" else "; give the pattern a position tolerance (features.csv position_tol) or a larger clearance class")))
    return out

def breakout(eid, P):
    """HOLE-020: a hole through a box or oriented box must stay inside it (edge distance ≥ 0); a hole that breaks the edge is a notch"""
    out = []; n = 0
    for i, d, c, ax, tg in own_holes(P):
        L, k, q = P[tg]
        if k == "box":
            x, y, z, dx, dy, dz = q; o = np.minimum([x, y, z], [x + dx, y + dy, z + dz]); E = np.eye(3); S = np.abs([dx, dy, dz])
        elif k == "obox":
            o0, ex, ey, ez, l, w, h = q; E = np.array([ex, ey, ez], float); S = np.array([l, w, h], float); o = np.array(o0, float)
            for a_ in range(3):
                if S[a_] < 0: o = o + E[a_] * S[a_]; S[a_] = -S[a_]
        else: continue
        n += 1; rel = np.array([(c - o) @ E[a_] for a_ in range(3)]); axl = np.abs([ax @ E[a_] for a_ in range(3)]); a = int(np.argmax(axl))
        edge = min(min(rel[j], S[j] - rel[j]) for j in range(3) if j != a) - d / 2
        if edge < -1e-6: out.append(("FAIL", "HOLE-020", eid, f"hole Ø{d:g} breaks out of its part ({L}) by {-edge:.2f} mm: move it in or make the part bigger"))
    if n and not out: out.append(("PASS", "HOLE-020", eid, f"{n} hole(s) inside their parts"))
    return out

SHEET = re.compile(r"M-(STEEL|GALV|ALU)")
def dfm(eid, P):
    out = []; bad = 0; n = 0
    for i, d, c, ax, tg in own_holes(P):
        L, k, q = P[tg]
        if k != "box" or not SHEET.search(L): continue
        x, y, z, dx, dy, dz = q; lo = np.minimum([x, y, z], [x + dx, y + dy, z + dz]); hi = np.maximum([x, y, z], [x + dx, y + dy, z + dz])
        a = int(np.argmax(np.abs(ax))); t = (hi - lo)[a]
        if t > 3.0: continue
        n += 1; other = [j for j in range(3) if j != a]
        edge = min(min(c[j] - lo[j], hi[j] - c[j]) for j in other) - d / 2
        if edge < 1.5 * t - 1e-6 or d < t - 1e-6:
            bad += 1; out.append(("REVIEW", "DFM-010", eid, f"hole Ø{d:g} in {t:g} sheet ({L}): edge distance {edge:.1f} < 1.5 t = {1.5 * t:.1f}" if edge < 1.5 * t else f"hole Ø{d:g} smaller than the sheet thickness {t:g}"))
    if n and not bad: out.append(("PASS", "DFM-010", eid, f"{n} sheet hole(s): edge distance ≥ 1.5 t and Ø ≥ t"))
    return out

# ------------------------------------------------------------------ attribute paths shared by mates and stacks
def resolve(eid, path):
    """element attribute by a dotted path: W, LID.t, PARAMS.door_t, std22.PANEL_RANGE"""
    v = library.load(eid)
    for part in path.split("."):
        v = v[part] if isinstance(v, dict) else getattr(v, part)
    return v

def stacks(path=None):
    path = path or os.path.join(ROOT, "stacks.csv"); S = {}; out = []
    for r in _rows(path): S.setdefault(r["stack"], []).append(r)
    for sid, rows in S.items():
        req = next((r for r in rows if r["term"] == "requirement"), None); terms = [r for r in rows if r["term"] != "requirement"]
        nom = 0.0; wc = 0.0; ss = 0.0; notes = []
        try:
            for r in terms:
                v = float(r["value"]) if r.get("value") else float(resolve(r["element"], r["attr"]))
                tol = float(r["tol"]) if r.get("tol") else general_tol(abs(v)); notes.append(f"{r['term']} {'+' if r['sign'] == '+' else '−'}{abs(v):g}±{tol:g}" + ("" if r.get("tol") else " (2768-m)"))
                nom += v if r["sign"] == "+" else -v; wc += tol; ss += tol * tol
        except Exception as e:
            out.append(("REVIEW", "STK-010", sid, f"cannot evaluate: {e}")); continue
        rss = math.sqrt(ss); lo_req = float(req["min"]) if req and req.get("min") else -math.inf; hi_req = float(req["max"]) if req and req.get("max") else math.inf
        if nom - wc >= lo_req and nom + wc <= hi_req: st = "PASS"
        elif nom - rss >= lo_req and nom + rss <= hi_req: st = "REVIEW"
        else: st = "FAIL"
        out.append((st, "STK-010", sid, f"nominal {nom:.2f}, worst case ±{wc:.2f} ({nom - wc:.2f}…{nom + wc:.2f}), RSS ±{rss:.2f}; requirement "
                    + (f"≥ {lo_req:g}" if lo_req > -math.inf else "") + (f" ≤ {hi_req:g}" if hi_req < math.inf else "") + f" ({req.get('note', '') if req else ''}). Terms: " + "; ".join(notes)))
    return out
