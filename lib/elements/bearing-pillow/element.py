#!/usr/bin/env python3
"""bearing-pillow: pillow block bearing unit, our own vendor-neutral design of the ETIM 10.0 class EC012129 (Bearing), built
unattended (OPERATING.md 12, generic elements; lib/inventory.csv row "bearing-pillow", own_design generic, etim EC012129; 6 systems:
bender-section, condition-monitoring-rig, mechanisms-bench, roll-plate, rotary-index-table, rotator-welding). This version is the
housing only: a cast block on a base with two M12 bolt holes (ISO 273 medium clearance), the shaft axis along y at the centre
height, and the insert bearing's seat drawn as a plain through bore at this design's figure. The insert bearing itself (the part
with the bore the class names, 25 for a 25 shaft) is a part a dimensional standard shapes (ISO 9628) and is never generic
(OPERATING.md 12): it is not drawn, and the seat's figures are a source wanted (spec.md, NOT ON FILE class B: ISO 9628 and ISO 3228).
No moving node (the shaft is the host's), no port, no load or speed claim. The folder's reference record (a catalogue pillow block
for a 20 shaft, references/source.txt) is not what this element is built from; every size below is a design choice. No vendor file
was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "bearing-pillow", "1.1", "device"
TITLE = "pillow block bearing unit, generic, housing for a 25 shaft insert, base 140 x 40 with 2 x M12 holes at 105, centre height 50"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic bearing (ETIM 10.0 EC012129), a pillow block housing for a 25 shaft insert bearing; class values "
            "are design inputs (spec.md); the base's bolt holes at M12's ISO 273 medium clearance; the insert bearing not drawn (a part "
            "ISO 9628 shapes) and its seat drawn plain at a design figure; every size a design choice; no load or speed claim; no vendor "
            "file opened")
ORIGIN = ("the mounting face plane (z = 0, the base's underside) under the shaft axis; the shaft axis along y at z 50 (the centre "
          "height); the base's length along x")
COMMAND = "BEARINGPB"
PARAMS = dict()

SHAFT = 25.0                                 # the insert's bore, the shaft it suits: the class's size (design input, spec.md Class values 3 and 4)
SEAT = 52.0                                  # the insert's seat in the housing, drawn as a plain through bore (design figure; ISO 9628 / ISO 3228 source wanted)
BASE_X, BASE_Y, BASE_Z = 140.0, 40.0, 14.0   # the base: x +-70, y +-20, z 0..14 (design choices)
BOLT_X = 52.5                                # the two bolt holes at x +-52.5 (105 centres), y 0 (design choice)
BOLT_D = 13.5                                # M12 clearance medium H13 (ISO 273, lib/standards/holes.csv)
TOWER_X, TOWER_Z = 70.0, 90.0                # the tower above the base: x +-35, y +-20, z 14..90 (design choices)
CENTRE = 50.0                                # the shaft axis height above the mounting face (design choice)
IN = 0.5                                     # the tower runs 0.5 into the base (one solid joint, gripper 1.0's way)
MAT = "M-CAST-BLUE"                          # a painted cast-iron housing

assert SEAT > SHAFT + 2 * 8.0                                                           # room for the insert's rings between shaft and seat
assert TOWER_X / 2 - SEAT / 2 >= 8.0 and TOWER_Z - (CENTRE + SEAT / 2) >= 8.0           # 8 or more of wall beside and above the seat
assert CENTRE - SEAT / 2 > BASE_Z + 3.0                                                 # the seat clears the base
assert BOLT_X - BOLT_D / 2 > TOWER_X / 2 + 8.0 and BASE_X / 2 - BOLT_X - BOLT_D / 2 >= 8.0   # the bolt holes clear the tower and the base's ends
assert BASE_Y - BOLT_D >= 2 * 8.0                                                       # 8 or more of base beside each bolt hole


def build():
    P = Prims(); hx, hy = BASE_X / 2, BASE_Y / 2
    base = P.box(MAT, -hx, -hy, 0.0, BASE_X, BASE_Y, BASE_Z)                             # base
    for x in (-BOLT_X, BOLT_X):
        P.hole(MAT, (x, 0, -1.0), (x, 0, BASE_Z + 1.0), BOLT_D / 2, base)                # M12 clearance holes through the base
    tower = P.box(MAT, -TOWER_X / 2, -hy, BASE_Z - IN, TOWER_X, BASE_Y, TOWER_Z - BASE_Z + IN)   # tower, 0.5 into the base
    P.hole(MAT, (0, -hy - 1.0, CENTRE), (0, hy + 1.0, CENTRE), SEAT / 2, tower)          # the insert's seat, a plain through bore along y
    P.collider("body", -hx, -hy, 0.0, BASE_X, BASE_Y, TOWER_Z)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="end", az=270, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
