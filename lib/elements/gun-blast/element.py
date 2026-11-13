#!/usr/bin/env python3
"""gun-blast: a hand-held suction blast gun for a blast cabinet. Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral
design of ETIM 10.0 EC004036 "Sand blasting gun (compressed air)"; lib/inventory.csv row `gun-blast` (own_design generic, "blast
gun"; 1 system, the sandblaster of lib/machines-factory.txt: cabinet-blast, hopper-abrasive, nozzle-blast, a foot switch). Air
enters `port-1` under the grip, a female NPT 1/4 bore (ASME B1.20.1, toolkit/pneu.py THREADS, D1; ISO 11727 number 1 as pneu.NODES)
at E1 + h, L2 + 2 deep, blind in its collar, as gun-spray 1.0's, so fitting-pushin 2.0's male stub screws in. The air jet in the
head draws the abrasive by suction through the hose nipple at the rear (from the cabinet's hopper) and drives it out through the
nozzle, which is its own element (inventory nozzle-blast, mech's): the nozzle holder at the front is drawn solid, with no bore,
until the nozzle is placed in a later version (OPERATING.md 12: a host doesn't model holes now for a part it will place later).
The air is switched upstream by the cabinet's foot control, not at the gun, so it has no trigger and no moving node. The abrasive
hose's nipple is drawn with no port node: no abrasive hose element or port unit is on file. Sizes are design choices, our own (no
vendor file opened). No safety claim."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "gun-blast", "1.0", "device"
TITLE = "generic suction blast gun for a blast cabinet, 10 bar, NPT 1/4 female air inlet, rear abrasive hose nipple"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic sand blasting gun (compressed air) (ETIM 10.0 EC004036; inventory own_design generic), a suction "
            "blast gun for a blast cabinet; air inlet female NPT 1/4 (ASME B1.20.1, toolkit/pneu.py THREADS, D1), numbered to ISO 11727 "
            "(pneu.NODES); grip, head, nozzle holder and hose nipple are design choices; the nozzle is its own element (nozzle-blast)")
ORIGIN = "joint plane: the air inlet collar's face z = 0 on the inlet's axis (x = y = 0); the air hose toward -z, the blast toward +x"
COMMAND = "GUN-BLAST"
PARAMS = dict()

PORT = "NPT1/4"                         # pneu.THREADS (D1): the bench's drop size, so fitting-pushin 2.0 (NPT 1/4 male) screws in
COLLAR_D, COLLAR_L = 22.0, 16.0         # design choices: the inlet collar under the grip, its face the joint plane z = 0
GRIP = (-14.0, 28.0, 22.0, 120.0)       # design choices: the grip, x from -14, 28 along x, 22 across y, up to z 120
HEAD = (-45.0, 100.0, 32.0, 44.0)       # design choices: the head (mixing chamber), x from -45, 100 long, 32 across, 44 high
HOLDER_D, HOLDER_L = 36.0, 30.0         # design choices: the nozzle holder (a nut) in front of the head, solid until the nozzle comes
NIPPLE_D, NIPPLE_L = 16.0, 35.0         # design choices: the abrasive hose nipple at the head's rear, on the blast axis
P_MAX_BAR = 10.0                        # class value 4 (EF020449 Max. operating pressure): ratings.csv p_max
IN = 0.5                                # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_BODY, MAT_GRIP, MAT_STEEL = "M-ALU-ANOD", "M-BLACK-PA", "M-SILVER"

ZH = GRIP[3]                            # the grip's top = the head's underside
ZC = ZH + HEAD[3] / 2.0                 # the blast axis height
X_HEAD0, X_HEAD1 = HEAD[0], HEAD[0] + HEAD[1]   # the head's rear and front faces
X_FRONT = X_HEAD1 + HOLDER_L            # the holder's front face
X_REAR = X_HEAD0 - NIPPLE_L             # the nipple's end


def bore():
    """the bore at the male stub's diameter, E1 + h (pneu.NPT, ASME B1.20.1 by its formulas), and its depth L2 + 2"""
    t = pneu.NPT[PORT]["table"]
    return (t["E1"] + t["h"]) * 25.4, pneu.NPT[PORT]["length"] + 2.0


def envelope():
    """class values 10 to 12: length along the blast axis, width across it, height from the inlet face"""
    return X_FRONT - X_REAR, max(HEAD[2], HOLDER_D, NIPPLE_D), ZH + HEAD[3]


assert PORT in pneu.THREADS
assert COLLAR_D - bore()[0] >= 2 * 3.0                           # at least 3 mm of collar wall round the bore
assert COLLAR_D >= pneu.NPT[PORT]["table"]["D"] * 25.4 + 6.0     # and round the pipe OD
assert COLLAR_L > bore()[1] >= pneu.NPT[PORT]["engagement"]      # bore deeper than make-up, blind inside the collar
assert COLLAR_D <= min(GRIP[1], GRIP[2])                         # the collar sits under the grip, inside its section
assert P_MAX_BAR * 100.0 >= pneu.P_SUPPLY                        # PNE-003 (kPa): 1000 >= 689.5
assert HOLDER_D < HEAD[3] and NIPPLE_D < min(HEAD[2], HEAD[3])   # holder and nipple stand within the head's height
assert GRIP[0] > X_HEAD0 and GRIP[0] + GRIP[1] < X_HEAD1 and GRIP[2] < HEAD[2]   # the grip under the head, inside its plan


def build():
    P = Prims(); d, l = bore(); gx0, gl, gw, _ = GRIP; x0, L, W, H = HEAD
    c = P.cyl(f"node:port-1|{MAT_BODY}", (0, 0, 0), (0, 0, COLLAR_L), COLLAR_D / 2.0)                    # inlet collar
    P.hole(MAT_BODY, (0, 0, -1.0), (0, 0, l), d / 2.0, c)                                                  # its NPT 1/4 bore
    P.pivot("port-1", "port", (0, 0, 0), axis=(0, 0, -1), range=(0, 0), unit=PORT, gender="female", role="supply")
    P.box(MAT_GRIP, gx0, -gw / 2.0, COLLAR_L - IN, gl, gw, ZH + IN - (COLLAR_L - IN))                    # grip, into the head
    P.box(MAT_BODY, x0, -W / 2.0, ZH, L, W, H)                                                             # head (mixing chamber)
    P.cyl(MAT_STEEL, (X_HEAD1 - IN, 0, ZC), (X_FRONT, 0, ZC), HOLDER_D / 2.0)                             # nozzle holder, solid
    P.cyl(MAT_STEEL, (X_HEAD0 + IN, 0, ZC), (X_REAR, 0, ZC), NIPPLE_D / 2.0)                              # abrasive hose nipple
    r = HOLDER_D / 2.0
    P.collider("env", X_REAR, -r, 0.0, X_FRONT - X_REAR, 2 * r, ZH + H)
    return P


PREVIEWS = [dict(name="side", az=270, el=10), dict(name="three-quarter", az=225, el=25), dict(name="inlet", az=300, el=-35)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
