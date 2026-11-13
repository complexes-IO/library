#!/usr/bin/env python3
"""conveyor-wheel: generic skate-wheel gravity conveyor, one straight section, our own vendor-neutral design of the ETIM 10.0 class
EC004417 (Wheel conveyor), built unattended (OPERATING.md 12, generic elements; the inventory row conveyor-wheel is own_design
"generic"; its etim cell and the class's features follow with the attended ETIM push, request mech-9's answer item 3). Goods travel
along y over 38 free skate wheels on 15 axle lines across the track: three wheels on the odd lines and two on the even ones,
staggered, so a carton rides on five wheel tracks. The track is conveyor-roller 1.0's: two side frames 500 apart on two supports
(two posts, two ties and two foot plates each), each foot plate with one M12 clearance hole (ISO 273 medium) for a floor anchor, so
sections of the two elements line up end to end. The wheels are nodes `wheel-<line>-<k>` (line 1 at the -y end; k from -x), each
spinning freely about its own axis (along x); nothing drives them. The axles and their bearings are not drawn: a wheel touches
nothing at rest or as it turns. The class values (spec.md, "Class values") are design inputs; every size below is a design choice.
No load rating, no safety claim. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "conveyor-wheel", "1.1", "furniture"
TITLE = "wheel conveyor, generic, gravity, 500 between frames, 1500 long, 38 skate wheels Ø50 on 15 lines at 100 pitch, wheel tops 750, 4 x M12 anchor holes"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic wheel conveyor (ETIM 10.0 EC004417); class values are design inputs (spec.md); anchor holes "
            "ISO 273 medium for M12; every size a design choice; no load rating, no safety claim; no vendor file opened")
ORIGIN = ("floor plane z = 0 at the centre of the section, x = 0 midway between the side frames, y = 0 midway along its length; "
          "goods travel along y, the wheels' axes along x at z 725, the wheels' tops at z 750")
COMMAND = "CONVWHEEL"
PARAMS = dict()
W = 500.0                                        # between the side frames' inner faces (x +-250): class value (design input)
L = 1500.0                                       # the section's length, y -750..750: class value (design input)
TOP = 750.0                                      # the wheels' tops above the floor: class value (design input)
NL, PITCH = 15, 100.0                            # 15 axle lines at 100 pitch, the end lines 50 from the section's ends: class values (design inputs, spec.md Class values)
ODD_X, EVEN_X = (-150.0, 0.0, 150.0), (-75.0, 75.0)   # wheel centres across the track: three on the odd lines, two on the even ones (staggered): design choice
WHEEL_R, WHEEL_W = 25.0, 25.0                    # skate wheels Ø50, 25 wide: class value (diameter), design choice (width)
AXIS_Z = TOP - WHEEL_R                           # 725: the wheels' axes
FR_W, FR_H = 50.0, 80.0                          # side frames 50 (x) by 80 (z), drawn by their outside: design choice (conveyor-roller's)
FR_TOP = TOP - 10.0                              # 740: the frames' tops, 10 below the wheels' tops, so goods wider than the track pass over
FR_Z = FR_TOP - FR_H                             # 660: the frames' undersides, the posts' tops
SUP_Y = 500.0                                    # the two supports' centres, y +-500: design choice
POST = 50.0                                      # posts 50 x 50 under each side frame, drawn by their outside: design choice
PL_W, PL_L, PL_T = 150.0, 100.0, 20.0            # foot plates 150 (x) by 100 (y), 20 thick, under each post, running outward: design choice
PL_X0 = W / 2 - 25.0                             # 225: a foot plate's inner edge, 25 inside the post's inner face
HOLE_X = W / 2 + POST + 40.0                     # 340: anchor hole centres x +-340, 40 outside the post, 35 from the plate's outer edge
M12_D = 13.5                                     # M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv)
TIE_UP = (600.0, 40.0)                           # upper tie between the posts: underside z 600, 40 deep (60 below the wheels' undersides at 700): design choice
TIE_LO = (150.0, 50.0)                           # lower tie between the posts: underside z 150, 50 deep: design choice

def line_y(i):
    return -L / 2 + PITCH / 2 + (i - 1) * PITCH                                                      # axle line i, i = 1..NL from the -y end

def line_x(i):
    return ODD_X if i % 2 else EVEN_X                                                                # the wheel centres on line i

def wheels():
    return [(f"wheel-{i}-{k}", x, line_y(i)) for i in range(1, NL + 1) for k, x in enumerate(line_x(i), 1)]

def build():
    P = Prims(); S = "M-STEEL-7035"; Z = "M-ZINC"                       # wheels: zinc-plated steel
    x0 = W / 2                                                          # the frames' and posts' inner faces: x +-250
    for sx, k in ((-1, "l"), (1, "r")):
        fx = x0 if sx > 0 else -x0 - FR_W
        P.box(S, fx, -L / 2, FR_Z, FR_W, L, FR_H)                                                    # side frame
        P.collider(f"frame-{k}", fx, -L / 2, FR_Z, FR_W, L, FR_H)
        for sy, j in ((-1, "a"), (1, "b")):
            y = sy * SUP_Y
            P.box(S, fx, y - POST / 2, PL_T, POST, POST, FR_Z - PL_T)                                # post, on its foot plate
            px = PL_X0 if sx > 0 else -PL_X0 - PL_W
            pl = P.box(S, px, y - PL_L / 2, 0, PL_W, PL_L, PL_T)                                     # foot plate
            P.hole(S, (sx * HOLE_X, y, -1), (sx * HOLE_X, y, PL_T + 1), M12_D / 2, pl)               # M12 anchor hole
            P.collider(f"post-{k}{j}", fx, y - POST / 2, PL_T, POST, POST, FR_Z - PL_T)
            P.collider(f"foot-{k}{j}", px, y - PL_L / 2, 0, PL_W, PL_L, PL_T)
    for sy, j in ((-1, "a"), (1, "b")):
        y = sy * SUP_Y
        for n, (z, h) in (("up", TIE_UP), ("lo", TIE_LO)):
            P.box(S, -x0, y - POST / 2, z, W, POST, h)                                               # tie, post to post
            P.collider(f"tie-{n}-{j}", -x0, y - POST / 2, z, W, POST, h)
    for n, x, y in wheels():
        P.cyl(f"node:{n}|{Z}", (x - WHEEL_W / 2, y, AXIS_Z), (x + WHEEL_W / 2, y, AXIS_Z), WHEEL_R)   # free skate wheel
        P.pivot(n, "rotate", (x - WHEEL_W / 2, y, AXIS_Z), axis=(1, 0, 0), range=(0, 360), unit="deg")   # spins on its axle (not drawn)
    xb = max(ODD_X) + WHEEL_W / 2                                       # 162.5: the wheel bed's half width
    P.collider("wheel-bed", -xb, -L / 2, AXIS_Z - WHEEL_R, 2 * xb, L, 2 * WHEEL_R)                  # the wheel bed: what goods ride on
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="side", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
