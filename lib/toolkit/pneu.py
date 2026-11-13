"""The pneumatic interface (request pneu-1, answered by the core 2026-11-05): what every compressed-air element shares, the
counterpart of m12.py, std22.py and din.py. Elements take their names, series, units, pressures and states from here, so two halves
built by different elements still meet. It covers compressed air only; liquid process ports (pump, tank, hx, the control-valve's
process side) wait for a process section (request pneu-2).

No pneumatic standard's text is on file. Every size table below starts NOT ON FILE (None) and fills one row at a time from a Stage 0
brief, as m12.py's did; no thread, tube, fitting, sub-base or cylinder dimension is written from memory. A clause marked CHECK is
named from the published catalogue and is to be confirmed when the text is on file. The one exception is NPT: its figures are
calculated from ASME B1.20.1's formulas (EM, 2026-11-07), checked against the Table 2 figures he sent (NPT_INPUTS below).

Decisions (request pneu-1 D1-D8, as answered in lib/requests/core/pneu-1-answer.md):
  D1 threads   every threaded air port on our elements is NPT (ASME B1.20.1-2013, sealed on the thread with sealant on the male), in
               1/8, 1/4 and 3/8. G (ISO 228-1:2000, not sealed on the thread: a face seal) is known only so PNE-002 catches a G part.
               The ISO 15552 cylinder takes NPT ports of the same nominal size: a deliberate difference, recorded in its spec.
  D2 tube      polyurethane tube in inch ODs 5/32, 1/4 and 3/8 in (exact conversions of the size names, not measured figures);
               push-in fittings to ISO 14743:2004, each made for one tube OD and one thread. Metric ODs are known only so PNE-001
               catches the look-alikes (6 mm and 1/4 in). The tube's own standard is ISO 7628 (CHECK: whether it lists inch ODs).
  D3 pressure  kPa gauge inside, psig first on labels. P_SUPPLY 100 psig (Assumption: held by a room regulator and relief valve not
               yet placed); P_WORK_MAX 80 psig, the bench regulator's highest setting. Ratings are checked against what can reach
               a part: P_SUPPLY, unless a relief valve upstream limits it (ISO 4414:2010 clause 5, sub-clause CHECK).
  D4 air       ISO 8573-1:2010 class [7:4:4] is the REQUIREMENT at the bench regulator's outlet; no lubricator. That our filter
               meets particle class 7 is an Assumption until a figure for our filter is on file (a micron rating is not a class).
  D5 cylinders ISO 6432:2015 (bores 8-25) and ISO 15552:2018 (32-320) mounting interfaces and rod-end threads; ports NPT (D1).
  D6 valves    ISO 15407-1:2000 18 mm sub-bases (26 mm above 40 bore); ports numbered to ISO 11727:1999; coils 24 V DC on a male
               M12 A-coded receptacle, pin 4 switched +24 V, pin 3 0 V (io-block-m12-8di8do measure.md:47, manual p. 35).
  D7 symbols   ISO 1219-1:2012 and ISO 1219-2:2012; node names follow ISO 11727 (NODES below).
  D8 sensing   a 2-wire reed switch in the cylinder's slot (IEC 60947-5-2) to a io-block-m12-8di8do type 3 input (IEC 61131-2).

Port frame (as in m12.py): the joint plane at y = 0, the counterpart toward -y, the body toward +y. An air port is a pivot of kind
"port" with `unit` = its thread ("NPT1/8", "G1/8") or its tube OD ("tube-1/4", "tube-6mm"), `gender` (male / female; a tube end
is male, a push-in port female) and `role` (ROLES)."""
import re

PSI_KPA = 6.894757                     # kPa per psi, exact to the 7th figure (1 lbf/in² = 6.894757 kPa)
def psig(v): return v * PSI_KPA        # psig -> kPa gauge
def to_kpa(value, unit):
    """a pressure in kPa gauge from a ratings.csv value and its unit (kPa, psig, psi, bar, MPa); None when it isn't one"""
    try: v = float(value)
    except (TypeError, ValueError): return None
    k = {"kpa": 1.0, "psig": PSI_KPA, "psi": PSI_KPA, "bar": 100.0, "mpa": 1000.0}.get((unit or "").strip().lower())
    return None if k is None else v * k

TOL_KPA = 0.1                          # every pressure comparison allows 0.1 kPa (a 0-100 psig span is 689.476 kPa)
P_SUPPLY = psig(100.0)                 # 689.476 kPa: the highest pressure a bench drop delivers (Assumption: room side not placed)
P_WORK_MAX = psig(80.0)                # 551.581 kPa: the bench regulator's highest setting; a circuit set above it waits for EM
AIR_CLASS = (7, 4, 4)                  # ISO 8573-1:2010 [particles:water:oil], required at the bench regulator's outlet
COIL_V = 24.0                          # V DC: psu-24v-2a4 and io-block-m12-8di8do's outputs (ELR-021 checks it; PNE-006)
GAUGE_FRACTION = 0.75                  # Assumption (A), for EM: a gauge reads at most 75 % of its span (ASME B40.100 guidance, NOT ON
                                       # FILE; the reviewer's reading). PNE-009 only REVIEWs above it, never FAILs on it.

THREADS = ("NPT1/8", "NPT1/4", "NPT3/8")                    # our series (D1)
THREADS_G = ("G1/8", "G1/4", "G3/8", "G1/2")                # known to PNE-002 only
TUBES_IN = {"5/32": 3.96875, "1/4": 6.35, "3/8": 9.525}     # mm: exact conversions of the size names (D2)
TUBES_MM = {"4mm": 4.0, "6mm": 6.0, "8mm": 8.0, "10mm": 10.0, "12mm": 12.0}   # known to PNE-001 only
ROLES = ("supply", "work", "exhaust", "pilot", "gauge", "silencer", "plug")
NODES = dict(supply="port-1", work=("port-2", "port-4"), exhaust=("port-3", "port-5"), coil="coil-14", override="ovr-14",
             led="led-14", cylinder=("port-cap", "port-rod"), station="st<k>-")   # ISO 11727 numbers; cylinder ends by name
STATES = ("sealed", "leaking", "pulled-out", "mismatch", "open", "blocked")
CONDITIONS = ("no-sealant", "no-face-seal", "no-oring", "angled-cut", "punctured", "short-insert", "collet-open")

# NPT, ASME B1.20.1 Table 2, our three sizes: CALCULATED values (EM, 2026-11-07: "calculated values"), until a licensed Table 2
# is on file (lib/standards/sources.csv, asme-b1.20.1). D (pipe OD), n (threads per inch) and L1 (hand-tight engagement: a
# committee figure, no formula) are the Table 2 figures EM sent 2026-11-07; everything else follows from B1.20.1's formulas and
# the 1:16 taper on the diameter (its 3.1). The figures he sent cross-check them: their "E0" column equals E0 + L1/16 below to
# the fifth decimal for all three sizes (their columns had shifted by one), their L2 equals (0.80D + 6.8)P and their h 0.8P.
# L3 (three threads, the wrench makeup) is not cross-checked: their L3 column was not usable. Inches; NPT[size]["table"].
NPT_INPUTS = {"NPT1/8": (0.405, 27, 0.1615), "NPT1/4": (0.540, 18, 0.2278), "NPT3/8": (0.675, 18, 0.240)}   # D in, n, L1 in
NPT_SOURCE = ("calculated: ASME B1.20.1 formulas (E0 = D - (0.05D + 1.1)P, E1 = E0 + L1/16, E2 = E0 + L2/16, E3 = E0 - L3/16, "
              "L2 = (0.80D + 6.8)P, L3 = 3P, h = 0.8P); D, n and L1 from the Table 2 figures EM sent 2026-11-07; EM 2026-11-07: "
              "use calculated values until a licensed Table 2 is on file")


def npt_calc(D, n, L1):
    """one NPT size's Table 2 figures in inches from its pipe OD D, threads per inch n and hand-tight engagement L1"""
    P = 1.0 / n
    E0 = D - (0.05 * D + 1.1) * P                       # pitch diameter at the small end of the external thread
    L2 = (0.80 * D + 6.8) * P                           # effective external thread length
    L3 = 3.0 * P                                        # wrench makeup, internal thread
    return dict(D=D, n=n, P=P, h=0.8 * P, E0=E0, L1=L1, E1=E0 + L1 / 16.0, L2=L2, E2=E0 + L2 / 16.0, L3=L3, E3=E0 - L3 / 16.0)


def npt_check(t, tol=2e-5):
    """[problems] for one size's Table 2 figures (inches: D, n, E0, E1, E2, L1, L2, h, and E3, L3 when given) against B1.20.1's
    formulas and its 1:16 taper; [] when they hold to the table's rounding. Catches a misread or shifted column."""
    P = 1.0 / t["n"]; out = []
    want = dict(E0=t["D"] - (0.05 * t["D"] + 1.1) * P, E1=t["E0"] + t["L1"] / 16.0, E2=t["E0"] + t["L2"] / 16.0,
                L2=(0.80 * t["D"] + 6.8) * P, h=0.8 * P)
    if "L3" in t: want["L3"] = 3.0 * P
    if "E3" in t and "L3" in t: want["E3"] = t["E0"] - t["L3"] / 16.0
    for k, v in want.items():
        if k in t and abs(t[k] - v) > (5e-5 if k in ("L1", "L2", "L3", "h") else tol):
            out.append(f"{k} {t[k]:.5f}: B1.20.1 gives {v:.5f}")
    if "E3" in t and not t["E3"] < t["E0"]: out.append("E3 is not below E0 (the internal thread's far end is the smaller one)")
    return out


# size tables: NOT ON FILE (None) until a Stage 0 brief fills a cell, with its source; NPT's from the calculation above:
# length = L2 (the male's effective thread), engagement = L1 + L3 (how far a male makes up into the port: hand-tight plus wrench;
# the port's full threads reach at least that deep), opening = E1 (the pitch diameter at the port's face), all in mm. hex_af is a
# fitting's own figure, not the thread standard's.
NPT = {s: dict(length=None, engagement=None, hex_af=None, source=None) for s in THREADS}
for _s, (_D, _n, _L1) in NPT_INPUTS.items():
    _t = npt_calc(_D, _n, _L1)
    NPT[_s].update(length=_t["L2"] * 25.4, engagement=(_t["L1"] + _t["L3"]) * 25.4, opening=_t["E1"] * 25.4, table=_t, source=NPT_SOURCE)
TUBE = {od: dict(id=None, bend_min=None, p_max=None, source=None) for od in TUBES_IN}
PUSHIN = {od: dict(depth=None, release=None, bore=None, source=None) for od in TUBES_IN}
ISO15407_18 = dict(face=None, ports=None, screws=None, source=None)
ISO15552 = {32: dict(rod_thread="M10x1.25", mount=None, port="NPT1/8", source="cylinder/references/source.txt:3 (rod thread); port by D1")}
ISO6432 = {}

def parse(unit):
    """an air unit -> dict(kind='thread'|'tube', series, size, od) or None when the unit is not an air unit"""
    u = (unit or "").replace(" ", "")
    m = re.fullmatch(r"(NPT|G)(\d+/\d+|\d+)", u)
    if m: return dict(kind="thread", series=m.group(1), size=m.group(2), od=None)
    m = re.fullmatch(r"tube-(.+)", u)
    if m:
        s = m.group(1); od = TUBES_IN.get(s, TUBES_MM.get(s))
        return dict(kind="tube", series="inch" if s in TUBES_IN else "metric" if s in TUBES_MM else "?", size=s, od=od)
    return None

def is_air(unit): return parse(unit) is not None

def _cond(p): return set(x for x in re.split(r"[\s,;]+", (p or {}).get("condition", "") or "") if x)

def pne001(a, b):
    """PNE-001: a tube end and a push-in port are the same OD in the same series. (status, message)"""
    pa, pb = parse(a["unit"]), parse(b["unit"])
    if pa["size"] == pb["size"]: return "PASS", f"tube {pa['size']} in a {pb['size']} push-in port"
    near = pa["od"] and pb["od"] and abs(pa["od"] - pb["od"]) < 0.5
    return "FAIL", f"tube {pa['size']} in a {pb['size']} push-in port" + (" (look-alikes: neither holds in the other's collet)" if near else "")

def pne002(a, b):
    """PNE-002: a threaded pair matches in series, nominal size and gender (one male, one female). (status, message)"""
    pa, pb = parse(a["unit"]), parse(b["unit"]); ga, gb = a.get("gender"), b.get("gender")
    if pa["series"] != pb["series"]:
        t = "a tapered NPT male in a parallel G female" if ga == "male" and pa["series"] == "NPT" else "a parallel G male in a tapered NPT female" if ga == "male" else "NPT against G"
        return "FAIL", f"{a['unit']} into {b['unit']}: {t} (ASME B1.20.1 / ISO 228-1: different forms and pitches, no seal)"
    if pa["size"] != pb["size"]: return "FAIL", f"{a['unit']} into {b['unit']}: nominal sizes differ"
    if {ga, gb} != {"male", "female"}: return "FAIL", f"{a['unit']} {ga} to {b['unit']} {gb}: a threaded joint needs one male and one female"
    return "PASS", f"{a['unit']} {ga} into {b['unit']} {gb}"

def mate(a, b=None, sealant=False, face_seal=False):
    """the state of one air joint between ports a and b (dicts with unit, gender, role, condition), as contact.mate is for M12:
    dict(state, rule, check, notes). sealant: on the NPT male's thread; face_seal: the G joint's seal ring."""
    notes = []
    if b is None: return dict(state="open", rule=None, check=None, notes=["no counterpart"])
    pa, pb = parse(a["unit"]), parse(b["unit"])
    if pa is None or pb is None: return dict(state="mismatch", rule=None, check=None, notes=[f"not an air unit: {a['unit']} / {b['unit']}"])
    if pa["kind"] != pb["kind"]: return dict(state="mismatch", rule="PNE-001", check=("FAIL", f"{a['unit']} to {b['unit']}: a tube end and a thread do not meet"), notes=[])
    if pa["kind"] == "tube":
        tube, port = (a, b) if a.get("gender") == "male" else (b, a)
        chk = pne001(tube, port); rule = "PNE-001"
        if chk[0] != "PASS": return dict(state="mismatch", rule=rule, check=chk, notes=[])
        c = _cond(tube) | _cond(port)
        if c & {"short-insert", "collet-open"}: return dict(state="pulled-out", rule=rule, check=chk, notes=sorted(c & {"short-insert", "collet-open"}))
        if c & {"no-oring", "angled-cut", "punctured"}: return dict(state="leaking", rule=rule, check=chk, notes=sorted(c & {"no-oring", "angled-cut", "punctured"}))
        if PUSHIN.get(pa["size"], {}).get("depth") is None: notes.append(f"push-in depth for {pa['size']} NOT ON FILE: insertion not judged")
    else:
        chk = pne002(a, b); rule = "PNE-002"
        if chk[0] != "PASS": return dict(state="mismatch", rule=rule, check=chk, notes=[])
        c = _cond(a) | _cond(b)
        if pa["series"] == "NPT" and (not sealant or "no-sealant" in c): return dict(state="leaking", rule=rule, check=chk, notes=["NPT seals on the thread: no sealant on the male"])
        if pa["series"] == "G" and (not face_seal or "no-face-seal" in c): return dict(state="leaking", rule=rule, check=chk, notes=["G does not seal on the thread: no face seal"])
    if "plug" in (a.get("role"), b.get("role")): return dict(state="blocked", rule=rule, check=chk, notes=notes)
    return dict(state="sealed", rule=rule, check=chk, notes=notes)
