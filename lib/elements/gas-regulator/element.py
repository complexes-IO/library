#!/usr/bin/env python3
"""gas-regulator: a shielding gas regulator with a flowmeter for a welding station: a preset single-stage pressure reducing valve
that hangs on a gas cylinder's valve, with a tube flowmeter on top that sets and shows the gas flow to the torch. Generic
(OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC010122 "Pressure reducing valve", synonym "Gas
regulator"; lib/inventory.csv row `gas-regulator`, own_design generic (welder-mig-station, welder-plasma, welder-tig-station). Its
sizes are design choices. Gas from the cylinder enters `port-1` (female NPT 1/4 on the body's back face, ISO 11727 number 1 as
pneu.NODES); the cylinder-valve connection itself (a nipple and nut, CGA V-1 in the US) is a part a dimensional standard shapes, not
on file: a separate element, screwed into `port-1`, once its standard is on file (OPERATING.md 12: never generic). `port-g` (female
NPT 1/4 on the left face, role gauge) takes a contents gauge of cylinder-pressure span (placed, never redrawn; gauge-p's 0-160 psig
is for air lines, not this port); `port-2` (female NPT 1/4 on the
flowmeter's top block, ISO 11727 number 2) is the outlet to the torch's gas hose. The flow knob on top (`knob`, a needle valve) is
the one moving part. Threads ASME B1.20.1 (toolkit/pneu.py THREADS, D1). 2.0 cuts each port's bore as tank 2.0 does: Ø E1 + h (the
male stub's own diameter, fitting-pushin 2.0 and gauge-p), L2 + 2 deep, blind in its boss, role in features.csv (HOLE-010); the
diaphragm, spring, needle and float inside are not modelled."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "gas-regulator", "2.2", "device"
TITLE = "generic shielding gas regulator with tube flowmeter, preset, NPT 1/4 female inlet, gauge port and outlet"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic pressure reducing valve (ETIM 10.0 EC010122, synonym gas regulator), a preset shielding gas "
            "regulator with a tube flowmeter (inventory own_design generic); ports female NPT (ASME B1.20.1, toolkit/pneu.py THREADS, "
            "D1), inlet and outlet numbered to ISO 11727 (pneu.NODES); body, bonnet, flowmeter and knob are design choices")
ORIGIN = ("the centre of port-1's joint plane on the inlet boss's back face (where the cylinder connection meets it); the gas "
          "flows in along +y, z up")
COMMAND = "GAS-REGULATOR"
PARAMS = dict()

PORT = "NPT1/4"                       # from pneu.THREADS (D1): inlet, gauge and outlet, the bench's FRL and gauge size (pneu.py D3)
BOSS_D, BOSS_L = 20.0, 14.0           # design choices: each port's round boss, its diameter and length along the port's axis
BODY = (50.0, 40.0, 50.0)             # design choice: the regulator body x, y, z (brass), behind the inlet boss
BONNET_D, BONNET_L = 40.0, 20.0       # design choice: the spring bonnet on the body's front face (preset: no adjusting screw)
BASE = (24.0, 24.0, 25.0)             # design choice: the flowmeter's base block on the body's top face (x, y, z)
TUBE_D, TUBE_L = 22.0, 70.0           # design choice: the flowmeter's clear sight tube, outside diameter and length
CAP = (28.0, 28.0, 24.0)              # design choice: the top block over the tube, holding the needle valve and the outlet
KNOB_D, KNOB_H = 18.0, 12.0           # design choice: the flow knob on the top block
WALL = 3.0                            # design choice: at least 3 mm of metal round each port's pipe OD
IN = 0.5                              # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_BRASS, MAT_ALU, MAT_TUBE, MAT_KNOB = "M-BRASS", "M-ALU-ANOD", "M-CASE-CLEAR", "M-BLACK-PA"
P_MAX_BAR = 300.0                     # class value 20 (EF020100 Max. inlet pressure): ratings.csv p_max
P_OUT_BAR = 3.5                       # class value 21 (EF024003 Reduced pressure): the preset outlet pressure the flowmeter reads at

assert PORT in pneu.THREADS
assert BOSS_D >= pneu.NPT[PORT]["table"]["D"] * 25.4 + 2 * WALL      # 3 mm round each port's pipe OD
assert BOSS_L >= pneu.NPT[PORT]["length"] + 2.0                       # a male's effective thread L2 fits in each boss
assert BOSS_L >= pneu.NPT[PORT]["engagement"] + 2.0                   # and its make-up depth L1 + L3
assert BONNET_D < min(BODY[0], BODY[2]) and BASE[0] < BODY[0] and BASE[1] < BODY[1]   # each part inside the face it sits on
assert TUBE_D < min(BASE[0], BASE[1]) and TUBE_D < min(CAP[0], CAP[1]) and KNOB_D < min(CAP[0], CAP[1])
assert BOSS_D < CAP[2] and BOSS_D < BODY[1]                           # the outlet boss on the top block's side, the gauge boss on the body's
_T = pneu.NPT[PORT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4      # 13.616 for NPT 1/4: the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # L2 (10.205) + 2: design choice, a run-out past the male's effective thread (tank 2.0)
assert BORE_L >= pneu.NPT[PORT]["engagement"] and BORE_L < BOSS_L     # deeper than make-up, blind inside its boss
assert BOSS_D - BORE_D >= 2 * WALL                                    # 3 mm of boss wall round each bore


def frame():
    """the main levels: body y and z, the flowmeter's column centre (y), and its z levels"""
    bx, by, bz = BODY
    y0, y1 = BOSS_L, BOSS_L + by                          # body, behind the inlet boss
    yc = (y0 + y1) / 2.0                                  # the flowmeter column's centre line (x = 0, y = yc)
    zt = bz / 2.0                                         # body top
    zb = zt + BASE[2]                                     # base block top
    zc = zb + TUBE_L                                      # sight tube top = top block bottom
    zk = zc + CAP[2]                                      # top block top = knob seat
    return y0, y1, yc, zt, zb, zc, zk


def build():
    P = Prims(); bx, by, bz = BODY
    y0, y1, yc, zt, zb, zc, zk = frame()
    b1 = P.cyl(f"node:port-1|{MAT_BRASS}", (0, 0, 0), (0, y0 + IN, 0), BOSS_D / 2.0)                    # inlet boss, 0.5 into the body
    P.box(MAT_BRASS, -bx / 2, y0, -bz / 2, bx, by, bz)                                                     # body
    P.cyl(MAT_ALU, (0, y1 - IN, 0), (0, y1 + BONNET_L, 0), BONNET_D / 2.0)                                # spring bonnet, front
    bg = P.cyl(f"node:port-g|{MAT_BRASS}", (-bx / 2 + IN, yc, 0), (-bx / 2 - BOSS_L, yc, 0), BOSS_D / 2.0)   # gauge boss, left face
    P.box(MAT_ALU, -BASE[0] / 2, yc - BASE[1] / 2, zt - IN, BASE[0], BASE[1], BASE[2] + IN)                # flowmeter base block
    P.cyl(MAT_TUBE, (0, yc, zb - IN), (0, yc, zc + IN), TUBE_D / 2.0)                                     # clear sight tube
    P.box(MAT_ALU, -CAP[0] / 2, yc - CAP[1] / 2, zc, CAP[0], CAP[1], CAP[2])                               # top block
    zo = zc + CAP[2] / 2.0
    b2 = P.cyl(f"node:port-2|{MAT_BRASS}", (CAP[0] / 2 - IN, yc, zo), (CAP[0] / 2 + BOSS_L, yc, zo), BOSS_D / 2.0)   # outlet boss, right
    P.cyl(f"node:knob|{MAT_KNOB}", (0, yc, zk), (0, yc, zk + KNOB_H), KNOB_D / 2.0)                       # flow knob, seated on top
    xg, x2 = -bx / 2 - BOSS_L, CAP[0] / 2 + BOSS_L                                                         # the gauge and outlet faces
    P.hole(MAT_BRASS, (0, -1.0, 0), (0, BORE_L, 0), BORE_D / 2.0, b1)                                     # bores: 1 outside each face,
    P.hole(MAT_BRASS, (xg - 1.0, yc, 0), (xg + BORE_L, yc, 0), BORE_D / 2.0, bg)                          # L2 + 2 into its boss
    P.hole(MAT_BRASS, (x2 + 1.0, yc, zo), (x2 - BORE_L, yc, zo), BORE_D / 2.0, b2)
    P.pivot("port-1", "port", (0, 0, 0), axis=(0, -1, 0), range=(0, 0), unit=PORT, gender="female", role="supply")
    P.pivot("port-g", "port", (-bx / 2 - BOSS_L, yc, 0), axis=(-1, 0, 0), range=(0, 0), unit=PORT, gender="female", role="gauge")
    P.pivot("port-2", "port", (CAP[0] / 2 + BOSS_L, yc, zo), axis=(1, 0, 0), range=(0, 0), unit=PORT, gender="female", role="work")
    P.pivot("knob", "rotate", (0, yc, zk), axis=(0, 0, 1), range=(0, 360), unit="deg")
    x0, x1 = -bx / 2 - BOSS_L, CAP[0] / 2 + BOSS_L
    P.collider("env", x0, 0.0, -bz / 2, x1 - x0, y1 + BONNET_L, zk + KNOB_H + bz / 2)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="inlet side", az=300, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
