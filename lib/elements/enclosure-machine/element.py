#!/usr/bin/env python3
"""enclosure-machine: sheet-metal machine enclosure, our own design (OPERATING.md 12, own designs: guards, cabinets; inventory row
own_design "yes"). A box of 2.0 sheet 2400 wide, 2000 deep and 2200 high, open at the bottom, that stands on the floor round a
machine tool. The front wall has a loading opening 1100 x 1500 closed by two sliding doors (nodes door-l and door-r, translate
along x, 0 to 580 outward), each with a clear window; each side wall has a fixed clear window. The doors hang under a top rail
and run over a bottom rail, both on the front wall. Four corner feet inside carry one M10 floor-anchor hole each, ISO 273 medium
(lib/standards/holes.csv). Rollers, door seals, the interlock, panel stiffeners, lights, chip and coolant parts are not drawn.
Every size is a design choice. Where the enclosure stands relative to the hazard, and any guard-locking device, are the
assembly's; the element makes no safety claim of its own."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "enclosure-machine", "1.0", "furniture"
TITLE = "machine enclosure 2400 x 2000 x 2200, sheet 2.0, two sliding front doors with windows, two side windows, 4 x M10 feet"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; floor-anchor holes M10 in ISO 273 medium; every "
            "size a design choice; no safety claim")
ORIGIN = ("the floor z = 0 (the enclosure's underside) at the centre of its width x = 0; y = 0 the front wall's outer face; the "
          "depth toward +y; the doors and their rails in front of it, toward -y")
COMMAND = "MENCL"
PARAMS = dict()
W, D, H, T = 2400.0, 2000.0, 2200.0, 2.0       # outside of the walls and roof; sheet 2.0 everywhere: design choices
OPEN_X, OPEN_Z = 550.0, (400.0, 1900.0)        # front opening x -550..550, z 400..1900 (1100 x 1500): design choice
DOOR_W, DOOR_T, DOOR_Y = 599.0, 30.0, 10.0     # each door 599 wide (1 from the centre to 600), 30 thick, 10 in front of the wall
DOOR_Z = (340.0, 1960.0)                       # doors 60 over the opening above and below: design choice
TRAVEL = 580.0                                 # each door slides 0 to 580 outward: the opening then fully clear (edge at x -+581)
RAIL_D, RAIL_GAP = 45.0, 5.0                   # rails 45 deep from the wall, 5 clear of the door's top and bottom edges
RAIL_H, RAIL_X = 40.0, 1190.0                  # rails 40 high, x -1190..1190 (10 short of the side walls' faces)
WIN_IN = 60.0                                  # door windows: 60 frame each side, from z 900 to 1850
WIN_Z = (900.0, 1850.0)
PANE_T = 6.0                                   # clear panes 6 thick (door panes centred in the door, side panes inside the wall)
SIDE_WIN = ((700.0, 1300.0), (1000.0, 1700.0)) # side window cut-outs y 700..1300, z 1000..1700: design choice
SIDE_LAP = 30.0                                # side panes lap 30 over the cut-out on the wall's inside face
HANDLE_L, HANDLE_IN, HANDLE_Z = 300.0, 25.0, 1100.0   # vertical bar handle, its inner face 25 from the door's meeting edge
FOOT, FOOT_T = 80.0, 6.0                       # corner feet 80 x 80 x 6 inside the walls: design choice
ANCHOR_D = 11.0                                # M10 clearance, ISO 273 medium H13 (lib/standards/holes.csv)

def build():
    P = Prims(); S, B, Z, C, R = "M-STEEL-7035", "M-BLUE", "M-ZINC", "M-CASE-CLEAR", "M-SILVER"
    x0 = W / 2                                                                          # the side walls' outer faces at x +-1200
    P.box(S, -x0, 0, H - T, W, D, T)                                                    # roof
    for sx in (-1, 1):                                                                  # side walls, full depth, under the roof
        side = P.box(S, x0 - T if sx > 0 else -x0, 0, 0, T, D, H - T)
        (y0, y1), (z0, z1) = SIDE_WIN
        P.cutbox(S, (x0 - T if sx > 0 else -x0) - 1, y0, z0, T + 2, y1 - y0, z1 - z0, side)            # side window cut-out
        px = x0 - T - PANE_T if sx > 0 else -x0 + T
        P.box(C, px, y0 - SIDE_LAP, z0 - SIDE_LAP, PANE_T, y1 - y0 + 2 * SIDE_LAP, z1 - z0 + 2 * SIDE_LAP)   # side pane, inside
    P.box(S, -x0 + T, D - T, 0, W - 2 * T, T, H - T)                                    # back wall, between the sides
    front = P.box(S, -x0 + T, 0, 0, W - 2 * T, T, H - T)                                # front wall, between the sides
    P.cutbox(S, -OPEN_X, -1, OPEN_Z[0], 2 * OPEN_X, T + 2, OPEN_Z[1] - OPEN_Z[0], front)              # loading opening
    yr = -RAIL_D
    P.box(R, -RAIL_X, yr, DOOR_Z[1] + RAIL_GAP, 2 * RAIL_X, RAIL_D, RAIL_H)             # top rail (the doors hang under it)
    P.box(R, -RAIL_X, yr, DOOR_Z[0] - RAIL_GAP - RAIL_H, 2 * RAIL_X, RAIL_D, RAIL_H)    # bottom rail (the doors' guide)
    for fx in (-x0 + T, x0 - T - FOOT):                                                 # corner feet, inside, on the floor
        for fy in (T, D - T - FOOT):
            foot = P.box(S, fx, fy, 0, FOOT, FOOT, FOOT_T)
            cx, cy = fx + FOOT / 2, fy + FOOT / 2
            P.hole(S, (cx, cy, -1), (cx, cy, FOOT_T + 1), ANCHOR_D / 2, foot)           # M10 floor anchor
    yd0, yd1 = -DOOR_Y - DOOR_T, -DOOR_Y                                                # the doors' front and back faces
    for n, xa, xb, hx, ax in (("door-l", -1.0 - DOOR_W, -1.0, -1.0 - HANDLE_IN - 12.0, -1),
                              ("door-r", 1.0, 1.0 + DOOR_W, 1.0 + HANDLE_IN, 1)):
        Ln = lambda m, n=n: f"node:{n}|{m}"
        door = P.box(Ln(B), xa, yd0, DOOR_Z[0], xb - xa, DOOR_T, DOOR_Z[1] - DOOR_Z[0])  # door, double wall drawn by its outside
        wa, wb = xa + WIN_IN, xb - WIN_IN
        P.cutbox(Ln(B), wa, yd0 - 1, WIN_Z[0], wb - wa, DOOR_T + 2, WIN_Z[1] - WIN_Z[0], door)          # door window cut-out
        P.box(Ln(C), wa, -DOOR_Y - DOOR_T / 2 - PANE_T / 2, WIN_Z[0], wb - wa, PANE_T, WIN_Z[1] - WIN_Z[0])   # its pane
        for z in (HANDLE_Z - HANDLE_L / 2, HANDLE_Z + HANDLE_L / 2 - 12.0):
            P.box(Ln(Z), hx, yd0 - 15.0, z, 12.0, 15.0, 12.0)                           # handle standoffs
        P.box(Ln(Z), hx, yd0 - 27.0, HANDLE_Z - HANDLE_L / 2, 12.0, 12.0, HANDLE_L)     # handle bar, vertical
        P.pivot(n, "translate", ((xa + xb) / 2, yd1, (DOOR_Z[0] + DOOR_Z[1]) / 2), axis=(ax, 0, 0), range=(0, TRAVEL))
        P.collider(n, xa, yd0 - 27.0, DOOR_Z[0], xb - xa, DOOR_T + 27.0, DOOR_Z[1] - DOOR_Z[0])
    P.collider("roof", -x0, 0, H - T, W, D, T)
    P.collider("back", -x0, D - T, 0, W, T, H - T)
    for n, x in (("side-l", -x0), ("side-r", x0 - T)): P.collider(n, x, 0, 0, T, D, H - T)
    for n, xa, xb, za, zb in (("front-l", -x0, -OPEN_X, 0, H - T), ("front-r", OPEN_X, x0, 0, H - T),
                              ("front-top", -OPEN_X, OPEN_X, OPEN_Z[1], H - T), ("front-sill", -OPEN_X, OPEN_X, 0, OPEN_Z[0])):
        P.collider(n, xa, 0, za, xb - xa, T, zb - za)                                   # the front wall round its opening
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="rear, side window", az=40, el=15)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
