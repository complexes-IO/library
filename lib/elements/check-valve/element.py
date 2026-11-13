#!/usr/bin/env python3
"""check-valve: an inline check (non-return) valve, two female NPT ports of one size, flow from port 1 to port 2 only. Generic
(OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC011469 "Check valve"; lib/inventory.csv row
`check-valve`, own_design generic, made_of fitting-pushin x2 (a fitting placed in each port, in an assembly). Its sizes are design
choices. Its ports are female NPT (ASME B1.20.1; the lane's thread series, toolkit/pneu.py THREADS and D1), numbered to ISO 11727
as pneu.NODES does (1 the inlet, 2 the outlet): `port-1` and `port-2`, each a pivot on its hex end's face, the valve's axis along
y. 2.0 cuts each port's bore as tank 2.0 and gas-regulator 2.0 do (review check-valve-1.0.md finding 1): Ø E1 + h (the male
stub's own diameter, fitting-pushin 2.0 and gauge-p), L2 + 2 deep, blind in its hex end, role in features.csv (HOLE-010). The
poppet and spring inside are not modelled (nothing moves outside the body)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "check-valve", "2.0", "device"
TITLE = "generic check valve, inline, NPT 1/4 female both ends, flow port 1 to port 2"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic check valve (ETIM 10.0 EC011469), an inline non-return valve (inventory own_design generic); "
            "ports female NPT (ASME B1.20.1, toolkit/pneu.py THREADS, D1), numbered to ISO 11727 (pneu.NODES); hex ends and body "
            "are design choices")
ORIGIN = "the centre of the valve on its axis; the axis along y, flow toward +y (port-1 at -y, port-2 at +y), z up"
COMMAND = "CHECK-VALVE"
PARAMS = dict(thread="NPT1/4")

HEX_AF = {"NPT1/8": 17.0, "NPT1/4": 22.0, "NPT3/8": 26.0}   # design choices: wrench flats per thread size (not a standard's figure)
HEX_D = 1.12                                               # corners turned to 1.12 x AF (a sharp hex is 1.155 x AF), design choice
HEX_L = 13.0                                               # design choice: each hex end's length along y (the threaded port's depth)
BODY_D = {"NPT1/8": 22.0, "NPT1/4": 28.0, "NPT3/8": 33.0}  # design choices: the round body holding the poppet and spring
BODY_L = {"NPT1/8": 22.0, "NPT1/4": 26.0, "NPT3/8": 30.0}  # design choices: its length between the hex ends
WALL = 3.0                                                 # design choice: at least 3 mm of metal at the flats round the pipe OD
IN = 0.5                                                   # the body runs 0.5 into each hex end (one solid joint)
MAT = "M-BRASS"                                            # bare brass, hex ends and body
CRACK_MBAR = 100                                           # design choice: opening (cracking) pressure, class value 32

for _t in HEX_AF:
    assert _t in pneu.THREADS and pneu.NPT[_t]["length"]
    assert HEX_AF[_t] >= pneu.NPT[_t]["table"]["D"] * 25.4 + 2 * WALL     # 3 mm at the flats round the pipe OD
    assert HEX_L >= pneu.NPT[_t]["length"] + 2.0                         # a male's effective thread L2 fits in the hex end
    assert HEX_L >= pneu.NPT[_t]["engagement"] + 2.0                     # and its make-up depth L1 + L3
    assert BODY_D[_t] > HEX_AF[_t] * HEX_D                               # the body stands proud of the hex corners


def bore(thread="NPT1/4"):
    """the port bore (diameter, depth): Ø E1 + h, the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas), and L2 + 2,
    a design choice: a run-out past the male's effective thread (tank 2.0)"""
    t = pneu.NPT[thread]["table"]
    return (t["E1"] + t["h"]) * 25.4, pneu.NPT[thread]["length"] + 2.0


for _t in HEX_AF:
    _d, _l = bore(_t)
    assert _l >= pneu.NPT[_t]["engagement"] and _l < HEX_L           # deeper than make-up, blind inside its hex end
    assert HEX_AF[_t] - _d >= 2 * WALL                                  # 3 mm of metal at the flats round each bore


def length(thread="NPT1/4"): return 2 * HEX_L + BODY_L[thread]


def _hex(P, L, y0, y1, af, d, turn=0.0):
    """a hex prism on the y axis: a cylinder of diameter d with six flats cut at af / 2 (gland-m20's and fitting-pushin's pattern)"""
    c = P.cyl(L, (0, y0, 0), (0, y1, 0), d / 2.0); lo = min(y0, y1); w = d + 4.0
    for k in range(6):
        t = math.radians(30 + turn + 60 * k); n = (math.sin(t), 0.0, math.cos(t)); tg = (math.cos(t), 0.0, -math.sin(t))
        o = (n[0] * af / 2.0 + tg[0] * w / 2.0, lo - 1.0, n[2] * af / 2.0 + tg[2] * w / 2.0)
        P.cut(L, o, n, (0, 1, 0), (-tg[0], 0.0, -tg[2]), 4.0, abs(y1 - y0) + 2.0, w, c)
    return c


def build(thread="NPT1/4"):
    if thread not in HEX_AF: raise ValueError(f"thread {thread}: one of {', '.join(HEX_AF)} (pneu.THREADS, D1)")
    P = Prims(); af = HEX_AF[thread]; bl = BODY_L[thread]
    ye = length(thread) / 2.0                                                     # each end face at y = -ye, +ye
    yb = bl / 2.0                                                                 # the body's ends at y = -yb, +yb
    h1 = _hex(P, f"node:port-1|{MAT}", -ye, -yb, af, af * HEX_D)                  # inlet hex end
    h2 = _hex(P, f"node:port-2|{MAT}", yb, ye, af, af * HEX_D)                    # outlet hex end
    P.cyl(MAT, (0, -yb - IN, 0), (0, yb + IN, 0), BODY_D[thread] / 2.0)           # body, 0.5 into each hex end
    bd, bl_ = bore(thread)
    P.hole(MAT, (0, -ye - 1.0, 0), (0, -ye + bl_, 0), bd / 2.0, h1)               # bores: 1 outside each end face,
    P.hole(MAT, (0, ye + 1.0, 0), (0, ye - bl_, 0), bd / 2.0, h2)                 # L2 + 2 into its hex end
    P.pivot("port-1", "port", (0, -ye, 0), axis=(0, -1, 0), range=(0, 0), unit=thread, gender="female")
    P.pivot("port-2", "port", (0, ye, 0), axis=(0, 1, 0), range=(0, 0), unit=thread, gender="female")
    r = max(af * HEX_D, BODY_D[thread]) / 2.0
    P.collider("env", -r, -ye, -r, 2 * r, 2 * ye, 2 * r)
    return P


PREVIEWS = [dict(name="three-quarter, NPT 1/4", az=250, el=25), dict(name="inlet end", az=200, el=10),
            dict(name="NPT 1/8", az=250, el=25, params=dict(thread="NPT1/8")),
            dict(name="NPT 3/8", az=250, el=25, params=dict(thread="NPT3/8"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
