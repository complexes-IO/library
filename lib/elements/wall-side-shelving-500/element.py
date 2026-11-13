#!/usr/bin/env python3
"""wall-side-shelving-500: generic side wall for one open side of shelving-steel's bay, our own vendor-neutral design of the ETIM 10.0
class EC004075 (Side wall/partition (rack element); synonyms side panel (rack element), shelf wall, rack wall), built unattended
(OPERATING.md 12, generic elements; group EG010340 Storage and racking systems, a tier-2 class, after plinth-shelving-1000,
lib/rounds/mech/r156.md). A painted steel sheet 1.5 thick, folded to a shallow tray: a face 396 wide and 1976 high on the bay's
outside and a flange 20 deep on each of its four edges, turned in toward the shelves. It stands in the left uprights' band (x -500 to
-450) between the front and the rear upright, 2 clear of each, 2 above the anchor plates and 2 below the uprights' tops, its face 2
inside the bay's outside plane and its flanges' edges 28 clear of the shelves' ends (asserted below). The right side takes the same
part turned 180 degrees about the bay's vertical centre line (x = 0, y = 250): it maps x to -x and y to 500 - y, and the part's y
band 52 to 448 onto itself. The bay is placed, never redrawn: its footprint, uprights, anchor plates, shelves and height are read
from shelving-steel with library.load. How the wall is held to the bay is the host's assembly: no fixing is drawn and no hole
modelled. The class's features are not on file (lib/standards/etim/class-features.csv has no EC004075 rows): spec.md gives the design
values under plain names, as plinth-shelving-1000 does. Every size is a design choice. No load or safety claim. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "wall-side-shelving-500", "1.0", "furniture"
TITLE = ("side wall for one open side of a 500 deep steel shelving bay, generic, painted steel sheet 1.5, "
         "396 x 1976 tray with 20 flanges")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic side wall (ETIM 10.0 EC004075), a folded steel sheet standing in the left uprights' band of "
            "shelving-steel 1.0 (bay 1000 x 500 x 2000, uprights 50 x 50, anchor plates 20 thick) between the front and the rear "
            "upright, 2 clear of them, of the anchor plates and of the uprights' tops; the right side takes the same part turned 180 "
            "degrees about the bay's centre line; the bay's figures read from shelving-steel (library.load); class features not on "
            "file, design values under plain names (spec.md); every size a design choice; no load or safety claim; no vendor file opened")
ORIGIN = ("shelving-steel's own origin, so the host places the left wall at the bay's origin: the floor z = 0, the middle of the "
          "bay's width x = 0, the front uprights' front faces y = 0; the wall's face toward -x, its flanges toward +x; the right "
          "wall: the same placement turned 180 degrees about the vertical line x = 0, y = 250")
COMMAND = "WSSH500"
PARAMS = dict()

SS = library.load("shelving-steel")          # shelving-steel 1.0: the bay whose open side the wall closes (one home for each figure)
W, D, H, UP = SS.W, SS.D, SS.H, SS.UP        # 1000, 500, 2000, 50: the bay over its uprights, the uprights' section
PL_T, PL_L = SS.PL_T, SS.PL_L                # 20, 100: the anchor plates' thickness and length (in the uprights' band, on the floor)
OUT_X = -W / 2                               # -500: the bay's left outside plane (the left uprights' outer faces)
IN_X = -W / 2 + UP                           # -450: the left uprights' inner faces, where the shelves end
T = 1.5                                      # design: sheet thickness (under 3: every sheet edge is thin to the gate's fillet check)
CL = 2.0                                     # design: clear space to the uprights, the anchor plates and the uprights' tops
SI = 2.0                                     # design: the face's set-in behind the bay's outside plane
F = 20.0                                     # design: the flanges' depth (the face included)
X0, X1 = OUT_X + SI, OUT_X + SI + F          # -498 .. -478: the face's outer side and the flanges' edges
Y0, Y1 = UP + CL, D - UP - CL                # 52 .. 448: between the front and the rear upright
Z0, Z1 = PL_T + CL, H - CL                   # 22 .. 1998: above the anchor plates, below the uprights' tops
MAT = "M-STEEL-7035"                         # painted steel, shelving-steel's layer

assert abs(Y1 - Y0 - 396.0) < 1e-9 and abs(Z1 - Z0 - 1976.0) < 1e-9                  # the bay's figures as read
assert X0 > OUT_X and X1 < IN_X and abs(IN_X - X1 - 28.0) < 1e-9                     # inside the band: 2 in from outside, 28 clear of the shelves
assert Y0 - CL == UP and Y1 + CL == D - UP                                           # 2 clear of the front and the rear upright
assert Z0 - CL == PL_T and Z1 + CL == H                                              # 2 above the anchor plates, 2 below the uprights' tops
assert UP + PL_L <= D - UP - PL_L                                                    # the anchor plates lie in the band, under the wall's foot
assert abs((D - Y1) - Y0) < 1e-9                                                     # y band symmetric about y = 250: the turned part fits the right side
assert T < 3.0 and min(F, Y1 - Y0, Z1 - Z0) >= 8.0                                   # sheet edges thin, every other free edge >= 8 (the gate's trap)
VOL = F * (Y1 - Y0) * (Z1 - Z0) - (F - T) * (Y1 - Y0 - 2 * T) * (Z1 - Z0 - 2 * T)    # 15649920 - 18.5 x 393 x 1973 = 1305223.5
assert abs(VOL - 1305223.5) < 1e-6
assert abs(VOL - (T * (Y1 - Y0) * (Z1 - Z0) + 2 * (F - T) * (Y1 - Y0) * T + 2 * (F - T) * T * (Z1 - Z0 - 2 * T))) < 1e-6  # face + 4 flanges


def build():
    P = Prims()
    wl = P.box(MAT, X0, Y0, Z0, F, Y1 - Y0, Z1 - Z0)                                              # the wall's envelope
    P.cutbox(MAT, X0 + T, Y0 + T, Z0 + T, F, Y1 - Y0 - 2 * T, Z1 - Z0 - 2 * T, wl)                # open toward the shelves: the tray
    P.collider("wall", X0, Y0, Z0, F, Y1 - Y0, Z1 - Z0)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="behind", az=50, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
