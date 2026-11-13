#!/usr/bin/env python3
"""hinge: butt hinge 80 x 80 x 3, our own design, built unattended (OPERATING.md 12, own designs; lib/inventory.csv row "hinge",
own_design yes, made_of screw-iso7380 x4; no ETIM class on file fits a hinge and no hinge standard is in lib/standards/sources.csv).
The hinge that hangs a guard door, an oven door, a cabinet door or a cover on its frame: a fixed leaf (screwed to the frame) with
two outer knuckles and the pin pressed through them, and a moving leaf (node `leaf`, screwed to the door, turning 0 to 180 degrees
about the pin's axis) with the middle knuckle, bored 0.5 clear round the pin. Three knuckles Ø12, 26 long with 1 between them; a
Ø6 pin 81 long whose ends stand 0.5 proud of the knuckles (a peened pin's heads, drawn flat). Each leaf 3 thick with two Ø6.6 holes
(ISO 273 medium, M6) for button head screws (ISO 7380-1, the inventory's made_of; a common part not built yet: the holes are
modelled, the part placed later; the two leaves' patterns staggered along the pin, 2.0, so the screw heads never meet when
folded). At rest (0, closed) the leaves lie flat in one plane, the door closed against its frame; at 180
(open) the moving leaf lies folded back over the fixed one, knuckle side to knuckle side. Every size is a design choice. No load,
no vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "hinge", "2.0", "device"
TITLE = "butt hinge 80 x 80 x 3, own design, three knuckles Ø12 on a Ø6 pin, moving leaf 0 to 180 degrees, 4 x M6 holes ISO 273"
TOOLKIT = "1.3"
BASELINE = ("our own design: butt hinge, two 3.0 steel leaves 80 long and 40 wide from the pin's axis, three knuckles on a pressed pin; "
            "screw holes ISO 273 medium for M6 (button head screws ISO 7380-1 placed later); every size a design choice; no load "
            "claim; no vendor file opened")
ORIGIN = ("the fixed leaf's mounting face plane (y = 0) under the pin's axis, at the hinge's mid-length (z = 0); the pin's axis is the "
          "line x = 0, y = 6 along z; -x the fixed leaf (the frame's), +x the moving leaf (the door's), +y the knuckle side (outside)")
COMMAND = "HINGEBUTT"
PARAMS = dict()
LEAF_T = 3.0                               # leaf thickness: steel sheet 3.0, y 0..3 on the mounting plane
LEAF_W, LEAF_L = 40.0, 80.0                # each leaf 40 wide from the pin's axis (x) and 80 long along the pin (z -40..40)
KN_R = 6.0                                 # knuckle Ø12 about the pin's axis at (0, 6): its underside tangent to the mounting plane y = 0
AX_Y = KN_R                                # the pin's axis y = 6 (x = 0): a flat butt hinge, both leaves in one plane when closed
PIN_R = 3.0                                # pin Ø6
PIN_PROUD = 0.5                            # the pin's ends stand 0.5 proud of the outer knuckles (no face in a knuckle's end plane)
KN_BORE_R = 3.5                            # Ø7 through the moving knuckle: 0.5 clear round the pin (features.csv, own)
KN_GAP = 1.0                               # 1 between knuckles along z
KN_L = (LEAF_L - 2 * KN_GAP) / 3           # 26: three equal knuckles, z -40..-14 (fixed), -13..13 (moving), 14..40 (fixed)
WEB_X = KN_R                               # the web that joins a leaf's plate to its knuckle spans x 0..6 (fixed: -6..0), the knuckle's own z range only
HOLE_D, HOLE_X = 6.6, 25.0                 # 2 x M6 clearance medium (ISO 273) per leaf, 25 from the pin's axis
HOLE_ZF, HOLE_ZM = 28.0, 8.0               # 2.0: staggered along the pin, the fixed leaf's at z +-28, the moving leaf's at z +-8, so at
                                           # 180 (folded, (x, y) -> (-x, 12 - y)) the moving leaf's land at (-25, +-8), 20 from the fixed
                                           # leaf's (-25, +-28): the heads in the 6 gap never face each other (review hinge-1.0 finding 1)
ZF = ((-LEAF_L / 2, -LEAF_L / 2 + KN_L), (LEAF_L / 2 - KN_L, LEAF_L / 2))   # the fixed knuckles' z ranges
ZM = (-KN_L / 2, KN_L / 2)                                                   # the moving knuckle's z range

def build():
    P = Prims(); Z = "M-ZINC"; S = "M-SILVER"; N = f"node:leaf|{Z}"
    # ---- fixed leaf: plate on -x, webs and two outer knuckles bored Ø6 for the pin; the pin pressed through them
    pl = P.box(Z, -LEAF_W, 0, -LEAF_L / 2, LEAF_W - WEB_X, LEAF_T, LEAF_L)                     # plate x -40..-6, y 0..3, z -40..40
    for sz in (-1, 1): P.hole(Z, (-HOLE_X, -1, sz * HOLE_ZF), (-HOLE_X, LEAF_T + 1, sz * HOLE_ZF), HOLE_D / 2, pl)
    for z0, z1 in ZF:
        P.box(Z, -WEB_X, 0, z0, WEB_X, LEAF_T, z1 - z0)                                        # web x -6..0 at the knuckle's z
        kn = P.cyl(Z, (0, AX_Y, z0), (0, AX_Y, z1), KN_R)                                      # knuckle Ø12
        P.hole(Z, (0, AX_Y, z0 - 1), (0, AX_Y, z1 + 1), PIN_R, kn)                             # bored Ø6: the pin is pressed in
    P.cyl(S, (0, AX_Y, -LEAF_L / 2 - PIN_PROUD), (0, AX_Y, LEAF_L / 2 + PIN_PROUD), PIN_R)      # pin Ø6 x 81, bright steel
    P.collider("fixed", -LEAF_W, 0, -LEAF_L / 2, LEAF_W - WEB_X, LEAF_T, LEAF_L)
    P.collider("knuckle", -KN_R, 0, -LEAF_L / 2 - PIN_PROUD, 2 * KN_R, 2 * KN_R, LEAF_L + 2 * PIN_PROUD)
    # ---- moving leaf (node): plate on +x, web and the middle knuckle bored Ø7 (0.5 clear round the pin)
    pm = P.box(N, WEB_X, 0, -LEAF_L / 2, LEAF_W - WEB_X, LEAF_T, LEAF_L)                       # plate x 6..40, y 0..3, z -40..40
    for sz in (-1, 1): P.hole(N, (HOLE_X, -1, sz * HOLE_ZM), (HOLE_X, LEAF_T + 1, sz * HOLE_ZM), HOLE_D / 2, pm)
    P.box(N, 0, 0, ZM[0], WEB_X, LEAF_T, ZM[1] - ZM[0])                                        # web x 0..6 at the middle knuckle's z
    km = P.cyl(N, (0, AX_Y, ZM[0]), (0, AX_Y, ZM[1]), KN_R)                                    # middle knuckle Ø12, z -13..13
    P.hole(N, (0, AX_Y, ZM[0] - 1), (0, AX_Y, ZM[1] + 1), KN_BORE_R, km)                       # bored Ø7
    P.pivot("leaf", "rotate", (0, AX_Y, 0), axis=(0, 0, 1), range=(0, 180), unit="deg")        # swings toward +y, the knuckle side
    P.collider("swing", WEB_X, 0, -LEAF_L / 2, LEAF_W - WEB_X, LEAF_T, LEAF_L)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="front", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
