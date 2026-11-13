#!/usr/bin/env python3
"""regulator: an inline compressed air pressure regulator for a bench air line: a relieving diaphragm regulator that reduces
the supply to an adjustable outlet pressure, set with the knob on its bonnet. Generic (OPERATING.md 12, EM 2026-11-07): our own
vendor-neutral design of ETIM 10.0 EC010122 "Pressure reducing valve", synonym "Compressed air regulator"; lib/inventory.csv row
`regulator`, own_design generic (pneumatic-trainer and test-bench-pneumatic: the bench air line; heat-exchanger-loop and
process-skid: the control air of control-valve's actuator, never the loop's liquid; pneu-7-answer.md item 2). Its sizes are
design choices. Air enters `port-1` (female NPT 1/4 on the inlet boss's left face, ISO 11727 number 1 as pneu.NODES) and leaves
`port-2` (female NPT 1/4 on the right face, number 2); `port-g` (female NPT 1/4 on the front face, role gauge) takes gauge-p
(placed, never redrawn), downstream of the seat. The adjusting knob on top (`knob`) is the one moving part. Threads ASME
B1.20.1 (toolkit/pneu.py THREADS, D1); each port's bore as tank 2.0's: Ø E1 + h (the male stub's own diameter, fitting-pushin
2.0 and gauge-p), L2 + 2 deep, blind in its boss, role in features.csv (HOLE-010). The diaphragm, spring, seat and the bonnet's
relief vent are not modelled."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "regulator", "1.1", "device"
TITLE = "generic compressed air pressure regulator, relieving, adjustable, NPT 1/4 female inlet, outlet and gauge port"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic pressure reducing valve (ETIM 10.0 EC010122, synonym compressed air regulator), an inline "
            "relieving regulator with an adjusting knob (inventory own_design generic); ports female NPT (ASME B1.20.1, "
            "toolkit/pneu.py THREADS, D1), inlet and outlet numbered to ISO 11727 (pneu.NODES); body, bonnet and knob are design choices")
ORIGIN = ("the centre of port-1's joint plane on the inlet boss's left face (where the supply fitting meets it); the air flows "
          "in along +x, z up")
COMMAND = "REGULATOR"
PARAMS = dict()

PORT = "NPT1/4"                       # from pneu.THREADS (D1): inlet, outlet and gauge, the bench's FRL and gauge size (pneu.py D3)
BOSS_D, BOSS_L = 20.0, 14.0           # design choices: each port's round boss, its diameter and length along the port's axis
BODY = (40.0, 40.0, 40.0)             # design choice: the regulator body x, y, z (anodised aluminium), between the port bosses
BONNET_D, BONNET_L = 36.0, 30.0       # design choice: the spring bonnet on the body's top face
KNOB_D, KNOB_H = 30.0, 16.0           # design choice: the adjusting knob on the bonnet
WALL = 3.0                            # design choice: at least 3 mm of metal round each port's pipe OD
IN = 0.5                              # each fixed part runs 0.5 into the one it sits on (one solid joint)
TURNS = 5                             # design choice: the knob's travel from the spring unloaded to the top of the range
MAT_BODY, MAT_KNOB = "M-ALU-ANOD", "M-BLACK-PA"
P_MAX_BAR = 10.0                      # class value 20 (EF020100 Max. inlet pressure): ratings.csv p_max
P_OUT_BAR = (0.5, 7.0)                # class value 21 (EF024003 Reduced pressure): the outlet's setting range

assert PORT in pneu.THREADS
assert BOSS_D >= pneu.NPT[PORT]["table"]["D"] * 25.4 + 2 * WALL      # 3 mm round each port's pipe OD
assert BOSS_L >= pneu.NPT[PORT]["length"] + 2.0                       # a male's effective thread L2 fits in each boss
assert BOSS_L >= pneu.NPT[PORT]["engagement"] + 2.0                   # and its make-up depth L1 + L3
assert BOSS_D < min(BODY[1], BODY[2]) and BOSS_D < min(BODY[0], BODY[2])   # each boss inside the face it sits on
assert BONNET_D < min(BODY[0], BODY[1]) and KNOB_D < BONNET_D              # the bonnet on the top face, the knob on the bonnet
assert P_MAX_BAR * 100.0 >= pneu.P_SUPPLY and P_OUT_BAR[1] * 100.0 >= pneu.P_WORK_MAX   # PNE-003 (kPa); the range spans P_WORK_MAX
_T = pneu.NPT[PORT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4      # 13.616 for NPT 1/4: the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # L2 (10.205) + 2: design choice, a run-out past the male's effective thread (tank 2.0)
assert BORE_L >= pneu.NPT[PORT]["engagement"] and BORE_L < BOSS_L     # deeper than make-up, blind inside its boss
assert BOSS_D - BORE_D >= 2 * WALL                                    # 3 mm of boss wall round each bore


def frame():
    """the main levels: body x span and centre, the outlet face, the gauge face, the bonnet top"""
    bx, by, bz = BODY
    x0, x1 = BOSS_L, BOSS_L + bx                          # body, right of the inlet boss
    xc = (x0 + x1) / 2.0                                  # the bonnet's and the gauge port's centre line
    x2 = x1 + BOSS_L                                      # outlet face
    yg = -by / 2.0 - BOSS_L                               # gauge face
    zk = bz / 2.0 + BONNET_L                              # bonnet top = knob seat
    return x0, x1, xc, x2, yg, zk


def build():
    P = Prims(); bx, by, bz = BODY
    x0, x1, xc, x2, yg, zk = frame()
    b1 = P.cyl(f"node:port-1|{MAT_BODY}", (0, 0, 0), (x0 + IN, 0, 0), BOSS_D / 2.0)                       # inlet boss, 0.5 into the body
    P.box(MAT_BODY, x0, -by / 2, -bz / 2, bx, by, bz)                                                       # body
    b2 = P.cyl(f"node:port-2|{MAT_BODY}", (x1 - IN, 0, 0), (x2, 0, 0), BOSS_D / 2.0)                       # outlet boss
    bg = P.cyl(f"node:port-g|{MAT_BODY}", (xc, -by / 2 + IN, 0), (xc, yg, 0), BOSS_D / 2.0)                # gauge boss, front face
    P.cyl(MAT_BODY, (xc, 0, bz / 2 - IN), (xc, 0, zk), BONNET_D / 2.0)                                    # spring bonnet, top
    P.cyl(f"node:knob|{MAT_KNOB}", (xc, 0, zk), (xc, 0, zk + KNOB_H), KNOB_D / 2.0)                       # adjusting knob, seated on top
    P.hole(MAT_BODY, (-1.0, 0, 0), (BORE_L, 0, 0), BORE_D / 2.0, b1)                                     # bores: 1 outside each face,
    P.hole(MAT_BODY, (x2 + 1.0, 0, 0), (x2 - BORE_L, 0, 0), BORE_D / 2.0, b2)                            # L2 + 2 into its boss
    P.hole(MAT_BODY, (xc, yg - 1.0, 0), (xc, yg + BORE_L, 0), BORE_D / 2.0, bg)
    P.pivot("port-1", "port", (0, 0, 0), axis=(-1, 0, 0), range=(0, 0), unit=PORT, gender="female", role="supply")
    P.pivot("port-2", "port", (x2, 0, 0), axis=(1, 0, 0), range=(0, 0), unit=PORT, gender="female", role="work")
    P.pivot("port-g", "port", (xc, yg, 0), axis=(0, -1, 0), range=(0, 0), unit=PORT, gender="female", role="gauge")
    P.pivot("knob", "rotate", (xc, 0, zk), axis=(0, 0, 1), range=(0, 360 * TURNS), unit="deg")
    P.collider("env", 0.0, yg, -bz / 2, x2, by / 2 - yg, zk + KNOB_H + bz / 2)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="gauge side", az=300, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
