#!/usr/bin/env python3
"""panel-operator: operator console box, sheet steel, 300 wide x 200 deep, 60 high at the front rising to 160 at the back (a sloped
operator face), four 22.5 mm operator cut-outs in the sloped face, a gland plate below with two M20 cable-entry holes and four M6
fixing holes, and a rear cover hinged at its bottom edge (node `door`). Our own design (EM r4 rule): every size is a design choice.
What it meets: the 22.5 mm operator cut-out (op-pb-22-1no / op-estop-22-2nc / op-pilot-22, toolkit/std22.py, lib/standards/holes.csv), the
M20 cable-entry hole (gland-m20), M6 fixing screws (Ø6.6, ISO 273 medium H13, lib/standards/holes.csv). The operators and glands are
not placed in this version: their holes are modelled (EM's rule). No rating and no safety claim."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "panel-operator", "1.1", "enclosure"
TITLE = "operator console box 300 x 200, sloped face, four 22.5 mm cut-outs, gland plate, rear cover"
TOOLKIT = "1.3"
BASELINE = "our own design (EM r4 rule, 2026-11-05): no product matched; every size a design choice; mates 22.5 mm operators (op-pb-22-1no), M20 glands (gland-m20), M6 screws (ISO 273)"
ORIGIN = "bench machine: the underside of the gland plate z = 0 at the box's front-left corner x = 0, y = 0; the operator face slopes up toward +y (the person stands at -y); the rear cover opens toward +y"
COMMAND = "OPCONS"
PARAMS = dict()

W, D, T = 300.0, 200.0, 2.0                     # outside width (x) and depth (y), sheet: design choices
HF, HB = 60.0, 160.0                            # height at the front and at the back, to the sloped face's underside: design choices
RISE = HB - HF                                  # 100 over 200: the face slopes 26.6 degrees
TH = math.atan2(RISE, D)
LS = math.hypot(D, RISE)                        # sloped face length, 223.6
EX = (1.0, 0.0, 0.0)
EY = (0.0, math.cos(TH), math.sin(TH))          # up the slope
EZ = (0.0, -math.sin(TH), math.cos(TH))         # the face's outward normal
OP_CUT = library.load("op-pb-22-1no").CUTOUT        # 22.5: toolkit/std22.py; lib/standards/holes.csv "22.5 operator cut-out"
OP_X = (52.5, 117.5, 182.5, 247.5)              # four cut-outs at 65 pitch, centred on the width: design choice
OP_S = LS / 2                                   # cut-out centres half-way up the slope: design choice
GLAND_CUT = library.load("gland-m20").CUTOUT    # 20.5: gland-m20 1.2 (lib/standards/holes.csv M20 x 1.5 entry 20.2 to 20.7)
GLAND_XY = ((100.0, 140.0), (200.0, 140.0))     # two cable entries in the gland plate, toward the back: design choice. A fitted
                                                # gland stands 27.7 below z = 0 (gland-m20 1.3): the mounting surface needs an
                                                # opening under the entries (spec.md "Mounting"), the box cannot sit on a flat top
FIX_D = 6.6                                     # M6 clearance, ISO 273 medium (H13), lib/standards/holes.csv
FIX_XY = ((25.0, 25.0), (275.0, 25.0), (25.0, 175.0), (275.0, 175.0))   # fixing holes 250 x 150: design choice
CLR = 0.5                                       # rear cover's clearance to the sides, the gland plate and the sloped face
DOOR_Z0 = T + CLR                               # rear cover's bottom edge, on the hinge line
DOOR_Z1 = HF + (D - T) * RISE / D - 1.0         # 158: 1 below the sloped face's underside at y = D - T (159)
SWING = -90.0                                   # rear cover opens outward and down about its bottom edge: design choice
MAT = "M-STEEL-7035"

def slope_pt(x, s, n=0.0):
    """a point on the sloped face: x across, s up the slope from its front edge, n along its outward normal from the underside"""
    return tuple(o + x * a + s * b + n * c for o, a, b, c in zip((0.0, 0.0, HF), EX, EY, EZ))

def build():
    P = Prims()
    g = P.box(MAT, 0, 0, 0, W, D, T)                                                    # gland plate (the bottom)
    for x, y in GLAND_XY: P.hole(MAT, (x, y, -1.0), (x, y, T + 1.0), GLAND_CUT / 2, g)
    for x, y in FIX_XY: P.hole(MAT, (x, y, -1.0), (x, y, T + 1.0), FIX_D / 2, g)
    for x0 in (0.0, W - T):                                                             # sides, cut along the sloped face's underside
        s = P.box(MAT, x0, 0, T, T, D, HB - T)
        P.cut(MAT, slope_pt(x0 - 1.0, -20.0), EX, EY, EZ, T + 2.0, LS + 60.0, 200.0, s)
    P.box(MAT, T, 0, T, W - 2 * T, T, HF - T)                                           # front, between the sides, under the slope
    f = P.obox(MAT, slope_pt(0, 0), EX, EY, EZ, W, LS, T)                               # sloped operator face, on the sides and the front
    for x in OP_X: P.hole(MAT, slope_pt(x, OP_S, -1.0), slope_pt(x, OP_S, T + 1.0), OP_CUT / 2, f)
    Ld = f"node:door|{MAT}"                                                             # rear cover, between the sides
    P.box(Ld, T + CLR, D - T, DOOR_Z0, W - 2 * T - 2 * CLR, T, DOOR_Z1 - DOOR_Z0)
    P.pivot("door", "rotate", (W / 2, D, DOOR_Z0), axis=(1, 0, 0), range=(0, SWING))
    P.collider("body", 0, 0, 0, W, D - T, HB)
    P.collider("door", T + CLR, D - T, DOOR_Z0, W - 2 * T - 2 * CLR, T, DOOR_Z1 - DOOR_Z0)
    return P

PREVIEWS = [dict(name="front three-quarter", az=230, el=25), dict(name="rear cover and gland plate", az=40, el=-25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
