#!/usr/bin/env python3
"""ramp-loading-150: generic loading ramp, a floor-standing steel ramp that takes wheeled loads (a hand pallet truck, a trolley) from the
floor up 150 to a landing, our own vendor-neutral design of the ETIM 10.0 class EC004428 (Loading ramp), built unattended
(OPERATING.md 12, generic elements; group EG010340 Storage and racking systems, a tier-2 class walked by name after corner-stacking-1000,
lib/rounds/mech/r170.md). One welded steel body: a nose 10 high at the floor, a deck rising 1 in 10 over 1400 to a flat landing 100 deep
at 150, closed side walls, three ribs between four bays, open underneath; the deck and every wall 8 thick. Drawn as one box with one
oblique cut above the slope, four oblique cuts (the bays under the deck, their tops 8 below the slope) and four axis-aligned cuts (the
bays under the landing). No host on file: it meets the floor and whatever platform stands at its landing; no element is placed or read.
The class's features are not on file (lib/standards/etim/class-features.csv has no EC004428 rows): spec.md gives the design values under
plain names, as corner-stacking-1000 does. Every size is a design choice; no standard is claimed (no access-ramp gradient rule is on
file). No load, mass or safety claim. No vendor file opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "ramp-loading-150", "1.0", "furniture"
TITLE = ("loading ramp, generic, painted steel, 150 rise at 1 in 10, 1000 wide, 1500 long with a landing 100 deep, hollow underneath")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic loading ramp (ETIM 10.0 EC004428), painted steel 8 thick welded as one body: a nose 10 high, a "
            "deck rising 1 in 10 over 1400 to a flat landing 100 deep at 150, 1000 wide, side walls and three ribs between four bays "
            "open underneath; no host on file; class features not on file, design values under plain names (spec.md); every size a "
            "design choice; no load, mass or safety claim; no vendor file opened")
ORIGIN = ("the nose's lower front corner on the floor: x up the ramp (the landing at x 1400 to 1500), y across it (0 to 1000), z up "
          "from the floor; the landing's back face x = 1500 stands against the platform it serves, whose top is at z = 150")
COMMAND = "RMPL150"
PARAMS = dict()

L = 1500.0                                      # design: the overall length, nose to the landing's back face
W = 1000.0                                      # design: the width (a hand pallet truck's forks and wheels inside it)
H = 150.0                                       # design: the rise, the landing's top above the floor
H0 = 10.0                                       # design: the nose's height at the floor (the step a wheel climbs onto the deck)
G = 0.1                                         # design: the deck's gradient, 1 in 10
XL = (H - H0) / G                               # 1400: the slope's run, nose to the landing
T = 8.0                                         # design: the steel's thickness (deck, landing, side walls, ribs, back walls)
NB = 4                                          # design: four bays under the deck, three ribs between them
X_F = 100.0                                     # design: the bays start 100 up the slope (the nose solid below it)
MAT = "M-STEEL-7035"                            # painted steel (post-partition-2000's and corner-stacking-1000's layer)

C = 1.0 / math.sqrt(1.0 + G * G)                # cos of the slope angle (5.71 degrees)
S = G * C                                       # sin of it
U = (C, 0.0, S)                                 # up the slope
N = (-S, 0.0, C)                                # the deck's upward normal (U x y = N, right-handed)
BAY = (W - (NB + 1) * T) / NB                   # 240: each bay's width, between walls and ribs 8 thick
# The bays under the deck: their tops on the plane 8 (normal) under the slope, z = H0 - T / C + G x; their front and back faces square to
# the deck. F: the front face's top, under the slope at x = X_F; the back face meets the floor at x = XL - T (a back wall 8 at the floor).
FX, FZ = X_F + T * S, H0 + G * X_F - T * C
TB = (H0 - T / C + G * (XL - T)) / (C + G * S)  # the back face's length, floor to the bay's top
BX, BZ = XL - T - TB * S, TB * C                # its top
LC = (BX - FX) / C                              # the bay's length along the slope
FL = FZ / C                                     # the front face's length, floor to the bay's top
ZL = H - T                                      # the bays under the landing: tops 8 under the landing's top, x XL to L - T

assert abs(XL - 1400.0) < 1e-9 and abs(BAY - 240.0) < 1e-9
assert abs((FZ - (H0 + G * FX - T / C))) < 1e-9 and abs(BZ - (H0 - T / C + G * BX)) < 1e-9   # F and B on the bays' top plane
assert FZ >= T and FL >= T                                                                   # the bays' front faces 12 high: no edge under 8
assert BX > FX and BZ < H - T and L - T > XL                                                 # the bays end under the slope; landing bays behind
assert XL - BX >= T                                                                          # the wall between the two bay rows: 8 at the floor, 22 at the top
assert H0 >= T and L - XL >= 100.0                                                           # no box edge in the 3 to 7 fillet trap
# Volume by hand (one body): the side section, a 1500 x 150 rectangle less the triangle-and-strip above the slope, 225000 - 98000 =
# 127000, over the width 1000; less the deck bays, each a trapezoid in section (its parallel sides the front and back faces, 12.1 and
# 140.46, LC 1283.6 apart) over 240; less the landing bays 92 x 142 over 240.
SEC = L * H - (XL * (H - H0) - G * XL * XL / 2.0)
VOL = SEC * W - NB * BAY * LC * (FL + TB) / 2.0 - NB * BAY * (L - T - XL) * ZL
assert abs(SEC - 127000.0) < 1e-6 and abs(VOL - 20462652.0) < 1.0


def build():
    P = Prims()
    b = P.box(MAT, 0.0, 0.0, 0.0, L, W, H)                                                       # the whole ramp, before its cuts
    P.cut(MAT, (-100.0, -10.0, H0 - 100.0 * G), U, (0, 1, 0), N, (XL + 200.0) / C, W + 20.0, 300.0, b)   # above the slope
    for i in range(NB):
        y0 = T + i * (BAY + T)
        P.cut(MAT, (FX + 400.0 * S, y0, FZ - 400.0 * C), U, (0, 1, 0), N, LC, BAY, 400.0, b)    # the bay under the deck, open below
        P.cutbox(MAT, XL, y0, -10.0, L - T - XL, BAY, ZL + 10.0, b)                              # the bay under the landing, open below
    P.collider("step-1", 0.0, 0.0, 0.0, 350.0, W, H0 + G * 350.0)
    P.collider("step-2", 350.0, 0.0, 0.0, 350.0, W, H0 + G * 700.0)
    P.collider("step-3", 700.0, 0.0, 0.0, 350.0, W, H0 + G * 1050.0)
    P.collider("landing", 1050.0, 0.0, 0.0, L - 1050.0, W, H)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="rear", az=50, el=20)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
