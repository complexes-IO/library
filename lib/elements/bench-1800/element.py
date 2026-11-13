#!/usr/bin/env python3
"""bench-1800: steel workbench 1829 x 762, 851 high, with our back-board for field devices. Brief: references/measure.md
(reference workbench, maker's 2-D drawing p. 1 and STEP read-back: top 1828.8 x 762.0, 12 ga, 38.1 apron, feet 1872.5 overall,
4 x Ø9.5 holes at 663.6). Figures marked Assumption (class) below are not on file; spec.md "Open figures" gives each reason."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "bench-1800", "1.3", "furniture"
TITLE = "steel workbench 1829 x 762 x 851 with a 400 high back-board for field devices"
TOOLKIT = "1.3"
BASELINE = "reference workbench: maker's 2-D drawing p. 1 and STEP read-back (references/measure.md); back-board our own design (400 high, 2.0 thick)"
ORIGIN = ("floor machine: floor plane z = 0; x = 0 at the outer edge of the flared left foot; y = 0 on the front anchor-hole line, "
          "49.2 behind the front edge; top toward +z, front edge toward -y")
COMMAND = "BENCH"
PARAMS = dict(backboard=True)
W, D, H, T, APRON = 1828.8, 762.0, 850.9, 2.67, 38.1          # drawing p. 1 (measure.md:13-16)
FLARE, HOLES_Y, HOLE_D = 21.8, 663.6, 9.5                      # flare: STEP read-back (measure.md:19, :22); holes: drawing p. 1 (:18)
Y0 = -(D - HOLES_Y) / 2                                        # top's front edge: the hole pair centred on the depth, as 1.0
HOLE_X = (FLARE + 50.0, FLARE + W - 50.0)                      # Assumption (B): holes 50 inside the top's ends (x pitch NOT on the drawing)
LEG = 60.0                                                     # Assumption (B): solid 60 x 60 (brief: channel 120.8 x 125.3, wall not on file)
LEG_CLR = 20.0                                                 # Assumption (B): leg face 20 inboard of the anchor-hole axis, so the anchor passes
FOOT_T, FOOT_IN = 8.0, 20.0                                    # Assumption (B): foot plate 8 thick, 20 past the leg's inner face
RAIL = (23.7, 82.6)                                            # side rail section (measure.md:23); Assumption (B): 82.6 upright, length between our legs
STR_Z, STR = 180.0, (120.7, 19.1)                              # stretcher section (measure.md:23); Assumption (B): z 180 (height not on file, :30)
PE_R, PE_L, PE_Z = 4.0, 12.0, 200.0                            # Assumption (A): stud Ø8 x 12 (mc-motor-1 bonds its PE here); Assumption (B): its position, as 1.0 (the `pe` port the twin reads)
TAB = (40.0, 2.0, 30.0)                                        # Assumption (C): the stud's tab off the rear-left leg (a housing part)
BB_H, BB_T = 400.0, 2.0                                        # back-board: design choice (OPERATING.md 12)

def build(backboard=True):
    P = Prims(); x0, y0 = FLARE, Y0; xc = x0 + W / 2
    P.box("M-STEEL-7035", x0, y0, H - T, W, D, T)                                               # top sheet
    za, ha = H - APRON, APRON - T                                                                # aprons under the sheet, no overlap
    P.box("M-STEEL-7035", x0, y0, za, W, T, ha); P.box("M-STEEL-7035", x0, y0 + D - T, za, W, T, ha)          # front, rear
    P.box("M-STEEL-7035", x0, y0 + T, za, T, D - 2 * T, ha); P.box("M-STEEL-7035", x0 + W - T, y0 + T, za, T, D - 2 * T, ha)   # ends
    legs_x = (HOLE_X[0] + LEG_CLR, HOLE_X[1] - LEG_CLR - LEG)                                    # 91.8, 1720.6
    for lx in legs_x:
        for ly in (y0 + T, y0 + D - T - LEG):                                                   # against the long aprons
            P.box("M-STEEL-7035", lx, ly, FOOT_T, LEG, LEG, H - T - FOOT_T)                     # legs: foot plate to the top sheet
        left = lx < xc
        fx0 = 0.0 if left else lx - FOOT_IN
        fx1 = lx + LEG + FOOT_IN if left else x0 + W + FLARE
        ft = P.box("M-STEEL-7035", fx0, y0, 0, fx1 - fx0, D, FOOT_T)                            # foot plate, flared 21.8 past the top
        cx = HOLE_X[0] if left else HOLE_X[1]
        for hy in (0.0, HOLES_Y): P.hole("M-GASKET", (cx, hy, -1), (cx, hy, FOOT_T + 1), HOLE_D / 2, ft)
        rx = lx + (LEG - RAIL[0]) / 2
        P.box("M-STEEL-7035", rx, y0 + T + LEG, STR_Z - RAIL[1], RAIL[0], D - 2 * T - 2 * LEG, RAIL[1])   # side rail, leg to leg
    sx0, sx1 = legs_x[0] + (LEG - RAIL[0]) / 2, legs_x[1] + (LEG + RAIL[0]) / 2
    P.box("M-STEEL-7035", sx0, y0 + D / 2 - STR[0] / 2, STR_Z, sx1 - sx0, STR[0], STR[1])         # stretcher on the side rails
    if backboard:
        P.box("node:backboard|M-STEEL-7035", x0, y0 + D - BB_T, H, W, BB_T, BB_H); P.pivot("backboard", "fixed", (x0, y0 + D - BB_T, H))
    px, py = x0 + 40, y0 + D - 30                                                                # stud base, as 1.0 (61.8, 682.8)
    P.box("M-STEEL-7035", px - 10, py, PE_Z - TAB[2] / 2, legs_x[0] - (px - 10), TAB[1], TAB[2])  # bonding tab, welded to the leg
    P.cyl("node:pe|M-BRASS", (px, py, PE_Z), (px, py - PE_L, PE_Z), PE_R)                       # frame bonding stud, axis -y, clear
    P.pivot("pe", "port", (px, py - PE_L, PE_Z), axis=(0, -1, 0), range=(0, 0), unit="PE", gender="none")
    P.collider("top", x0, y0, H - APRON, W, D, APRON); P.collider("base", 0, y0, 0, W + 2 * FLARE, D, H - APRON)
    if backboard: P.collider("backboard", x0, y0 + D - BB_T, H, W, BB_T, BB_H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=22), dict(name="rear back-board and PE stud", az=60, el=22)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
