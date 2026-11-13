#!/usr/bin/env python3
"""conveyor-guard: fixed tunnel guard over a belt conveyor section, our own design (OPERATING.md 12, own designs: guards; inventory
row own_design "yes"). An inverted U of 2.0 sheet, 1000 long, open at both ends so the conveyor's load passes through: two side
walls and a roof with a clear inspection window. Each side wall is bent out at its foot into a 40 wide flange that sits on the top
face of the conveyor's side frame and carries three M8 clearance holes, ISO 273 medium (lib/standards/holes.csv). The screws and
the T-slot nuts they take in the conveyor's frame (screw-iso4762, tslot-nut, tslot-40: not built yet) are the assembly's, placed
later; the holes are cut. The bends' radii and the welds are not drawn. Every size is a design choice. The tunnel's length against
the reach of a person, and the gap under the flanges, are the assembly's (ISO 13857 not on file); the element makes no safety
claim of its own."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "conveyor-guard", "1.0", "furniture"
TITLE = "conveyor tunnel guard 1000 long, 560 clear inside, 400 high, sheet 2.0, roof window, 6 x M8 flange holes"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; flange fixing holes M8 in ISO 273 medium; every "
            "size a design choice; no safety claim")
ORIGIN = ("the flanges' underside z = 0 (the face that sits on the conveyor's side frames); x = 0 at the middle of the guard's "
          "length, along the conveyor; y = 0 on the conveyor's centre line")
COMMAND = "CNVGRD"
PARAMS = dict()
L, CLEAR_W, H, T = 1000.0, 560.0, 400.0, 2.0   # length along x, clear width inside the walls, height, sheet 2.0: design choices
FL_W = 40.0                                    # flange out from the wall's outer face: design choice
HOLE_D = 9.0                                   # M8 clearance, ISO 273 medium H13 (lib/standards/holes.csv)
HOLE_X = (-400.0, 0.0, 400.0)                  # three holes a flange, 400 apart: design choice
WIN_X, WIN_Y = 400.0, 180.0                    # roof window cut-out x -400..400, y -180..180 (800 x 360): design choice
PANE_T, PANE_LAP = 6.0, 30.0                   # clear pane 6 thick, under the roof, lapping 30 round the cut-out

def build():
    P = Prims(); Y, C = "M-YELLOW", "M-CASE-CLEAR"
    yi = CLEAR_W / 2                                                   # the walls' inner faces at y +-280
    yo = yi + T                                                        # their outer faces at y +-282
    x0 = -L / 2
    roof = P.box(Y, x0, -yo, H - T, L, 2 * yo, T)                      # roof, across both walls
    P.cutbox(Y, -WIN_X, -WIN_Y, H - T - 1, 2 * WIN_X, 2 * WIN_Y, T + 2, roof)                 # roof window cut-out
    P.box(C, -WIN_X - PANE_LAP, -WIN_Y - PANE_LAP, H - T - PANE_T,
          2 * (WIN_X + PANE_LAP), 2 * (WIN_Y + PANE_LAP), PANE_T)      # clear pane under the roof
    for sy in (-1, 1):
        P.box(Y, x0, yi if sy > 0 else -yo, 0, L, T, H - T)           # side wall, under the roof
        fy = yo if sy > 0 else -yo - FL_W
        fl = P.box(Y, x0, fy, 0, L, FL_W, T)                           # flange, out from the wall's foot
        hy = sy * (yo + FL_W / 2)                                      # hole centres at y +-302
        for hx in HOLE_X:
            P.hole(Y, (hx, hy, -1), (hx, hy, T + 1), HOLE_D / 2, fl)  # M8 fixing hole
    P.collider("roof", x0, -yo, H - T, L, 2 * yo, T)
    for n, sy in (("side-l", -1), ("side-r", 1)):
        P.collider(n, x0, yi if sy > 0 else -yo, 0, L, T, H - T)        # the side walls (the flanges left out)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="along the conveyor", az=270, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
