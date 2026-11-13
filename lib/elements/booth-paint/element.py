#!/usr/bin/env python3
"""booth-paint: open-front spray paint booth with a dry filter wall (a batch booth), our own design (OPERATING.md 12, own designs;
inventory row own_design "yes": "spray paint booth (walls, filter wall, lighting)"). Sheet-steel side walls, roof and back wall
standing on the floor, open at the front where the operator sprays; the back wall has the exhaust opening, covered from inside by
a filter wall (a bank of filter media held by a galvanised retaining grid of four columns and two rows), and behind it a sheet
plenum box with a round duct collar on its top for the exhaust duct. Lighting: two light housings on the roof, each over a
glazed opening in the roof, so the light fittings stand outside the booth's inside; the lamps and their gear are not drawn. The
fan, the floor, the wall frame and the doors are not drawn (the model is the envelope, the filter wall and the openings). Every
size is a design choice. The exhaust airflow, the fire and explosion protection, the lighting level and every other safety
figure of a spray booth are the system's and the standards' (none on file): the element makes no airflow, fire, lighting or
safety claim. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "booth-paint", "1.1", "furniture"
TITLE = ("spray paint booth, open front 3000 x 2500, 2400 deep, sheet 2.0, dry filter wall 2600 x 1800, two glazed roof lights, "
         "plenum, duct Ø500")
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; every size a design choice; fan, lamps, floor and "
            "frame not drawn; no airflow, fire, lighting or safety claim; no vendor file opened")
ORIGIN = ("the floor z = 0 under the middle of the open front: x = 0 across the booth's width, y = 0 the front plane (the work "
          "opening), the booth toward +y; the operator stands toward -y")
COMMAND = "PNTBOOTH"
PARAMS = dict()
W, D, H, T = 3000.0, 2400.0, 2500.0, 2.0          # outside width (x), depth (y), height, sheet 2.0: design choices
OPEN_X, OPEN_Z = 1300.0, (300.0, 2100.0)          # exhaust opening in the back wall, x -1300..1300, z 300..2100 (2600 x 1800): design choice
MEDIA_LAP, MEDIA_T = 50.0, 50.0                   # filter media 50 thick, lapping the opening 50 on every side: design choice
GRID_W, GRID_D = 40.0, 20.0                       # retaining grid bars 40 wide, 20 deep, in front of the media: design choice
GRID_COLS = 4                                     # the grid divides the media into 4 columns, its middle bar into 2 rows: design choice
GRID_IN = 10.0                                    # the grid stands 10 inside the media's edges: design choice
PL_X, PL_D, PL_Z = 1400.0, 600.0, (200.0, 2200.0)  # plenum behind the back wall: x -1400..1400, 600 deep, z 200..2200: design choice
DUCT_D, DUCT_H, COLLAR_T = 500.0, 150.0, 2.0       # duct collar: bore Ø500, 150 high, wall 2.0, on the plenum's top, centred: design choice
LIGHT_X, LIGHT_Y = 600.0, ((600.0, 900.0), (1400.0, 1700.0))   # glazed roof openings x -600..600, 300 deep (y), two: design choice
PANE_T, PANE_LAP = 8.0, 20.0                      # glazing 8 thick under the roof, lapping its opening 20: design choice
HOUSE_LAP, HOUSE_H = 50.0, 150.0                  # light housing on the roof, 50 beyond its opening, 150 high: design choice

def build():
    P = Prims(); S, G, F, C = "M-STEEL-7035", "M-GALV", "M-WHITE-PVC", "M-CASE-CLEAR"
    xi = W / 2 - T                                                         # side walls' inner faces at x +-1498
    yb = D - T                                                             # back wall y 2398..2400
    zr = H - T                                                             # roof's underside z 2498
    roof = P.box(S, -W / 2, 0, zr, W, D, T)                                # roof, across the side walls
    for sx in (-1, 1):
        P.box(S, xi if sx > 0 else -W / 2, 0, 0, T, D, zr)                 # side wall, under the roof
    back = P.box(S, -xi, yb, 0, 2 * xi, T, zr)                             # back wall, between the side walls
    P.cutbox(S, -OPEN_X, yb - 1, OPEN_Z[0], 2 * OPEN_X, T + 2, OPEN_Z[1] - OPEN_Z[0], back)   # exhaust opening
    # the filter wall: media against the back wall's inner face, the retaining grid in front of it
    mx, mz0, mz1 = OPEN_X + MEDIA_LAP, OPEN_Z[0] - MEDIA_LAP, OPEN_Z[1] + MEDIA_LAP   # media x +-1350, z 250..2150
    ym = yb - MEDIA_T                                                      # media y 2348..2398
    P.box(F, -mx, ym, mz0, 2 * mx, MEDIA_T, mz1 - mz0)                     # filter media
    yg = ym - GRID_D                                                       # grid y 2328..2348
    gx, gz0, gz1 = mx - GRID_IN, mz0 + GRID_IN, mz1 - GRID_IN              # grid x +-1340, z 260..2140, inside the media's edges
    P.box(G, -gx, yg, gz1 - GRID_W, 2 * gx, GRID_D, GRID_W)                # grid top bar
    P.box(G, -gx, yg, gz0, 2 * gx, GRID_D, GRID_W)                         # grid bottom bar
    vz0, vz1 = gz0 + GRID_W, gz1 - GRID_W                                  # verticals between top and bottom bars
    pitch = (2 * gx - GRID_W) / GRID_COLS                                  # vertical bars' left edges on a 660 pitch
    vx = [-gx + i * pitch for i in range(GRID_COLS + 1)]
    for x in vx:
        P.box(G, x, yg, vz0, GRID_W, GRID_D, vz1 - vz0)                    # grid vertical bar
    zm = (gz0 + gz1) / 2 - GRID_W / 2                                      # middle bar z 1180..1220
    for i in range(GRID_COLS):
        xa, xb = vx[i] + GRID_W, vx[i + 1]
        P.box(G, xa, yg, zm, xb - xa, GRID_D, GRID_W)                      # grid middle bar, between two verticals
    # the plenum behind the back wall and its duct collar
    y0, y1 = D, D + PL_D                                                   # plenum y 2400..3000
    z0, z1 = PL_Z
    P.box(S, -PL_X, y1 - T, z0, 2 * PL_X, T, z1 - z0)                      # plenum back panel
    P.box(S, -PL_X, y0, z0, 2 * PL_X, PL_D - T, T)                         # plenum bottom
    top = P.box(S, -PL_X, y0, z1 - T, 2 * PL_X, PL_D - T, T)               # plenum top
    for sx in (-1, 1):
        P.box(S, PL_X - T if sx > 0 else -PL_X, y0, z0 + T, T, PL_D - T, z1 - z0 - 2 * T)   # plenum side panel
    yc = y0 + (PL_D - T) / 2                                               # duct axis at y 2699
    P.hole(S, (0, yc, z1 - T - 1), (0, yc, z1 + 1), DUCT_D / 2, top)       # duct opening in the plenum's top
    collar = P.cyl(G, (0, yc, z1), (0, yc, z1 + DUCT_H), DUCT_D / 2 + COLLAR_T)               # duct collar
    P.hole(G, (0, yc, z1 - 1), (0, yc, z1 + DUCT_H + 1), DUCT_D / 2, collar)                 # its bore
    # lighting: a glazed opening in the roof under a light housing, two
    for ly0, ly1 in LIGHT_Y:
        P.cutbox(S, -LIGHT_X, ly0, zr - 1, 2 * LIGHT_X, ly1 - ly0, T + 2, roof)                # roof opening
        P.box(C, -LIGHT_X - PANE_LAP, ly0 - PANE_LAP, zr - PANE_T, 2 * (LIGHT_X + PANE_LAP), ly1 - ly0 + 2 * PANE_LAP,
              PANE_T)                                                                         # its glazing, under the roof
        P.box(S, -LIGHT_X - HOUSE_LAP, ly0 - HOUSE_LAP, H, 2 * (LIGHT_X + HOUSE_LAP), ly1 - ly0 + 2 * HOUSE_LAP,
              HOUSE_H)                                                                        # light housing, on the roof
    P.collider("roof", -W / 2, 0, zr, W, D, T)
    for n, sx in (("wall-l", -1), ("wall-r", 1)):
        P.collider(n, xi if sx > 0 else -W / 2, 0, 0, T, D, zr)
    P.collider("wall-back", -xi, yb, 0, 2 * xi, T, zr)
    P.collider("filter", -mx, yg, mz0, 2 * mx, GRID_D + MEDIA_T, mz1 - mz0)
    P.collider("plenum", -PL_X, y0, z0, 2 * PL_X, PL_D, z1 - z0)
    for n, (ly0, ly1) in zip(("light-a", "light-b"), LIGHT_Y):
        P.collider(n, -LIGHT_X - HOUSE_LAP, ly0 - HOUSE_LAP, H, 2 * (LIGHT_X + HOUSE_LAP), ly1 - ly0 + 2 * HOUSE_LAP, HOUSE_H)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="back", az=60, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
