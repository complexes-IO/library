#!/usr/bin/env python3
"""bolster: press bolster plate, our own design (OPERATING.md 12, own designs; inventory row own_design "yes"). The thick
machined plate on the bed of a hydraulic press (press-hydraulic, press-shop-hydraulic in lib/machines-factory.txt) that the
lower die stands on: a plate 1000 x 700 x 80 (one fixed body, no node: the lower die a BOM puts on the press is placed on its
top face, z = 80 above the origin), six M12 fixing holes, ISO 273 medium (lib/standards/holes.csv), that bolt it to the press bed, and one central Ø100
knock-out passage for the press's ejector (a design choice, declared in features.csv). The plate fits on frame-welded's
1200 x 800 seat. Die-clamping T-slots are not in this version: no T-slot table (ISO 299) is on file (needs-em 66), so the top
is plain. Every size is a design choice. No load rating, no flatness or parallelism claim."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "bolster", "1.0", "furniture"
TITLE = "press bolster plate 1000 x 700 x 80, plain top, 6 x M12 fixing holes, central knock-out passage Ø100"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; fixing holes M12 in ISO 273 medium holes; "
            "every size a design choice; no load rating, no flatness or parallelism claim")
ORIGIN = ("the plate's underside z = 0 (the press bed's top face) at the plate's centre x = 0, y = 0; the long side along x; "
          "front toward -y; the top face (the lower die's seat) at z = 80")
COMMAND = "BOLSTER"
PARAMS = dict()
L, W, T = 1000.0, 700.0, 80.0           # plate 1000 x 700 x 80: design choice (fits frame-welded's 1200 x 800 seat)
FIX_D = 13.5                            # M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv)
FIX_X = (-450.0, 0.0, 450.0)            # three fixing holes a side, 50 in from each end: design choice
FIX_Y = 300.0                           # fixing hole centres at y +-300, 50 in from the long edges: design choice
KO_D = 100.0                            # central knock-out passage Ø100 for the press's ejector: design choice

def build():
    P = Prims(); S = "M-SILVER"                                    # bare machined steel, the library's bright-metal layer
    plate = P.box(S, -L / 2, -W / 2, 0, L, W, T)                                              # the bolster plate (the body)
    for sy in (-1, 1):
        for x in FIX_X:
            P.hole(S, (x, sy * FIX_Y, -1), (x, sy * FIX_Y, T + 1), FIX_D / 2, plate)          # fixing hole M12
    P.hole(S, (0, 0, -1), (0, 0, T + 1), KO_D / 2, plate)                                    # knock-out passage
    P.collider("plate", -L / 2, -W / 2, 0, L, W, T)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="side", az=270, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
