#!/usr/bin/env python3
"""actuator-valve: a pneumatic quarter-turn valve actuator, rack and pinion, double-acting: two pistons in an aluminium body drive
racks on a pinion whose shaft turns the valve below it a quarter turn. Generic (OPERATING.md 12, EM 2026-11-07): our own
vendor-neutral design of ETIM 10.0 EC011197 "Pneumatic servomotor for valves" (synonyms "Pneumatic actuator for valve",
"Actuator for valves"); lib/inventory.csv row `actuator-valve`, own_design generic (gap list 2026-11-05), the actuator valve-ball and
valve-butterfly are made of. Its sizes are design choices. Air into `port-2` (female NPT 1/4 on the front face, ISO 11727 number 2
as pneu.NODES work) drives the pistons apart and turns the shaft 90° counter-clockwise seen from above (open); air into `port-4`
turns it back (closed). The shaft's top and its position indicator are the node `shaft`, the one moving part. The mounting flange
underneath is a plain pad: ISO 5211's bolt circle, threads and drive (square or star) are not on file (spec.md Open figures, class
B), so nothing is cut there, and the VDI/VDE 3845 top interface is not drawn either. Threads ASME B1.20.1 (toolkit/pneu.py THREADS,
D1); each port's bore as regulator 1.0's: Ø (E1 + h) × (L2 + 2) deep, blind in its boss, role in features.csv (HOLE-010). The
pistons, racks, pinion and end stops are inside and not modelled."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "actuator-valve", "1.0", "actuator"
TITLE = "generic pneumatic quarter-turn valve actuator, rack and pinion, double-acting, NPT 1/4 female ports 2 and 4"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic pneumatic servomotor for valves (ETIM 10.0 EC011197), a double-acting rack and pinion "
            "quarter-turn actuator (inventory own_design generic); ports female NPT (ASME B1.20.1, toolkit/pneu.py THREADS, D1) "
            "numbered 2 and 4 to ISO 11727 (pneu.NODES); the ISO 5211 mounting flange and the VDI/VDE 3845 top interface not on "
            "file (class B, plain pad and shaft); body, caps, pad and indicator are design choices; no vendor file opened")
ORIGIN = ("the centre of the mounting pad's underside on the shaft's axis (the face the valve's ISO 5211 flange meets); the shaft "
          "along +z, the body's length along x, the air ports on the front (-y)")
COMMAND = "ACTUATOR-VALVE"
PARAMS = dict()

PORT = "NPT1/4"                       # from pneu.THREADS (D1): the size of the bench valves' work ports (pneu.py D3)
PAD_D, PAD_T = 66.0, 8.0             # design choice: the mounting pad under the body (the ISO 5211 flange's place; its figures open)
BODY = (160.0, 70.0, 70.0)            # design choice: the body x (length), y, z; anodised aluminium, the two cylinders inside
CAP_T, CAP_W = 6.0, 74.0              # design choice: the end caps, thickness along x and their square size (y, z)
BOSS_D, BOSS_L = 20.0, 14.0           # design choice: each port's round boss on the front face (as regulator 1.0's)
PORT_DX = 16.0                        # design choice: port-2 at x = -16, port-4 at x = +16 (32 apart; VDI/VDE 3845's spacing not on file)
SHAFT_D, SHAFT_H = 20.0, 16.0         # design choice: the shaft's top above the body, seated face to face on it (it turns)
IND = (56.0, 10.0, 6.0)               # design choice: the position indicator bar on the shaft's top, x y z (closed: along x)
WALL = 3.0                            # design choice: at least 3 mm of metal round each port's pipe OD
IN = 0.5                              # each fixed part runs 0.5 into the one it sits on (one solid joint)
TURN = 90.0                           # class value 17: max. angle of rotation, closed (0) to open (90)
PISTON_D = 52.0                       # design choice: each piston's diameter (inside the 70 body, not modelled)
PINION_R = 15.0                       # design choice: the pinion's pitch radius (not modelled)
PISTON_L = 30.0                       # design choice: each piston with its rack, along x (not modelled)
MAT_BODY, MAT_CAP, MAT_SHAFT, MAT_IND = "M-ALU-ANOD", "M-BLACK-PA", "M-STEEL-7035", "M-YELLOW-PA"


def torque_nm(p_kpa=pneu.P_WORK_MAX):
    """class value 11: double-acting torque, two pistons on one pinion, theoretical (no friction, no seal drag): 2 × p × A × r"""
    return 2.0 * (p_kpa / 1000.0) * math.pi * PISTON_D ** 2 / 4.0 * PINION_R / 1000.0


def stroke_mm(): return PINION_R * math.radians(TURN)      # class value 15: each piston's travel for the quarter turn


assert PORT in pneu.THREADS
assert BOSS_D >= pneu.NPT[PORT]["table"]["D"] * 25.4 + 2 * WALL      # 3 mm round each port's pipe OD
assert BOSS_L >= pneu.NPT[PORT]["length"] + 2.0                       # a male's effective thread L2 fits in each boss
assert BOSS_L >= pneu.NPT[PORT]["engagement"] + 2.0                   # and its make-up depth L1 + L3
assert 2 * PORT_DX >= BOSS_D + 2.0                                    # the two bosses 2 apart at least, a fitting's hex aside
assert PISTON_D + 2 * 6.0 <= min(BODY[1], BODY[2])                    # 6 of wall round each piston's cylinder (not modelled)
assert PINION_R + PISTON_L + stroke_mm() < BODY[0] / 2.0              # pinion, rack and piston and the travel fit in each half
assert PAD_D <= min(BODY[1], BODY[2]) - 4.0 and SHAFT_D < IND[0]           # the pad under the body, the indicator wider than the shaft
_T = pneu.NPT[PORT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4      # 13.616 for NPT 1/4: the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # L2 (10.205) + 2: design choice, a run-out past the male's effective thread (tank 2.0)
assert BORE_L >= pneu.NPT[PORT]["engagement"] and BORE_L < BOSS_L     # deeper than make-up, blind inside its boss
assert BOSS_D - BORE_D >= 2 * WALL                                    # 3 mm of boss wall round each bore


def frame():
    """the main levels: body bottom and top, its centre height, the front face, the boss faces, the indicator's top"""
    bx, by, bz = BODY
    z0 = PAD_T - IN                       # body bottom, 0.5 into the pad
    z1 = z0 + bz                          # body top = the shaft's seat
    zc = (z0 + z1) / 2.0                  # the ports' and the caps' centre height
    yf = -by / 2.0                        # front face
    yb = yf - BOSS_L                      # the boss faces: the joint planes
    zt = z1 + SHAFT_H + IND[2]            # the indicator's top
    return z0, z1, zc, yf, yb, zt


def build():
    P = Prims(); bx, by, bz = BODY
    z0, z1, zc, yf, yb, zt = frame()
    P.cyl(MAT_BODY, (0, 0, 0), (0, 0, PAD_T), PAD_D / 2.0)                                                  # mounting pad (ISO 5211's place)
    P.box(MAT_BODY, -bx / 2, -by / 2, z0, bx, by, bz)                                                       # body
    for s in (-1, 1):                                                                                       # end caps, 0.5 into the body
        xa = s * (bx / 2 - IN)
        P.box(MAT_CAP, min(xa, xa + s * CAP_T), -CAP_W / 2, zc - CAP_W / 2, CAP_T, CAP_W, CAP_W)
    b2 = P.cyl(f"node:port-2|{MAT_BODY}", (-PORT_DX, yf + IN, zc), (-PORT_DX, yb, zc), BOSS_D / 2.0)     # port-2 boss, front face
    b4 = P.cyl(f"node:port-4|{MAT_BODY}", (PORT_DX, yf + IN, zc), (PORT_DX, yb, zc), BOSS_D / 2.0)       # port-4 boss
    P.cyl(f"node:shaft|{MAT_SHAFT}", (0, 0, z1), (0, 0, z1 + SHAFT_H), SHAFT_D / 2.0)                      # shaft top, seated on the body
    P.box(f"node:shaft|{MAT_IND}", -IND[0] / 2, -IND[1] / 2, z1 + SHAFT_H - IN, IND[0], IND[1], IND[2] + IN)  # indicator bar, along x closed
    P.hole(MAT_BODY, (-PORT_DX, yb - 1.0, zc), (-PORT_DX, yb + BORE_L, zc), BORE_D / 2.0, b2)            # bores: 1 outside each face,
    P.hole(MAT_BODY, (PORT_DX, yb - 1.0, zc), (PORT_DX, yb + BORE_L, zc), BORE_D / 2.0, b4)              # L2 + 2 into its boss
    P.pivot("port-2", "port", (-PORT_DX, yb, zc), axis=(0, -1, 0), range=(0, 0), unit=PORT, gender="female", role="work")
    P.pivot("port-4", "port", (PORT_DX, yb, zc), axis=(0, -1, 0), range=(0, 0), unit=PORT, gender="female", role="work")
    P.pivot("shaft", "rotate", (0, 0, z1), axis=(0, 0, 1), range=(0, TURN), unit="deg")
    xe = bx / 2 - IN + CAP_T
    P.collider("env", -xe, yb, 0.0, 2 * xe, CAP_W / 2 - yb, zt)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="ports", az=270, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
