#!/usr/bin/env python3
"""conveyor-roller: generic gravity roller conveyor, one straight section, our own vendor-neutral design of the ETIM 10.0 class
EC004418 (Roller conveyor), built unattended (OPERATING.md 12, generic elements; inventory row own_design "generic", etim
EC004418). Goods travel along y over twenty free rollers that lie across the track between two side frames; the frames stand on
two supports (two posts, two ties and two foot plates each), and each foot plate has one M12 clearance hole (ISO 273 medium) for a
floor anchor. The rollers are nodes `roller-1` to `roller-20`, each spinning freely about its own axis (along x); nothing drives
them. The axles and their bearings are not drawn: each roller's end faces stand 5 clear of the side frames. The class values
(spec.md, "Class values") are design inputs; every size below is a design choice, and none is taken from the catalogue record
that came with the element's folder (references/source.txt). No load rating, no safety claim. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "conveyor-roller", "1.1", "furniture"
TITLE = "roller conveyor, generic, gravity, 500 between frames, 1500 long, 20 rollers Ø50 at 75 pitch, roller tops 750, 4 x M12 anchor holes"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic roller conveyor (ETIM 10.0 EC004418); class values are design inputs (spec.md); anchor holes "
            "ISO 273 medium for M12; every size a design choice; no load rating, no safety claim; no vendor file opened")
ORIGIN = ("floor plane z = 0 at the centre of the section, x = 0 midway between the side frames, y = 0 midway along its length; "
          "goods travel along y, the rollers' axes along x at z 725, the rollers' tops at z 750")
COMMAND = "CONVROLLER"
PARAMS = dict()
W = 500.0                                        # between the side frames' inner faces (x +-250): class value (design input)
L = 1500.0                                       # the section's length, y -750..750: class value (design input)
TOP = 750.0                                      # the rollers' tops above the floor: class value (design input)
N, PITCH = 20, 75.0                              # 20 rollers at 75 pitch, the end rollers' axes 37.5 from the section's ends: class value, pitch a design choice
ROLL_R = 25.0                                    # rollers Ø50: class value (design input)
ROLL_GAP = 5.0                                   # each roller's end face 5 clear of the side frame (the axle is not drawn)
AXIS_Z = TOP - ROLL_R                            # 725: the rollers' axes
FR_W, FR_H = 50.0, 80.0                          # side frames 50 (x) by 80 (z), drawn by their outside: design choice
FR_TOP = TOP - 10.0                              # 740: the frames' tops, 10 below the rollers' tops, so goods wider than the track pass over
FR_Z = FR_TOP - FR_H                             # 660: the frames' undersides, the posts' tops
SUP_Y = 500.0                                    # the two supports' centres, y +-500: design choice
POST = 50.0                                      # posts 50 x 50 under each side frame, drawn by their outside: design choice
PL_W, PL_L, PL_T = 150.0, 100.0, 20.0            # foot plates 150 (x) by 100 (y), 20 thick, under each post, running outward: design choice
PL_X0 = W / 2 - 25.0                             # 225: a foot plate's inner edge, 25 inside the post's inner face
HOLE_X = W / 2 + POST + 40.0                     # 340: anchor hole centres x +-340, 40 outside the post, 35 from the plate's outer edge
M12_D = 13.5                                     # M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv)
TIE_UP = (600.0, 40.0)                           # upper tie between the posts: underside z 600, 40 deep, its top z 640 (60 below the rollers' undersides at z 700): design choice
TIE_LO = (150.0, 50.0)                           # lower tie between the posts: underside z 150, 50 deep: design choice

def roller_y(i):
    return -L / 2 + PITCH / 2 + (i - 1) * PITCH                                                      # roller i's axis, i = 1..N from the -y end

def build():
    P = Prims(); S = "M-STEEL-7035"; R = "M-ZINC"                       # rollers: zinc-plated steel tube
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
    xr = x0 - ROLL_GAP                                                  # the rollers' end faces: x +-245
    for i in range(1, N + 1):
        n, y = f"roller-{i}", roller_y(i)
        P.cyl(f"node:{n}|{R}", (-xr, y, AXIS_Z), (xr, y, AXIS_Z), ROLL_R)                            # free roller
        P.pivot(n, "rotate", (-xr, y, AXIS_Z), axis=(1, 0, 0), range=(0, 360), unit="deg")           # spins on its axle
    P.collider("roll-bed", -xr, -L / 2, AXIS_Z - ROLL_R, 2 * xr, L, 2 * ROLL_R)                      # the roller bed: what goods ride on
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="side", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
