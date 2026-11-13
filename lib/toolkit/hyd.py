"""The hydraulic contract (request pneu-8, the pneumatics lane's answer to the core's hydraulic request of 2026-11-09; coded by core
watch 2026-11-10). Air has toolkit/pneu.py; oil has this file. The checks on an assembly's hyd.csv and hyd-circuit.csv are
toolkit/v_hyd.py (HYD-001..008). No hydraulic standard is in lib/standards/sources.csv yet: every figure a hydraulic standard
tabulates is NOT ON FILE here (None), and the two velocity limits are Assumption (A), EM's.

H1  port: SAE J1926-1 straight-thread O-ring boss (the same port as ISO 11926-1), UN/UNF threads (FED-STD-H28/2B, on file). The
    series choice (against ISO 6149-1, metric) is EM's to confirm, as pneu-1 D1 was (needs-em 2026-11-10); the code changes here.
    A port's unit is "hyd-port" while its dash size is open, "hyd-port-<dash>" (hyd-port-8: dash -8, 1/2 in) once the lane states it.
H2  fitting ends: 37° flare, SAE J514 (ISO 8434-2). Inventory row fitting-hyd-iso8434 keeps its id; its type names the flare.
H3  hose: SAE J517 (ISO 18752 for the pressure classes); two-wire braid on P, A and B. A size's working pressure is the hose element's
    ratings.csv p_max (a rating: NOT ON FILE (A) until on file).
H4  sizes: the press's P, A, B dash -8, T dash -12 (hydraulic.csv). SAE J1926-1 table 1 (dash size, thread, spot face, depth): NOT ON
    FILE (B), DASH below. Dash -12's thread is above lib/standards/un-threads.csv's 1 in limit.
H5  pressure: one relief setting per circuit; every element on the pressure side has p_max >= it; an element whose every port sits on
    the tank line is judged at the tank line's pressure (P_TANK unless hyd-circuit.csv names one).
H6  velocity: P, A and B lines <= 6 m/s, T <= 3 m/s: Assumption (A), EM's (hydraulic.csv's figures; ISO 4413 is not on file, so
    whether it states figures is not known). Suction: NOT ON FILE (A).
H7  fluid: mineral hydraulic oil ISO VG 46, ISO 11158 category HM (HLP 46 is DIN 51524-2's name for it). No check reads the fluid.
H8  hyd-valve-d03's mounting face, ISO 4401-03 (NFPA T3.5.1): NOT ON FILE (B); the valve waits on the standard (OPERATING.md 12).
H9  spool: hyd-valve-d03 parameter `spool` in SPOOLS (centre conditions, not ISO 1219-1 symbols); coils sol-a / sol-b loads; state
    centre / a / b. Which device holds a vertical ram is a safety function: EM's (HYD-008).
H10 meter-out: a flow control that slows a ram pulled by its own weight sits in the line that weight pressurises (the rod end, B, for
    a ram that extends downward); in the inlet line it meters in and the ram can run ahead of the oil.
H11 port marking (request pneu-10 2, core watch 2026-11-11): a hydraulic port's letter or number is ISO 9461's (identification of
    valve ports, subplates, control devices and solenoids), NOT ON FILE (B): lib/standards/sources.csv iso-9461, wanted. ISO 11727
    is the pneumatic standard and never marks an oil port. Until ISO 9461 is on file a hydraulic port is named by its function
    (port-in, port-out, port-pilot; "design: named by its function") and its spec claims no letter or number. Once it is on file,
    PORT_MARKS below takes the marks with their clause, and every hydraulic element's next text minor marks its ports from it, one
    marking for the lane."""
import math
PORT_MARKS = None   # H11: ISO 9461's port identification, NOT ON FILE (B); {function: (mark, clause)} once the document is on file
from .pneu import GAUGE_FRACTION    # Assumption (A), EM's: a gauge reads at most 75 % of its span (HYD-006 as PNE-009)

SERIES = "SAE J1926-1"                 # H1 (EM to confirm the series, needs-em 2026-11-10)
FITTING = "SAE J514 37° flare (ISO 8434-2)"   # H2
HOSE = "SAE J517 / ISO 18752"          # H3
DASH = {4: None, 5: None, 6: None, 8: None, 10: None, 12: None, 16: None}   # SAE J1926-1 table 1: NOT ON FILE (B), every cell
V_LIMIT = {"P": 6.0, "A": 6.0, "B": 6.0, "T": 3.0}     # m/s, H6: Assumption (A), EM's
P_TANK = 10.0                          # bar: the tank line's pressure (hydraulic.csv T), when hyd-circuit.csv names none
LINES = ("P", "A", "B", "T")
SPOOLS = ("closed", "tandem", "float", "open")       # H9: all blocked; P to T with A, B blocked; P blocked with A, B to T; all joined
TOL_BAR = 0.001
VERTICAL = math.cos(math.radians(45.0))              # HYD-008: a cylinder axis within 45° of z is vertical (the proposal's figure)


def is_hyd(unit): return isinstance(unit, str) and (unit == "hyd-port" or unit.startswith("hyd-port-"))


def dash(unit):
    """the port's dash size (int) from its unit, or None while it is open ("hyd-port")"""
    if not is_hyd(unit) or unit == "hyd-port": return None
    try: return int(unit[len("hyd-port-"):])
    except ValueError: return None


def to_bar(value, unit):
    """a pressure in bar gauge from a ratings.csv value and its unit (bar, MPa, kPa, psi, psig); None when it isn't one"""
    try: v = float(value)
    except (TypeError, ValueError): return None
    k = {"bar": 1.0, "mpa": 10.0, "kpa": 0.01, "psi": 0.06894757, "psig": 0.06894757}.get((unit or "").strip().lower())
    return None if k is None else v * k


def velocity(q_lpm, bore_mm):
    """mean velocity in m/s of q l/min through a bore of d mm: v = Q / (π d² / 4)"""
    return (q_lpm / 60000.0) / (math.pi * (bore_mm / 1000.0) ** 2 / 4.0)


def hyd001(a, b):
    """(status, message) of a joined pair of hydraulic ports: opposite genders, and the same dash size (REVIEW while either is open)"""
    ga, gb = (a.get("gender") or "").lower(), (b.get("gender") or "").lower()
    if {ga, gb} != {"male", "female"}: return "FAIL", f"genders {ga or '?'} and {gb or '?'}: a joint is one male into one female ({SERIES})"
    da, db = dash(a.get("unit")), dash(b.get("unit"))
    if da is None or db is None: return "REVIEW", f"{a.get('unit')} to {b.get('unit')}: a dash size is open ({SERIES} table 1 NOT ON FILE (B))"
    if da != db: return "FAIL", f"dash -{da} into dash -{db}: the threads differ ({SERIES})"
    return "PASS", f"dash -{da} into dash -{db} ({SERIES})"
