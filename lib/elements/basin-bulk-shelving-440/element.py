#!/usr/bin/env python3
"""basin-bulk-shelving-440: generic bulk material basin for one half of a shelf of shelving-steel's bay, our own vendor-neutral design
of the ETIM 10.0 class EC004076 (Bulk material basin (rack element); synonym rack bulk material basin), built unattended (OPERATING.md
12, generic elements; group EG010340 Storage and racking systems, a tier-2 class, after wall-side-shelving-500,
lib/rounds/mech/r157.md). A painted steel sheet 1.5 thick, folded to an open-topped tub 440 wide, 480 deep and 250 high, standing on
the bay's lowest shelf in its left half: 5 clear of the left uprights' inner faces and 5 short of the bay's middle, 10 in from the
shelf's front and rear edges. Its front is lowered over the first 100 of its depth to 120 high, so loose goods are scooped out from the
front; the rest stands 250, which leaves 160 clear under the second shelf (asserted below). The right half takes the same part moved
450 in x (the shelf is symmetric about x = 0, so the moved part keeps the same clearances). The bay is placed, never redrawn: its
width, depth, uprights and shelf levels are read from shelving-steel with library.load. The basin stands on the shelf by its own
weight: no fixing is drawn and no hole modelled. The class's features are not on file (lib/standards/etim/class-features.csv has no
EC004076 rows): spec.md gives the design values under plain names, as wall-side-shelving-500 does. Every size is a design choice. No
load or safety claim. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "basin-bulk-shelving-440", "1.0", "furniture"
TITLE = ("bulk material basin for one half of a shelf of a 1000 x 500 steel shelving bay, generic, painted steel sheet 1.5, "
         "440 x 480 x 250 open tub, front lowered to 120")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic bulk material basin (ETIM 10.0 EC004076), a folded steel sheet tub standing on the lowest shelf "
            "of shelving-steel 1.0 (bay 1000 x 500 x 2000, uprights 50 x 50, shelves 40 deep, tops at 150 and 600) in its left half, "
            "5 clear of the uprights and of the bay's middle, 10 in from the shelf's edges, 160 clear under the second shelf; the "
            "right half takes the same part moved 450 in x; the bay's figures read from shelving-steel (library.load); class features "
            "not on file, design values under plain names (spec.md); every size a design choice; no load or safety claim; no vendor "
            "file opened")
ORIGIN = ("shelving-steel's own origin, so the host places the left basin at the bay's origin: the floor z = 0, the middle of the "
          "bay's width x = 0, the front uprights' front faces y = 0; the basin's lowered front toward -y, where goods are taken out; "
          "the right basin: the same placement moved 450 in +x")
COMMAND = "BBSH440"
PARAMS = dict()

SS = library.load("shelving-steel")          # shelving-steel 1.0: the bay whose shelf the basin stands on (one home for each figure)
W, D, UP, SH_T = SS.W, SS.D, SS.UP, SS.SH_T  # 1000, 500, 50, 40: the bay over its uprights, the uprights' section, the shelves' depth
SH1, SH2 = SS.SH_TOPS[0], SS.SH_TOPS[1]      # 150, 600: the lowest shelf's top face, the second shelf's top face
IN_X = -W / 2 + UP                           # -450: the left uprights' inner faces, where the shelves end
T = 1.5                                      # design: sheet thickness (under 3: every sheet edge is thin to the gate's fillet check)
CX = 5.0                                     # design: clear space to the uprights' inner faces and to the bay's middle
CY = 10.0                                    # design: set-in from the shelf's front and rear edges
HB = 250.0                                   # design: the basin's height (sides and back)
HF = 120.0                                   # design: the lowered front's height
LF = 100.0                                   # design: how far back from the front the walls stay lowered
X0, X1 = IN_X + CX, -CX                      # -445 .. -5: the left half of the shelf, less 5 each side
Y0, Y1 = CY, D - CY                          # 10 .. 490: 10 in from the shelf's front and rear edges
Z0, Z1 = SH1, SH1 + HB                       # 150 .. 400: on the lowest shelf's top face
ZF = SH1 + HF                                # 270: the lowered front's top
STEP = X1 - X0 + 2 * CX                      # 450: the move from the left basin to the right one
MAT = "M-STEEL-7035"                         # painted steel, shelving-steel's layer

assert abs(X1 - X0 - 440.0) < 1e-9 and abs(Y1 - Y0 - 480.0) < 1e-9 and abs(Z1 - Z0 - 250.0) < 1e-9   # the bay's figures as read
assert X0 - CX == IN_X and X1 + CX == 0.0                                            # 5 clear of the left uprights and of the bay's middle
assert X0 + STEP - CX == 0.0 and X1 + STEP + CX == -IN_X                             # the moved part: 5 clear of the middle and the right uprights
assert Y0 >= 0.0 and Y1 <= D and abs((D - Y1) - Y0) < 1e-9                           # on the shelf (y 0 .. 500), 10 in at front and back
assert (SH2 - SH_T) - Z1 == 160.0                                                    # 160 clear under the second shelf's underside (560)
assert T < 3.0 and min(HF, LF, Z1 - ZF, Y1 - Y0 - LF, X1 - X0) >= 8.0                # sheet edges thin, every other free edge >= 8 (the gate's trap)
TUB = (X1 - X0) * (Y1 - Y0) * (Z1 - Z0) - (X1 - X0 - 2 * T) * (Y1 - Y0 - 2 * T) * (Z1 - Z0 - T)   # 52800000 - 437 x 477 x 248.5
NOTCH = (X1 - X0) * T * (Z1 - ZF) + 2 * T * (LF - T) * (Z1 - ZF)                     # front wall 440 x 1.5 x 130 + two side strips 1.5 x 98.5 x 130
VOL = TUB - NOTCH
assert abs(TUB - 1000423.5) < 1e-6 and abs(NOTCH - 124215.0) < 1e-6 and abs(VOL - 876208.5) < 1e-6


def build():
    P = Prims()
    bs = P.box(MAT, X0, Y0, Z0, X1 - X0, Y1 - Y0, Z1 - Z0)                                        # the basin's envelope
    P.cutbox(MAT, X0 + T, Y0 + T, Z0 + T, X1 - X0 - 2 * T, Y1 - Y0 - 2 * T, Z1 - Z0, bs)          # open at the top: the tub
    P.cutbox(MAT, X0 - 1, Y0 - 1, ZF, X1 - X0 + 2, LF + 1, Z1 - ZF + 1, bs)                       # the lowered front, 100 back
    P.collider("basin", X0, Y0, Z0, X1 - X0, Y1 - Y0, Z1 - Z0)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="behind", az=50, el=30)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
