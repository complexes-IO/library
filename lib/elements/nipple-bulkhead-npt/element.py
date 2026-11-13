#!/usr/bin/env python3
"""nipple-bulkhead-npt: tank feed-through (bulkhead) nipple: a wrench-hex collar on the outside of a tank or panel wall, a straight
threaded shank through a hole in the wall, a locknut that clamps the wall against the collar from the inside, and one male NPT stub
at each end (the line outside, a dip tube or fitting inside). Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design
of ETIM 10.0 EC010488 "Tank feed-through nipple"; the class values it is designed to are in spec.md "## Class values". The NPT
series and units come from toolkit/pneu.py (request pneu-1: D1 NPT threads). Each male stub is nipple-hex-npt's: a plain cylinder
L2 long at the external thread's major diameter at the hand-tight plane, E1 + h, from pneu.NPT (calculated from ASME B1.20.1's
formulas, EM 2026-11-07). The shank's straight thread is a Unified fine thread whose size and pitch are read from
lib/standards/un-threads.csv (ASME B1.1 via FED-STD-H28/2B, on file), drawn plain at its major diameter as the library draws every
thread; an NPT taper can't carry a locknut, so the wall thread is straight. Collar and nut flats, lengths and the wall range are
design choices. No vendor file was opened (pneu-r114)."""
import csv, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "nipple-bulkhead-npt", "1.0", "connector"
TITLE = "generic tank feed-through nipple, male NPT 1/4 both ends, locknut"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic tank feed-through nipple (ETIM 10.0 EC010488), a bulkhead nipple with a hex collar and a "
            "locknut; NPT series from toolkit/pneu.py D1, male stubs from pneu.NPT (calculated from ASME B1.20.1's formulas); the "
            "shank's straight thread from lib/standards/un-threads.csv (ASME B1.1); the collar, nut and lengths are design choices")
ORIGIN = ("the collar's wall face (the face that bears on the wall's outside) y = 0 on the axis (x = z = 0); the wall and the "
          "inside toward +y, port-a's host toward -y, port-b's toward +y")
COMMAND = "NIPPLE-BULKHEAD-NPT"
PARAMS = dict(thread="NPT1/4", wall=3.0)

SHANK = {"NPT1/8": "1/2-20", "NPT1/4": "5/8-18", "NPT3/8": "3/4-16"}   # design choices: the UNF size whose major clears each stub
HEX_AF = {"NPT1/8": 19.0, "NPT1/4": 22.0, "NPT3/8": 27.0}             # design choices: collar and nut flats, >= shank + 6
HEX_D = 1.05            # corners turned to 1.05 x AF (a sharp hex is 1.155 x AF); round(AF x HEX_D) - AF <= 1.5 (cap-hex-npt r106)
COLLAR_L = 8.0          # design choice: collar length along y (fillet pre-flight)
NUT_L = 6.0             # design choice: locknut length along y
WALL_MIN, WALL_MAX = 1.0, 10.0   # design choice: the wall thicknesses the shank grips (sheet to plate)
THREAD_OUT = 3.0        # design choice: thread left past the nut at the thickest wall
SHANK_L = WALL_MAX + NUT_L + THREAD_OUT   # 19: the shank from the collar's wall face to its inner end
STUB_IN = 0.5           # each stub runs 0.5 into the collar or the shank (one solid joint)
MAT = "M-BRASS"         # class value: brass (spec.md Class values)

_UN = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "standards", "un-threads.csv")


def _un_rows():
    with open(_UN, newline="", encoding="utf-8") as f:
        return {r["size"]: r for r in csv.DictReader(l for l in f if not l.startswith("#"))}


UN = _un_rows()


def shank_d(thread):
    """the shank's straight thread's major diameter in mm, D from un-threads.csv"""
    return float(UN[SHANK[thread]]["D_in"]) * 25.4


def stub(thread):
    """(diameter, length) of the NPT male stub in mm from pneu.NPT: the major diameter at the hand-tight plane, E1 + h, and L2"""
    t = pneu.NPT[thread]["table"]
    return (t["E1"] + t["h"]) * 25.4, pneu.NPT[thread]["length"]


for _t in SHANK:
    assert _t in pneu.THREADS and SHANK[_t] in UN and UN[SHANK[_t]]["series"] == "UNF"
    _tb = pneu.NPT[_t]["table"]
    assert shank_d(_t) > (_tb["E2"] + _tb["h"]) * 25.4     # the shank's major clears the stub's largest major diameter (E2 + h)
    assert HEX_AF[_t] >= shank_d(_t) + 6.0                  # collar and nut bear 3 or more round a clearance hole
    assert round(HEX_AF[_t] * HEX_D) - HEX_AF[_t] <= 1.5   # the glb's turned corners stay within the catalogue's rounding (Godot qa)
assert COLLAR_L >= 8.0 and SHANK_L - (WALL_MAX + NUT_L) >= 2.5 * 0.5 * 2


def length(thread="NPT1/4"):
    """overall length, stub end to stub end: L2 + collar + shank + L2 (47.42 for NPT 1/4)"""
    return 2 * stub(thread)[1] + COLLAR_L + SHANK_L


def _hex(P, L, y0, y1, af, d, turn=0.0):
    """a hex prism on the y axis: a cylinder of diameter d with six flats cut at af / 2 (nipple-hex-npt's pattern)"""
    c = P.cyl(L, (0, y0, 0), (0, y1, 0), d / 2.0); lo = min(y0, y1); w = d + 4.0
    for k in range(6):
        t = math.radians(30 + turn + 60 * k); n = (math.sin(t), 0.0, math.cos(t)); tg = (math.cos(t), 0.0, -math.sin(t))
        o = (n[0] * af / 2.0 + tg[0] * w / 2.0, lo - 1.0, n[2] * af / 2.0 + tg[2] * w / 2.0)
        P.cut(L, o, n, (0, 1, 0), (-tg[0], 0.0, -tg[2]), 4.0, abs(y1 - y0) + 2.0, w, c)
    return c


def build(thread="NPT1/4", wall=3.0):
    if thread not in SHANK: raise ValueError(f"thread {thread}: one of {', '.join(SHANK)} (pneu.THREADS, D1)")
    wall = float(wall)
    if not WALL_MIN <= wall <= WALL_MAX: raise ValueError(f"wall {wall}: {WALL_MIN} to {WALL_MAX} mm (the shank's grip)")
    P = Prims(); af = HEX_AF[thread]; d = af * HEX_D
    sd, sl = stub(thread); kd = shank_d(thread)
    _hex(P, MAT, -COLLAR_L, 0.0, af, d)                                                           # collar, outside the wall
    P.cyl(MAT, (0, -STUB_IN, 0), (0, wall + STUB_IN, 0), kd / 2.0)                                # shank through the wall
    _hex(P, MAT, wall, wall + NUT_L, af, d)                                                        # locknut on the wall's inside
    P.cyl(MAT, (0, wall + NUT_L - STUB_IN, 0), (0, SHANK_L, 0), kd / 2.0)                         # shank past the nut
    P.cyl(f"node:port-a|{MAT}", (0, -COLLAR_L - sl, 0), (0, -COLLAR_L + STUB_IN, 0), sd / 2.0)    # NPT male stub a, outside
    P.cyl(f"node:port-b|{MAT}", (0, SHANK_L - STUB_IN, 0), (0, SHANK_L + sl, 0), sd / 2.0)        # NPT male stub b, inside
    P.pivot("port-a", "port", (0, -COLLAR_L, 0), axis=(0, -1, 0), range=(0, 0), unit=thread, gender="male", length=round(sl, 3))
    P.pivot("port-b", "port", (0, SHANK_L, 0), axis=(0, 1, 0), range=(0, 0), unit=thread, gender="male", length=round(sl, 3))
    r = d / 2.0
    P.collider("env", -r, -COLLAR_L - sl, -r, 2 * r, COLLAR_L + SHANK_L + 2 * sl, 2 * r)
    return P


PREVIEWS = [dict(name="three-quarter", az=250, el=25), dict(name="from the inside", az=70, el=25),
            dict(name="wall 10", az=250, el=25, params=dict(wall=10.0)),
            dict(name="thread NPT 1/8", az=250, el=25, params=dict(thread="NPT1/8")),
            dict(name="thread NPT 3/8", az=250, el=25, params=dict(thread="NPT3/8"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
