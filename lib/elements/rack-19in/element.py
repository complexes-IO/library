#!/usr/bin/env python3
"""rack-19in: floor-standing rack frame 600 x 800 x 2000 for 19-inch equipment: a plinth, a 40 x 40 frame, side and rear panels,
a roof, four plain vertical mounting rails on cross-bars, and a front door (node door-front, rotates about the frame's front-left
vertical edge, 0 to 110 degrees outward). Our own design (EM r4 rule): every size is a design choice. The 19-inch figures (the panel
opening between the rails, the rail hole pitch, the unit height; IEC 60297 / EIA-310) are not on file here, so the rails are plain
bars placed by this frame, not at the standard's figures (spec.md, open figures). No load rating and no safety claim."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "rack-19in", "1.1", "furniture"
TITLE = "rack frame 600 x 800 x 2000 for 19-inch equipment, plain rails, front door"
TOOLKIT = "1.3"
BASELINE = "our own design (EM r4 rule, 2026-11-05): no product matched; every size a design choice; the 19-inch rail figures not on file"
ORIGIN = "bench machine: the plinth underside z = 0 at its front-left corner x = 0, y = 0; the door opens toward -y; the rear panel y = 800"
COMMAND = "RACK19"
PARAMS = dict()

W, D, H = 600.0, 800.0, 2000.0                   # overall, door shut: design choices
PL = 100.0                                       # plinth height
M = 40.0                                         # frame members 40 x 40, built solid
T = 1.5                                          # side, rear and roof sheet
TOP = H - T                                      # frame top, under the roof sheet
DOOR_T = 20.0                                    # door 20 thick (double wall), over the frame's front
SWING = 110.0                                    # the door opens 0 to 110 degrees outward: design choice
HANDLE_L, HANDLE_IN = 200.0, 40.0                # vertical bar handle, as hardware-cabinet's; inner face 40 from the free edge
RAIL_W, RAIL_T = 25.0, 2.0                       # plain rails 25 wide, 2.0 sheet, on the cross-bars' front faces
CARRIER_Y = (100.0, 660.0)                       # front and rear cross-bars' front faces: rails at y 98 to 100 and 658 to 660
                                                 # the 19-inch opening, hole pitch and unit height: NOT ON FILE (spec.md); these
                                                 # positions are this frame's, not the standard's

def build():
    P = Prims(); S, F, G, Z = "M-STEEL-7035", "M-BLUE", "M-GALV", "M-ZINC"
    P.box(S, 0, 0, 0, W, D, PL)                                                         # plinth, built solid
    for x in (0.0, W - M):
        for y in (0.0, D - M): P.box(S, x, y, PL, M, M, TOP - PL)                       # corner posts
    for z in (PL, TOP - M):
        for x in (0.0, W - M): P.box(S, x, M, z, M, D - 2 * M, M)                       # side members, between the posts
        for y in (0.0, D - M): P.box(S, M, y, z, W - 2 * M, M, M)                       # front and rear members, between the posts
        for y in CARRIER_Y: P.box(S, M, y, z, W - 2 * M, M, M)                          # rail cross-bars, between the side members
    for x in (0.0, W - T): P.box(S, x, M, PL + M, T, D - 2 * M, TOP - PL - 2 * M)       # side panels, in the posts' outer faces
    P.box(S, M, D - T, PL + M, W - 2 * M, T, TOP - PL - 2 * M)                          # rear panel, in the posts' rear faces
    P.box(S, 0, 0, TOP, W, D, T)                                                        # roof
    for y in CARRIER_Y:
        for x in (M, W - M - RAIL_W): P.box(G, x, y - RAIL_T, PL, RAIL_W, RAIL_T, TOP - PL)   # plain rails, plinth to frame top
    P.collider("body", 0, 0, 0, W, D, H)
    n = "door-front"; Ln = lambda m: f"node:{n}|{m}"; cz = (PL + H) / 2; hx = W - HANDLE_IN - 12.0
    P.box(Ln(F), 0, -DOOR_T, PL, W, DOOR_T, H - PL)                                     # door, plinth top to roof top
    for z in (cz - HANDLE_L / 2, cz + HANDLE_L / 2 - 12.0):
        P.box(Ln(Z), hx, -DOOR_T - 15.0, z, 12.0, 15.0, 12.0)                           # handle standoffs
    P.box(Ln(Z), hx, -DOOR_T - 27.0, cz - HANDLE_L / 2, 12.0, 12.0, HANDLE_L)           # handle bar, vertical
    P.pivot(n, "rotate", (0.0, 0.0, cz), axis=(0, 0, 1), range=(0.0, -SWING))           # about the frame's front-left vertical edge
    P.collider(n, 0, -DOOR_T - 27.0, PL, W, DOOR_T + 27.0, H - PL)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="rear", az=40, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
