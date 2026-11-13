#!/usr/bin/env python3
"""coolant-pump: an immersion coolant pump for a machine tool, vertical, close-coupled. Its square mounting flange sits on a coolant
tank's cover (the tank is its own element, placed by the assembly); the column, the pump housing and the suction strainer hang
below the flange in the coolant; the head with the outlet, the motor and its fan cover stand above it. Generic (OPERATING.md 12, EM
2026-11-07): our own vendor-neutral design of ETIM 10.0 EC010732 "Block pump" (its synonyms in lib/standards/etim/classes.csv
include "Coolant pump"); lib/inventory.csv row `coolant-pump`, own_design generic (12 machines in lib/machines-factory.txt). Its
sizes are design choices. Its one port, the outlet `port-out`, is female NPT 3/8 (ASME B1.20.1; the lane's thread series,
toolkit/pneu.py THREADS and D1, as tank 1.0 took it for its liquid ports): a pivot on the outlet boss's face, axis +x. 2.0 cuts the
port's bore as tank 2.0 and drain-auto 2.0 do (review coolant-pump-1.0.md finding 1): Ø E1 + h (the male stub's own diameter,
fitting-pushin 2.0's rule), L2 + 2 deep, blind inside the boss's proud part, role in features.csv (HOLE-010). 2.0 also adds the
supply port `pwr` (finding 2): the cable entry boss is the node, unit 480V-3P+E, gender none (screw terminals), pins.csv L1 / L2 / L3
(U1 / V1 / W1) and PE, motor-iec71-370w's and hpu-7.5kw 1.0's pattern; no hole in the entry (the gland is placed, never redrawn).
The suction is the strainer's open bottom, not a port. The impeller and shaft inside are not modelled; the supply cable is the
assembly's."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "coolant-pump", "2.1", "device"
TITLE = "generic immersion coolant pump, 0.12 kW 460 V 3-phase 60 Hz, 250 immersion, outlet NPT 3/8 female"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic block pump (ETIM 10.0 EC010732), a vertical immersion coolant pump for a machine tool "
            "(inventory own_design generic); outlet female NPT 3/8 (ASME B1.20.1, toolkit/pneu.py THREADS, D1); flange, head, motor, "
            "column, pump housing and strainer are design choices")
ORIGIN = ("the centre of the mounting flange's underside (the tank cover's top plane, z = 0); the pump's axis along z, the motor "
          "up (+z), the immersed part down (-z); the outlet toward +x, the terminal box toward +y")
COMMAND = "COOLANT-PUMP"
PARAMS = dict()

FLANGE, FLANGE_T = 150.0, 10.0          # design choice: square mounting flange, 150 x 150 x 10 (z 0 to 10)
HEAD_D, HEAD_Z = 100.0, (10.0, 60.0)    # design choice: the pump head (discharge housing) above the flange
MOTOR_D, MOTOR_Z = 120.0, (60.0, 220.0) # design choice: the motor frame (0.12 kW, class value 17)
FAN_D, FAN_Z = 116.0, (220.0, 250.0)    # design choice: the fan cover on the motor's top end (forced cooling, class value 63)
TBOX = (70.0, 60.0, 60.0)               # design choice: terminal box (x, y, z), on the motor's +y side, z 110 to 170
TBOX_Y0, TBOX_Z0 = 45.0, 110.0          # its inner face runs into the motor frame (the frame's surface is at y 48.7 at x = 35)
ENTRY_D, ENTRY_L = 24.0, 12.0           # design choice: cable entry boss on the terminal box's +y face (`pwr`; no thread cut, Notes)
PWR_UNIT = "480V-3P+E"                  # the library's 480 V three-phase + PE power unit (hpu-7.5kw 1.0, motor-iec71-370w)
COLUMN_D, COLUMN_Z = 40.0, (-180.0, 0.0)          # design choice: the column (shaft tube) below the flange
HOUSING_D, HOUSING_Z = 110.0, (-230.0, -180.0)    # design choice: the pump housing (volute) round the impeller
STRAINER_D, STRAINER_Z = 80.0, (-250.0, -230.0)   # design choice: suction strainer, open at the bottom (z = -250)
PORT = "NPT3/8"                         # from pneu.THREADS (ASME B1.20.1), the lane's largest size on file
BOSS_D, BOSS_X0, BOSS_X1, BOSS_Z = 28.0, 40.0, 64.0, 35.0   # design choice: outlet boss Ø28 from inside the head (x 40) to its face (x 64)
IN = 0.5                                # every attached part runs 0.5 into what it sits on (one solid joint)
MAT_CAST, MAT_MOTOR, MAT_FAN, MAT_STEEL = "M-CAST-BLUE", "M-STEEL-7035", "M-BLACK-PA", "M-GALV"
assert PORT in pneu.THREADS and pneu.NPT[PORT]["length"]
assert BOSS_D > pneu.NPT[PORT]["table"]["D"] * 25.4 + 6.0                      # the boss stands at least 3 mm round the pipe OD
assert BOSS_X1 - HEAD_D / 2.0 >= pneu.NPT[PORT]["engagement"] + 2.0            # a male makes up (L1 + L3) inside the boss's proud part
assert BOSS_Z - BOSS_D / 2.0 > HEAD_Z[0] and BOSS_Z + BOSS_D / 2.0 < HEAD_Z[1]  # the boss sits on the head, clear of flange and motor


def bore():
    """the outlet bore (diameter, depth): Ø E1 + h, the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas), and L2 + 2,
    a design choice: a run-out past the male's effective thread (tank 2.0, drain-auto 2.0)"""
    t = pneu.NPT[PORT]["table"]
    return (t["E1"] + t["h"]) * 25.4, pneu.NPT[PORT]["length"] + 2.0


_D, _L = bore()
assert _L >= pneu.NPT[PORT]["engagement"] and _L < BOSS_X1 - HEAD_D / 2.0     # deeper than make-up, blind inside the boss's proud part
assert BOSS_D - _D >= 2 * 3.0                                                  # 3 mm of metal round the bore


def immersion():
    """the immersed length below the flange's underside (class value 64, height of the suction end)"""
    return -STRAINER_Z[0]


def build():
    P = Prims(); f = FLANGE / 2.0
    P.box(MAT_CAST, -f, -f, 0.0, FLANGE, FLANGE, FLANGE_T)                                              # mounting flange
    P.cyl(MAT_CAST, (0, 0, HEAD_Z[0] - IN), (0, 0, HEAD_Z[1]), HEAD_D / 2.0)                           # pump head
    P.cyl(MAT_MOTOR, (0, 0, MOTOR_Z[0] - IN), (0, 0, MOTOR_Z[1]), MOTOR_D / 2.0)                       # motor frame
    P.cyl(MAT_FAN, (0, 0, FAN_Z[0] - IN), (0, 0, FAN_Z[1]), FAN_D / 2.0)                               # fan cover
    P.box(MAT_MOTOR, -TBOX[0] / 2.0, TBOX_Y0, TBOX_Z0, TBOX[0], TBOX[1], TBOX[2])                      # terminal box
    yt = TBOX_Y0 + TBOX[1]; ze = TBOX_Z0 + TBOX[2] / 2.0
    P.cyl(f"node:pwr|{MAT_FAN}", (0, yt - IN, ze), (0, yt + ENTRY_L, ze), ENTRY_D / 2.0)              # cable entry boss
    P.pivot("pwr", "port", (0, yt + ENTRY_L, ze), axis=(0, 1, 0), range=(0, 0), unit=PWR_UNIT, gender="none")   # to screw terminals
    P.cyl(MAT_STEEL, (0, 0, COLUMN_Z[0]), (0, 0, COLUMN_Z[1] + IN), COLUMN_D / 2.0)                    # column
    P.cyl(MAT_CAST, (0, 0, HOUSING_Z[0]), (0, 0, HOUSING_Z[1] + IN), HOUSING_D / 2.0)                  # pump housing
    P.cyl(MAT_STEEL, (0, 0, STRAINER_Z[0]), (0, 0, STRAINER_Z[1] + IN), STRAINER_D / 2.0)              # suction strainer
    boss = P.cyl(f"node:port-out|{MAT_STEEL}", (BOSS_X0, 0, BOSS_Z), (BOSS_X1, 0, BOSS_Z), BOSS_D / 2.0)   # outlet boss
    d, l = bore()
    P.hole(MAT_STEEL, (BOSS_X1 + 1.0, 0, BOSS_Z), (BOSS_X1 - l, 0, BOSS_Z), d / 2.0, boss)             # its bore, L2 + 2 deep
    P.pivot("port-out", "port", (BOSS_X1, 0, BOSS_Z), axis=(1, 0, 0), range=(0, 0), unit=PORT, gender="female")
    P.collider("env", -f, -f, STRAINER_Z[0], FLANGE, f + yt + ENTRY_L, FAN_Z[1] - STRAINER_Z[0])
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=20), dict(name="outlet side", az=60, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
