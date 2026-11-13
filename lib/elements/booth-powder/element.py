#!/usr/bin/env python3
"""booth-powder: open-front powder coating booth (a batch booth), our own design (OPERATING.md 12, own designs; inventory row
own_design "yes": "powder coating booth (sheet-metal walls, extraction opening)"). Sheet-steel side walls, roof and back wall
standing on the floor, open at the front where the operator sprays; the back wall has the extraction opening, behind it a sheet
plenum box with a round duct collar on its top for the extraction duct. The fan, the filter cartridges, the powder recovery, the
lights and the wall frame are not drawn (the model is the envelope and the openings). Parts come in through the open front on a
hanger. Every size is a design choice. The extraction airflow, the explosion protection and every other safety figure of a powder
booth are the system's and the standards' (none on file): the element makes no airflow, fire or safety claim. No vendor file was
opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "booth-powder", "1.0", "furniture"
TITLE = "powder coating booth, open front 2000 x 2200, 1200 deep, sheet 2.0, back extraction opening 1200 x 1000, plenum, duct Ø300"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; every size a design choice; fan, filters and frame "
            "not drawn; no airflow, fire or safety claim; no vendor file opened")
ORIGIN = ("the floor z = 0 under the middle of the open front: x = 0 across the booth's width, y = 0 the front plane (the work "
          "opening), the booth toward +y; the operator stands toward -y")
COMMAND = "PWDBOOTH"
PARAMS = dict()
W, D, H, T = 2000.0, 1200.0, 2200.0, 2.0   # outside width (x), depth (y), height, sheet 2.0: design choices
OPEN_X, OPEN_Z = 600.0, (500.0, 1500.0)    # extraction opening in the back wall, x -600..600, z 500..1500 (1200 x 1000): design choice
PL_X, PL_D, PL_Z = 700.0, 400.0, (400.0, 1600.0)   # plenum behind the back wall: x -700..700, 400 deep, z 400..1600: design choice
DUCT_D, DUCT_H = 300.0, 100.0                      # duct collar: bore Ø300, 100 high, on the plenum's top, centred: design choice
COLLAR_T = 2.0                                     # the collar's wall: design choice

def build():
    P = Prims(); S, G = "M-STEEL-7035", "M-GALV"
    xi = W / 2 - T                                                         # side walls' inner faces at x +-998
    yb = D - T                                                             # back wall y 1198..1200
    P.box(S, -W / 2, 0, H - T, W, D, T)                                    # roof, across the side walls
    for sx in (-1, 1):
        P.box(S, xi if sx > 0 else -W / 2, 0, 0, T, D, H - T)              # side wall, under the roof
    back = P.box(S, -xi, yb, 0, 2 * xi, T, H - T)                          # back wall, between the side walls
    P.cutbox(S, -OPEN_X, yb - 1, OPEN_Z[0], 2 * OPEN_X, T + 2, OPEN_Z[1] - OPEN_Z[0], back)   # extraction opening
    y0, y1 = D, D + PL_D                                                   # plenum y 1200..1600
    z0, z1 = PL_Z
    P.box(S, -PL_X, y1 - T, z0, 2 * PL_X, T, z1 - z0)                      # plenum back panel
    P.box(S, -PL_X, y0, z0, 2 * PL_X, PL_D - T, T)                         # plenum bottom
    top = P.box(S, -PL_X, y0, z1 - T, 2 * PL_X, PL_D - T, T)               # plenum top
    for sx in (-1, 1):
        P.box(S, PL_X - T if sx > 0 else -PL_X, y0, z0 + T, T, PL_D - T, z1 - z0 - 2 * T)   # plenum side panel
    yc = y0 + (PL_D - T) / 2                                               # duct axis at y 1399
    P.hole(S, (0, yc, z1 - T - 1), (0, yc, z1 + 1), DUCT_D / 2, top)       # duct opening in the plenum's top
    collar = P.cyl(G, (0, yc, z1), (0, yc, z1 + DUCT_H), DUCT_D / 2 + COLLAR_T)               # duct collar
    P.hole(G, (0, yc, z1 - 1), (0, yc, z1 + DUCT_H + 1), DUCT_D / 2, collar)                 # its bore
    P.collider("roof", -W / 2, 0, H - T, W, D, T)
    for n, sx in (("wall-l", -1), ("wall-r", 1)):
        P.collider(n, xi if sx > 0 else -W / 2, 0, 0, T, D, H - T)
    P.collider("wall-back", -xi, yb, 0, 2 * xi, T, H - T)
    P.collider("plenum", -PL_X, y0, z0, 2 * PL_X, PL_D, z1 - z0)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="back", az=60, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
