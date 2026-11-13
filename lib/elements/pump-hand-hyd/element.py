#!/usr/bin/env python3
"""pump-hand-hyd: a hand hydraulic pump for a small shop press: a lever works a plunger in the pump head, which draws oil from the
horizontal reservoir behind it and delivers it through one oil port to a single-acting press cylinder; a release valve on the head's
front lets the oil back into the reservoir. lib/inventory.csv row `pump-hand-hyd` (own_design generic, "hand hydraulic pump"; 1 system,
press-shop-hydraulic, whose line in lib/machines-factory.txt places it with hyd-cylinder-da-40 and hyd-gauge). Generic (OPERATING.md 12, EM
2026-11-07): our own vendor-neutral design of ETIM 10.0 EC004260 "Hand pump (hydraulic)" (group EG020079 Pumps, tier 2), the class
lib/standards/etim/classes.csv gives for it; the row names no class. Its three features are not in class-features.csv (tier 2, on no
inventory row: the case of request pneu-4, lib/requests/core/pneu-4-answer.md), so spec.md's Class values gives the design values under
plain names. No vendor file was opened. Base plate, head, reservoir, lever and knob are design choices; the base's four holes are M8
clearance, medium (ISO 273, lib/standards/holes.csv), the screws the host's. The oil port `port-p` is a plain spot face on the head's
front, unit "hyd-port" (the lane's placeholder, as hold-down's and hyd-flow-control's), its thread open (class B, spec.md Open figures,
not drawn). Two moving parts: the lever (`lever`, rotate about its socket's rear lower edge, 0 to 60°, lifting) and the release knob
(`knob`, rotate about -x, one turn). The plunger, the check valves and the oil inside are not modelled."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "pump-hand-hyd", "1.1", "device"
TITLE = "hand hydraulic pump, generic, lever operated, single-acting outlet, release valve, horizontal reservoir, base mounted"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic hand pump (hydraulic) (ETIM 10.0 EC004260), a lever-operated pump with a horizontal reservoir and "
            "a release valve for a shop press (inventory own_design generic); design values in spec.md; base holes M8 clearance (ISO 273 "
            "medium, lib/standards/holes.csv); port thread and max. pressure not on file (classes B and A, spec.md Open figures); base, "
            "head, reservoir, lever and knob are design choices; no vendor file opened")
ORIGIN = ("the mounting face: the base plate's underside (z = 0), x = 0 at the pump head's front face, y = 0 on the reservoir's axis; "
          "the reservoir and the lever toward +x, the port and the release knob on the head's front (-x)")
COMMAND = "PUMP-HAND-HYD"
PARAMS = dict()

BASE_X, BASE_W, BASE_T = (-10.0, 430.0), 140.0, 8.0   # design choices: the base plate, x -10 to 430, 140 wide, 8 thick
HOLE_D = 9.0                                          # M8 clearance, medium (ISO 273 H13: 9.0 to 9.22; holes.csv)
HOLE_X, HOLE_Y = (10.0, 410.0), 57.5                  # design choice: four holes on a 400 x 115 rectangle
HEAD_L, HEAD_W, HEAD_H = 80.0, 90.0, 110.0            # design choices: the pump head block, x 0 to 80, top at z = 110
RES_D, RES_X = 84.0, (HEAD_L, 410.0)                  # design choices: the reservoir tube Ø84 from the head to x = 410
CAP_D, CAP_X, CAP_TOP = 30.0, 370.0, 98.0             # design choice: the filler / breather cap on the reservoir's top
POST = (5.0, 25.0, 30.0)                              # design choice: the fulcrum post on the head's top, x 5 to 25, 30 wide (y)
HOUSING_D, HOUSING_X = 36.0, 40.0                     # design choice: the plunger housing on the head's top, its axis at x = 40
Z_SEAT = 150.0                                        # design choice: the post's and the housing's top, where the lever seats
SOCKET = (5.0, 70.0, 24.0, 20.0)                      # design choice: the lever's socket, x 5 to 70, 24 wide, 20 high
TUBE_D, GRIP_D, GRIP_X, TIP_X = 25.0, 30.0, 480.0, 560.0   # design choices: the lever tube Ø25 and its grip Ø30 to the tip
LIFT = 60.0                                           # design choice: the lever's swing, 0 (down, at rest) to 60° up
KNOB_D, KNOB_L, KNOB_YZ = 24.0, 14.0, (20.0, 40.0)    # design choice: the release valve's knob on the head's front face
TURNS = 1                                             # design choice: the release knob, shut (0) to open, one turn
SPOT_D, SPOT_T, SPOT_YZ = 26.0, 1.0, (-20.0, 70.0)    # design choice: the oil port's spot face, Ø26, 1 proud of the front face
IN = 0.5                                              # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_BASE, MAT_BODY, MAT_LEVER, MAT_GRIP, MAT_SPOT = "M-STEEL-7035", "M-CAST-BLUE", "M-SILVER", "M-BLACK-PA", "M-STEEL-7035"

Z_RES = BASE_T - IN + RES_D / 2                       # 49.5: the reservoir's axis, its underside 0.5 into the base
Z_LEVER = Z_SEAT + SOCKET[3] / 2                      # 160: the lever tube's axis, mid-socket
assert BASE_X[0] < 0.0 and RES_X[1] < BASE_X[1]       # the head's front and the reservoir's end stand in from the base's ends
assert RES_D / 2 < HEAD_W / 2 and HEAD_W / 2 < BASE_W / 2      # neither the head nor the reservoir is flush with the base's sides
assert HOLE_Y - HOLE_D / 2 - HEAD_W / 2 >= 7.0        # the holes clear the head and the reservoir by 7 (an M8 head's room)
assert BASE_W / 2 - HOLE_Y - HOLE_D / 2 >= 5.0 and HOLE_X[0] - HOLE_D / 2 - BASE_X[0] >= 5.0   # 5 of plate past each hole
assert Z_RES + RES_D / 2 < HEAD_H                     # the reservoir's top below the head's top
assert Z_LEVER - TUBE_D / 2 > CAP_TOP + 30.0          # at rest the lever clears the filler cap by more than 30
assert TUBE_D < SOCKET[3] + 10.0 and TUBE_D > SOCKET[3]   # the tube a little larger than the socket's height (it reads as a sleeve)
assert ((SPOT_YZ[0] - KNOB_YZ[0]) ** 2 + (SPOT_YZ[1] - KNOB_YZ[1]) ** 2) ** 0.5 > (SPOT_D + KNOB_D) / 2 + 20.0   # room for a spanner
assert abs(SPOT_YZ[0]) + SPOT_D / 2 < HEAD_W / 2 - 5.0 and KNOB_YZ[0] + KNOB_D / 2 < HEAD_W / 2 - 5.0


def lever_reach(): return TIP_X - SOCKET[0]           # 555: the pivot to the grip's end


def build():
    P = Prims(); bw, hw = BASE_W / 2, HEAD_W / 2
    base = P.box(MAT_BASE, BASE_X[0], -bw, 0.0, BASE_X[1] - BASE_X[0], BASE_W, BASE_T)              # base plate
    for x in HOLE_X:
        for y in (-HOLE_Y, HOLE_Y):
            P.hole(MAT_BASE, (x, y, -1.0), (x, y, BASE_T + 1.0), HOLE_D / 2, base)                 # M8 clearance, through
    P.box(MAT_BODY, 0.0, -hw, BASE_T - IN, HEAD_L, HEAD_W, HEAD_H - BASE_T + IN)                    # pump head, 0.5 into the base
    P.cyl(MAT_BODY, (RES_X[0] - IN, 0, Z_RES), (RES_X[1], 0, Z_RES), RES_D / 2)                      # reservoir, 0.5 into the head
    P.cyl(MAT_GRIP, (CAP_X, 0, Z_RES + 38.0), (CAP_X, 0, CAP_TOP), CAP_D / 2)                        # filler / breather cap
    P.box(MAT_BODY, POST[0], -POST[2] / 2, HEAD_H - IN, POST[1] - POST[0], POST[2], Z_SEAT - HEAD_H + IN)   # fulcrum post
    P.cyl(MAT_BODY, (HOUSING_X, 0, HEAD_H - IN), (HOUSING_X, 0, Z_SEAT), HOUSING_D / 2)               # plunger housing
    s0, s1, sw, sh = SOCKET
    P.box(f"node:lever|{MAT_LEVER}", s0, -sw / 2, Z_SEAT, s1 - s0, sw, sh)                            # lever socket, face to face
    P.cyl(f"node:lever|{MAT_LEVER}", (s1 - IN, 0, Z_LEVER), (GRIP_X + IN, 0, Z_LEVER), TUBE_D / 2)    # lever tube
    P.cyl(f"node:lever|{MAT_GRIP}", (GRIP_X, 0, Z_LEVER), (TIP_X, 0, Z_LEVER), GRIP_D / 2)            # grip
    P.pivot("lever", "rotate", (s0, 0, Z_SEAT), axis=(0, -1, 0), range=(0, LIFT), unit="deg")        # lifts about the socket's rear lower edge
    ky, kz = KNOB_YZ
    P.cyl(f"node:knob|{MAT_GRIP}", (0, ky, kz), (-KNOB_L, ky, kz), KNOB_D / 2)                       # release knob, face to face
    P.pivot("knob", "rotate", (0, ky, kz), axis=(-1, 0, 0), range=(0, 360 * TURNS), unit="deg")
    py, pz = SPOT_YZ
    P.cyl(f"node:port-p|{MAT_SPOT}", (IN, py, pz), (-SPOT_T, py, pz), SPOT_D / 2)                    # oil port: spot face
    P.pivot("port-p", "port", (-SPOT_T, py, pz), axis=(-1, 0, 0), range=(0, 0), unit="hyd-port", gender="female", role="supply")
    P.collider("body", BASE_X[0], -bw, 0.0, BASE_X[1] - BASE_X[0], BASE_W, Z_SEAT)
    P.collider("lever", s0, -GRIP_D / 2, Z_LEVER - GRIP_D / 2, TIP_X - s0, GRIP_D, GRIP_D)          # z 145 to 175 (the grip)
    P.collider("knob", -KNOB_L, ky - KNOB_D / 2, kz - KNOB_D / 2, KNOB_L, KNOB_D, KNOB_D)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="front", az=270, el=10), dict(name="rear", az=60, el=30)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
