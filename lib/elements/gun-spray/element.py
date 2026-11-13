#!/usr/bin/env python3
"""gun-spray: a hand-held compressed air paint spray gun, gravity fed from a cup on top, for the paint booths. Generic (OPERATING.md
12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC004054 "Spray gun (compressed air)"; lib/inventory.csv row
`gun-spray` (own_design generic, "paint spray gun"; booth-paint, booth-spray-paint). The row names no class; EC004054 is the class
lib/standards/etim/classes.csv gives for a compressed air spray gun, and its features (reservoir volume, nozzle diameter, round and
wide stream, air volume, max. viscosity, discharge) are a paint gun's, so it fits both systems. Its sizes are design choices, our
own (no vendor file opened). Air enters `port-1` under the handle: a female NPT 1/4 bore (ASME B1.20.1, toolkit/pneu.py THREADS,
D1; ISO 11727 number 1 as pneu.NODES) at E1 + h, L2 + 2 deep, blind in its collar, as regulator 1.0's, so fitting-pushin 2.0's male
stub screws in and a tube-pneu runs to the booth's frl. The trigger (`trigger`, rotate about y at its top rear edge, 0 to 10
degrees) is the one moving part. The paint path (cup, fluid nozzle, needle) and the air passages inside are not modelled: the
nozzle diameter is a class value, not a drawn bore. No safety claim."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "gun-spray", "1.0", "device"
TITLE = "generic paint spray gun, gravity cup 600 ml, nozzle 1.4 mm, 10 bar, NPT 1/4 female air inlet"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic spray gun (compressed air) (ETIM 10.0 EC004054; inventory own_design generic), a gravity fed "
            "paint spray gun; air inlet female NPT 1/4 (ASME B1.20.1, toolkit/pneu.py THREADS, D1), numbered to ISO 11727 (pneu.NODES); "
            "handle, head, air cap, cup and trigger are design choices")
ORIGIN = "joint plane: the air inlet collar's face z = 0 on the inlet's axis (x = y = 0); the hose toward -z, the spray toward +x"
COMMAND = "GUN-SPRAY"
PARAMS = dict()

PORT = "NPT1/4"                         # pneu.THREADS (D1): the bench's drop size, so fitting-pushin 2.0 (NPT 1/4 male) screws in
COLLAR_D, COLLAR_L = 22.0, 16.0         # design choices: the inlet collar under the handle, its face the joint plane z = 0
HANDLE = (-14.0, 28.0, 22.0, 120.0)     # design choices: the grip, x from -14, 28 along x, 22 across y, up to z 120
HEAD = (-40.0, 110.0, 28.0, 40.0)       # design choices: the head (gun body), x from -40, 110 long, 28 across, 40 high, on the grip
CAP_D, CAP_X = 30.0, 20.0               # design choices: the air cap ring in front of the head, 20 long on the spray axis
TIP_D, TIP_X = 6.0, 5.0                 # design choices: the fluid nozzle's tip standing out of the air cap
KNOB_D, KNOB_X = 16.0, 18.0             # design choices: the fluid needle's adjusting knob at the head's rear (fixed in 1.0)
NECK_D, NECK_Z, NECK_XC = 14.0, 15.0, 30.0   # design choices: the cup's neck on the head's top, x = 30
CUP_D, CUP_H, CUP_WALL = 90.0, 110.0, 2.0    # design choices: the gravity cup; the wall for the volume only (modelled solid)
LID_D, LID_H = 94.0, 8.0                # design choice: the cup's lid
TRIG = (34.0, 6.0, 18.0, 42.0)          # design choices: the trigger, x from 34, 6 thick, 18 across y, from z 42 to the head's underside
TRAVEL = 10.0                           # deg: design choice, the trigger's pull (rest 0 to fully pulled)
RESERVOIR_ML = 600.0                    # class value 2 (EF000176 Reservoir volume)
NOZZLE_MM = 1.4                         # class value 3 (EF015067 Nozzle diameter): stated, not drawn
P_MAX_BAR = 10.0                        # class value 7 (EF020449 Max. operating pressure): ratings.csv p_max
IN = 0.5                                # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_BODY, MAT_CAP, MAT_GRIP, MAT_CUP, MAT_TRIG = "M-ALU-ANOD", "M-SILVER", "M-BLACK-PA", "M-CASE-CLEAR", "M-SILVER"

ZH = HANDLE[3]                          # the grip's top = the head's underside
ZC = ZH + HEAD[3] / 2.0                 # the spray axis height
X_HEAD1 = HEAD[0] + HEAD[1]             # the head's front face
Z_CUP0 = ZH + HEAD[3] + NECK_Z          # the cup's foot


def bore():
    """the bore at the male stub's diameter, E1 + h (pneu.NPT, ASME B1.20.1 by its formulas), and its depth L2 + 2"""
    t = pneu.NPT[PORT]["table"]
    return (t["E1"] + t["h"]) * 25.4, pneu.NPT[PORT]["length"] + 2.0


def cup_ml():
    """the cup's inner volume in ml: its bore (less the wall) over its height less the floor"""
    d = CUP_D - 2 * CUP_WALL
    return math.pi / 4 * d * d * (CUP_H - CUP_WALL) / 1000.0


def trigger_reach(deg):
    """the x of the trigger's lowest rear corner when pulled by deg (rotation about +y at its top rear edge)"""
    t = math.radians(deg); h = ZH - TRIG[3]
    return TRIG[0] - h * math.sin(t)


assert PORT in pneu.THREADS
assert COLLAR_D - bore()[0] >= 2 * 3.0                           # at least 3 mm of collar wall round the bore
assert COLLAR_D >= pneu.NPT[PORT]["table"]["D"] * 25.4 + 6.0     # and round the pipe OD
assert COLLAR_L > bore()[1] >= pneu.NPT[PORT]["engagement"]      # bore deeper than make-up, blind inside the collar
assert COLLAR_D <= min(HANDLE[1], HANDLE[2])                     # the collar sits under the grip, inside its section
assert cup_ml() >= RESERVOIR_ML                                  # 627 ml inner: the nominal 600 ml
assert P_MAX_BAR * 100.0 >= pneu.P_SUPPLY                        # PNE-003 (kPa): 1000 >= 689.5
assert trigger_reach(TRAVEL) > HANDLE[0] + HANDLE[1] + 5.0       # fully pulled, the trigger stays 5 clear of the grip's front
assert TRIG[0] > HANDLE[0] + HANDLE[1] and TRIG[0] + TRIG[1] < X_HEAD1 and TRIG[2] < HEAD[2]
assert X_HEAD1 > NECK_XC + NECK_D / 2.0 and NECK_D < CUP_D
assert CUP_D / 2.0 + NECK_XC > X_HEAD1                           # the cup overhangs the head's front, above the air cap:
assert Z_CUP0 > ZC + CAP_D / 2.0                                 # its foot clears the air cap's top


def build():
    P = Prims(); d, l = bore(); hx0, hl, hw, _ = HANDLE; x0, L, W, H = HEAD
    c = P.cyl(f"node:port-1|{MAT_BODY}", (0, 0, 0), (0, 0, COLLAR_L), COLLAR_D / 2.0)                    # inlet collar
    P.hole(MAT_BODY, (0, 0, -1.0), (0, 0, l), d / 2.0, c)                                                  # its NPT 1/4 bore
    P.pivot("port-1", "port", (0, 0, 0), axis=(0, 0, -1), range=(0, 0), unit=PORT, gender="female", role="supply")
    P.box(MAT_GRIP, hx0, -hw / 2.0, COLLAR_L - IN, hl, hw, ZH + IN - (COLLAR_L - IN))                    # grip, into the head
    P.box(MAT_BODY, x0, -W / 2.0, ZH, L, W, H)                                                             # head
    P.cyl(MAT_CAP, (X_HEAD1 - IN, 0, ZC), (X_HEAD1 + CAP_X, 0, ZC), CAP_D / 2.0)                          # air cap ring
    P.cyl(MAT_CAP, (X_HEAD1 + CAP_X - IN, 0, ZC), (X_HEAD1 + CAP_X + TIP_X, 0, ZC), TIP_D / 2.0)          # fluid nozzle tip
    P.cyl(MAT_GRIP, (x0 + IN, 0, ZC), (x0 - KNOB_X, 0, ZC), KNOB_D / 2.0)                                 # needle adjusting knob
    zt = ZH + H
    P.cyl(MAT_CAP, (NECK_XC, 0, zt - IN), (NECK_XC, 0, Z_CUP0 + IN), NECK_D / 2.0)                        # cup neck
    P.cyl(MAT_CUP, (NECK_XC, 0, Z_CUP0), (NECK_XC, 0, Z_CUP0 + CUP_H), CUP_D / 2.0)                       # gravity cup
    P.cyl(MAT_GRIP, (NECK_XC, 0, Z_CUP0 + CUP_H - IN), (NECK_XC, 0, Z_CUP0 + CUP_H + LID_H), LID_D / 2.0)  # lid
    tx, tt, tw, tz = TRIG
    P.box(f"node:trigger|{MAT_TRIG}", tx, -tw / 2.0, tz, tt, tw, ZH - tz)                                  # trigger, face to face under the head
    P.pivot("trigger", "rotate", (tx, 0, ZH), axis=(0, 1, 0), range=(0, TRAVEL), unit="deg")
    xa, xb = x0 - KNOB_X, X_HEAD1 + CAP_X + TIP_X
    xa = min(xa, NECK_XC - LID_D / 2.0); xb = max(xb, NECK_XC + LID_D / 2.0)
    r = LID_D / 2.0
    P.collider("env", xa, -r, 0.0, xb - xa, 2 * r, Z_CUP0 + CUP_H + LID_H)
    return P


PREVIEWS = [dict(name="side", az=270, el=10), dict(name="three-quarter", az=225, el=25), dict(name="inlet", az=300, el=-35)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
