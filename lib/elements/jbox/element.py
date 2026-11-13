#!/usr/bin/env python3
"""jbox: wall-mount junction box, sheet steel 240 wide x 240 high x 120 deep, a flat lid hinged at its left edge (node `lid`, rotates
about the box's front-left vertical edge, 0 to 110 degrees outward), two M20 cable-entry holes in the bottom and four M6 wall-fixing
holes in the back. Our own design (EM r4 rule): every size is a design choice. What it meets: the M20 cable-entry hole (gland-m20
`CUTOUT`, lib/standards/holes.csv), M6 fixing screws (Ø6.6, ISO 273 medium H13, lib/standards/holes.csv). The glands are not part
of the box: the entry holes are its own feature, and an assembly fits gland-m20 (released) in the ones its cables use. The lid's hinge
and latch are not modelled in this version (later own designs, next.md #12, #13). No IP rating, no rating and no safety claim."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "jbox", "1.1", "enclosure"
TITLE = "junction box 240 x 240 x 120, wall mount, hinged lid, two M20 entries"
TOOLKIT = "1.3"
BASELINE = "our own design (EM r4 rule, 2026-11-05): no product matched; every size a design choice; mates M20 glands (gland-m20), M6 wall-fixing screws (ISO 273)"
ORIGIN = "bench machine: the box's underside z = 0 at its front-left corner x = 0, y = 0; the lid opens toward -y; the back face y = 120 goes against the wall"
COMMAND = "JBOX"
PARAMS = dict()

W, H, D, T = 240.0, 240.0, 120.0, 2.0           # outside width (x), height (z), depth (y) and sheet: design choices
LID_T = 2.0                                     # the lid, a flat 2.0 plate over the box's front edges: design choice
SWING = 110.0                                   # the lid opens 0 to 110 degrees outward about the front-left edge: design choice
GLAND_CUT = library.load("gland-m20").CUTOUT    # 20.5: gland-m20 1.3 (lib/standards/holes.csv M20 x 1.5 entry 20.2 to 20.7)
GLAND_XY = ((80.0, 60.0), (160.0, 60.0))        # two cable entries in the bottom, 80 pitch, centred on the width; y = 60, the
                                                # middle of the bottom's depth (0 to 120): design choice. A fitted gland's locknut (25 AF, 28.87 across
                                                # corners, 6.0 high, gland-m20 1.3) sits inside on the bottom; its body hangs
                                                # 27.7 below z = 0, 29.72 across (spec.md "Mounting")
FIX_D = 6.6                                     # M6 clearance, ISO 273 medium (H13), lib/standards/holes.csv
FIX_XZ = ((30.0, 30.0), (210.0, 30.0), (30.0, 210.0), (210.0, 210.0))   # wall-fixing holes 180 x 180 in the back: design choice
MAT = "M-STEEL-7035"

def build():
    P = Prims()
    b = P.box(MAT, 0, 0, 0, W, D, T)                                                    # bottom, the entries in it
    for x, y in GLAND_XY: P.hole(MAT, (x, y, -1.0), (x, y, T + 1.0), GLAND_CUT / 2, b)
    P.box(MAT, 0, 0, H - T, W, D, T)                                                    # top
    for x in (0.0, W - T): P.box(MAT, x, 0, T, T, D, H - 2 * T)                         # sides, between the bottom and the top
    back = P.box(MAT, T, D - T, T, W - 2 * T, T, H - 2 * T)                             # back, between the sides
    for x, z in FIX_XZ: P.hole(MAT, (x, D - T - 1.0, z), (x, D + 1.0, z), FIX_D / 2, back)
    P.collider("body", 0, 0, 0, W, D, H)
    Ll = f"node:lid|{MAT}"
    P.box(Ll, 0, -LID_T, 0, W, LID_T, H)                                                # lid, over the box's front edges
    P.pivot("lid", "rotate", (0.0, 0.0, H / 2), axis=(0, 0, 1), range=(0.0, -SWING))    # about the front-left vertical edge
    P.collider("lid", 0, -LID_T, 0, W, LID_T, H)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="rear and bottom, fixing and entry holes", az=40, el=-25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
