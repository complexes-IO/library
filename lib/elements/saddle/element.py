#!/usr/bin/env python3
"""saddle: the saddle of a bed-type vertical mill, between the bed and the table, our own design (OPERATING.md 12, own designs;
inventory row own_design "yes": "mill saddle between bed and table"). Two way shoes sit on bed-cast's two flat ways and carry a
box body; on the body's top face two flat machined ways run across the bed (along y) for the table (node `ways`, fixed: the
table a BOM puts on the saddle is placed on the ways' top plane). The saddle slides along the bed (x); that travel is the
machine's, between the elements, so the saddle has no moving node of its own. The shoes' spacing and width are read from
bed-cast itself (library.load), so the two cannot drift apart. The body is drawn by its outside. Gibs, way wipers, the feed
nut's bracket, the clamp and the oil lines are not drawn. Every other size is a design choice. No load rating, no accuracy
claim. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "saddle", "1.1", "furniture"
TITLE = "mill saddle 600 x 700 x 270, two shoes on bed-cast's ways, two flat cross ways 80 wide for the table"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; the shoes on bed-cast 1.0's ways, every other "
            "size a design choice; no load rating, no accuracy claim; no vendor file opened")
ORIGIN = ("bed-cast's ways' top plane z = 0 (the saddle's seat) at the saddle's centre x = 0, y = 0; it slides along x, the "
          "bed's length; front toward -y; the cross ways' top plane (the table's seat) at z = 270")
COMMAND = "SADDLE"
PARAMS = dict()
BED = library.load("bed-cast")                    # bed-cast 1.0: the ways it sits on (one home for the figure)
SHOE_Y, SHOE_W = BED.WAY_Y, BED.WAY_W             # shoe centres at y +-170, each as wide as the bed's way, 80
SL = 600.0                                        # saddle length along the bed (x -300..300): design choice
SW = 700.0                                        # saddle width across the bed (y -350..350): design choice
SHOE_H = 40.0                                     # way shoes 40 high (z 0..40): design choice
BODY_TOP = 240.0                                  # box body z 40..240: design choice
WAY_W, WAY_H = 80.0, 30.0                         # cross ways 80 wide, 30 proud (z 240..270), as bed-cast's: design choice
WAY_X = 200.0                                     # cross way centres at x +-200 (400 apart): design choice
WAY_END = 20.0                                    # the cross ways stop 20 short of each side of the body: design choice

def build():
    P = Prims(); S = "M-STEEL-7035"; W = "M-SILVER"                   # the ways: bare machined steel, the library's bright-metal layer
    for sy in (-1, 1):
        P.box(S, -SL / 2, sy * SHOE_Y - SHOE_W / 2, 0, SL, SHOE_W, SHOE_H)                        # way shoe, on bed-cast's way
    P.box(S, -SL / 2, -SW / 2, SHOE_H, SL, SW, BODY_TOP - SHOE_H)                                 # box body
    wl = SW - 2 * WAY_END
    for sx in (-1, 1):                                                                            # the two cross ways
        P.box(f"node:ways|{W}", sx * WAY_X - WAY_W / 2, -wl / 2, BODY_TOP, WAY_W, wl, WAY_H)
    P.pivot("ways", "fixed", (0, 0, BODY_TOP + WAY_H), axis=(0, 0, 1))
    P.collider("saddle", -SL / 2, -SW / 2, 0, SL, SW, BODY_TOP)
    P.collider("cross-ways", -WAY_X - WAY_W / 2, -wl / 2, BODY_TOP, 2 * WAY_X + WAY_W, wl, WAY_H)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="end", az=270, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
