#!/usr/bin/env python3
"""cabinet-blast: sandblast cabinet with a viewing window and two glove-port openings, our own design (OPERATING.md 12, own
designs: cabinets; inventory row own_design "yes": "sandblast cabinet with viewing window and glove ports"). A work chamber of
2.0 sheet 1000 wide, 800 deep and 800 high standing on four legs 50 x 50, its floor open at z 850 over the abrasive hopper
(hopper-abrasive, our own design, not built yet: it is a separate element of the sandblaster, lib/machines-factory.txt line 106).
The front wall has a viewing window with a clear pane inside it and, below it, two round glove-port openings; the glove ports
themselves (glove-port, a new element, not built yet) are placed in them later. The right side wall has a loading opening closed
by a side door (node `door`, rotate about its back vertical edge, 0 to 90 degrees outward). The roof has a round extraction
opening for the dust collector's duct (dust-collector, duct-round: not built yet). The grate, the lamp, the blast gun and nozzle,
the footswitch, seals, the latch and the hinges are not drawn. Every size is a design choice. No pressure, abrasive, dust or
safety claim. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "cabinet-blast", "1.0", "furniture"
TITLE = "sandblast cabinet 1000 x 800 x 800 chamber on legs, sheet 2.0, viewing window, 2 x Ø180 glove-port openings, side door"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; every size a design choice; glove ports, hopper, "
            "lamp, gun and dust collector separate elements, not drawn; no pressure, dust or safety claim; no vendor file opened")
ORIGIN = ("the floor z = 0 (the legs' underside) at the middle of the cabinet's width x = 0; y = 0 the front wall's outer face "
          "(the operator stands toward -y); the depth toward +y")
COMMAND = "BLASTCAB"
PARAMS = dict()
W, D, T = 1000.0, 800.0, 2.0                   # chamber outside width (x) and depth (y), sheet 2.0 everywhere: design choices
Z0, Z1 = 850.0, 1650.0                         # chamber from its open floor at z 850 to the roof's top at 1650 (800 high)
LEG = 50.0                                     # four legs 50 x 50 under the chamber's corners, 850 long: design choice
SPLIT_Z = 1300.0                               # the front wall in two panels: the glove-port panel below z 1300, the window panel above
WIN_X, WIN_Z = 350.0, (1350.0, 1600.0)         # viewing window cut-out x -350..350, z 1350..1600 (700 x 250): design choice
PANE_T, PANE_LAP = 6.0, 30.0                   # clear pane 6 thick inside the front wall, lapping 30 round the cut-out
PORT_D, PORT_X, PORT_Z = 180.0, 250.0, 1100.0  # two glove-port openings Ø180 at x -+250, z 1100 (500 apart): design choice
DOOR_Y, DOOR_Z = (150.0, 650.0), (950.0, 1550.0)   # loading opening in the right wall, y 150..650, z 950..1550 (500 x 600)
DOOR_LAP, DOOR_T, DOOR_GAP = 30.0, 20.0, 2.0   # the door 30 over the opening each side, 20 thick, 2 clear of the wall
SWING = 90.0                                   # the door opens 0 to 90 degrees outward about its back vertical edge
HANDLE_L, HANDLE_IN = 200.0, 40.0              # vertical bar handle (hardware-cabinet's section), 40 from the door's front edge
OUTLET_D, OUTLET_XY = 150.0, (300.0, 600.0)    # roof extraction opening Ø150 at x 300, y 600: design choice

def build():
    P = Prims(); S, B, Z, C = "M-STEEL-7035", "M-BLUE", "M-ZINC", "M-CASE-CLEAR"
    x0 = W / 2                                                                          # the side walls' outer faces at x -+500
    for lx in (-x0, x0 - LEG):                                                          # legs under the chamber's corners
        for ly in (0.0, D - LEG):
            P.box(S, lx, ly, 0, LEG, LEG, Z0)
    roof = P.box(S, -x0, 0, Z1 - T, W, D, T)                                            # roof, over the walls
    ox, oy = OUTLET_XY
    P.hole(S, (ox, oy, Z1 - T - 1), (ox, oy, Z1 + 1), OUTLET_D / 2, roof)              # extraction opening
    hz = Z1 - T - Z0                                                                    # walls 798 high, under the roof
    P.box(S, -x0, 0, Z0, T, D, hz)                                                      # left wall
    right = P.box(S, x0 - T, 0, Z0, T, D, hz)                                           # right wall
    (dy0, dy1), (dz0, dz1) = DOOR_Y, DOOR_Z
    P.cutbox(S, x0 - T - 1, dy0, dz0, T + 2, dy1 - dy0, dz1 - dz0, right)               # loading opening
    P.box(S, -x0 + T, D - T, Z0, W - 2 * T, T, hz)                                      # back wall, between the sides
    low = P.box(S, -x0 + T, 0, Z0, W - 2 * T, T, SPLIT_Z - Z0)                          # front, glove-port panel
    for px in (-PORT_X, PORT_X):
        P.hole(S, (px, -1, PORT_Z), (px, T + 1, PORT_Z), PORT_D / 2, low)              # glove-port opening
    up = P.box(S, -x0 + T, 0, SPLIT_Z, W - 2 * T, T, Z1 - T - SPLIT_Z)                  # front, window panel
    P.cutbox(S, -WIN_X, -1, WIN_Z[0], 2 * WIN_X, T + 2, WIN_Z[1] - WIN_Z[0], up)        # viewing window cut-out
    P.box(C, -WIN_X - PANE_LAP, T, WIN_Z[0] - PANE_LAP, 2 * (WIN_X + PANE_LAP), PANE_T,
          WIN_Z[1] - WIN_Z[0] + 2 * PANE_LAP)                                           # clear pane, inside the front wall
    Ln = lambda m: f"node:door|{m}"
    xa = x0 + DOOR_GAP                                                                  # the door's inner face at x 502
    ya, yb = dy0 - DOOR_LAP, dy1 + DOOR_LAP                                             # y 120..680
    za, zb = dz0 - DOOR_LAP, dz1 + DOOR_LAP                                             # z 920..1580
    P.box(Ln(B), xa, ya, za, DOOR_T, yb - ya, zb - za)                                  # side door, double wall drawn by its outside
    cz, hy = (za + zb) / 2, ya + HANDLE_IN
    for z in (cz - HANDLE_L / 2, cz + HANDLE_L / 2 - 12.0):
        P.box(Ln(Z), xa + DOOR_T, hy, z, 15.0, 12.0, 12.0)                              # handle standoffs
    P.box(Ln(Z), xa + DOOR_T + 15.0, hy, cz - HANDLE_L / 2, 12.0, 12.0, HANDLE_L)       # handle bar, vertical
    P.pivot("door", "rotate", (xa, yb, cz), axis=(0, 0, 1), range=(0, SWING))           # about the door's inner back edge
    P.collider("leaf", xa, ya, za, DOOR_T + 27.0, yb - ya, zb - za)
    P.collider("roof", -x0, 0, Z1 - T, W, D, T)
    P.collider("back", -x0, D - T, Z0, W, T, hz)
    P.collider("front", -x0, 0, Z0, W, T, hz)
    for n, x in (("side-l", -x0), ("side-r", x0 - T)): P.collider(n, x, 0, Z0, T, D, hz)
    for i, (lx, ly) in enumerate(((-x0, 0.0), (x0 - LEG, 0.0), (-x0, D - LEG), (x0 - LEG, D - LEG)), 1):
        P.collider(f"leg-{i}", lx, ly, 0, LEG, LEG, Z0)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="side door", az=320, el=15)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
