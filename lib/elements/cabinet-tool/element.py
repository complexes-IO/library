#!/usr/bin/env python3
"""cabinet-tool: floor-standing steel tool cabinet 900 x 600 x 1000 with five drawers (nodes drawer-1 .. drawer-5, translate -y,
0 to 450). Our own design (EM r4 rule): every size is a design choice; drawer slides are not modelled. No load rating."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "cabinet-tool", "1.1", "furniture"
TITLE = "tool cabinet 900 x 600 x 1000, five drawers"
TOOLKIT = "1.3"
BASELINE = "our own design (EM r4 rule, 2026-11-05): no product matched; every size a design choice"
ORIGIN = "floor machine: floor plane z = 0, the carcass's front-left corner x = 0, y = 0; drawers open toward -y"
COMMAND = "TOOLCAB"
PARAMS = dict()
W, D, H, T = 900.0, 600.0, 1000.0, 1.5          # carcass outside and sheet: design choices
PLINTH, INSET = 80.0, 30.0                       # plinth height and set-back
FRONT_T, GAP = 20.0, 3.0                         # drawer fronts 20 thick (double wall), 3 between fronts
FRONTS = [222.0, 200.0, 180.0, 150.0, 150.0]     # front heights, bottom to top (sum 902 + 4 gaps = 914, from z 83 to 997)
SIDE_CLR = 12.5                                  # each side between the tray and the carcass, for the slides (not modelled)
TRAY_D, TRAY_T = 560.0, 1.5                      # tray depth and sheet
TRAVEL = 450.0                                   # pull-out
HANDLE_L = 300.0

def build():
    P = Prims(); S, F, Z = "M-STEEL-7035", "M-BLUE", "M-ZINC"
    P.box(S, INSET, INSET, 0, W - 2 * INSET, D - 2 * INSET, PLINTH)                      # plinth
    P.box(S, 0, 0, PLINTH, W, D, T)                                                     # bottom
    P.box(S, 0, 0, H - T, W, D, T)                                                      # top
    for x in (0.0, W - T): P.box(S, x, 0, PLINTH + T, T, D, H - PLINTH - 2 * T)         # sides
    P.box(S, T, D - T, PLINTH + T, W - 2 * T, T, H - PLINTH - 2 * T)                    # back
    P.collider("body", 0, 0, 0, W, D, H)
    z = PLINTH + T + GAP / 2 + 0.5                                                      # 83.0
    tx0, tx1 = T + SIDE_CLR, W - T - SIDE_CLR
    for k, fh in enumerate(FRONTS, start=1):
        n = f"drawer-{k}"; Ln = lambda m: f"node:{n}|{m}"
        P.box(Ln(F), 0, -FRONT_T, z, W, FRONT_T, fh)                                    # front, over the carcass edges
        tz0, tz1 = z + 10.0, z + fh - 20.0                                              # tray: bottom 10 above the front's lower edge, sides 20 below its top (spec.md)
        P.box(Ln(S), tx0, 0, tz0, tx1 - tx0, TRAY_D, TRAY_T)                            # tray bottom
        for x in (tx0, tx1 - TRAY_T): P.box(Ln(S), x, 0, tz0 + TRAY_T, TRAY_T, TRAY_D, tz1 - tz0 - TRAY_T)   # tray sides
        P.box(Ln(S), tx0 + TRAY_T, TRAY_D - TRAY_T, tz0 + TRAY_T, tx1 - tx0 - 2 * TRAY_T, TRAY_T, tz1 - tz0 - TRAY_T)  # tray back
        cz = z + fh / 2
        for x in (W / 2 - HANDLE_L / 2, W / 2 + HANDLE_L / 2 - 12.0):
            P.box(Ln(Z), x, -FRONT_T - 15.0, cz - 6.0, 12.0, 15.0, 12.0)                # handle standoffs
        P.box(Ln(Z), W / 2 - HANDLE_L / 2, -FRONT_T - 27.0, cz - 6.0, HANDLE_L, 12.0, 12.0)   # handle bar
        P.pivot(n, "translate", (W / 2, -FRONT_T, cz), axis=(0, -1, 0), range=(0, TRAVEL))
        P.collider(n, 0, -FRONT_T - 27.0, z, W, FRONT_T + 27.0 + TRAY_D, fh)
        z += fh + GAP
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="side", az=270, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
