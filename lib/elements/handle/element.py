#!/usr/bin/env python3
"""handle: pull handle 136 x 42, our own design, built unattended (OPERATING.md 12, own designs; lib/inventory.csv row "handle",
own_design yes, made_of screw-iso4762 x2; no ETIM class on file fits a plain pull handle and no handle standard is in
lib/standards/sources.csv). The handle a hand pulls to open a guard door, a cabinet door, a drawer or a cover: two round legs
Ø12, 30 long, standing on the mounting face 120 apart, and a grip bar 12 x 12 across their ends, 136 long. Each leg's foot carries
a tapped M6 hole, 12 deep, for a socket head cap screw (ISO 4762, the inventory's made_of; a common part not built yet) driven from
behind through the door's clearance hole (the host's, ISO 273). The tapped holes are drawn at the thread's minor diameter, derived
(derive.thread(6.0, 1.0): ISO 68-1, ISO 965-1 6H D1 4.9175). One fixed body, no moving node, no terminal. Every other size is a design
choice. No load claim, no vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "handle", "1.0", "device"
TITLE = "pull handle 136 x 42, own design, two Ø12 legs 120 apart under a 12 x 12 grip bar, 2 x M6 tapped ends (thread derived, ISO 965-1)"
TOOLKIT = "1.3"
BASELINE = ("our own design: pull handle, two Ø12 bright steel legs 30 long standing 120 apart on the mounting face, a 12 x 12 grip bar "
            "136 long across their ends; each foot tapped M6 12 deep for a socket head cap screw (ISO 4762, placed later) from behind "
            "the door, the thread's figures derived (ISO 68-1, ISO 965-1); every other size a design choice; no load claim; no vendor "
            "file opened")
ORIGIN = ("the mounting face plane (y = 0, the door's outer face) at the handle's centre: x = 0 midway between the legs, z = 0 on the "
          "legs' axes; +y away from the door (the legs stand along +y, the grip at y 30 to 42), the grip runs along x, the legs' axes "
          "are the lines x = +-60, z = 0 along y")
COMMAND = "HANDLEPULL"
PARAMS = dict()
LEG_R = 6.0                                # legs Ø12: round bar a hand clears; design choice
LEG_X = 60.0                               # the legs' axes at x +-60 (120 between them): design choice, a hand's width and more between the legs
LEG_H = 30.0                               # the legs stand 30 from the mounting face to the grip's underside: the fingers' room behind the grip (design choice)
GRIP_T = 12.0                              # the grip bar 12 x 12 in section (y 30..42, z +-6): the legs' diameter, so its sides lie flush with the legs' extremes
GRIP_L = 136.0                             # the grip 136 long (x +-68): 8 past each leg's axis, 2 past each leg's outer side
TAP_D1 = 4.9175                            # the tapped M6 holes drawn at the thread's minor diameter D1 (6H min): derived: derive.thread(6.0, 1.0) (ISO 68-1; ISO 965-1 clause 10)
TAP_DEPTH = 12.0                           # each tapped hole 12 deep from the foot (2 x the thread's nominal diameter): design choice

def build():
    P = Prims(); S = "M-SILVER"
    for sx in (-1, 1):
        leg = P.cyl(S, (sx * LEG_X, 0, 0), (sx * LEG_X, LEG_H, 0), LEG_R)                              # leg Ø12, y 0..30, its end face on the grip's underside
        P.hole(S, (sx * LEG_X, -1, 0), (sx * LEG_X, TAP_DEPTH, 0), TAP_D1 / 2, leg)                    # tapped M6 from the foot, 12 deep, at the minor diameter
    P.box(S, -GRIP_L / 2, LEG_H, -GRIP_T / 2, GRIP_L, GRIP_T, GRIP_T)                                   # grip bar x +-68, y 30..42, z +-6
    P.collider("pull", -GRIP_L / 2, 0, -GRIP_T / 2, GRIP_L, LEG_H + GRIP_T, GRIP_T)                    # the whole handle: x +-68, y 0..42, z +-6
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="front", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
