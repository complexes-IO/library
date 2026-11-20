#!/usr/bin/env python3
"""corner-stacking-1000: generic stacking corner for a block pallet, 1000 clear between the lower pallet's deck and the upper pallet's
underside, our own vendor-neutral design of the ETIM 10.0 class EC003948 (Stacking corner), built unattended (OPERATING.md 12, generic
elements; group EG010340 Storage and racking systems, a tier-2 class walked by name after reel-cable-630, lib/rounds/mech/r169.md).
A painted steel corner post: a foot plate on the lower pallet's corner deck board with two lips turned down over the deck's outer edges,
an angle post of two legs 60 x 8 at the outer corner, and a top plate under the upper pallet's corner with two lips turned up over its
bottom board's outer edges. Four of them, one at each corner, carry a loaded pallet over another; the part is symmetric about its
diagonal, so the same part serves every corner turned about z (no mirrored part). It sits on pallet 1.2 (built, station 6): the
pallet's figures are read with library.load and the fit is asserted here (the plates on the corner deck board and under the corner
bottom board, the lips shallower than the deck and the bottom boards they cover, four corners inside the footprint). No element is
placed or redrawn. The class's features are not on file (lib/standards/etim/class-features.csv has no EC003948 rows): spec.md gives
the design values under plain names, as reel-cable-630 does. Every size is a design choice; no standard is claimed. No load, mass or
safety claim. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "corner-stacking-1000", "1.0", "furniture"
TITLE = ("stacking corner for a block pallet, generic, painted steel, 1000 clear between the pallets, angle post 60 x 60 x 8 between "
         "lipped plates 120 x 120")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic stacking corner (ETIM 10.0 EC003948), painted steel: a foot plate 128 x 128 x 8 with two lips "
            "16 down, an angle post of two legs 60 x 8, a top plate 128 x 128 x 8 with two lips 16 up, 1000 between the lower "
            "pallet's deck and the upper pallet's underside; sized on pallet 1.2 (read with library.load, fit asserted); one part for "
            "all four corners, turned about z; class features not on file, design values under plain names (spec.md); every size a "
            "design choice; no load, mass or safety claim; no vendor file opened")
ORIGIN = ("the lower pallet's outer corner on its deck top: x and y along the pallet's outer edges (the pallet at x >= 0, y >= 0), "
          "z = 0 the lower pallet's deck top, z = 1000 the upper pallet's underside; on pallet 1.2 the origin goes at its corner "
          "(0, 0, 144), the other three corners the same part turned 90, 180 and 270 degrees about z")
COMMAND = "CRST1000"
PARAMS = dict()

PALLET_V = "1.2"
PL = library.load("pallet", PALLET_V)            # the pallet it stands on and carries (its corner boards: the fit)

HC = 1000.0                                     # design: the clear height, lower deck top to upper pallet underside
S = 120.0                                       # design: the plates' bearing square on the pallet, inside the corner
T = 8.0                                         # design: the steel's thickness (plates, lips, post legs)
A = 60.0                                        # design: the post's legs, an angle 60 x 60 x 8 at the outer corner
LD = 16.0                                       # design: the foot lips' depth below the deck top
LU = 16.0                                       # design: the top lips' height above the upper pallet's underside
IN = 0.5                                        # each lip and post leg 0.5 into its plate, so the part is one body
MAT = "M-STEEL-7035"                            # painted steel (post-partition-2000's layer)

assert S <= PL.DECK_W and S <= PL.B                                                                  # 120: on the corner deck board (x 0 to 120) over the corner block
assert S <= PL.BOT_W                                                                                 # 120 <= 145: under the upper pallet's corner bottom board
assert LD < PL.DECK and LU < PL.BOT                                                                  # 16 < 20, 16 < 18: the lips cover the board edges, never reach past them
assert 2 * S < PL.LX and 2 * S < PL.LY                                                               # four corners, one at each, never meet
assert A < S and T < A                                                                               # the post stands inside the plates
assert T >= 8.0 and LD >= 8.0 and LU >= 8.0                                                          # no edge in the 3 to 7 fillet trap
# Volume by hand (the union): two plates 128 x 128 x 8; two L-shaped lips 16 deep, (8 x 128 + 120 x 8) x 16 each; the post between the
# plates, an L section 60 x 8 + 8 x 60 - 8 x 8 = 896 over 984.
VOL = 2 * (S + T) ** 2 * T + 2 * (T * (S + T) + S * T) * LD + (2 * A * T - T * T) * (HC - 2 * T)
assert abs(VOL - 1207296.0) < 0.5


def build():
    P = Prims()
    H = HC - 2 * T + 2 * IN                                                                      # 985: the post legs, 0.5 into each plate
    P.box(MAT, -T, -T, 0.0, S + T, S + T, T)                                                     # the foot plate, z 0 to 8
    P.box(MAT, -T, -T, -LD, T, S + T, LD + IN)                                                   # its lip down over the deck's x edge
    P.box(MAT, -T, -T, -LD, S + T, T, LD + IN)                                                   # its lip down over the deck boards' y ends
    P.box(MAT, 0.0, 0.0, T - IN, A, T, H)                                                        # the post's leg along x
    P.box(MAT, 0.0, 0.0, T - IN, T, A, H)                                                        # the post's leg along y
    P.box(MAT, -T, -T, HC - T, S + T, S + T, T)                                                  # the top plate, z 992 to 1000
    P.box(MAT, -T, -T, HC - IN, T, S + T, LU + IN)                                               # its lip up over the bottom board's x edge
    P.box(MAT, -T, -T, HC - IN, S + T, T, LU + IN)                                               # its lip up over the bottom boards' y ends
    P.collider("foot", -T, -T, -LD, S + T, S + T, LD + T)
    P.collider("post-x", 0.0, 0.0, T, A, T, HC - 2 * T)
    P.collider("post-y", 0.0, T, T, T, A - T, HC - 2 * T)
    P.collider("top", -T, -T, HC - T, S + T, S + T, LU + T)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="inside", az=50, el=20)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
