#!/usr/bin/env python3
"""tb-rollcab: roll cabinet (toolbox station) 680 x 460 x 800, sheet steel, five drawers (nodes drawer-1 .. drawer-5, translate -y,
0 to 320), a push bar on the right side, and four caster plates' fixing holes in the 3.0 bottom (4 x Ø9.0 each, M8 clearance,
ISO 273 medium H13, lib/standards/holes.csv). Our own design (EM r4 rule): every size is a design choice. The casters are not
built yet (lib/rounds/mech/next.md #14): EM's rule, the holes are modelled and a later version places the part. Drawer slides,
the caster screws and a lock are not modelled. No load rating and no safety claim."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "tb-rollcab", "1.0", "furniture"
TITLE = "roll cabinet 680 x 460 x 800, five drawers, caster plate holes"
TOOLKIT = "1.3"
BASELINE = "our own design (EM r4 rule, 2026-11-05): no product matched; every size a design choice; caster fixing holes M8 ISO 273 medium"
ORIGIN = "bench machine: the carcass underside z = 0 at its front-left corner x = 0, y = 0; drawers open toward -y; the casters (not built yet) go under z = 0"
COMMAND = "ROLLCAB"
PARAMS = dict()

W, D, H = 680.0, 460.0, 800.0                    # carcass outside: design choices
T, BOT = 1.5, 3.0                                # sheet; the bottom 3.0, it carries the four caster plates
FRONT_T, GAP = 20.0, 3.0                         # drawer fronts 20 thick (double wall), 3 between fronts
FRONTS = [240.0, 180.0, 150.0, 110.0, 100.0]     # front heights, bottom to top (sum 780 + 4 gaps = 792, z 4.5 to 796.5)
SIDE_CLR = 12.5                                  # each side between the tray and the carcass, for the slides (not modelled)
TRAY_D, TRAY_T = 420.0, 1.5                      # tray depth and sheet
TRAVEL = 320.0                                   # pull-out: 100 of the 420 tray stays inside
HANDLE_L = 300.0                                 # drawer handles, cabinet-tool's
PUSH_Z, PUSH_IN = 700.0, 60.0                    # push bar: centred at z 700, standoffs 60 in from the front and back
CAST_D = 9.0                                     # M8 clearance, ISO 273 medium (H13), lib/standards/holes.csv
CAST_IN, CAST_PX, CAST_PY = 70.0, 80.0, 60.0     # caster plate centres 70 in from each side, front and back; holes 80 x 60 apart
PAD = 2 * CAST_IN                                # the bottom's corner pads 140 x 140, one per caster plate
CAST_C = [(x, y) for x in (CAST_IN, W - CAST_IN) for y in (CAST_IN, D - CAST_IN)]

def build():
    P = Prims(); S, F, Z = "M-STEEL-7035", "M-BLUE", "M-ZINC"
    # bottom, 3.0, built as seven plates in one plane: a pad 140 x 140 at each corner (the caster plate's four holes, each pad cut
    # on its own keeps the cut small), and the three plates between them
    P.box(S, PAD, 0, 0, W - 2 * PAD, D, BOT)                                            # middle, full depth
    for x in (0.0, W - PAD): P.box(S, x, PAD, 0, PAD, D - 2 * PAD, BOT)                 # left and right, between the pads
    for cx, cy in CAST_C:                                                               # four caster pads, four holes each
        pad = P.box(S, cx - PAD / 2, cy - PAD / 2, 0, PAD, PAD, BOT)
        for dx in (-CAST_PX / 2, CAST_PX / 2):
            for dy in (-CAST_PY / 2, CAST_PY / 2):
                P.hole(S, (cx + dx, cy + dy, -1.0), (cx + dx, cy + dy, BOT + 1.0), CAST_D / 2, pad)
    P.box(S, 0, 0, H - T, W, D, T)                                                      # top
    for x in (0.0, W - T): P.box(S, x, 0, BOT, T, D, H - BOT - T)                       # sides, between the bottom and the top
    P.box(S, T, D - T, BOT, W - 2 * T, T, H - BOT - T)                                  # back, between the sides
    for y in (PUSH_IN, D - PUSH_IN - 12.0):
        P.box(Z, W, y, PUSH_Z - 6.0, 15.0, 12.0, 12.0)                                  # push bar standoffs, right side
    P.box(Z, W + 15.0, PUSH_IN, PUSH_Z - 6.0, 12.0, D - 2 * PUSH_IN, 12.0)              # push bar, along y
    P.collider("body", 0, 0, 0, W + 27.0, D, H)
    z = BOT + T                                                                         # 4.5: the first front's lower edge
    tx0, tx1 = T + SIDE_CLR, W - T - SIDE_CLR
    for k, fh in enumerate(FRONTS, start=1):
        n = f"drawer-{k}"; Ln = lambda m, n=n: f"node:{n}|{m}"
        P.box(Ln(F), 0, -FRONT_T, z, W, FRONT_T, fh)                                    # front, over the carcass edges
        tz0, tz1 = z + 10.0, z + fh - 20.0                                              # tray: bottom 10 above the front's lower edge, sides 20 below its top
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

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="underside, caster holes", az=40, el=-35)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
