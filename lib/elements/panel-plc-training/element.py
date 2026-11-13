#!/usr/bin/env python3
"""panel-plc-training: bench-top PLC training panel, sheet steel: an upright back plate 600 wide x 480 high standing on two feet with a
rib behind each, the fixing holes of two 35 mm DIN rails (for the PLC, its I/O, the power supply and the terminals) and a row of six
22.5 mm operator cut-outs below them. Our own design (EM r4 rule): every size is a design choice. What it meets: the DIN rail's panel
screws (din-rail-35 1.1: M5 through the slots at its fix_pitch, slot pattern from the element; clearance Ø5.5, ISO 273 medium H13), the
22.5 mm operator cut-out (op-pb-22-1no, toolkit/std22.py, lib/standards/holes.csv), M6 bench screws (Ø6.6, ISO 273 medium H13). The rails,
the PLC (plc0), the terminals (term-4mm) and the operators are not placed in this version: their holes are modelled (EM's rule).
No rating and no safety claim."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "panel-plc-training", "1.1", "furniture"
TITLE = "bench-top PLC training panel 600 x 480, two DIN-rail rows, six 22.5 mm operator cut-outs, two feet"
TOOLKIT = "1.3"
BASELINE = "our own design (EM r4 rule, 2026-11-05): no product matched; every size a design choice; mates the 35 mm rail's M5 panel screws (din-rail-35), 22.5 mm operators (op-pb-22-1no), M6 screws (ISO 273)"
ORIGIN = "bench device: the bench top z = 0 under the plate's front face y = 0 at its left edge x = 0; the devices mount on the front (-y), where the person stands; the feet reach 150 to each side of the plate"
COMMAND = "PLCTRN"
PARAMS = dict()

W, H, T = 600.0, 480.0, 2.0                     # back plate width (x) and height (z), sheet: design choices
RAIL = library.load("din-rail-35")
RAIL_L = 425.0                                  # rail length: 17 slots, panel screws on the 1st, 9th and 17th (symmetric): design choice
RAIL_X0 = (W - RAIL_L) / 2 + RAIL.SLOT["first"] # 100: the rail's origin (first slot centre) on the plate, rail centred on the width
RAIL_N = int((RAIL_L - 2 * RAIL.SLOT["first"]) // RAIL.SLOT["pitch"]) + 1                      # slots that fit (din-rail-35 build())
RAIL_K = max(1, int(round(RAIL.PARAMS["fix_pitch"] / RAIL.SLOT["pitch"])))                    # a panel screw every K-th slot
RAIL_FIX_X = tuple(RAIL_X0 + i * RAIL.SLOT["pitch"] for i in range(RAIL_N)[::RAIL_K])        # 100, 300, 500
RAIL_Z = (T + 258.0, T + 398.0)                 # rail centrelines, 140 apart (a 105 high device on each, 35 between): design choice; plc0 upper row only (spec.md "Where plc0 goes")
FIX_D = 5.5                                     # M5 clearance, ISO 273 medium (H13), lib/standards/holes.csv
OP_CUT = library.load("op-pb-22-1no").CUTOUT        # 22.5: toolkit/std22.py; lib/standards/holes.csv "22.5 operator cut-out"
OP_X = tuple(100.0 + 80.0 * i for i in range(6))  # six cut-outs at 80 pitch, centred on the width: design choice
OP_Z = T + 108.0                                # cut-out centres 110 above the bench: design choice
FOOT_W, FOOT_D = 60.0, 300.0                    # feet: 60 wide, 300 deep, 150 to each side of the plate: design choice
FOOT_X = (30.0, W - 30.0 - FOOT_W)              # feet 30 in from the plate's ends
RIB_D, RIB_H = 148.0, 150.0                     # rib behind the plate on each foot's outer edge: design choice
BENCH_D = 6.6                                   # M6 clearance, ISO 273 medium (H13), lib/standards/holes.csv
BENCH_Y = (-120.0, 120.0)                       # two bench screws per foot, on the foot's centre line: design choice
MAT = "M-STEEL-7035"

def build():
    P = Prims()
    for fx in FOOT_X:                                                                   # feet, on the bench
        f = P.box(MAT, fx, -FOOT_D / 2, 0, FOOT_W, FOOT_D, T)
        for y in BENCH_Y: P.hole(MAT, (fx + FOOT_W / 2, y, -1.0), (fx + FOOT_W / 2, y, T + 1.0), BENCH_D / 2, f)
    pl = P.box(MAT, 0, 0, T, W, T, H)                                                   # back plate, standing on the feet
    for z in RAIL_Z:
        for x in RAIL_FIX_X: P.hole(MAT, (x, -1.0, z), (x, T + 1.0, z), FIX_D / 2, pl)
    for x in OP_X: P.hole(MAT, (x, -1.0, OP_Z), (x, T + 1.0, OP_Z), OP_CUT / 2, pl)
    for rx in (FOOT_X[0], FOOT_X[1] + FOOT_W - T):                                       # ribs behind the plate, on the feet's outer edges
        P.box(MAT, rx, T, T, T, RIB_D, RIB_H)
    P.collider("body", 0, -FOOT_D / 2, 0, W, FOOT_D, T + H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=230, el=20), dict(name="back ribs and feet", az=40, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
