#!/usr/bin/env python3
"""rack-cable-drum-1000: generic cable drum rack, free-standing, 1000 clear between its side frames, two tiers of axles, our own
vendor-neutral design of the ETIM 10.0 class EC004067 (Cable drum rack; synonyms Stoarge rack, Storage and factory equipment), built
unattended (OPERATING.md 12, generic elements; group EG010340 Storage and racking systems, a tier-2 class walked by name after
rack-bins-1000, lib/rounds/mech/r162.md). Two side frames of painted steel tube 50 x 50 x 2, each an upright standing on a foot laid
along y, joined by a top bar between the uprights and a floor tie between the feet's rear ends; two removable round bright-steel axles
Ø40 run through Ø42 bores in both uprights, one above the other, and each carries cable drums up to Ø700 x 960 wide that turn on it
as cable is paid out to the front (-y). The axles' retention (a pin or a collar at each end) and the drums are not drawn. rack-bins-1000's
tube (50 x 50 x 2, one box less one through cutbox) is its construction; no other element is placed or redrawn. The class's features are
not on file (lib/standards/etim/class-features.csv has no EC004067 rows): spec.md gives the design values under plain names, as
rack-bins-1000 does. Every size is a design choice. No load, stability or safety claim: fixing the rack to the floor is the host's.
No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "rack-cable-drum-1000", "1.0", "furniture"
TITLE = ("cable drum rack, free-standing, generic, 1000 clear between two side frames of painted steel tube 50 x 50 x 2, two removable "
         "axles Ø40 for drums up to Ø700 x 960")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic cable drum rack (ETIM 10.0 EC004067), two side frames of painted steel tube 50 x 50 x 2 (an "
            "upright 1600 high on a foot 700 long, centred on it), 1000 apart inside, joined by a top bar and a floor tie 1000 long; two "
            "removable bright-steel axles Ø40 x 1180 through Ø42 bores in both uprights at z 450 and 1200, for cable drums up to Ø700 "
            "and 960 wide; class features not on file, design values under plain names (spec.md); every size a design choice; drums and "
            "the axles' retention not drawn; no load, stability or safety claim; no vendor file opened")
ORIGIN = ("the floor under the middle of the rack: z = 0 the feet's undersides, x = 0 midway between the side frames, y = 0 the axles' "
          "axis (the uprights' middle); cable pays out toward -y; the feet reach y -350 to 350")
COMMAND = "RCDR1000"
PARAMS = dict()

UP = 50.0                                       # design: the tube's section, rack-bins-1000's (50 x 50)
T = 2.0                                         # design: the tube's wall (painted steel tube 50 x 50 x 2)
XI = 500.0                                      # design: the side frames' inner faces x +-500, 1000 clear for a drum 960 wide
XO = XI + UP                                    # 550: their outer faces, the frame's width 1100
FY = 350.0                                      # design: the feet reach 350 in front of and behind the axles' axis
H = 1650.0                                      # design: the rack's height (the top bar's and the uprights' tops)
ZA = (450.0, 1200.0)                            # design: the axles' axis heights, lower and upper
RA = 20.0                                       # design: the axle, round bright-steel bar Ø40
RB = 21.0                                       # design: the bores in the uprights Ø42, 1 clear all round (a loose sliding fit, so the axle draws out)
XA = XO + 40.0                                  # 590: the axles' ends, 40 past each upright's outer face for a pin or collar (not drawn)
D_MAX, W_MAX = 700.0, 960.0                     # design: the largest drum, diameter and width
TIE_Y0 = FY - UP                                # 300: the floor tie between the feet's rear ends, y 300 to 350
MAT, AX = "M-STEEL-7035", "M-SILVER"           # painted steel (rack-bins-1000's layer); the axles bright steel

R = D_MAX / 2                                   # 350
assert W_MAX < 2 * XI                                                                               # a drum fits between the frames, 20 a side
assert ZA[0] - R >= UP                                                                              # 100: the lower drum clears the floor tie's top
assert ZA[1] - ZA[0] >= D_MAX                                                                       # 750 >= 700: the drums clear each other
assert (H - UP) - (ZA[1] + R) >= 0                                                                  # 50: the upper drum clears the top bar
assert FY >= R                                                                                      # the feet reach as far as the drum's rim, front and back
assert RB - RA >= 0.5                                                                              # the bore clears the axle
# The tube: section 50 x 50, wall 2; every tube is one box less one through cutbox (rack-bins-1000's), so its edges are 2, 50 and its
# length: none falls in the 3 to 7 fillet trap. The bores go through both walls of each upright, across its cavity.
SEC = UP * UP - (UP - 2 * T) ** 2                                                                   # 384 mm^2
L_UP, L_FOOT, L_BAR = H - UP, 2 * FY, 2 * XI                                                        # 1600, 700, 1000
TUBES = SEC * (2 * L_UP + 2 * L_FOOT + 2 * L_BAR)                                                   # 384 x 6600 = 2534400 (before the bores)
assert abs(SEC - 384.0) < 1e-9 and abs(TUBES - 2534400.0) < 1e-6


def build():
    P = Prims()
    for sx, s in ((-1, "l"), (1, "r")):
        x0 = -XO if sx < 0 else XI
        f = P.box(MAT, x0, -FY, 0.0, UP, L_FOOT, UP)                                            # the foot, a tube laid along y
        P.cutbox(MAT, x0 + T, -FY - 1.0, T, UP - 2 * T, L_FOOT + 2.0, UP - 2 * T, f)
        P.collider(f"foot-{s}", x0, -FY, 0.0, UP, L_FOOT, UP)
        u = P.box(MAT, x0, -UP / 2, UP, UP, UP, L_UP)                                           # the upright, centred on its foot
        P.cutbox(MAT, x0 + T, -UP / 2 + T, UP - 1.0, UP - 2 * T, UP - 2 * T, L_UP + 2.0, u)
        for za in ZA:                                                                           # the axle bores, through both walls
            P.hole(MAT, (x0 - 1.0, 0.0, za), (x0 + UP + 1.0, 0.0, za), RB, u)
        P.collider(f"upright-{s}", x0, -UP / 2, UP, UP, UP, L_UP)
    t = P.box(MAT, -XI, -UP / 2, H - UP, L_BAR, UP, UP)                                         # the top bar between the uprights' inner faces
    P.cutbox(MAT, -XI - 1.0, -UP / 2 + T, H - UP + T, L_BAR + 2.0, UP - 2 * T, UP - 2 * T, t)
    P.collider("bar-top", -XI, -UP / 2, H - UP, L_BAR, UP, UP)
    b = P.box(MAT, -XI, TIE_Y0, 0.0, L_BAR, UP, UP)                                            # the floor tie between the feet's rear ends
    P.cutbox(MAT, -XI - 1.0, TIE_Y0 + T, T, L_BAR + 2.0, UP - 2 * T, UP - 2 * T, b)
    P.collider("tie-floor", -XI, TIE_Y0, 0.0, L_BAR, UP, UP)
    for k, za in enumerate(ZA, start=1):                                                        # the axles, lower then upper
        P.cyl(AX, (-XA, 0.0, za), (XA, 0.0, za), RA)
        P.collider(f"axle-{k}", -XA, -RA, za - RA, 2 * XA, 2 * RA, 2 * RA)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
