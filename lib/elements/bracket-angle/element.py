#!/usr/bin/env python3
"""bracket-angle: inner-corner angle bracket for 40 x 40 T-slot profile, one M8 hole per leg. Our own design (EM r4 rule).
What it meets: tslot-40's 40 face and its slot opening 10 (both read from tslot-40 1.0 with library.load: one home for the
figures); and an M8 screw (clearance Ø9.0, ISO 273 medium H13, lib/standards/holes.csv). Its own sizes (leg length, width,
thickness) are design choices. 1.1 (review bracket-angle-1.0 finding 1): the two profile figures marked; the part unchanged.
1.2 (review mech-r109 finding 1 (a)): tslot-40 1.0 is built, so the face and slot are cited from it (slot 10, not the catalogue
record's 8); the part unchanged."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "bracket-angle", "1.2", "plate"
TITLE = "angle bracket 40 for T-slot profile, 2 x M8"
TOOLKIT = "1.3"
BASELINE = "our own design (EM r4 rule, 2026-11-05): no product matched; mates tslot-40 1.0's 40 x 40 face and its 10 slot (library.load) and M8 clearance ISO 273"
ORIGIN = "inner corner: the line where the two profile faces meet, at the bracket's mid-width; leg H on the face z = 0 toward +x, leg V on the face x = 0 toward +z, width along y"
COMMAND = "BRKA"
PARAMS = dict()
TS = library.load("tslot-40")   # tslot-40 1.0: the profile it meets (one home for the face and the slot)
PROFILE = TS.S          # 40: the profile's face width, its slot centred on it (tslot-40 1.0)
SLOT = TS.THROAT        # 10: the slot's opening in the face (tslot-40 1.0); an M8 shank (just under 8) passes it with about 1 each side
assert PROFILE == 40.0 and SLOT == 10.0
L = PROFILE             # leg length along each profile face: design choice, one profile width
W = PROFILE - 4.0       # bracket width 36: design choice, 2 mm inside each edge of the 40 face
T = 6.0                 # leg thickness: design choice, a cast bracket's wall (4 in mech-r4's first gate: see spec.md)
HOLE_AT = 20.0          # hole centre from the inner corner along each leg: design choice, mid-leg (an M8 head clears the other leg)
HOLE_D = 9.0            # M8 clearance, ISO 273 medium (H13), lib/standards/holes.csv

def build():
    P = Prims()
    h = P.box("M-ALU-ANOD", 0, -W / 2, 0, L, W, T)                                   # leg H, on the horizontal profile's face
    v = P.box("M-ALU-ANOD", 0, -W / 2, T, T, W, L - T)                               # leg V, on the vertical profile's face
    P.hole("M-ALU-ANOD", (HOLE_AT, 0, -1), (HOLE_AT, 0, T + 1), HOLE_D / 2, h)
    P.hole("M-ALU-ANOD", (-1, 0, HOLE_AT), (T + 1, 0, HOLE_AT), HOLE_D / 2, v)
    P.collider("body", 0, -W / 2, 0, L, W, L)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="from behind", az=50, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
