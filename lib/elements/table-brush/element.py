#!/usr/bin/env python3
"""table-brush: a brush table for the sheet feed of a turret punch, our own design (OPERATING.md 12, own designs; inventory row
own_design "yes": "brush table for sheet feed (turret punch)"; lib/machines-factory.txt, punch-turret). A sheet slides over a field
of upright brush strips, so it can be pushed in any direction without scratching and the punched slugs and parts fall between
the strips. A welded table on four legs: a top frame 2000 x 1250, one solid cut open in the middle (rack-bar 1.0's lesson), two
lower stretchers, and nineteen brush strips across the frame's long rails, each an aluminium holder with a nylon bristle block on
it. One fixed body, no node, no hole: the table's fixing to the floor and its height match to the punch's table are the
assembly's (punch-turret is not built, so the work plane z 920 is a design choice checked when it is). Every size is a design
choice. No load rating, no bristle stiffness, no safety claim. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "table-brush", "1.0", "furniture"
TITLE = "brush table 2000 x 1250, work plane at 920, nineteen brush strips across a top frame on four legs"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; no hole, thread or standard interface; the work "
            "plane's match to the punch's table is checked when punch-turret is on file; every size a design choice; no load, "
            "stiffness or safety claim; no vendor file opened")
ORIGIN = ("the floor plane z = 0 at the centre of the table's footprint x = 0, y = 0; the table's length along x; the side toward "
          "the punch is +y; the brushes' tops (the work plane, the sheet's underside) at z = 920")
COMMAND = "BRUSHTABLE"
PARAMS = dict()
LX, LY = 2000.0, 1250.0                           # footprint 2000 (x) x 1250 (y): design choice
RIM = 60.0                                        # the top frame's rim 60 wide, 60 deep: design choice
FR_BOT, FR_TOP = 820.0, 880.0                     # the top frame from z 820 to 880: design choice
LEG = 60.0                                        # legs 60 x 60, under the frame's corners: design choice
ST, ST_Z = 40.0, 150.0                            # stretchers 40 x 40 along x, underside at z 150: design choice
N_STRIP, PITCH = 19, 100.0                        # nineteen strips at a pitch of 100 along x (x -900 to 900): design choice
STRIP_Y = 615.0                                   # strips span y -615 to 615 (10 inside the frame's faces, no flush face): design choice
HOLD_W, HOLD_H = 30.0, 20.0                       # aluminium holder 30 wide, 20 high (z 880 to 900): design choice
BRISTLE_W, BRISTLE_H = 24.0, 20.0                 # nylon bristle block 24 wide, 20 high (z 900 to 920): design choice
BRISTLE_Y = STRIP_Y - 10.0                        # bristles span y -605 to 605, 10 short of the holder's ends (no flush face, GEO-050)
WORK = FR_TOP + HOLD_H + BRISTLE_H                # the work plane z 920

def build():
    P = Prims(); S, A, N = "M-STEEL-7035", "M-ALU-ANOD", "M-BLACK-PA"
    hx, hy = LX / 2, LY / 2
    frame = P.box(S, -hx, -hy, FR_BOT, LX, LY, FR_TOP - FR_BOT)                                  # top frame: one solid
    P.cutbox(S, -hx + RIM, -hy + RIM, FR_BOT - 1, LX - 2 * RIM, LY - 2 * RIM, FR_TOP - FR_BOT + 2, frame)   # cut open
    for sx in (-1, 1):
        for sy in (-1, 1):
            x0 = hx - LEG if sx > 0 else -hx
            y0 = hy - LEG if sy > 0 else -hy
            P.box(S, x0, y0, 0, LEG, LEG, FR_BOT)                                                # legs
    for sy in (-1, 1):
        yc = sy * (hy - LEG / 2)
        P.box(S, -hx + LEG, yc - ST / 2, ST_Z, LX - 2 * LEG, ST, ST)                             # stretchers between the legs
    for i in range(N_STRIP):
        x = (i - (N_STRIP - 1) / 2) * PITCH
        P.box(A, x - HOLD_W / 2, -STRIP_Y, FR_TOP, HOLD_W, 2 * STRIP_Y, HOLD_H)                  # holder
        P.box(N, x - BRISTLE_W / 2, -BRISTLE_Y, FR_TOP + HOLD_H, BRISTLE_W, 2 * BRISTLE_Y, BRISTLE_H)  # bristle block
    P.collider("brushes", -hx, -STRIP_Y, FR_TOP, LX, 2 * STRIP_Y, WORK - FR_TOP)
    P.collider("frame", -hx, -hy, FR_BOT, LX, LY, FR_TOP - FR_BOT)
    for sx in (-1, 1):
        for sy in (-1, 1):
            x0 = hx - LEG if sx > 0 else -hx
            y0 = hy - LEG if sy > 0 else -hy
            P.collider(f"leg-{'r' if sx > 0 else 'l'}{'b' if sy > 0 else 'f'}", x0, y0, 0, LEG, LEG, FR_BOT)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="side", az=270, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
