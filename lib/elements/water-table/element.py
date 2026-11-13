#!/usr/bin/env python3
"""water-table: the water table under a CNC plasma cutter's slat bed, our own design (OPERATING.md 12, own designs; inventory
row own_design "yes": "water table under a plasma bed"; lib/machines-factory.txt line 13, plasma-cutter-cnc, places frame-welded,
bed-slat and water-table). An open steel tank, one solid: a floor plate and four walls 20 thick, open at the top. bed-slat drops
into it and sits on two seat ledges welded along the long walls, so the slats' top stands above the tank's rim and the water
under the sheet catches the cut's sparks, dross and fume. The tank's inside is read from bed-slat itself (library.load), so the
two cannot drift apart. One fixed body, no node, no hole: no drain, fill or water-level fitting is drawn (no pipe thread is on
file), and the tank's fixing is the assembly's. Every size is a design choice. No load rating, no capacity, no claim about the
cutting process. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "water-table", "1.0", "furniture"
TITLE = "water table 3190 x 1690 x 550, open tank 20 thick, two seat ledges carrying bed-slat 1.1 with its underside at 400"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; no hole, thread or standard interface; the "
            "inside sized to bed-slat (library.load); every other size a design choice; no load, capacity or process claim; no "
            "vendor file opened")
ORIGIN = ("the floor plane z = 0 at the centre of the tank's footprint x = 0, y = 0; the tank's length along x, as bed-slat's; "
          "bed-slat's origin (its frame's underside) sits at x = 0, y = 0, z = 400")
COMMAND = "WATERTABLE"
PARAMS = dict()
BS = library.load("bed-slat")                     # bed-slat 1.1: the bed it carries (one home for the figure)
BED_X = BS.IN_X / 2 + BS.RAIL_T                   # the bed's outer half-length 1550 (x)
BED_Y = BS.IN_Y / 2 + BS.RAIL_T                   # the bed's outer half-width 800 (y)
BED_H = BS.LEDGE_TOP + BS.SLAT_H                  # the bed's height 200, frame underside to the slats' top
CLEAR = 25.0                                      # 25 clear round the bed inside the tank (drop-in fit): design choice
WALL, FLOOR = 20.0, 20.0                          # walls and floor plate 20 thick: design choice (not 10: rack-bar 1.0's fillet trap)
IX, IY = BED_X + CLEAR, BED_Y + CLEAR             # the tank's inside half-sizes 1575, 825
OX, OY = IX + WALL, IY + WALL                     # the tank's outside half-sizes 1595, 845
SEAT = 400.0                                      # the bed's underside (the ledges' top) 400 above the floor: design choice
TOP = 550.0                                       # the tank's rim 550 above the floor, 50 below the slats' top (600): design choice
LEDGE_W, LEDGE_T = 100.0, 20.0                    # seat ledges 100 wide, 20 thick, the inside's full length: design choice

def build():
    P = Prims(); S = "M-STEEL-7035"
    tank = P.box(S, -OX, -OY, 0, 2 * OX, 2 * OY, TOP)                                       # the tank: floor plate and walls
    P.cutbox(S, -IX, -IY, FLOOR, 2 * IX, 2 * IY, TOP - FLOOR + 1, tank)                     # in one solid (rack-bar 1.0's lesson)
    for sy in (-1, 1):                                                                      # seat ledges on the long walls' inside
        P.box(S, -IX, IY - LEDGE_W if sy > 0 else -IY, SEAT - LEDGE_T, 2 * IX, LEDGE_W, LEDGE_T)
    P.collider("floor", -OX, -OY, 0, 2 * OX, 2 * OY, FLOOR)
    P.collider("wall-front", -OX, -OY, FLOOR, 2 * OX, WALL, TOP - FLOOR)
    P.collider("wall-back", -OX, IY, FLOOR, 2 * OX, WALL, TOP - FLOOR)
    P.collider("wall-left", -OX, -IY, FLOOR, WALL, 2 * IY, TOP - FLOOR)
    P.collider("wall-right", IX, -IY, FLOOR, WALL, 2 * IY, TOP - FLOOR)
    P.collider("ledge-front", -IX, -IY, SEAT - LEDGE_T, 2 * IX, LEDGE_W, LEDGE_T)
    P.collider("ledge-back", -IX, IY - LEDGE_W, SEAT - LEDGE_T, 2 * IX, LEDGE_W, LEDGE_T)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="end", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
