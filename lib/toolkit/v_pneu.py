"""Pneumatic checkers of the validation suite (request pneu-1; the contract is toolkit/pneu.py). They run on an assembly that has an
air circuit on file, and on nothing else:
  assemblies/<aid>/air.csv          from,to,params,note       one air joint per row; `to` empty = left open on purpose (PNE-004 FAILs)
                                                              params: sealant=yes; face_seal=yes; condition=<a planted fault>
  assemblies/<aid>/air-circuit.csv  key,tag,value,unit,note   source (the drop's endpoint in `tag`), supply (default P_SUPPLY),
                                                              set (the regulator setting), dump (the lockable 3/2 dump valve's tag),
                                                              limit (a relief valve's limit on `tag` and what lies downstream of it)
Ports are the placed elements' pivots whose unit is an air unit (pneu.parse). Ratings come from each element's ratings.csv (or its
ratings_for): p_max, p_min, span, with a pressure unit (kPa, psig, bar); lockable (yes) on the dump valve.
The checks are pure functions of a Circuit (dict), so the selftest plants faults without building an element:
  Circuit = dict(ports={endpoint: dict(unit, gender, role, condition)}, joints=[dict(a, b, sealant, face_seal, condition, row)],
                 rating={tag: dict(p_max, p_min, span, lockable)}, supply=kPa, p_set=kPa, limit={tag: kPa}, dump=tag, source=endpoint)
PNE-006 (coil voltage = its supply) is ELR-021 and ELR-020 in v_electrical.ratings (a coil is a `load` in a dc-supply circuit)."""
import csv, os
from . import pneu as PN

def _tag(endpoint): return endpoint.rsplit(".", 1)[0] if "." in endpoint else endpoint

def joints(C):
    """PNE-001 / PNE-002 on every joint, and the joint's state (pneu.mate)"""
    out = []
    for j in C["joints"]:
        if not j.get("b"): continue
        a, b = C["ports"].get(j["a"]), C["ports"].get(j["b"])
        where = f"row {j.get('row', '?')} {j['a']} ↔ {j['b']}"
        if a is None or b is None:
            out.append(("FAIL", "PNE-004", where, f"{j['a'] if a is None else j['b']} is not an air port of a placed element")); continue
        a = dict(a, condition=" ".join(x for x in (a.get("condition"), j.get("condition")) if x))
        r = PN.mate(a, b, sealant=j.get("sealant", False), face_seal=j.get("face_seal", False))
        st, msg = r["check"] if r["check"] else ("FAIL", "; ".join(r["notes"]))
        rule = r["rule"] or "PNE-002"
        if r["state"] == "mismatch": out.append(("FAIL", rule, where, msg))
        elif r["state"] in ("leaking", "pulled-out"):
            declared = bool(j.get("condition") or PN._cond(C["ports"][j["a"]]) or PN._cond(b))
            out.append(("REVIEW" if declared else "FAIL", rule, where, f"{msg}: {r['state']} ({'; '.join(r['notes'])})" + (" (a declared fault)" if declared else "")))
        else: out.append(("PASS", rule, where, f"{msg}: {r['state']}" + (f" ({'; '.join(r['notes'])})" if r["notes"] else "")))
    return out

def open_ports(C):
    """PNE-004 every air port joined (to a counterpart, a plug or a silencer); PNE-005 every exhaust port silenced"""
    out = []; other = {}
    for j in C["joints"]:
        if j.get("b"): other.setdefault(j["a"], []).append(j["b"]); other.setdefault(j["b"], []).append(j["a"])
    for e, p in sorted(C["ports"].items()):
        if p.get("role") in ("silencer", "plug") and e not in other: continue                 # a spare silencer or plug on the bench
        if e not in other: out.append(("FAIL", "PNE-004", e, f"{p['unit']} {p.get('role') or 'port'} left open: uncontrolled release (ISO 4414 clause 5, CHECK)"))
        if p.get("role") == "exhaust":
            to = [C["ports"].get(x, {}).get("role") for x in other.get(e, [])]
            if "silencer" in to: out.append(("PASS", "PNE-005", e, "exhaust silenced"))
            elif to: out.append(("REVIEW", "PNE-005", e, f"exhaust piped to {', '.join(other[e])}: confirm the line ends in a silencer"))
            else: out.append(("FAIL", "PNE-005", e, "exhaust with no silencer (the library's decision: an unsilenced exhaust is the loudest thing on a bench; 29 CFR 1910.95 and ISO 4414's noise clause as background)"))
    return out

def reach(C, tag): return min(C.get("supply") or PN.P_SUPPLY, C.get("limit", {}).get(tag, float("inf")))

def pressures(C):
    """PNE-003 ratings against what can reach a part; PNE-007 the setting within each part's range; PNE-009 gauge spans"""
    out = []; t = PN.TOL_KPA; p_set = C.get("p_set")
    f = lambda k: f"{k:.1f} kPa ({k / PN.PSI_KPA:.1f} psig)"
    for tag, R in sorted(C["rating"].items()):
        p = reach(C, tag)
        if "p_max" in R:
            if R["p_max"] is None: out.append(("REVIEW", "PNE-003", tag, f"pressure rating NOT ON FILE; {f(p)} can reach it"))
            elif R["p_max"] + t < p: out.append(("FAIL", "PNE-003", tag, f"rated {f(R['p_max'])} < {f(p)} that can reach it (a failed regulator passes its inlet; ISO 4414:2010 clause 5, CHECK)"))
            else: out.append(("PASS", "PNE-003", tag, f"rated {f(R['p_max'])} ≥ {f(p)}"))
        if p_set is not None and (R.get("p_min") is not None or R.get("p_max") is not None):
            lo, hi = R.get("p_min"), R.get("p_max")
            if lo is not None and p_set + t < lo: out.append(("FAIL", "PNE-007", tag, f"set {f(p_set)} below its minimum {f(lo)}: it does not shift"))
            elif hi is not None and p_set > hi + t: out.append(("FAIL", "PNE-007", tag, f"set {f(p_set)} above its rating {f(hi)}"))
            else: out.append(("PASS", "PNE-007", tag, f"set {f(p_set)} within its range" + ("" if lo is not None else " (minimum NOT ON FILE)")))
        if R.get("span") is not None:
            s = R["span"]
            if p > s + t: out.append(("FAIL", "PNE-009", tag, f"span {f(s)} < {f(p)} that can reach it: it pegs"))
            elif p > PN.GAUGE_FRACTION * s + t: out.append(("REVIEW", "PNE-009", tag, f"{f(p)} is {p / s * 100:.0f} % of its {f(s)} span, above {PN.GAUGE_FRACTION * 100:.0f} % (Assumption (A), ASME B40.100 NOT ON FILE)"))
            else: out.append(("PASS", "PNE-009", tag, f"{f(p)} is {p / s * 100:.0f} % of its {f(s)} span"))
    if p_set is not None and p_set > PN.P_WORK_MAX + t:
        out.append(("REVIEW", "PNE-007", "circuit", f"set {f(p_set)} above the bench's P_WORK_MAX {f(PN.P_WORK_MAX)}: a circuit above it is EM's decision"))
    return out

def isolation(C):
    """PNE-008 one lockable 3/2 shut-off and dump valve first after the drop"""
    d, src = C.get("dump"), C.get("source"); basis = "29 CFR 1910.147(b), (c)(2)(iii), (d)(5)(i); ISO 4414 clause 5 (CHECK)"
    if not d: return [("FAIL", "PNE-008", "circuit", f"no lockable shut-off and dump valve: the circuit cannot be isolated and exhausted ({basis})")]
    first = [_tag(j["b"] if j["a"] == src else j["a"]) for j in C["joints"] if src and src in (j["a"], j.get("b")) and j.get("b")]
    if d not in first: return [("FAIL", "PNE-008", d, f"the dump valve {d} is not the first element after the drop {src or '(no source on file)'} ({basis})")]
    if (C["rating"].get(d, {}).get("lockable") or "").lower() != "yes": return [("FAIL", "PNE-008", d, f"the dump valve takes no padlock (ratings: lockable) ({basis})")]
    return [("PASS", "PNE-008", d, f"lockable dump valve first after the drop ({basis})")]

def check(C): return joints(C) + open_ports(C) + pressures(C) + isolation(C)

# ------------------------------------------------------------------ files
def _rows(p): return [r for r in csv.DictReader(open(p, encoding="utf-8")) if r and list(r.values())[0] and not list(r.values())[0].startswith("#")] if os.path.isfile(p) else []

def _params(s):
    d = {}
    for kv in (s or "").split(";"):
        if "=" in kv: k, v = kv.split("=", 1); d[k.strip()] = v.strip()
    return d

def circuit(folder, P, rating_of=None):
    """the Circuit of an assembly folder and its built prims, or None when it has no air.csv"""
    if not os.path.isfile(os.path.join(folder, "air.csv")): return None
    ports = {e: dict(unit=p["unit"], gender=p.get("gender"), role=p.get("role"), condition=p.get("condition", ""))
             for e, p in P.pivots.items() if PN.is_air(p.get("unit"))}
    J = []
    for i, r in enumerate(_rows(os.path.join(folder, "air.csv")), 1):
        q = _params(r.get("params"))
        J.append(dict(a=r["from"], b=r.get("to") or None, row=i, sealant=q.get("sealant") == "yes", face_seal=q.get("face_seal") == "yes", condition=q.get("condition", "")))
    C = dict(ports=ports, joints=J, rating={}, supply=None, p_set=None, limit={}, dump=None, source=None)
    for r in _rows(os.path.join(folder, "air-circuit.csv")):
        k, v = r["key"], PN.to_kpa(r.get("value"), r.get("unit"))
        if k == "source": C["source"] = r["tag"]
        elif k == "supply": C["supply"] = v
        elif k == "set": C["p_set"] = v
        elif k == "dump": C["dump"] = r["tag"]
        elif k == "limit": C["limit"][r["tag"]] = v
    tags = {_tag(e) for e in ports}
    for tag in sorted(tags):
        _, R = rating_of(P, tag) if rating_of else (None, {})
        g = lambda k: PN.to_kpa(R[k].get("value"), R[k].get("unit")) if k in R and R[k].get("status") != "NOT ON FILE" else None
        C["rating"][tag] = dict(p_max=g("p_max"), **{k: g(k) for k in ("p_min", "span") if k in R})     # no p_max: NOT ON FILE
        if "lockable" in R: C["rating"][tag]["lockable"] = R["lockable"].get("value", "")
    return C

def run(aid, P, root):
    from . import v_electrical as E
    C = circuit(os.path.join(root, "assemblies", aid), P, E.rating_of)
    return check(C) if C else []
