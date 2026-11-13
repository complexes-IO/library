#!/usr/bin/env python3
"""conveyor-stop: a pneumatic conveyor stop (stopper cylinder) for a roller conveyor: a square cylinder body hung under the
conveyor frame by its top flange, with a rod and a stop head that stand up between two rollers and hold a pallet or a package
back. Single acting, spring extended: the spring inside holds the head up (the stop closed) at rest; air into `port-rod` (pneu.NODES'
cylinder end name: air in drives the piston in) pulls the head down below the rollers and lets the load pass. lib/inventory.csv row
`conveyor-stop` (own_design generic, "pneumatic conveyor stop (stopper cylinder)"; used_by conveyor-types-bench), which names no
class. Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC011632 "Pneumatic cylinder" (group
EG015640, 3 features on file). No vendor file was opened; this folder's metadata.json and references/ (a product picked 2026-11-02)
are not used. A stop cylinder's flange and head are not an ISO cylinder interface (no ISO 15552 / 6432 mounting or rod-end thread is
used), so its sizes are design choices. The air port is female NPT 1/8 (ASME B1.20.1, toolkit/pneu.py THREADS and D1), bored plain
at E1 + h, L2 + 2 deep, through a spot-faced boss on the body's +x face into the body. The rod with its stop head (`rod`, translate -z, 0 to the stroke) is the moving part;
the piston, the spring and the seals inside are not modelled. The flange's fixing holes are not cut (a later version, with the
screws once built)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "conveyor-stop", "1.0", "actuator"
TITLE = "pneumatic conveyor stop, generic, single acting spring extended, bore 32, stroke 25, NPT 1/8 female"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Pneumatic cylinder (ETIM 10.0 EC011632), a roller conveyor's single-acting, spring-extended "
            "stopper cylinder (inventory own_design generic); class values in spec.md; air port female NPT 1/8 (ASME B1.20.1, "
            "toolkit/pneu.py THREADS, D1); body, flange, rod and stop head are design choices; no vendor file opened")
ORIGIN = ("the mounting plane: the flange's top face (z = 0) on the rod's axis (x = y = 0); the body hangs below (-z), the rod and "
          "its stop head stand up (+z), the port faces +x")
COMMAND = "CONVEYOR-STOP"
PARAMS = dict()

BODY = 50.0                                # design choice: the square body, 50 x 50
BODY_Z = (-100.0, -9.5)                    # design choice: the body below the flange, 0.5 into it (one solid joint)
FLANGE = (70.0, 90.0, 10.0)                # design choice: the top flange x, y, z (z -10 to 0), screwed under the conveyor frame
NOSE_D, NOSE_TOP = 28.0, 10.0              # design choice: the rod guide on the flange's top, z -0.5 to 10
BORE, STROKE = 32.0, 25.0                  # class values 1 and 2: the piston's bore (not modelled) and the stroke
ROD_D, CLEAR = 16.0, 0.5                   # design choice: the piston rod Ø16, 0.5 clear all round in its bore (the guide)
ROD_Z = (-30.0, 45.5)                      # the rod at rest (extended), its top 0.5 into the stop head
BORE_FLOOR = -61.0                         # the rod's bore ends in the body (piston and spring space below, not modelled)
HEAD = (20.0, 36.0, 15.0)                  # design choice: the stop head x (along the flow), y (across), z; z 45 to 60 at rest
HEAD_Z0 = 45.0
PORT = "NPT1/8"                            # pneu.THREADS (D1): the smallest size, as clamp-sheet's and vacuum's ports
PORT_Z = -25.0                             # design choice: the port near the body's top, above the piston (air in drives it down)
BOSS_D, BOSS_L = 20.0, 3.0                 # design choice: a spot-faced port boss on the body's +x face, 3 proud (the joint plane)
IN = 0.5                                   # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_BODY, MAT_FLANGE, MAT_ROD, MAT_HEAD = "M-ALU-ANOD", "M-GALV", "M-SILVER", "M-STEEL-7035"

_T = pneu.NPT[PORT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4      # Ø E1 + h: the male stub's own diameter (ASME B1.20.1 by its formulas, pneu.NPT)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # L2 + 2: design choice, a run-out past the male's effective thread (tank 2.0)
ROD_BORE = ROD_D + 2 * CLEAR
assert PORT in pneu.THREADS
assert BORE_L >= pneu.NPT[PORT]["engagement"]                           # deeper than a male's make-up (L1 + L3)
assert BODY >= _T["D"] * 25.4 + 2 * 3.0                                  # 3 mm round the pipe OD on the port face
assert BODY - BORE >= 2 * 6.0                                            # 6 mm of wall round the piston's bore
assert BODY / 2 + BOSS_L - BORE_L >= ROD_BORE / 2 + 3.0                # the port's bore ends 3 clear of the rod's bore
assert BOSS_D > 15.68 and BOSS_D - BORE_D >= 2 * 3.0                     # a male's hex (AF 14, corners Ø15.68) seats on the boss; its wall
assert PORT_Z + BOSS_D / 2 + 3.0 <= -FLANGE[2] and PORT_Z - BOSS_D / 2 >= BODY_Z[0]   # the boss on the body face, clear of the flange
assert NOSE_D - ROD_BORE >= 2 * 5.0 and FLANGE[0] > BODY and FLANGE[1] > BODY    # the guide's wall; the flange wider than the body
assert ROD_Z[0] - STROKE - BORE_FLOOR >= 5.0                            # at full stroke the rod stays 5 above its bore's floor
assert HEAD_Z0 - STROKE - NOSE_TOP >= 5.0                               # retracted, the head stays 5 above the guide
assert NOSE_TOP - ROD_Z[0] >= 2 * ROD_D                                 # extended, at least 2 x Ø of rod in its bore (40 >= 32)


def retract_n():
    """the pull-in force in N: P_WORK_MAX (the bench regulator's highest setting, pneu.py) on the piston's rod-side annulus;
    theoretical, the spring's force and friction not deducted"""
    return pneu.P_WORK_MAX / 1000.0 * math.pi * (BORE ** 2 - ROD_D ** 2) / 4.0


def build():
    P = Prims(); b = BODY / 2.0; fx, fy, fz = FLANGE
    body = P.box(MAT_BODY, -b, -b, BODY_Z[0], BODY, BODY, BODY_Z[1] - BODY_Z[0])                          # cylinder body
    flange = P.box(MAT_FLANGE, -fx / 2, -fy / 2, -fz, fx, fy, fz)                                          # top flange
    nose = P.cyl(MAT_BODY, (0, 0, -IN), (0, 0, NOSE_TOP), NOSE_D / 2.0)                                     # rod guide
    P.hole(MAT_BODY, (0, 0, NOSE_TOP + 1.0), (0, 0, -1.0), ROD_BORE / 2.0, nose)                           # the rod's bore, in turn
    P.hole(MAT_FLANGE, (0, 0, 1.0), (0, 0, -fz - 1.0), ROD_BORE / 2.0, flange)                             # through each solid it
    P.hole(MAT_BODY, (0, 0, BODY_Z[1] + 1.0), (0, 0, BORE_FLOOR), ROD_BORE / 2.0, body)                    # crosses, blind in the body
    P.box(f"node:rod|{MAT_HEAD}", -HEAD[0] / 2, -HEAD[1] / 2, HEAD_Z0, HEAD[0], HEAD[1], HEAD[2])          # stop head
    P.cyl(f"node:rod|{MAT_ROD}", (0, 0, ROD_Z[0]), (0, 0, ROD_Z[1]), ROD_D / 2.0)                           # piston rod
    P.pivot("rod", "translate", (0, 0, HEAD_Z0), axis=(0, 0, -1), range=(0, STROKE), unit="mm")            # air pulls it down
    xb = b + BOSS_L                                                                                         # the boss face, the joint plane
    boss = P.cyl(f"node:port-rod|{MAT_FLANGE}", (b - IN, 0, PORT_Z), (xb, 0, PORT_Z), BOSS_D / 2.0)        # port boss
    P.hole(MAT_FLANGE, (xb + 1.0, 0, PORT_Z), (b - IN - 1.0, 0, PORT_Z), BORE_D / 2.0, boss)                # port bore through it
    P.hole(MAT_BODY, (b + 1.0, 0, PORT_Z), (xb - BORE_L, 0, PORT_Z), BORE_D / 2.0, body)                    # and on into the body
    P.pivot("port-rod", "port", (xb, 0, PORT_Z), axis=(1, 0, 0), range=(0, 0), unit=PORT, gender="female", role="work")
    P.collider("body", -fx / 2, -fy / 2, BODY_Z[0], fx, fy, HEAD_Z0 + HEAD[2] - BODY_Z[0])
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="port", az=30, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
