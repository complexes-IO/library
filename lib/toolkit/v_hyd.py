"""Hydraulic checkers of the validation suite (request pneu-8; the contract is toolkit/hyd.py). They run on an assembly that has a
hydraulic circuit on file, and on nothing else (an assembly with no hyd.csv gets no HYD finding):
  assemblies/<aid>/hyd.csv           from,to,params,note       one joint or hose per row; `to` empty = a port left open (HYD-002 FAILs)
                                                               params: line=P|A|B|T; hose=<tag of the placed hose>; bore=<mm>;
                                                               plug=yes (the port is plugged); tank=yes (a declared tank return)
  assemblies/<aid>/hyd-circuit.csv   key,tag,value,unit,note   source (tag: the pump or HPU; value: its flow, l/min), relief (tag: the
                                                               relief valve or the source; value: its setting), tank (the T line's
                                                               pressure), hold (tag: the holding device of the vertical cylinder tag
                                                               in note "for <cyl>", or for every vertical cylinder; EM's sign-off in
                                                               note "Safety sign-off ... · EM <date>"), cylinder (tag; value vertical
                                                               or horizontal, when the build gives no rod axis)
Ports are the placed elements' pivots whose unit is a hydraulic unit (hyd.is_hyd). Ratings come from each element's ratings.csv:
p_max and span with a pressure unit. A cylinder is a placed element with a hydraulic port and a translating node `rod`; it is
vertical when that node's axis lies within 45° of z.
  Circuit = dict(ports={endpoint: dict(unit, gender, role)}, joints=[dict(a, b, line, hose, bore, plug, tank, row)],
                 rating={tag: dict(p_max, span)}, flow=l/min, source=tag, reliefs=[(tag, bar)], tank=bar,
                 cylinders={tag: vertical bool}, hold={cyl tag or '*': (device tag, signed bool)})"""
import csv, os, re
from . import hyd as H

def _tag(endpoint): return endpoint.rsplit(".", 1)[0] if "." in endpoint else endpoint

def _f(b): return f"{b:.1f} bar"

def relief(C): return C["reliefs"][0][1] if len(C.get("reliefs") or []) == 1 else (max(b for _, b in C["reliefs"]) if C.get("reliefs") else None)

def tank(C): return C.get("tank") if C.get("tank") is not None else H.P_TANK

def joints(C):
    """HYD-001 every joined pair matches"""
    out = []
    for j in C["joints"]:
        if not j.get("b"): continue
        a, b = C["ports"].get(j["a"]), C["ports"].get(j["b"])
        where = f"row {j.get('row', '?')} {j['a']} ↔ {j['b']}"
        if a is None or b is None:
            out.append(("FAIL", "HYD-002", where, f"{j['a'] if a is None else j['b']} is not a hydraulic port of a placed element")); continue
        st, msg = H.hyd001(a, b); out.append((st, "HYD-001", where, msg))
    return out

def open_ports(C):
    """HYD-002 every hydraulic port joined, plugged, or a declared tank return"""
    out = []; done = set()
    for j in C["joints"]:
        if j.get("b") or j.get("plug") or j.get("tank"): done.add(j["a"])
        if j.get("b"): done.add(j["b"])
    for e, p in sorted(C["ports"].items()):
        if p.get("role") == "plug" or e in done: continue
        out.append(("FAIL", "HYD-002", e, f"{p['unit']} port left open: at {_f(relief(C) or 0)} an open port is an oil jet (join it, plug it, or declare it a tank return)"))
    return out

def _line_of(C):
    """{endpoint: set of lines} from hyd.csv's line= params"""
    on = {}
    for j in C["joints"]:
        for e in (j["a"], j.get("b")):
            if e and j.get("line"): on.setdefault(e, set()).add(j["line"])
    return on

def reach(C, tag, on=None):
    """the highest pressure that can reach an element: the relief setting, or the tank line's when every port of it on a line is on T"""
    on = _line_of(C) if on is None else on
    lines = set().union(*[on.get(e, set()) for e in C["ports"] if _tag(e) == tag]) if C["ports"] else set()
    if lines and lines <= {"T"}: return tank(C)
    return relief(C)

def pressures(C):
    """HYD-003 ratings against what can reach a part; HYD-006 gauge spans"""
    out = []; on = _line_of(C); r = relief(C)
    for tag, R in sorted(C["rating"].items()):
        p = reach(C, tag, on)
        if "p_max" in R:
            if p is None: out.append(("REVIEW", "HYD-003", tag, "no relief setting on file (hyd-circuit.csv relief): nothing bounds the pressure that reaches it"))
            elif R["p_max"] is None: out.append(("REVIEW", "HYD-003", tag, f"pressure rating NOT ON FILE; {_f(p)} can reach it"))
            elif R["p_max"] + H.TOL_BAR < p: out.append(("FAIL", "HYD-003", tag, f"rated {_f(R['p_max'])} < {_f(p)} that can reach it (H5: every element on the pressure side ≥ the relief setting)"))
            else: out.append(("PASS", "HYD-003", tag, f"rated {_f(R['p_max'])} ≥ {_f(p)}"))
        if R.get("span") is not None and p is not None:
            s = R["span"]
            if p > s + H.TOL_BAR: out.append(("FAIL", "HYD-006", tag, f"span {_f(s)} < {_f(p)} that can reach it: it pegs"))
            elif p > H.GAUGE_FRACTION * s + H.TOL_BAR: out.append(("REVIEW", "HYD-006", tag, f"{_f(p)} is {p / s * 100:.0f} % of its {_f(s)} span, above {H.GAUGE_FRACTION * 100:.0f} % (Assumption (A), as PNE-009)"))
            else: out.append(("PASS", "HYD-006", tag, f"{_f(p)} is {p / s * 100:.0f} % of its {_f(s)} span"))
    return out

def hoses(C):
    """HYD-004 a hose's working pressure ≥ its line's; HYD-005 each line's velocity within H6's limit for its kind"""
    out = []; r = relief(C); q = C.get("flow")
    for j in C["joints"]:
        ln = j.get("line"); where = f"row {j.get('row', '?')} {j['a']} ↔ {j.get('b') or '(open)'}"
        p = tank(C) if ln == "T" else r
        if j.get("hose"):
            hp = (C["rating"].get(j["hose"]) or {}).get("p_max")
            if hp is None: out.append(("REVIEW", "HYD-004", where, f"hose {j['hose']}: working pressure NOT ON FILE (A) ({H.HOSE} table; the hose element's ratings.csv p_max)"))
            elif p is None: out.append(("REVIEW", "HYD-004", where, f"hose {j['hose']} rated {_f(hp)}: no relief setting on file to judge it by"))
            elif hp + H.TOL_BAR < p: out.append(("FAIL", "HYD-004", where, f"hose {j['hose']} rated {_f(hp)} < {_f(p)} on line {ln or '?'}"))
            else: out.append(("PASS", "HYD-004", where, f"hose {j['hose']} rated {_f(hp)} ≥ {_f(p)} on line {ln or '?'}"))
        if ln in H.V_LIMIT and q:
            if not j.get("bore"): out.append(("REVIEW", "HYD-005", where, f"line {ln}: bore NOT ON FILE, so the velocity at {q:g} l/min is not known")); continue
            v = H.velocity(q, j["bore"]); lim = H.V_LIMIT[ln]
            st = "REVIEW" if v > lim + 1e-9 else "PASS"
            out.append((st, "HYD-005", where, f"line {ln}: {q:g} l/min through Ø{j['bore']:g} mm is {v:.1f} m/s, {'above' if st == 'REVIEW' else 'within'} {lim:g} m/s (H6, Assumption (A), EM's)"))
    return out

def reliefs(C):
    """HYD-007 one relief per source, set ≤ the source's p_max"""
    R = C.get("reliefs") or []; src = C.get("source")
    if not R: return [("FAIL", "HYD-007", src or "circuit", "no relief setting on file: nothing limits the source's pressure (H5)")]
    if len(R) > 1: return [("FAIL", "HYD-007", src or "circuit", f"{len(R)} reliefs on one source ({', '.join(f'{t} {_f(b)}' for t, b in R)}): one setting per circuit (H5)")]
    t, b = R[0]; pm = (C["rating"].get(src) or {}).get("p_max") if src else None
    if pm is not None and b > pm + H.TOL_BAR: return [("FAIL", "HYD-007", t, f"relief {_f(b)} above the source {src}'s rating {_f(pm)}")]
    return [("PASS", "HYD-007", t, f"one relief, {_f(b)}" + (f", within the source's {_f(pm)}" if pm is not None else " (the source's rating NOT ON FILE)"))]

SIGNED = re.compile(r"Safety sign-off.*·\s*EM\s+\d{4}-\d{2}-\d{2}")

def holding(C):
    """HYD-008 a vertical cylinder has a holding device named, with EM's Safety sign-off (a safety function, OPERATING.md 12): REVIEW
    until both are on file"""
    out = []
    for cyl, vertical in sorted((C.get("cylinders") or {}).items()):
        if not vertical: continue
        h = (C.get("hold") or {}).get(cyl) or (C.get("hold") or {}).get("*")
        if not h: out.append(("REVIEW", "HYD-008", cyl, "a vertical cylinder with no holding device named (hyd-circuit.csv hold: a counterbalance, a pilot-operated check, or the valve's centre): whether the ram holds or drifts is EM's safety decision (H9)"))
        elif not h[1]: out.append(("REVIEW", "HYD-008", cyl, f"held by {h[0]}: waits on EM's \"Safety sign-off: ... · EM <date>\" (a safety function, OPERATING.md 12)"))
        else: out.append(("PASS", "HYD-008", cyl, f"held by {h[0]}, EM's Safety sign-off on file"))
    return out

def check(C): return joints(C) + open_ports(C) + pressures(C) + hoses(C) + reliefs(C) + holding(C)

# ------------------------------------------------------------------ files
def _rows(p): return [r for r in csv.DictReader(open(p, encoding="utf-8")) if r and list(r.values())[0] and not list(r.values())[0].startswith("#")] if os.path.isfile(p) else []

def _params(s):
    d = {}
    for kv in (s or "").split(";"):
        if "=" in kv: k, v = kv.split("=", 1); d[k.strip()] = v.strip()
    return d

def circuit(folder, P, rating_of=None):
    """the Circuit of an assembly folder and its built prims, or None when it has no hyd.csv"""
    if not os.path.isfile(os.path.join(folder, "hyd.csv")): return None
    piv = getattr(P, "pivots", {})
    ports = {e: dict(unit=p["unit"], gender=p.get("gender"), role=p.get("role")) for e, p in piv.items() if H.is_hyd(p.get("unit"))}
    J = []
    for i, r in enumerate(_rows(os.path.join(folder, "hyd.csv")), 1):
        q = _params(r.get("params"))
        try: bore = float(q["bore"]) if q.get("bore") else None
        except ValueError: bore = None
        J.append(dict(a=r["from"], b=r.get("to") or None, row=i, line=(q.get("line") or "").upper() or None, hose=q.get("hose") or None,
                      bore=bore, plug=q.get("plug") == "yes", tank=q.get("tank") == "yes"))
    tags = {_tag(e) for e in ports}
    cyl = {}
    for t in tags:
        rod = piv.get(f"{t}.rod")
        if rod and rod.get("kind") == "translate":
            ax = rod.get("axis") or (0, 0, 1); n = sum(a * a for a in ax) ** 0.5 or 1.0
            cyl[t] = abs(ax[2]) / n >= H.VERTICAL
    C = dict(ports=ports, joints=J, rating={}, flow=None, source=None, reliefs=[], tank=None, cylinders=cyl, hold={})
    for r in _rows(os.path.join(folder, "hyd-circuit.csv")):
        k, tag, note = r["key"], r.get("tag") or "", r.get("note") or ""
        if k == "source":
            C["source"] = tag
            try: C["flow"] = float(r.get("value")) if r.get("value") else None
            except ValueError: pass
        elif k == "relief": C["reliefs"].append((tag, H.to_bar(r.get("value"), r.get("unit"))))
        elif k == "tank": C["tank"] = H.to_bar(r.get("value"), r.get("unit"))
        elif k == "cylinder": C["cylinders"][tag] = (r.get("value") or "").strip().lower() == "vertical"
        elif k == "hold":
            m = re.search(r"\bfor\s+([\w.\-]+)", note)
            C["hold"][m.group(1) if m else "*"] = (tag, bool(SIGNED.search(note)))
    C["reliefs"] = [(t, b) for t, b in C["reliefs"] if b is not None]
    for tag in sorted(tags | {j["hose"] for j in J if j["hose"]} | ({C["source"]} if C["source"] else set())):
        _, R = rating_of(P, tag) if rating_of else (None, {})
        g = lambda k: H.to_bar(R[k].get("value"), R[k].get("unit")) if k in R and R[k].get("status") != "NOT ON FILE" else None
        C["rating"][tag] = dict(p_max=g("p_max"), **{k: g(k) for k in ("span",) if k in R})
    return C

def run(aid, P, root):
    from . import v_electrical as E
    C = circuit(os.path.join(root, "assemblies", aid), P, E.rating_of)
    return check(C) if C else []
