#!/usr/bin/env python3
"""plinth-shelving-1000: generic plinth panel (base cover) for the front of shelving-steel's bay, our own vendor-neutral design of the
ETIM 10.0 class EC004074 (Base/base element (rack element); synonyms 19 inch plinth panel, base cover for rack), built unattended
(OPERATING.md 12, generic elements; group EG010340 Storage and racking systems, a tier-2 class, after bar-depth-support-1067,
lib/rounds/mech/r155.md). A painted steel sheet 1.5 thick, folded to a channel open at the back and below: a front face standing on
the floor between the bay's two front uprights, closing the space under the lowest shelf, a top fold 40 deep and an end return 40
deep at each end. It stands 2 clear of the uprights' inner faces and of the lowest shelf's underside, and 2 back from the uprights'
front faces; it touches neither the uprights, nor their anchor plates, nor the shelf (asserted below). The bay is placed, never
redrawn: its width, upright section and lowest shelf are read from shelving-steel with library.load. How the panel is held to the
bay is the host's assembly: no fixing is drawn and no hole modelled. The class's features are not on file
(lib/standards/etim/class-features.csv has no EC004074 rows): spec.md gives the design values under plain names, as guard-upright-80
and bar-depth-support-1067 do. Every size is a design choice. No load or safety claim. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "plinth-shelving-1000", "1.0", "furniture"
TITLE = ("plinth panel (base cover) for the front of a 1000 wide steel shelving bay, generic, painted steel sheet 1.5, "
         "896 x 40 x 108 channel")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic plinth panel (ETIM 10.0 EC004074), a folded steel sheet standing on the floor between the two "
            "front uprights of shelving-steel 1.0 (bay 1000 wide, uprights 50 x 50, lowest shelf underside 110), 2 clear of the "
            "uprights and of the shelf, the bay's figures read from shelving-steel (library.load); class features not on file, "
            "design values under plain names (spec.md); every size a design choice; no load or safety claim; no vendor file opened")
ORIGIN = ("shelving-steel's own origin, so the host places the panel at the bay's: the floor z = 0, the middle of the bay's width "
          "x = 0, the front uprights' front faces y = 0; the panel's front face 2 behind that plane, its returns toward +y")
COMMAND = "PLSH1000"
PARAMS = dict()

SS = library.load("shelving-steel")          # shelving-steel 1.0: the bay whose front the plinth closes (one home for each figure)
W, UP = SS.W, SS.UP                          # 1000 and 50: the bay's width over the uprights, the uprights' section
SHELF_U = SS.SH_TOPS[0] - SS.SH_T            # 110: the lowest shelf's underside (top 150, 40 deep)
PL_W = SS.PL_W                               # 50: the anchor plates' width, the upright's own (they lie behind the front uprights)
IN_X = W / 2 - UP                            # 450: the front uprights' inner faces at x = +-450
T = 1.5                                      # design: sheet thickness (under 3: every sheet edge is thin to the gate)
CL = 2.0                                     # design: clear space to the uprights' inner faces and to the shelf's underside
SB = 2.0                                     # design: the front face's set-back behind the uprights' front faces
R = 40.0                                     # design: the depth of the top fold and the end returns (front face included)
HX = IN_X - CL                               # 448: half the panel's width
TOP = SHELF_U - CL                           # 108: the panel's top
Y0, Y1 = SB, SB + R                          # 2 .. 42: the panel's depth
MAT = "M-STEEL-7035"                         # painted steel, shelving-steel's layer

assert abs(SHELF_U - 110.0) < 1e-9 and abs(IN_X - 450.0) < 1e-9                      # the bay's figures as read
assert HX + CL == IN_X and TOP + CL == SHELF_U                                       # 2 clear of the uprights and of the shelf
assert HX < W / 2 - PL_W                                                             # inside x +-450: clear of the anchor plates (x 450 .. 500)
assert T < 3.0 and min(R, TOP, 2 * HX) >= 8.0                                        # sheet edges thin, every other free edge >= 8 (the gate's trap)
VOL = 2 * HX * R * TOP - (2 * HX - 2 * T) * (R - T) * (TOP - T)                      # 3870720 - 893 x 38.5 x 106.5 = 209196.75
assert abs(VOL - 209196.75) < 1e-6
assert abs(VOL - (2 * HX * T * TOP + 2 * HX * (R - T) * T + 2 * T * (R - T) * (TOP - T))) < 1e-6   # front + top fold + two returns


def build():
    P = Prims()
    pn = P.box(MAT, -HX, Y0, 0, 2 * HX, R, TOP)                                                    # the panel's envelope
    P.cutbox(MAT, -HX + T, Y0 + T, -1, 2 * HX - 2 * T, R, TOP - T + 1, pn)                         # open behind and below: the channel
    P.collider("plinth", -HX, Y0, 0, 2 * HX, R, TOP)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="behind", az=50, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
