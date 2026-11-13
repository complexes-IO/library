#!/usr/bin/env python3
"""base-cast: machine base of a drill, our own design (OPERATING.md 12, own designs; inventory row own_design "yes"). The base of
the pillar and radial drills of lib/machines-factory.txt: a box-section body standing on two runners, a machined column seat at
its rear (node `column-seat`, fixed: column 1.1 is placed there) with column 1.1's pattern of eight M12 clearance holes, ISO 273
medium (lib/standards/holes.csv), and a machined work face at its front (node `work-face`, fixed: the work, or a table a BOM puts
there, is placed on it). The bolts pass through the base and take their nuts in the space between the runners: a floating
fastener, as column 1.1 requires of its mate. The body is drawn by its outside: a cast base is cored and ribbed inside, not seen.
No T-slots (ISO 299 is not on file), no floor fixing (the installation's). Every size is a design choice. No load rating, no
accuracy claim."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "base-cast", "1.0", "furniture"
TITLE = "drill base 900 x 1500 x 270, column seat 600 x 600 with 8 x M12 for column 1.1, work face 700 x 700"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; column seat holes M12 in ISO 273 medium, "
            "column 1.1's pattern; every size a design choice; no load rating, no accuracy claim")
ORIGIN = ("the floor plane z = 0 under the column seat's centre x = 0, y = 0; front (the work face) toward -y; the column seat's "
          "top plane (column 1.1's base flange underside) at z = 270")
COMMAND = "BASECST"
PARAMS = dict()
W_X = 900.0                             # base 900 wide (x -450 to 450): design choice
Y0, Y1 = -1100.0, 400.0                 # base 1500 long, 100 behind the column seat and 800 in front of it: design choice
RUN_W, RUN_H = 60.0, 60.0               # two runners 60 wide, 60 high, under the body's long sides: design choice
TOP = 250.0                             # the body's top face 250 above the floor: design choice
PAD_T = 20.0                            # machined pads 20 proud of the body's top: design choice
SEAT = 600.0                            # column seat 600 x 600 = column 1.1's base flange
WORK = 700.0                            # work face 700 x 700: design choice
WORK_Y = -700.0                         # work face centre y = -700 (50 from the body's front, 50 from the seat): design choice
BOLT_D = 13.5                           # M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv), column 1.1's flange holes
BOLT_C = 250.0                          # column 1.1's pattern: a 500 x 500 square, corners and mid-sides

def build():
    P = Prims(); S = "M-STEEL-7035"; M = "M-SILVER"                  # the pads: bare machined steel, the library's bright-metal layer
    for sx in (-1, 1):                                                                          # two runners on the floor
        P.box(S, (W_X / 2 - RUN_W) if sx > 0 else -W_X / 2, Y0, 0, RUN_W, Y1 - Y0, RUN_H)
    body = P.box(S, -W_X / 2, Y0, RUN_H, W_X, Y1 - Y0, TOP - RUN_H)                             # box body
    seat = P.box(f"node:column-seat|{M}", -SEAT / 2, -SEAT / 2, TOP, SEAT, SEAT, PAD_T)         # column seat
    for x in (-BOLT_C, 0.0, BOLT_C):
        for y in (-BOLT_C, 0.0, BOLT_C):
            if x == 0.0 and y == 0.0:
                continue                                                                        # column 1.1 has no hole there
            P.hole(f"node:column-seat|{M}", (x, y, TOP - 1), (x, y, TOP + PAD_T + 1), BOLT_D / 2, seat)   # M12 through the seat
            P.hole(S, (x, y, RUN_H - 1), (x, y, TOP + 1), BOLT_D / 2, body)                     # and on through the body
    P.box(f"node:work-face|{M}", -WORK / 2, WORK_Y - WORK / 2, TOP, WORK, WORK, PAD_T)          # work face
    P.pivot("column-seat", "fixed", (0, 0, TOP + PAD_T), axis=(0, 0, 1))
    P.pivot("work-face", "fixed", (0, WORK_Y, TOP + PAD_T), axis=(0, 0, 1))
    P.collider("base", -W_X / 2, Y0, 0, W_X, Y1 - Y0, TOP)
    P.collider("seat", -SEAT / 2, -SEAT / 2, TOP, SEAT, SEAT, PAD_T)
    P.collider("table", -WORK / 2, WORK_Y - WORK / 2, TOP, WORK, WORK, PAD_T)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="front", az=270, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
