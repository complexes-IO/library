#!/usr/bin/env python3
"""conveyor-mattop: modular plastic belt (mat-top) conveyor, one straight section, our own design, built unattended
(OPERATING.md 12, own designs; inventory row own_design "yes": "modular plastic belt (mat-top) conveyor section, 1 in pitch
(our own build)"). Goods travel along y on a belt of plastic modules hinged at 25.4 pitch. The belt is drawn as its top run at
rest, one plate 58 pitches long: it rests on two bed rails, which two cross members carry between the side frames. The modules,
their hinge rods, the return run under the bed and the drive are not drawn. The head shaft and the tail shaft, each with three
sprockets, are nodes `shaft-head` and `shaft-tail`, each turning about its own axis (along x): they are what the twin turns when
the conveyor runs. The frames stand on two supports (two posts, a tie and two foot plates each), the same pattern as
conveyor-roller's and conveyor-slat's, and each foot plate has one M12 clearance hole (ISO 273 medium) for a floor anchor. Every
size below is a design choice. No load rating, no speed, no safety claim. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "conveyor-mattop", "1.1", "furniture"
TITLE = "mat-top conveyor section, 500 between frames, 1500 long, plastic belt 490 wide at 25.4 pitch, belt top 750, head and tail shafts, 4 x M12 anchor holes"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; anchor holes ISO 273 medium for M12; every size a "
            "design choice; no load rating, no speed, no safety claim; no vendor file opened")
ORIGIN = ("floor plane z = 0 at the centre of the section, x = 0 midway between the side frames, y = 0 midway along its length; "
          "goods travel along y toward +y (the head end), the belt's top at z 750, the shafts' axes along x at z 670")
COMMAND = "CONVMATTOP"
PARAMS = dict()
W = 500.0                                        # between the side frames' inner faces (x +-250): design choice, conveyor-roller's
L = 1500.0                                       # the section's length, y -750..750: design choice, conveyor-roller's
TOP = 750.0                                      # the belt's top above the floor: design choice, conveyor-roller's roller tops
PITCH, N = 25.4, 58                              # the belt's hinge pitch, 25.4 (1 in, the inventory row's); the top run drawn 58 pitches long
BELT_L = N * PITCH                               # 1473.2: the plate's length, y +-736.6, 13.4 short of each end of the section
BELT_T = 10.0                                    # the belt 10 thick, drawn as one plate by its outside: design choice
BELT_GAP = 5.0                                   # the belt's edges 5 clear of the side frames
BELT_Z = TOP - BELT_T                            # 740: the belt's underside, the bed rails' tops
FR_W, FR_H = 50.0, 160.0                         # side frames 50 (x) by 160 (z), drawn by their outside: design choice
FR_TOP = TOP - 10.0                              # 740: the frames' tops, 10 below the belt's top, so goods wider than the track pass over
FR_Z = FR_TOP - FR_H                             # 580: the frames' undersides, the posts' tops
RAIL_X, RAIL_W, RAIL_H = 125.0, 50.0, 40.0       # two bed rails, centres x +-125, 50 wide, 40 deep (z 700..740): design choice
RAIL_Y = 730.0                                   # the rails' ends, y +-730: under the whole plate but its last 6.6; 10 above the shafts, between the sprockets
XM_H = 40.0                                      # cross members between the side frames at the supports, 40 deep (z 660..700), 50 along y
XM_Z = BELT_Z - RAIL_H - XM_H                    # 660: the cross members' undersides
SH_Y, SH_Z = 650.0, 670.0                        # the shafts' axes: y +-650 (100 from the section's ends), z 670
SH_R = 20.0                                      # shafts Ø40, drawn round: design choice
SP_R, SP_W = 60.0, 30.0                          # sprockets Ø120, 30 wide, drawn as plain discs (no teeth): design choice
SP_X = (-200.0, 0.0, 200.0)                      # three sprockets on each shaft, centres x -200, 0, +200
SUP_Y = 500.0                                    # the two supports' centres, y +-500: conveyor-roller's
POST = 50.0                                      # posts 50 x 50 under each side frame, drawn by their outside
PL_W, PL_L, PL_T = 150.0, 100.0, 20.0            # foot plates 150 (x) by 100 (y), 20 thick, under each post, running outward
PL_X0 = W / 2 - 25.0                             # 225: a foot plate's inner edge, 25 inside the post's inner face
HOLE_X = W / 2 + POST + 40.0                     # 340: anchor hole centres x +-340, 40 outside the post, 35 from the plate's outer edge
M12_D = 13.5                                     # M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv)
TIE_LO = (150.0, 50.0)                           # lower tie between the posts: underside z 150, 50 deep

def build():
    P = Prims(); S = "M-STEEL-7035"; R = "M-ZINC"; B = "M-GREY-PA"; K = "M-BLACK-PA"   # belt grey plastic, sprockets black plastic
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
        rx = sx * RAIL_X - RAIL_W / 2
        P.box(S, rx, -RAIL_Y, BELT_Z - RAIL_H, RAIL_W, 2 * RAIL_Y, RAIL_H)                           # bed rail, on the cross members
        P.collider(f"rail-{k}", rx, -RAIL_Y, BELT_Z - RAIL_H, RAIL_W, 2 * RAIL_Y, RAIL_H)
    for sy, j in ((-1, "a"), (1, "b")):
        y = sy * SUP_Y
        P.box(S, -x0, y - POST / 2, XM_Z, W, POST, XM_H)                                             # cross member, frame to frame
        P.collider(f"cross-{j}", -x0, y - POST / 2, XM_Z, W, POST, XM_H)
        P.box(S, -x0, y - POST / 2, TIE_LO[0], W, POST, TIE_LO[1])                                   # lower tie, post to post
        P.collider(f"tie-lo-{j}", -x0, y - POST / 2, TIE_LO[0], W, POST, TIE_LO[1])
    xs = x0 - BELT_GAP                                                  # the belt's edges and the shafts' end faces: x +-245
    P.box(B, -xs, -BELT_L / 2, BELT_Z, 2 * xs, BELT_L, BELT_T)                                       # the belt's top run, one plate, on the bed rails
    P.collider("belt-deck", -xs, -BELT_L / 2, BELT_Z, 2 * xs, BELT_L, BELT_T)                        # what goods ride on
    for n, y in (("shaft-head", SH_Y), ("shaft-tail", -SH_Y)):
        xa = -xs                                                        # stacked end to end, no solid inside another:
        for cx in SP_X:
            P.cyl(f"node:{n}|{R}", (xa, y, SH_Z), (cx - SP_W / 2, y, SH_Z), SH_R)                    # shaft, up to the sprocket's face
            P.cyl(f"node:{n}|{K}", (cx - SP_W / 2, y, SH_Z), (cx + SP_W / 2, y, SH_Z), SP_R)         # sprocket, a plain disc
            xa = cx + SP_W / 2
        P.cyl(f"node:{n}|{R}", (xa, y, SH_Z), (xs, y, SH_Z), SH_R)                                   # shaft, the last length to its end face
        P.pivot(n, "rotate", (-xs, y, SH_Z), axis=(1, 0, 0), range=(0, 360), unit="deg")             # turns in its bearings (not drawn)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="side", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
