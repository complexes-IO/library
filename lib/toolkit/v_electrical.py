"""Electrical checkers of the validation suite (an ERC on the cell's real cables, then ratings on its circuits).
  pins(aid)      PIN-010 every pin a cable lands on has a role on file (element pins.csv, host pins.csv or assembly pins.csv)
  erc(aid)       ERC-0xx nets built pin by pin from connections.csv and lib/standards/cables.csv, checked by role:
                 shorts between potentials, driver conflicts, unpowered loads, lamps no output can drive, contacts that signal
                 nothing, data polarity, safety channels crossed, earth mixed with live conductors, phases on the wrong pins
  ratings(aid)   ELR-0xx from circuits.csv and each element's ratings.csv: overload range covers the motor's full-load current,
                 contactor AC-3 rating, breaker vs load and vs connector / cable, disconnect, voltage, 24 V budget, coil voltage,
                 output channel current
Roles (pins.csv `role`): supply+:<V>:<group> · supply0 · load+:<V>:<group> · load0 · in · out · sw-com · sw-no · sw-nc · lamp+ ·
lamp0 · data:<TD+|TD-|RD+|RD-> · safe-src:<ch> · safe-in:<ch> · safe-contact:<ch> · phase-src:<L> · phase-load:<L> · PE · FE · nc ·
pass (a bulkhead: its host says what the pin carries). The outermost definition wins: assembly over host element over element."""
import csv, importlib.util, math, os
from . import library

ROOT = library.ROOT

def _rows(path):
    return [r for r in csv.DictReader(open(path, encoding="utf-8")) if r and list(r.values())[0] and not list(r.values())[0].startswith("#")] if os.path.isfile(path) else []

def standards():
    con = {}
    for r in _rows(os.path.join(ROOT, "standards", "connectors.csv")): con.setdefault(r["unit"], {})[r["pin"]] = r
    cab = {(r["cable"], r["unit"]): r for r in _rows(os.path.join(ROOT, "standards", "cables.csv"))}
    return con, cab

def _assembly(aid):
    p = os.path.join(ROOT, "assemblies", aid, "assembly.py")
    sp = importlib.util.spec_from_file_location(f"asmE_{aid.replace('-', '_')}", p); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    return m.build(report=False)

def _owner_chain(P, endpoint):
    """[(owner tag, element-or-assembly id, local node)] from the outermost owner to the innermost that contains the endpoint node"""
    tags = {t: e for _, _, t, e in P.owners}; out = []
    for t, e in sorted(tags.items(), key=lambda kv: len(kv[0])):
        if endpoint == t: out.append((t, e, "self"))
        elif endpoint.startswith(t + "."): out.append((t, e, endpoint[len(t) + 1:]))
    return out

def _pins_file(eid):
    for base in (os.path.join(ROOT, "assemblies", eid), os.path.join(library.ELEMENTS, eid)):
        p = os.path.join(base, "pins.csv")
        if os.path.isfile(p): return _rows(p)
    return []

def roles(aid, P, endpoint, unit):
    """pin -> dict(role, signal, rated_A, source, where) for one port endpoint; the outermost definition wins"""
    con, _ = standards(); pins = list(con.get(unit, {}).keys()); found = {}
    chain = [("", aid, endpoint)] + _owner_chain(P, endpoint)                       # the assembly itself first (outermost)
    for tag, eid, local in reversed(chain):                                         # innermost first, outer ones overwrite
        for r in _pins_file(eid):
            if r["port"] != local: continue
            for pin in (pins if r["pin"] == "*" else [r["pin"]]):
                if r["role"] == "pass" and pin in found: continue
                found[pin] = dict(r, where=eid)
    return found

def _conns(aid):
    return list(csv.DictReader(open(os.path.join(ROOT, "assemblies", aid, "connections.csv"), encoding="utf-8"))) if os.path.isfile(os.path.join(ROOT, "assemblies", aid, "connections.csv")) else []

def nets(aid, P=None):
    """the cell's nets: list of dict(row, cable, members=[(endpoint, pin, role-dict)]) and the pin findings"""
    P = P or _assembly(aid); con, cab = standards(); out = []; find = []
    for i, c in enumerate(_conns(aid), 1):
        ends = []
        for e in (c["from"], c["to"]):
            pv = P.pivots.get(e); ends.append((e, pv["unit"] if pv else None))
        (ea, ua), (eb, ub) = ends
        if ua is None or ub is None: continue                                    # pinout reports missing ports
        spec = cab.get((c["cable"], ua))
        if not spec: find.append(("REVIEW", "PIN-020", f"row {i}", f"no wiring map for cable {c['cable']} with unit {ua} (lib/standards/cables.csv)")); continue
        ra, rb = roles(aid, P, ea, ua), roles(aid, P, eb, ub)
        for pair in spec["map"].split():
            pa, pb = pair.split("-")
            ma, mb = ra.get(pa), rb.get(pb)
            for e, p, m in ((ea, pa, ma), (eb, pb, mb)):
                if m is None or m["role"] == "pass": find.append(("REVIEW", "PIN-010", f"{e} pin {p}", "no role on file (pins.csv of the element, its host or the assembly)"))
            out.append(dict(row=i, cable=c["cable"], conn=c, members=[(ea, pa, ma or {}), (eb, pb, mb or {})], rated=spec.get("rated_A")))
    return out, find, P

def _pot(role):
    """the potential a source role puts on a net, or None"""
    if role.startswith("supply+:"): return "+" + role.split(":")[1]
    if role == "supply0": return "0V"
    if role.startswith("phase-src:"): return role.split(":")[1]
    if role in ("PE", "FE"): return "PE"
    return None

def net_rules(R):
    """the rule check on one conductor: R is the list of pin roles on it; returns ([(status, rule, message)], [spare notes])"""
    bad = []; spare = []
    pots = {_pot(r) for r in R if _pot(r)}
    if len(pots) > 1: bad.append(("FAIL", "ERC-001", f"short: {' and '.join(sorted(pots))} on one conductor"))
    groups = {r.split(":")[2] for r in R if r.startswith("supply+:") and r.count(":") == 2}
    if len(groups) > 1: bad.append(("REVIEW", "ERC-002", f"supply groups {' and '.join(sorted(groups))} tied together"))
    drivers = [r for r in R if r in ("out", "sw-no", "sw-nc")]
    if R.count("out") > 1: bad.append(("FAIL", "ERC-003", "two outputs drive one conductor"))
    if "out" in R and pots: bad.append(("FAIL", "ERC-003", "an output is tied to a supply rail"))
    for r in R:
        if r.startswith("load+:") and not any(x.startswith("supply+:") for x in R): bad.append(("FAIL", "ERC-004", "a supply input has no supply on its conductor (device unpowered)"))
        if r == "load0" and "supply0" not in R: bad.append(("FAIL", "ERC-004", "a 0 V input has no 0 V on its conductor"))
        if r == "lamp+":
            if "out" in R: pass
            elif any(x.startswith("supply+:") for x in R): bad.append(("REVIEW", "ERC-005", "lamp tied straight to +24 V: always lit"))
            else: bad.append(("FAIL", "ERC-005", "lamp has no output to drive it" + (" (the other end is an input)" if "in" in R else "")))
        if r == "lamp0" and "supply0" not in R: bad.append(("FAIL", "ERC-005", "lamp return has no 0 V"))
        if r == "sw-com" and not any(x.startswith("supply+:") for x in R): bad.append(("FAIL", "ERC-006", "contact common has no +24 V: the button cannot signal"))
        if r in ("sw-no", "sw-nc") and "in" not in R: bad.append(("FAIL", "ERC-006", "contact output reaches no input"))
        if r == "in":
            if drivers: pass
            elif any(x.startswith("supply+:") for x in R): bad.append(("REVIEW", "ERC-007", "input tied to +24 V: permanently on"))
            else: spare.append("input with nothing to drive it (spare)")
        if r == "out" and not any(x in ("lamp+", "in") or x.startswith("load") for x in R if x != "out"): spare.append("output drives nothing (spare)")
    data = [r for r in R if r.startswith("data:")]
    if data:
        if len(data) != len([r for r in R if r != "nc"]): bad.append(("FAIL", "ERC-008", "data pin on a conductor with a non-data pin"))
        elif len({d[-1] for d in data}) > 1: bad.append(("FAIL", "ERC-008", "data polarity crossed (+ to -)"))
    safe = [r for r in R if r.startswith("safe-")]
    if safe:
        ch = {r.split(":")[1] for r in safe}
        if len(ch) > 1: bad.append(("FAIL", "ERC-009", f"safety channels {' and '.join(sorted(ch))} crossed: redundancy lost"))
        if len(safe) != len([r for r in R if r != "nc"]): bad.append(("FAIL", "ERC-009", "safety conductor shared with a non-safety pin"))
        if any(r.startswith("safe-in") for r in safe) and not any(r.startswith("safe-contact") for r in safe): bad.append(("REVIEW", "ERC-009", "safety input open: the chain never closes"))
    if "PE" in [_pot(r) for r in R] and any(_pot(r) and _pot(r) != "PE" for r in R): pass                                # already a short (ERC-001)
    ph_src = [r.split(":")[1] for r in R if r.startswith("phase-src:")]; ph_ld = [r.split(":")[1] for r in R if r.startswith("phase-load:")]
    if ph_ld and not ph_src: bad.append(("FAIL", "ERC-010", "motor terminal has no phase"))
    if ph_ld and ph_src and set(ph_ld) != set(ph_src): bad.append(("REVIEW", "ERC-010", f"phase {ph_src[0]} lands on {ph_ld[0]}: rotation reverses"))
    return bad, spare

def erc(aid, P=None):
    N, find, P = nets(aid, P); out = list(find); n_ok = 0; spare = []
    for n in N:
        R = [m.get("role", "") for _, _, m in n["members"]]; tag = " ↔ ".join(f"{e} {p}" for e, p, _ in n["members"])
        sig = " / ".join(m.get("signal", "") for _, _, m in n["members"] if m.get("signal"))
        bad, sp = net_rules(R)
        spare += [f"{tag}: {x}" for x in sp]
        for st, rule, msg in bad: out.append((st, rule, f"row {n['row']} {tag}", msg + (f" [{sig}]" if sig else "")))
        if not bad: n_ok += 1
    out.append(("PASS", "ERC-000", aid, f"{n_ok} of {len(N)} conductors pass the rule check" + (f"; {len(spare)} spare channel(s) noted" if spare else "")))
    return out, spare

# ------------------------------------------------------------------ ratings
def rating(eid):
    p = os.path.join(library.ELEMENTS, eid, "ratings.csv"); d = {}
    for r in _rows(p): d[r["property"]] = r
    return d

def _val(R, k):
    r = R.get(k)
    if not r or r.get("status") == "NOT ON FILE" or r.get("value", "") == "": return None
    try: return float(r["value"])
    except ValueError: return r["value"]

def rating_of(P, tag):
    """(element id, ratings) of a placed instance: ratings.csv, then what the element's ratings_for(params) says for this instance"""
    e = _eid(P, tag)
    if not e: return None, {}
    R = dict(rating(e)); m = library.load(e); f = getattr(m, "ratings_for", None)
    if f:
        for k, v in f(**{**getattr(m, "PARAMS", {}), **getattr(P, "params", {}).get(tag, {})}).items(): R[k] = dict(property=k, value=str(v[0]), unit=v[1], status=v[2], source=v[3])
    return e, R

def _eid(P, tag):
    for _, _, t, e in P.owners:
        if t == tag: return e
    return None

def coil_voltage(cv, vout, where):
    """ELR-021 (and PNE-006, a valve coil): a coil or device voltage against its supply's"""
    return ("PASS" if abs(cv - vout) < 0.5 else "FAIL", "ELR-021", where, f"{cv:g} V device on the {vout:g} V supply")

def ratings(aid, P=None):
    P = P or _assembly(aid); path = os.path.join(ROOT, "assemblies", aid, "circuits.csv"); out = []
    if not os.path.isfile(path): return out
    C = {}
    for r in _rows(path): C.setdefault(r["circuit"], []).append(r)
    con, cab = standards()
    for cid, rows in C.items():
        kind = rows[0]["kind"]; V = float(rows[0]["voltage"]); by = {}
        for r in rows: by.setdefault(r["role"], []).append(r["tag"])
        def R(tag): return rating_of(P, tag)
        if kind == "motor-branch":
            e, M = R(by["load"][0]); kw, vm = _val(M, "power"), _val(M, "voltage"); fla = _val(M, "fla")
            if fla: lo = hi = fla; how = f"FLA {fla:g} A on file"
            elif kw and vm:
                k = _val(M, "eta_pf_min") or 0.45
                hi = kw * 1000 / (math.sqrt(3) * vm * k); lo = kw * 1000 / (math.sqrt(3) * vm * 0.95)
                tb = _val(M, "fla_table")
                if tb: hi = max(hi, tb)
                how = f"FLA NOT ON FILE; from {kw:g} kW at {vm:g} V" + (f" and the NEC table ({tb:g} A)" if tb else "") + f" it lies between {lo:.2f} and {hi:.2f} A"; out.append(("REVIEW", "ELR-001", f"{cid} {by['load'][0]}", how + " (read the nameplate FLA into ratings.csv)"))
            else:
                out.append(("REVIEW", "ELR-001", cid, "motor power, voltage and FLA not on file")); continue
            for tag in by.get("overload", []):
                _, O = R(tag); a, b = _val(O, "ir_min"), _val(O, "ir_max")
                if a is None or b is None: out.append(("REVIEW", "ELR-010", tag, "overload range not on file"))
                elif hi < a or lo > b: out.append(("FAIL", "ELR-010", f"{cid} {tag}", f"overload range {a:g}–{b:g} A cannot be set to the motor's current ({how}): it would never trip on a motor overload (IEC 60947-4-1 / NEC 430.32: set at FLA)"))
                elif lo < a or hi > b: out.append(("REVIEW", "ELR-010", f"{cid} {tag}", f"overload range {a:g}–{b:g} A may not cover the motor ({how})"))
                else: out.append(("PASS", "ELR-010", f"{cid} {tag}", f"overload range {a:g}–{b:g} A covers the motor ({how})"))
            for tag in by.get("switching", []):
                _, K = R(tag); ie = _val(K, "ie_ac3")
                if ie is None: out.append(("REVIEW", "ELR-011", tag, "AC-3 rating not on file"))
                else: out.append(("PASS" if ie >= hi else "FAIL", "ELR-011", f"{cid} {tag}", f"AC-3 {ie:g} A {'≥' if ie >= hi else '<'} motor current {hi:.2f} A (IEC 60947-4-1 utilisation category AC-3)"))
            In = None
            for tag in by.get("protective", []):
                _, Q = R(tag); In = _val(Q, "in")
                if In is None: out.append(("REVIEW", "ELR-012", tag, "breaker rating not on file"))
                else: out.append(("PASS" if In >= hi else "FAIL", "ELR-012", f"{cid} {tag}", f"breaker {In:g} A {'carries' if In >= hi else 'cannot carry'} the motor current {hi:.2f} A"))
            for tag in by.get("connector", []) + by.get("cable", []):
                if tag in cab or any(k[0] == tag for k in cab):
                    spec = next(v for k, v in cab.items() if k[0] == tag); ra = spec.get("rated_A")
                    try: ra = float(ra)
                    except (TypeError, ValueError): ra = None
                else:
                    _, X = R(tag); ra = _val(X, "rated_a")
                if ra is None: out.append(("REVIEW", "ELR-013", f"{cid} {tag}", "conductor / connector current rating NOT ON FILE: cannot confirm the breaker protects it"))
                elif In is not None: out.append(("PASS" if ra >= In else "FAIL", "ELR-013", f"{cid} {tag}", f"rated {ra:g} A {'≥' if ra >= In else '<'} breaker {In:g} A (IEC 60364-4-43 / NEC 240.4: the device protects the conductor)"))
            flc = _val(M, "fla_table") or hi                                     # NEC 430.6(A)(1): conductors are sized from the table current
            for tag in by.get("cable", []):
                spec = next((v for k, v in cab.items() if k[0] == tag), None)
                try: ra = float(spec.get("rated_A")) if spec else None
                except (TypeError, ValueError): ra = None
                if ra is None: continue                                          # ELR-013 already asks for the rating
                need = 1.25 * flc
                out.append(("PASS" if ra >= need else "FAIL", "ELR-016", f"{cid} {tag}", f"conductor ampacity {ra:g} A {'≥' if ra >= need else '<'} 125 % of the motor's full-load current, {need:.2f} A from {flc:g} A (NEC 430.22; the table current per 430.6(A)(1))"))
            for tag in by.get("isolation", []):
                _, D = R(tag); ith = _val(D, "ith")
                if ith is None: out.append(("REVIEW", "ELR-014", tag, "disconnect rating not on file"))
                elif In is not None: out.append(("PASS" if ith >= In else "FAIL", "ELR-014", f"{cid} {tag}", f"disconnect {ith:g} A {'≥' if ith >= In else '<'} branch breaker {In:g} A"))
            if vm: out.append(("PASS" if abs(vm - V) / V <= 0.1 else "FAIL", "ELR-015", f"{cid} {by['load'][0]}", f"motor {vm:g} V on a {V:g} V system ({abs(vm - V) / V * 100:.0f} %; NEMA MG 1 / IEC 60034-1 allow ±10 %)"))
            for tag in by.get("connector", []):
                _, X = R(tag); rv = _val(X, "rated_v")
                if rv is not None: out.append(("PASS" if rv >= V else "FAIL", "ELR-015", f"{cid} {tag}", f"connector rated {rv:g} V {'≥' if rv >= V else '<'} {V:g} V"))
        elif kind == "dc-supply":
            e, S = R(by["supply"][0]); iout, vout, der = _val(S, "iout"), _val(S, "vout"), _val(S, "derate") or 1.0
            known, unknown = 0.0, []
            for tag in by.get("load", []):
                _, L = R(tag); i = _val(L, "load_i")
                if i is None: unknown.append(tag)
                else: known += i
                cv = _val(L, "coil_v") or _val(L, "supply_v") or _val(L, "lamp_v") or _val(L, "us_v")
                if cv is not None and vout is not None:
                    out.append(coil_voltage(cv, vout, f"{cid} {tag}"))
            if iout is None: out.append(("REVIEW", "ELR-020", cid, "supply current rating not on file"))
            else:
                cap = iout * der
                if known > cap: out.append(("FAIL", "ELR-020", cid, f"known loads {known:.2f} A exceed {cap:.2f} A ({iout:g} A × {der:g})"))
                elif unknown: out.append(("REVIEW", "ELR-020", cid, f"known loads {known:.2f} A of {cap:.2f} A usable; {len(unknown)} load current(s) NOT ON FILE: {', '.join(unknown)}"))
                else: out.append(("PASS", "ELR-020", cid, f"loads {known:.2f} A ≤ {cap:.2f} A usable ({iout:g} A × {der:g})"))
            for tag in by.get("connector", []):
                pv = P.pivots.get(tag); u = pv["unit"] if pv else None; ra = min((float(r["rated_A"]) for r in con.get(u, {}).values() if r.get("rated_A")), default=None)
                if ra is not None: out.append(("PASS" if ra >= known else "FAIL", "ELR-022", f"{cid} {tag}", f"{u}-coded contact rating {ra:g} A ≥ the {known:.2f} A it feeds"))
    # output channels: each output's rating against the lamp it drives
    N, _, _ = nets(aid, P)
    for n in N:
        (ea, pa, ma), (eb, pb, mb) = n["members"]
        for drv, ld, le in ((ma, mb, eb), (mb, ma, ea)):
            if drv.get("role") == "out" and ld.get("role") == "lamp+":
                host = le.rsplit(".", 1)[0]; lamp = f"{host}.{ld.get('signal', '')}"; e = _eid(P, lamp)
                il = _val(rating(e), "load_i") if e else None; ir = float(drv["rated_A"]) if drv.get("rated_A") else None
                if il is not None and ir is not None: out.append(("PASS" if ir >= il else "FAIL", "ELR-030", f"row {n['row']} {lamp}", f"output {ir:g} A ≥ lamp {il:g} A"))
    return out
