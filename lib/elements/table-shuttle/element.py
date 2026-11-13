#!/usr/bin/env python3
"""table-shuttle: the shuttle (pallet-change) table of a sheet laser cutter, our own design (OPERATING.md 12, own designs;
inventory row own_design "yes": "shuttle (pallet-change) table for a sheet laser"; lib/machines-factory.txt, laser-cutter-sheet,
places frame-welded, bed-slat, gantry-beam and table-shuttle). A fixed runway (two girders on eight legs, tied at both ends, each
girder carrying a bright steel rail) and one pallet (node `pallet`) that runs on the rails along +x, from the cutting position
(x = 0, under the gantry) out to the load station beside it and back. The pallet is one frame, cut open in the middle so the slag
falls through, sized to bed-slat itself (library.load), so the two cannot drift apart: bed-slat's frame stands on the pallet's
top. The pallet's drive (chain, rack or screw), its lift and locating pins, end stops, wheels and the second (upper) pallet of
a two-level changer are not drawn; the drive belongs to the machine, between the elements. Every size is a design choice. No
load rating, no speed or change-time claim. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "table-shuttle", "1.0", "furniture"
TITLE = "shuttle table, runway 6500 x 1700 on eight legs, one pallet 3200 x 1700 carrying bed-slat 1.1, 3300 of travel"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; no hole, thread or standard interface; the "
            "pallet sized to bed-slat (library.load); every other size a design choice; no load, speed or change-time claim; "
            "no vendor file opened")
ORIGIN = ("the floor plane z = 0 at the centre of the cutting position x = 0, y = 0 (the pallet's centre at rest); the runway "
          "along +x toward the load station; the pallet's top (bed-slat's seat) at z = 700")
COMMAND = "SHUTTLETABLE"
PARAMS = dict()
BS = library.load("bed-slat")                     # bed-slat 1.1: the bed the pallet carries (one home for the figure)
BED_X = BS.IN_X / 2 + BS.RAIL_T                   # the bed's outer half-length 1550 (x)
BED_Y = BS.IN_Y / 2 + BS.RAIL_T                   # the bed's outer half-width 800 (y)
PX, PY = BED_X + 50.0, BED_Y + 50.0               # the pallet's outer half-sizes 1600, 850 (50 round the bed): design choice
OPEN_X, OPEN_Y = BED_X - 100.0, BED_Y - 100.0     # the pallet's opening half-sizes 1450, 700 (the bed's rails bear on the rim)
RAIL_TOP = 600.0                                  # the rails' top, the pallet's underside, at z 600: design choice
PAL_TOP = 700.0                                   # the pallet frame 100 deep (z 600 to 700): design choice
TRAVEL = 2 * PX + 100.0                           # 3300 along +x: the pallet's length and 100 clear: design choice
RUN_X0, RUN_X1 = -PX, PX + TRAVEL                 # the runway from x -1600 to 4900
RAIL_Y, RAIL_W, RAIL_H = 775.0, 60.0, 40.0        # rails 60 x 40 at y +-775 (under the pallet's rim), z 560 to 600: design choice
RAIL_END = 20.0                                   # rails stop 20 inside the girders' ends (no flush face across materials, GEO-050)
GIRDER_W, GIRDER_H = 100.0, 200.0                 # girders 100 x 200 under the rails, z 360 to 560: design choice
GIRDER_BOT = RAIL_TOP - RAIL_H - GIRDER_H         # 360
LEG = 100.0                                       # legs 100 x 100 under the girders, z 0 to 360: design choice
LEGS_X = (-1550.0, 600.0, 2750.0, 4850.0)         # leg centres along each girder (spans 2150, 2150, 2100): design choice
TIE_L = GIRDER_W                                  # end ties 100 along x, between the girders, as deep as them: design choice

def build():
    P = Prims(); S = "M-STEEL-7035"; R = "M-SILVER"                   # rails: bare steel, the library's bright-metal layer
    L = RUN_X1 - RUN_X0
    for sy in (-1, 1):
        yg = sy * RAIL_Y - GIRDER_W / 2
        P.box(S, RUN_X0, yg, GIRDER_BOT, L, GIRDER_W, GIRDER_H)                                    # girder
        P.box(R, RUN_X0 + RAIL_END, sy * RAIL_Y - RAIL_W / 2, GIRDER_BOT + GIRDER_H,
              L - 2 * RAIL_END, RAIL_W, RAIL_H)                                                     # rail on the girder
        for x in LEGS_X:
            P.box(S, x - LEG / 2, yg, 0, LEG, GIRDER_W, GIRDER_BOT)                                 # legs under the girder
    yi = RAIL_Y - GIRDER_W / 2                                                                      # the girders' inner faces, y +-725
    for x0 in (RUN_X0, RUN_X1 - TIE_L):
        P.box(S, x0, -yi, GIRDER_BOT, TIE_L, 2 * yi, GIRDER_H)                                      # end ties between the girders
    N = f"node:pallet|{S}"
    pal = P.box(N, -PX, -PY, RAIL_TOP, 2 * PX, 2 * PY, PAL_TOP - RAIL_TOP)                          # pallet frame: one solid
    P.cutbox(N, -OPEN_X, -OPEN_Y, RAIL_TOP - 1, 2 * OPEN_X, 2 * OPEN_Y, PAL_TOP - RAIL_TOP + 2, pal)  # cut open
    P.pivot("pallet", "translate", (0, 0, PAL_TOP), axis=(1, 0, 0), range=(0, TRAVEL))
    P.collider("pallet-frame", -PX, -PY, RAIL_TOP, 2 * PX, 2 * PY, PAL_TOP - RAIL_TOP)
    for n, sy in (("runway-a", -1), ("runway-b", 1)):
        P.collider(n, RUN_X0, sy * RAIL_Y - GIRDER_W / 2, GIRDER_BOT, L, GIRDER_W, RAIL_TOP - GIRDER_BOT)
    for n, x0 in (("tie-a", RUN_X0), ("tie-b", RUN_X1 - TIE_L)):
        P.collider(n, x0, -yi, GIRDER_BOT, TIE_L, 2 * yi, GIRDER_H)
    for sy, s in ((-1, "a"), (1, "b")):
        for i, x in enumerate(LEGS_X):
            P.collider(f"leg-{s}{i + 1}", x - LEG / 2, sy * RAIL_Y - GIRDER_W / 2, 0, LEG, GIRDER_W, GIRDER_BOT)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="side", az=270, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
