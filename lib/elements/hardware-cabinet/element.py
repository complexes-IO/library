#!/usr/bin/env python3
"""hardware-cabinet: wall or bench cabinet for small parts, sheet steel 600 x 300 x 700, two doors (nodes door-l and door-r, rotate
about the carcass's front vertical edges, 0 to 110 degrees outward) over four levels of four open bins. Our own design (EM r4 rule):
every size is a design choice. What it meets: M6 wall-fixing screws (four Ø6.6 holes in the back, ISO 273 medium H13,
lib/standards/holes.csv). Hinges, catches and the screws themselves are not modelled. No load rating and no safety claim."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "hardware-cabinet", "1.0", "furniture"
TITLE = "hardware cabinet 600 x 300 x 700, two doors, sixteen small-parts bins"
TOOLKIT = "1.3"
BASELINE = "our own design (EM r4 rule, 2026-11-05): no product matched; every size a design choice; M6 wall-fixing holes ISO 273 medium"
ORIGIN = "bench machine: the carcass underside z = 0 at its front-left corner x = 0, y = 0; the doors open toward -y; the back face y = 300 goes against the wall"
COMMAND = "HWCAB"
PARAMS = dict()

W, D, H, T = 600.0, 300.0, 700.0, 1.5           # carcass outside and sheet: design choices
DOOR_T, GAP = 20.0, 3.0                          # doors 20 thick (double wall), 3 between them
SWING = 110.0                                    # each door opens 0 to 110 degrees outward: design choice
LEVELS, BINS = 4, 4                              # four levels of four bins: design choice
PITCH = 174.0                                    # level pitch: bin floors' tops at z 1.5 (the bottom), 175.5, 349.5, 523.5
LIP, DIV = 50.0, 80.0                            # bin front lip and divider heights above their floor
HANDLE_L = 200.0                                 # vertical bar handles, as cabinet-tool's section (12 x 12 on 12 x 15 x 12 standoffs)
HANDLE_IN = 40.0                                 # handle's inner face 40 from the door's free edge
FIX_D = 6.6                                      # M6 clearance, ISO 273 medium (H13), lib/standards/holes.csv
FIX_XZ = ((50.0, 100.0), (550.0, 100.0), (50.0, 600.0), (550.0, 600.0))   # fixing holes 500 x 500 in the back: design choice

def build():
    P = Prims(); S, F, Z = "M-STEEL-7035", "M-BLUE", "M-ZINC"
    P.box(S, 0, 0, 0, W, D, T)                                                          # bottom
    P.box(S, 0, 0, H - T, W, D, T)                                                      # top
    for x in (0.0, W - T): P.box(S, x, 0, T, T, D, H - 2 * T)                           # sides
    back = P.box(S, T, D - T, T, W - 2 * T, T, H - 2 * T)                               # back, between the sides
    for x, z in FIX_XZ: P.hole(S, (x, D - T - 1.0, z), (x, D + 1.0, z), FIX_D / 2, back)
    BW = (W - 2 * T - (BINS - 1) * T) / BINS                                            # 148.125 inside each bin
    for k in range(LEVELS):
        if k: P.box(S, T, 0, T + k * PITCH - T, W - 2 * T, D - T, T)                    # shelves (levels 2 to 4); level 1 is the bottom
        f = T + k * PITCH                                                               # the level's floor top
        P.box(S, T, 0, f, W - 2 * T, T, LIP)                                            # bin front lip
        for j in range(1, BINS):
            P.box(S, T + j * BW + (j - 1) * T, T, f, T, D - 2 * T, DIV)                 # dividers, behind the lip
    P.collider("body", 0, 0, 0, W, D, H)
    cz = H / 2
    for n, x0, x1, hx, hinge, rng in (
            ("door-l", 0.0, W / 2 - GAP / 2, W / 2 - GAP / 2 - HANDLE_IN - 12.0, 0.0, (0.0, -SWING)),
            ("door-r", W / 2 + GAP / 2, W, W / 2 + GAP / 2 + HANDLE_IN, W, (0.0, SWING))):
        Ln = lambda m, n=n: f"node:{n}|{m}"
        P.box(Ln(F), x0, -DOOR_T, 0, x1 - x0, DOOR_T, H)                                # door, over the carcass edges
        for z in (cz - HANDLE_L / 2, cz + HANDLE_L / 2 - 12.0):
            P.box(Ln(Z), hx, -DOOR_T - 15.0, z, 12.0, 15.0, 12.0)                       # handle standoffs
        P.box(Ln(Z), hx, -DOOR_T - 27.0, cz - HANDLE_L / 2, 12.0, 12.0, HANDLE_L)       # handle bar, vertical
        P.pivot(n, "rotate", (hinge, 0.0, cz), axis=(0, 0, 1), range=rng)               # about the carcass's front vertical edge
        P.collider(n, x0, -DOOR_T - 27.0, 0, x1 - x0, DOOR_T + 27.0, H)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="rear, fixing holes", az=40, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
