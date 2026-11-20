#!/usr/bin/env python3
"""rack-lifting-gear-1000: generic lifting equipment rack, free-standing, 1000 clear between its side frames, eight hooks on a top bar,
our own vendor-neutral design of the ETIM 10.0 class EC004245 (Lifting equipment rack; synonyms Attachment gear stand, Lifting
equipment stand), built unattended (OPERATING.md 12, generic elements; group EG010340 Storage and racking systems, a tier-2 class
walked by name after rack-cable-drum-1000, lib/rounds/mech/r163.md). Slings, chains and their fittings hang from the hooks on both
faces, so the rack is used from the front and from the back. Two side frames of painted steel tube 50 x 50 x 2, each an upright
standing on the middle of a foot laid along y, joined by a top bar between the uprights' tops and a floor tie between the feet's
middles; on each face of the top bar four L-shaped hooks of round bar Ø20 (an arm straight out, a tip turned up, hook-rack's pin
construction), welded on and painted with the frame. hook-rack 1.0 is a hanger for powder coating that hangs from a conveyor; this is
a floor stand: neither draws the other. rack-cable-drum-1000's tube (50 x 50 x 2, one box less one through cutbox) is its construction;
no element is placed or redrawn. The class's features are not on file (lib/standards/etim/class-features.csv has no EC004245 rows):
spec.md gives the design values under plain names, as rack-cable-drum-1000 does. Every size is a design choice. No working load limit,
stability or safety claim: the lifting gear's own rating is its maker's, and fixing the rack to the floor is the host's. No vendor
file opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "rack-lifting-gear-1000", "1.0", "furniture"
TITLE = ("lifting equipment rack, free-standing, generic, 1000 clear between two side frames of painted steel tube 50 x 50 x 2, eight "
         "L-hooks Ø20 on a top bar at 1625, four on each face")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic lifting equipment rack (ETIM 10.0 EC004245), two side frames of painted steel tube 50 x 50 x 2 (an "
            "upright 1600 high on a foot 800 long, centred on it), 1000 apart inside, joined by a top bar and a floor tie 1000 long; "
            "eight L-hooks of round bar Ø20 on the top bar, four on each face, 250 apart, each an arm reaching 150 out and a tip turned "
            "up 25, welded on; class features not on file, design values under plain names (spec.md); every size a design choice; the "
            "lifting gear not drawn; no working load limit, stability or safety claim; no vendor file opened")
ORIGIN = ("the floor under the middle of the rack: z = 0 the feet's undersides, x = 0 midway between the side frames, y = 0 the top "
          "bar's middle (the uprights' middle); the hooks stand out toward -y (front) and +y (back); the feet reach y -400 to 400")
COMMAND = "RLGR1000"
PARAMS = dict()

UP = 50.0                                       # design: the tube's section, rack-cable-drum-1000's (50 x 50)
T = 2.0                                         # design: the tube's wall (painted steel tube 50 x 50 x 2)
XI = 500.0                                      # design: the side frames' inner faces x +-500, 1000 clear
XO = XI + UP                                    # 550: their outer faces, the frame's width 1100
FY = 400.0                                      # design: the feet reach 400 in front of and behind the top bar's middle
H = 1650.0                                      # design: the rack's height (the top bar's and the uprights' tops)
ZH = H - UP / 2                                 # 1625: the hooks' arm axis, the top bar's middle
HX = (-375.0, -125.0, 125.0, 375.0)             # design: four hooks on each face, 250 apart
HR = 10.0                                       # design: the hooks' round bar Ø20
H_IN = 2.0                                      # each arm starts 2 inside the bar's face, in its wall (one body, no gap): hook-rack's PIN_IN
H_OUT = 150.0                                   # design: the tip's axis 150 out from the bar's face (y +-175)
TIP_UP = UP / 2                                 # 25: the tip's top 25 above the arm's axis, flush with the bar's top (z 1650)
MAT = "M-STEEL-7035"                            # painted steel (rack-cable-drum-1000's layer); the hooks welded on and painted with it

Y_TIP = UP / 2 + H_OUT                          # 175: the tip's axis
REACH = Y_TIP + HR                              # 185: the hooks' outer faces
assert ZH + TIP_UP <= H                                                                             # the tips stay under the bar's top
assert TIP_UP - HR >= 10.0                                                                          # 15: the tip stands 15 above the arm's top, so a sling's eye stays on
assert FY - REACH >= 200.0                                                                          # 215: the feet reach past the hooks, front and back
assert XI - (max(HX) + HR) >= 100.0                                                                 # 115: the outer hooks clear the uprights
assert min(b - a for a, b in zip(HX, HX[1:])) - 2 * HR >= 200.0                                     # 230 clear between neighbouring hooks
# The tube: section 50 x 50, wall 2; every tube is one box less one through cutbox (rack-cable-drum-1000's), so its edges are 2, 50 and
# its length: none falls in the 3 to 7 fillet trap.
SEC = UP * UP - (UP - 2 * T) ** 2                                                                   # 384 mm^2
L_UP, L_FOOT, L_BAR = H - UP, 2 * FY, 2 * XI                                                        # 1600, 800, 1000
TUBES = SEC * (2 * L_UP + 2 * L_FOOT + 2 * L_BAR)                                                   # 384 x 6800 = 2611200
assert abs(SEC - 384.0) < 1e-9 and abs(TUBES - 2611200.0) < 1e-6
# A hook, by hand: the arm pi r^2 x 152, the tip pi r^2 x 35, less the arm's 2 in the bar's wall and half a Steinmetz solid (16 r^3 / 3)
# where the arm ends on the tip's axis.
HOOK = math.pi * HR ** 2 * (H_IN + H_OUT) + math.pi * HR ** 2 * (TIP_UP + HR) - math.pi * HR ** 2 * H_IN - 8 * HR ** 3 / 3
assert abs(HOOK - 55453.0) < 1.0                                                                    # about 55453 mm^3 a hook


def build():
    P = Prims()
    for sx, s in ((-1, "l"), (1, "r")):
        x0 = -XO if sx < 0 else XI
        f = P.box(MAT, x0, -FY, 0.0, UP, L_FOOT, UP)                                            # the foot, a tube laid along y
        P.cutbox(MAT, x0 + T, -FY - 1.0, T, UP - 2 * T, L_FOOT + 2.0, UP - 2 * T, f)
        P.collider(f"foot-{s}", x0, -FY, 0.0, UP, L_FOOT, UP)
        u = P.box(MAT, x0, -UP / 2, UP, UP, UP, L_UP)                                           # the upright, centred on its foot
        P.cutbox(MAT, x0 + T, -UP / 2 + T, UP - 1.0, UP - 2 * T, UP - 2 * T, L_UP + 2.0, u)
        P.collider(f"upright-{s}", x0, -UP / 2, UP, UP, UP, L_UP)
    t = P.box(MAT, -XI, -UP / 2, H - UP, L_BAR, UP, UP)                                         # the top bar between the uprights' inner faces
    P.cutbox(MAT, -XI - 1.0, -UP / 2 + T, H - UP + T, L_BAR + 2.0, UP - 2 * T, UP - 2 * T, t)
    P.collider("bar-top", -XI, -UP / 2, H - UP, L_BAR, UP, UP)
    b = P.box(MAT, -XI, -UP / 2, 0.0, L_BAR, UP, UP)                                           # the floor tie between the feet's middles
    P.cutbox(MAT, -XI - 1.0, -UP / 2 + T, T, L_BAR + 2.0, UP - 2 * T, UP - 2 * T, b)
    P.collider("tie-floor", -XI, -UP / 2, 0.0, L_BAR, UP, UP)
    for sy, s in ((-1, "front"), (1, "back")):
        y_in, y_tip = sy * (UP / 2 - H_IN), sy * Y_TIP
        for x in HX:
            P.cyl(MAT, (x, y_in, ZH), (x, y_tip, ZH), HR)                                       # the arm, straight out of the bar's face
            P.cyl(MAT, (x, y_tip, ZH - HR), (x, y_tip, ZH + TIP_UP), HR)                        # the tip, turned up; the arm ends on its axis
        y0 = UP / 2 if sy > 0 else -REACH
        P.collider(f"hooks-{s}", min(HX) - HR, y0, ZH - HR, max(HX) - min(HX) + 2 * HR, REACH - UP / 2, HR + TIP_UP)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
