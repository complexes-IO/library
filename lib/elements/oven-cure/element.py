#!/usr/bin/env python3
"""oven-cure: batch powder cure oven body of insulated panels, our own design (OPERATING.md 12, own designs; inventory row
own_design "yes": "powder cure oven (insulated panels)"). Two side walls, a back wall, a front wall and a roof of 100 thick
insulated panels stand on the floor (drawn by their outside: the skins and the insulation are not drawn apart). The front wall
has the door opening at floor level, so a cart rolls in; the door is the inventory's door-oven, a later element, placed over the
opening in a later version (OPERATING.md 12: model the opening, place the part later). On the roof at the back stands the
circulation housing, a hollow box of 50 thick panels over two openings in the roof (return and supply): the circulation fan,
its motor and the heaters (the inventory's fan-circulation, motor-iec and heater-oven) are the system's and go in it later;
none is drawn. On the roof at the front, an exhaust collar Ø150. Every size is a design choice. The cure temperature, the
insulation's value, the heat input, the exhaust rate and every fire, explosion and safety figure of an oven are the system's
and its standards' (none on file): the element makes no temperature, thermal, airflow or safety claim. No vendor file was
opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "oven-cure", "1.1", "furniture"
TITLE = ("powder cure oven, batch, outside 2400 x 3200 x 2400, insulated panels 100, door opening 1800 x 2100, roof circulation "
         "housing, exhaust Ø150")
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; every size a design choice; door, fan, motor and "
            "heaters not drawn; no temperature, thermal, airflow or safety claim; no vendor file opened")
ORIGIN = ("the floor z = 0 under the middle of the door opening's front plane: x = 0 across the oven's width, y = 0 the front "
          "wall's outer face, the oven toward +y")
COMMAND = "CUREOVEN"
PARAMS = dict()
W, D, H, T = 2400.0, 3200.0, 2400.0, 100.0        # outside width (x), depth (y), height; insulated panel 100 thick: design choices
DOOR_X, DOOR_H = 900.0, 2100.0                    # door opening x -900..900, z 0..2100 (1800 x 2100), at floor level: design choice
HX, HY, HZ, HT = 700.0, (1900.0, 3100.0), 600.0, 50.0   # circulation housing x -700..700, y 1900..3100, 600 high, panels 50: design choice
PORT_X, PORT_Y = (100.0, 500.0), (2100.0, 2900.0)  # roof openings under the housing: return x -500..-100, supply x 100..500, 400 x 800: design choice
STACK_D, STACK_Y, STACK_H, COLLAR_T = 150.0, 600.0, 200.0, 2.0   # exhaust collar: bore Ø150 at y 600, 200 high, wall 2.0: design choice

def build():
    P = Prims(); S, G = "M-STEEL-7035", "M-GALV"
    xi = W / 2 - T                                                         # side walls' inner faces at x +-1100
    zr = H - T                                                             # roof's underside z 2300
    roof = P.box(S, -W / 2, 0, zr, W, D, T)                                # roof, across the side walls
    for sx in (-1, 1):
        P.box(S, xi if sx > 0 else -W / 2, 0, 0, T, D, zr)                 # side wall, under the roof
    P.box(S, -xi, D - T, 0, 2 * xi, T, zr)                                 # back wall, between the side walls
    front = P.box(S, -xi, 0, 0, 2 * xi, T, zr)                             # front wall, between the side walls
    P.cutbox(S, -DOOR_X, -1, -1, 2 * DOOR_X, T + 2, DOOR_H + 1, front)     # door opening, from the floor
    # the circulation housing on the roof: a top and four sides of 50 thick panels; the roof is its floor
    y0, y1 = HY
    z0, z1 = H, H + HZ                                                     # housing z 2400..3000
    P.box(S, -HX, y0, z1 - HT, 2 * HX, y1 - y0, HT)                        # housing top
    for sx in (-1, 1):
        P.box(S, HX - HT if sx > 0 else -HX, y0, z0, HT, y1 - y0, HZ - HT)  # housing side
    for yy in (y0, y1 - HT):
        P.box(S, -HX + HT, yy, z0, 2 * (HX - HT), HT, HZ - HT)             # housing front and back, between the sides
    for sx in (-1, 1):
        xa, xb = (PORT_X[0], PORT_X[1]) if sx > 0 else (-PORT_X[1], -PORT_X[0])
        P.cutbox(S, xa, PORT_Y[0], zr - 1, xb - xa, PORT_Y[1] - PORT_Y[0], T + 2, roof)   # return (x-) and supply (x+) openings
    # the exhaust collar on the roof
    P.hole(S, (0, STACK_Y, zr - 1), (0, STACK_Y, H + 1), STACK_D / 2, roof)               # exhaust opening in the roof
    collar = P.cyl(G, (0, STACK_Y, H), (0, STACK_Y, H + STACK_H), STACK_D / 2 + COLLAR_T)  # exhaust collar
    P.hole(G, (0, STACK_Y, H - 1), (0, STACK_Y, H + STACK_H + 1), STACK_D / 2, collar)    # its bore
    P.collider("roof", -W / 2, 0, zr, W, D, T)
    for n, sx in (("wall-l", -1), ("wall-r", 1)):
        P.collider(n, xi if sx > 0 else -W / 2, 0, 0, T, D, zr)
    P.collider("wall-back", -xi, D - T, 0, 2 * xi, T, zr)
    P.collider("jamb-l", -xi, 0, 0, xi - DOOR_X, T, zr)
    P.collider("jamb-r", DOOR_X, 0, 0, xi - DOOR_X, T, zr)
    P.collider("lintel", -DOOR_X, 0, DOOR_H, 2 * DOOR_X, T, zr - DOOR_H)
    P.collider("housing", -HX, y0, z0, 2 * HX, y1 - y0, HZ)
    r = STACK_D / 2 + COLLAR_T
    P.collider("stack", -r, STACK_Y - r, H, 2 * r, 2 * r, STACK_H)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="back", az=60, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
