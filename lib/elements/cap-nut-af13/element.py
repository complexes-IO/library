#!/usr/bin/env python3
"""cap-nut-af13: generic screw/nut cap, our own vendor-neutral design of the ETIM 10.0 class EC002375 (Screw/nut cap; the class's
synonyms name the cover cap, the protection cap and the hexagon cap), built unattended (OPERATING.md 12, generic elements; the first
tier-1 class of group EG020045 Fasteners and anchoring systems in lib/toolkit/generic.py's order whose shape no dimensional standard
fixes, mech-r143). A soft PVC cap pushed over a hexagon nut or a hexagon screw head of 13 across flats, with the thread end that
stands past it, to cover the sharp edges and the thread: a round cap Ø20, 16 high, flat top 2 thick, a round socket Ø15.2 that
clears the hexagon's corners (Ø15.01 by geometry, 13 / cos 30°), 14 deep. How the cap grips (internal ribs or a snap bead) is not
drawn and not claimed. Which screw size carries a 13 across-flats hexagon is the screw standards' (not on file), so no screw size is
claimed. The class values (spec.md, "Class values") are design inputs; every size is a design choice. No vendor file opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "cap-nut-af13", "1.0", "connector-part"
TITLE = "Screw/nut cap, generic, soft PVC, grey, round D20 x 16, flat top, socket D15.2 x 14 for a hexagon of 13 across flats"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic screw/nut cap (ETIM 10.0 EC002375), soft PVC, grey, round cap D20 x 16 with a flat top 2 thick "
            "and a round socket D15.2 x 14 over a hexagon of 13 across flats; class values are design inputs (spec.md); every size a "
            "design choice; its grip not drawn or claimed; no screw size, temperature or fire claim; no vendor file opened")
ORIGIN = ("the cap's open end (its seat on the clamped part's face) z = 0 on the cap's axis; the axis along +z, the flat top at z 16")
COMMAND = "NUTCAP"
PARAMS = dict()

AF = 13.0                                    # across flats of the hexagon it covers: design input (class value Diameter cap follows)
E = AF / math.cos(math.radians(30.0))        # 15.011: the hexagon's corner circle, by geometry (a regular hexagon, e = s / cos 30)
SOCKET_D = 15.2                              # the socket, round over the corners: 0.19 over E on the diameter: design choice
DEPTH = 14.0                                 # socket depth: the nut or head and the thread end past it, 14 in all: design choice
CAP_D, CAP_H = 20.0, 16.0                    # the cap Ø20 (class value Diameter cap), 16 high: design choices
TOP = CAP_H - DEPTH                          # 2: the flat top's thickness
WALL = (CAP_D - SOCKET_D) / 2.0              # 2.4: the side wall
MAT = "M-GREY-PVC"                           # soft PVC, grey (lib/materials.csv pvc; render layer M-GREY-PVC, not a printed layer)

assert SOCKET_D > E and SOCKET_D - E < 0.5                               # the socket clears the hexagon's corners, by under 0.5
assert WALL >= 2.0 and TOP >= 2.0                                        # wall 2.4 and top 2: the cap's own sizes
assert abs(TOP - 2.0) < 1e-9 and abs(WALL - 2.4) < 1e-9


def build():
    P = Prims()
    cap = P.cyl(MAT, (0, 0, 0), (0, 0, CAP_H), CAP_D / 2.0)                                     # the cap, Ø20 x 16
    P.hole(MAT, (0, 0, -1.0), (0, 0, DEPTH), SOCKET_D / 2.0, cap)                               # its socket Ø15.2, 14 deep (blind)
    P.collider("cap", -CAP_D / 2.0, -CAP_D / 2.0, 0, CAP_D, CAP_D, CAP_H)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
