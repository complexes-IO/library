#!/usr/bin/env python3
"""chuck-zero-point-120: generic zero-point clamping module (the module bolted to a machine table or a fixture plate that takes a
pallet's clamping nipple in its receiving bore and holds it, so a pallet changed between machines comes back to the same point), our
own vendor-neutral design of the ETIM 10.0 class EC004396 (Zero-point clamping system), built unattended (OPERATING.md 12, generic
elements; `python lib/build.py inventory mech` lists the class once no inventory row builds unattended: group EG020054 Clamping tools,
lib/needs-em/mech.md). A steel flange with four M8 holes carries the round body; its top face is the pallet's seat and its centre the
receiving bore. The clamping slides, their springs, the release piston and its air port are internal mechanism the twin doesn't read:
not drawn, not claimed, so the module has no node and no port. The pallet's nipple is the pallet's (not drawn). The class values
(spec.md, "Class values") are design inputs; every size below is a design choice. No clamping or pull-in force is designed or claimed.
No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "chuck-zero-point-120", "1.0", "device"
TITLE = "zero-point clamping module, generic, flange Ø120 with 4 x M8 on Ø100, body Ø80, receiving bore Ø25, height 40"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic zero-point clamping system (ETIM 10.0 EC004396), one flange-mounted module; class values are "
            "design inputs (spec.md); flange holes M8 to ISO 273 medium, the screws placed by the host; the clamping slides, springs, "
            "release piston and air port not drawn; every size a design choice; no clamping force claimed; no vendor file opened")
ORIGIN = ("on the flange's underside (z = 0, the mounting face) on the module's axis (the line x = 0, y = 0 along z); the top face z = 40 "
          "is the pallet's seat and the receiving bore opens upward on the axis; the flange holes on the x and y axes")
COMMAND = "ZEROPNT"
PARAMS = dict()

FL_R, FL_T = 60.0, 12.0                    # flange Ø120 x 12 (z 0..12): design choice
BODY_R, TOP = 40.0, 40.0                   # body Ø80 from the flange to the seat z 40: design choice
BORE_R, BORE_DEPTH = 12.5, 18.0            # receiving bore Ø25, 18 deep (z 22..40): design choice
PCD_R = 50.0                               # 4 x M8 on a Ø100 circle, on the x and y axes: design choice
M8_D = 9.0                                 # M8 clearance, ISO 273 medium H13 (lib/standards/holes.csv)
STEEL = "M-SILVER"

assert PCD_R - M8_D / 2 - BODY_R >= 5.0 and FL_R - PCD_R - M8_D / 2 >= 5.0   # the holes 5.5 off the body and the flange's rim
assert TOP - BORE_DEPTH > FL_T                                              # the bore's floor above the flange


def build():
    P = Prims()
    fl = P.cyl(STEEL, (0, 0, 0), (0, 0, FL_T), FL_R)                                                          # flange Ø120
    for x, y in ((PCD_R, 0), (0, PCD_R), (-PCD_R, 0), (0, -PCD_R)):
        P.hole(STEEL, (x, y, -1), (x, y, FL_T + 1), M8_D / 2, fl)                                            # M8 clearance
    body = P.cyl(STEEL, (0, 0, FL_T), (0, 0, TOP), BODY_R)                                                   # body Ø80 to the seat
    P.hole(STEEL, (0, 0, TOP - BORE_DEPTH), (0, 0, TOP + 1), BORE_R, body)                                   # receiving bore Ø25
    P.collider("flange", -FL_R, -FL_R, 0, 2 * FL_R, 2 * FL_R, FL_T)
    P.collider("module", -BODY_R, -BODY_R, FL_T, 2 * BODY_R, 2 * BODY_R, TOP - FL_T)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
