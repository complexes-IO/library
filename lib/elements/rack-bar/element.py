#!/usr/bin/env python3
"""rack-bar: a bar stock rack, our own design (OPERATING.md 12, own designs; inventory row own_design "yes": "bar stock rack";
lib/machines-factory.txt line 122, storage-steel, lists it beside rack-cantilever and rack-sheet-vertical, so this one is the
vertical kind: bars stand on end). A floor tray with a 100 high rim catches the bars' feet; four corner posts carry a top grid
that divides the rack into ten cells, two rows of five, so each bar leans in its own cell. One fixed body, no node, no hole: the
rack's fixing to the floor or a wall is the assembly's. Every size is a design choice. No load rating, no safety claim. No
vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "rack-bar", "1.1", "furniture"
TITLE = "bar stock rack 1200 x 600 x 1270, floor tray with a 100 rim, top grid of ten cells 192 x 235, bars stood on end"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; every size a design choice; no load rating, "
            "no safety claim; no vendor file opened")
ORIGIN = ("floor plane z = 0 at the centre of the rack's footprint x = 0, y = 0; the front (the side a bar is taken from) "
          "toward -y; the cells' rows run along x")
COMMAND = "BARRACK"
PARAMS = dict()
W, D = 1200.0, 600.0                              # footprint 1200 (x) by 600 (y): design choice
PLATE_T = 10.0                                    # tray floor plate 10 thick (z 0..10): design choice
RIM_T, RIM_H = 10.0, 100.0                        # tray rim 10 thick, 100 high above the floor plate (z 10..110): design choice
POST = 50.0                                       # corner posts 50 x 50, inside the rim's corners: design choice
TOP = 1270.0                                      # posts' and top grid's top, 1270 above the floor: design choice
RAIL_W, RAIL_H = 30.0, 50.0                       # grid rails 30 wide, 50 deep (z 1220..1270): design choice
CELLS_X = 5                                       # five cells along x, two rows (front and back): design choice

def build():
    P = Prims(); S = "M-STEEL-7035"
    x0, y0 = W / 2 - RIM_T, D / 2 - RIM_T                                                   # rim's inner faces: x +-590, y +-290
    tray = P.box(S, -W / 2, -D / 2, 0, W, D, PLATE_T + RIM_H)                               # floor tray: floor plate and rim in
    P.cutbox(S, -x0, -y0, PLATE_T, 2 * x0, 2 * y0, RIM_H + 1, tray)                         # one solid (1.0 first gate: four
                                                                                            # rim boxes left 10 mm free-corner
                                                                                            # edges the fillet gate read at 89 %)
    for sx in (-1, 1):
        for sy in (-1, 1):
            px = (x0 - POST) if sx > 0 else -x0; py = (y0 - POST) if sy > 0 else -y0
            P.box(S, px, py, PLATE_T, POST, POST, TOP - PLATE_T)                            # corner post, inside the rim's corner
    gx = x0 - POST                                                                          # posts' inner faces: x +-540
    z0 = TOP - RAIL_H
    ry = (-y0 + (POST - RAIL_W) / 2, -RAIL_W / 2, y0 - POST + (POST - RAIL_W) / 2)          # front, middle, back rails (y start)
    for y in ry:
        P.box(S, -gx, y, z0, 2 * gx, RAIL_W, RAIL_H)                                        # long rails, post to post
    sy0 = y0 - POST                                                                         # posts' inner faces: y +-240
    for sx in (-1, 1):
        P.box(S, gx if sx > 0 else -gx - RAIL_W, -sy0, z0, RAIL_W, 2 * sy0, RAIL_H)        # side rail, front post to back post;
                                                                                            # the middle rail's ends abut it
    cell = (2 * gx - (CELLS_X - 1) * RAIL_W) / CELLS_X                                      # 192 clear between dividers
    for i in range(1, CELLS_X):
        dx = -gx + i * cell + (i - 1) * RAIL_W                                              # divider's left face
        P.box(S, dx, ry[0] + RAIL_W, z0, RAIL_W, ry[1] - ry[0] - RAIL_W, RAIL_H)           # divider, front row
        P.box(S, dx, ry[1] + RAIL_W, z0, RAIL_W, ry[2] - ry[1] - RAIL_W, RAIL_H)           # divider, back row
    P.collider("floor", -W / 2, -D / 2, 0, W, D, PLATE_T)
    P.collider("rim-front", -W / 2, -D / 2, PLATE_T, W, RIM_T, RIM_H)
    P.collider("rim-back", -W / 2, D / 2 - RIM_T, PLATE_T, W, RIM_T, RIM_H)
    P.collider("rim-left", -W / 2, -y0, PLATE_T, RIM_T, 2 * y0, RIM_H)
    P.collider("rim-right", W / 2 - RIM_T, -y0, PLATE_T, RIM_T, 2 * y0, RIM_H)
    for sx in (-1, 1):
        for sy in (-1, 1):
            px = (x0 - POST) if sx > 0 else -x0; py = (y0 - POST) if sy > 0 else -y0
            P.collider(f"post-{'r' if sx > 0 else 'l'}{'b' if sy > 0 else 'f'}", px, py, PLATE_T, POST, POST, TOP - PLATE_T)
    for k, y in zip(("front", "middle", "back"), ry):
        P.collider(f"rail-{k}", -gx, y, z0, 2 * gx, RAIL_W, RAIL_H)
    P.collider("rail-left", -gx - RAIL_W, -(y0 - POST), z0, RAIL_W, 2 * (y0 - POST), RAIL_H)
    P.collider("rail-right", gx, -(y0 - POST), z0, RAIL_W, 2 * (y0 - POST), RAIL_H)
    for i in range(1, CELLS_X):
        dx = -gx + i * cell + (i - 1) * RAIL_W
        P.collider(f"divider-{i}", dx, ry[0] + RAIL_W, z0, RAIL_W, ry[2] - ry[0] - RAIL_W, RAIL_H)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="top", az=180, el=60)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
