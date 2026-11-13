#!/usr/bin/env python3
"""clamp-sheet: a pneumatic sheet clamp for a turret punch: a C-shaped body screwed to the punch's carriage, a fixed lower jaw the
sheet's edge rests on, and an upper jaw a single-acting piston in the upper arm presses down onto the sheet; a spring inside lifts
it when the air is let out. The punch carries three of them on its carriage (lib/machines-factory.txt, punch-turret: clamp-sheet
x3), each placed by the machine. Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC004755
"Gripper (pneumatic/hydraulic)" (group EG020054 Clamping tools, 3 features on file); lib/inventory.csv row `clamp-sheet`
(own_design generic, "pneumatic sheet clamp (turret punch)"), which names no class. No vendor file was opened. Its sizes are design
choices. The air port `port-cap` (pneu.NODES' cylinder end name: air in closes the jaw) on the upper arm's boss is female NPT 1/8
(ASME B1.20.1, toolkit/pneu.py THREADS and D1), bored plain at E1 + h, L2 + 2 deep, as vacuum's ports. The upper jaw with its rod
(`jaw`, translate -z, 0 to the stroke) is the moving part; the piston, the spring and the seals inside are not modelled. The body's
fixing holes are not cut (a later version, with the screws once built)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "clamp-sheet", "1.0", "actuator"
TITLE = "pneumatic sheet clamp, generic, turret punch, single acting, jaw opening 8, NPT 1/8 female"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Gripper (pneumatic/hydraulic) (ETIM 10.0 EC004755), a turret punch's single-acting pneumatic "
            "sheet clamp (inventory own_design generic); class values in spec.md; air port female NPT 1/8 (ASME B1.20.1, "
            "toolkit/pneu.py THREADS, D1); body, jaws, rod and boss are design choices; no vendor file opened")
ORIGIN = ("the clamping plane: the fixed lower jaw's top face (z = 0) at its front edge (x = 0), centred across the clamp (y = 0); "
          "the body behind (-x), the jaw's mouth open toward +x, the port up (+z)")
COMMAND = "CLAMP-SHEET"
PARAMS = dict()

WIDTH = 50.0                               # design choice: the clamp across (y -25 to 25)
BODY_X, BODY_Z = (-70.0, -40.0), (-30.0, 60.0)   # design choice: the back column; its back face (x = -70) meets the carriage
JAW_X0 = -40.0 - 0.5                       # the lower jaw and the upper arm run 0.5 into the column (one solid joint)
LOWER_Z = (-30.0, 0.0)                     # design choice: the fixed lower jaw, its top face the clamping plane (z = 0)
ARM_Z = (30.0, 60.0)                       # design choice: the upper arm, holding the piston (not modelled) above the jaw
OPEN, STROKE = 8.0, 7.5                    # design choices: the jaw's face 8 above the plane at rest; the stroke stops it 0.5 above
PAD_X, PAD_Y, PAD_TOP = (-33.0, -7.0), 15.0, 20.0   # design choice: the upper jaw 26 x 30 x 12 (z 8 to 20 at rest), centred on the rod
ROD_X, ROD_D = -20.0, 12.0                 # design choice: the piston rod Ø12 on the arm's centre (x = -20)
CLEAR = 0.5                                # design choice: radial clearance of the rod in the arm's bore (the guide; seals not modelled)
ROD_TOP = 55.0                             # the rod's top at rest, 1 below its bore's floor (z = 56); the arm's top at 60
PISTON_D = 32.0                            # design choice: the piston inside the arm (not modelled), for the holding force only
PORT = "NPT1/8"                            # pneu.THREADS (D1): the smallest size, as vacuum's ports
BOSS_D, BOSS_L = 18.0, 12.0                # design choice: the port boss on the arm's top, 12 proud
IN = 0.5                                   # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_BODY, MAT_JAW, MAT_ROD, MAT_BOSS = "M-CAST-BLUE", "M-STEEL-7035", "M-SILVER", "M-GALV"

_T = pneu.NPT[PORT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4      # Ø E1 + h: the male stub's own diameter (ASME B1.20.1 by its formulas, pneu.NPT)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # L2 + 2: design choice, a run-out past the male's effective thread (tank 2.0)
assert PORT in pneu.THREADS
assert BOSS_D > _T["D"] * 25.4 + 6.0                                    # at least 3 mm round the pipe OD
assert BOSS_D - BORE_D >= 2 * 3.0                                       # 3 mm of metal round the bore
assert BOSS_L >= pneu.NPT[PORT]["engagement"] + 2.0 and BORE_L < BOSS_L   # a male makes up inside the boss; the bore blind in it
assert BORE_L >= pneu.NPT[PORT]["engagement"]                          # deeper than a male's make-up (L1 + L3)
assert 0.0 < OPEN - STROKE                                              # the jaw never reaches the lower jaw (the thinnest sheet held)
assert PAD_X[0] > JAW_X0 + 2.0 and PAD_X[1] < 0.0 and PAD_Y < WIDTH / 2.0   # the upper jaw inside the arm's footprint
assert PAD_X[0] < ROD_X - ROD_D / 2.0 and PAD_X[1] > ROD_X + ROD_D / 2.0     # the rod lands on the jaw
assert ROD_TOP - STROKE - ARM_Z[0] >= ROD_D                             # at full stroke the rod keeps at least 1 x Ø in its bore
assert PISTON_D < WIDTH - 2 * 6.0 and PISTON_D < -JAW_X0 - 2 * 3.0      # the piston fits the arm with wall round it


def hold_n():
    """class value 3, holding force in N: P_WORK_MAX (the bench regulator's highest setting, pneu.py) on the Ø32 piston's area;
    theoretical, the spring's force and friction not deducted"""
    return pneu.P_WORK_MAX / 1000.0 * math.pi * PISTON_D ** 2 / 4.0


def build():
    P = Prims(); w = WIDTH / 2.0
    P.box(MAT_BODY, BODY_X[0], -w, BODY_Z[0], BODY_X[1] - BODY_X[0], WIDTH, BODY_Z[1] - BODY_Z[0])           # back column
    P.box(MAT_BODY, JAW_X0, -w, LOWER_Z[0], -JAW_X0, WIDTH, LOWER_Z[1] - LOWER_Z[0])                         # fixed lower jaw
    arm = P.box(MAT_BODY, JAW_X0, -w, ARM_Z[0], -JAW_X0, WIDTH, ARM_Z[1] - ARM_Z[0])                         # upper arm
    P.hole(MAT_BODY, (ROD_X, 0, ARM_Z[0] - 1.0), (ROD_X, 0, ROD_TOP + 1.0), ROD_D / 2.0 + CLEAR, arm)       # the rod's bore, blind
    P.cyl(f"node:jaw|{MAT_ROD}", (ROD_X, 0, PAD_TOP - IN), (ROD_X, 0, ROD_TOP), ROD_D / 2.0)                 # piston rod
    P.box(f"node:jaw|{MAT_JAW}", PAD_X[0], -PAD_Y, OPEN, PAD_X[1] - PAD_X[0], 2 * PAD_Y, PAD_TOP - OPEN)    # upper jaw
    P.pivot("jaw", "translate", (ROD_X, 0, OPEN), axis=(0, 0, -1), range=(0, STROKE), unit="mm")             # closes down by the stroke
    zt = ARM_Z[1] + BOSS_L
    boss = P.cyl(f"node:port-cap|{MAT_BOSS}", (ROD_X, 0, ARM_Z[1] - IN), (ROD_X, 0, zt), BOSS_D / 2.0)       # port boss
    P.hole(MAT_BOSS, (ROD_X, 0, zt + 1.0), (ROD_X, 0, zt - BORE_L), BORE_D / 2.0, boss)                    # its bore, L2 + 2 deep
    P.pivot("port-cap", "port", (ROD_X, 0, zt), axis=(0, 0, 1), range=(0, 0), unit=PORT, gender="female", role="work")
    P.collider("body", BODY_X[0], -w, BODY_Z[0], -BODY_X[0], WIDTH, zt - BODY_Z[0])
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="mouth", az=60, el=15)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
