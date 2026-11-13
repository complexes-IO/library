#!/usr/bin/env python3
"""door-oven: the insulated double door of oven-cure, our own design (OPERATING.md 12, own designs; inventory row own_design
"yes": "insulated oven door"). A fixed door frame (two jambs and a head, 100 wide, 50 deep) stands on the floor round oven-cure's
door opening, on the oven's front face; two leaves of 100 thick insulated panel (as the oven's walls, drawn by their outside) hang
in front of it, nodes `door-l` and `door-r`, each rotating about its outer back vertical edge, 0 to 110 degrees outward. Each leaf
laps the opening by 100 at its side and at the head; 10 between the leaves where they meet, 10 above the floor. A bar handle on
each leaf. The opening's figures are read from oven-cure itself (library.load), so the two cannot drift apart. The hinges, the
latch, the seal and the frame's fixing to the oven are not drawn (later versions). Every other size is a design choice. No
temperature, thermal, seal or safety claim (no oven standard on file); no interlock (the system's guard-interlock). No vendor file
was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "door-oven", "1.0", "furniture"
TITLE = "oven door, double, insulated leaves 100, for oven-cure's opening 1800 x 2100, frame 2000 x 2200"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; the opening from oven-cure 1.0, every other size a "
            "design choice; hinges, latch, seal and fixing not drawn; no temperature, thermal, seal or safety claim; no vendor file opened")
ORIGIN = ("oven-cure's origin: the floor z = 0 under the middle of the door opening, y = 0 the oven's front face; the door stands "
          "on that face toward -y, the oven toward +y")
COMMAND = "OVENDOOR"
PARAMS = dict()
OV = library.load("oven-cure")                    # oven-cure 1.0: the opening it meets (one home for the figure)
OPEN_X, OPEN_H, PANEL = OV.DOOR_X, OV.DOOR_H, OV.T   # opening x -900..900, z 0..2100; the oven's insulated panel 100
FW, FD = 100.0, 50.0                              # frame bars 100 wide, 50 deep (y -50..0): design choice
XO, ZT = OPEN_X + FW, OPEN_H + FW                 # frame outside x +-1000, top z 2200
GAP, FLOOR = 10.0, 10.0                           # 10 between the leaves, leaves 10 above the floor: design choice
SWING = 110.0                                     # each leaf opens 0 to 110 degrees outward: design choice (spec.md, Mechanism)
HANDLE_L, HANDLE_Z, HANDLE_IN = 400.0, 1100.0, 60.0   # bar handle 400 long, centred at z 1100, 60 in from the free edge
BAR, STAND = 20.0, 40.0                           # handle bar 20 x 20 on two 20 x 40 x 20 standoffs: design choice

def build():
    P = Prims(); S, Z = "M-STEEL-7035", "M-ZINC"
    for sx in (-1, 1):
        P.box(S, OPEN_X if sx > 0 else -XO, -FD, 0, FW, FD, ZT)                  # jamb, on the floor
    P.box(S, -OPEN_X, -FD, OPEN_H, 2 * OPEN_X, FD, FW)                           # head, between the jambs
    P.collider("jamb-l", -XO, -FD, 0, FW, FD, ZT)
    P.collider("jamb-r", OPEN_X, -FD, 0, FW, FD, ZT)
    P.collider("head", -OPEN_X, -FD, OPEN_H, 2 * OPEN_X, FD, FW)
    y0 = -FD - PANEL                                                             # leaves' front face y -150
    for n, c, sx in (("door-l", "leaf-l", -1), ("door-r", "leaf-r", 1)):
        L = lambda m, n=n: f"node:{n}|{m}"
        x0, x1 = (-XO, -GAP / 2) if sx < 0 else (GAP / 2, XO)
        P.box(L(S), x0, y0, FLOOR, x1 - x0, PANEL, ZT - FLOOR)                   # leaf, in front of the frame
        hx = (x1 - HANDLE_IN - BAR) if sx < 0 else (x0 + HANDLE_IN)              # handle near the free edge
        z0 = HANDLE_Z - HANDLE_L / 2
        for z in (z0, z0 + HANDLE_L - BAR):
            P.box(L(Z), hx, y0 - STAND, z, BAR, STAND, BAR)                      # handle standoffs
        P.box(L(Z), hx, y0 - STAND - BAR, z0, BAR, BAR, HANDLE_L)                # handle bar, vertical
        P.pivot(n, "rotate", (sx * XO, -FD, ZT / 2), axis=(0, 0, 1), range=(0.0, sx * SWING))   # about the leaf's outer back edge
        P.collider(c, x0, y0 - STAND - BAR, FLOOR, x1 - x0, PANEL + STAND + BAR, ZT - FLOOR)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=20), dict(name="back", az=50, el=20)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
