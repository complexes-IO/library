#!/usr/bin/env python3
"""robot-pedestal: steel pedestal that raises a robot's base 700 above the floor: base plate with 4 x M12 floor anchors, a 300 x 300
column with four gussets, and the mounting face (node `mount`). Our own design (EM r4 rule). The robot's own bolt pattern is NOT ON
FILE (no robot element yet), so the mounting face is blank in this version. No load rating."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "robot-pedestal", "1.0", "furniture"
TITLE = "robot pedestal 600 x 600 x 700, mounting face 400 x 400"
TOOLKIT = "1.3"
BASELINE = "our own design (EM r4 rule, 2026-11-05): no product matched; floor anchors M12 in ISO 273 medium holes; robot bolt pattern not on file"
ORIGIN = "floor machine on its axis: floor plane z = 0, the base plate's centre x = 0, y = 0 (the robot's axis); front toward -y"
COMMAND = "RPED"
PARAMS = dict()
BASE, BASE_T = 600.0, 25.0       # base plate 600 x 600 x 25: design choice
COL = 300.0                      # column 300 x 300 (closed box): design choice
TOP, TOP_T = 400.0, 25.0         # mounting plate 400 x 400 x 25: design choice
H = 700.0                        # mounting face above the floor: design choice
GUS_L, GUS_H, GUS_T = 130.0, 150.0, 12.0   # four gussets, column face to 20 inside the base plate's edge: design choice
ANCHOR_D, ANCHOR_AT = 13.5, 250.0          # 4 x M12 anchors at +-250, +-250; Ø13.5 = M12 clearance, ISO 273 medium H13

def build():
    P = Prims(); S, M = "M-STEEL-7035", "M-GALV"
    bp = P.box(S, -BASE / 2, -BASE / 2, 0, BASE, BASE, BASE_T)                          # base plate
    for sx in (-1, 1):
        for sy in (-1, 1):
            x, y = sx * ANCHOR_AT, sy * ANCHOR_AT
            P.hole(S, (x, y, -1), (x, y, BASE_T + 1), ANCHOR_D / 2, bp)
    P.box(S, -COL / 2, -COL / 2, BASE_T, COL, COL, H - TOP_T - BASE_T)                 # column
    for sx, sy in ((1, 0), (-1, 0), (0, 1), (0, -1)):                                  # gussets on the four faces' centre lines
        if sx: x0 = COL / 2 if sx > 0 else -COL / 2 - GUS_L; P.box(S, x0, -GUS_T / 2, BASE_T, GUS_L, GUS_T, GUS_H)
        else:  y0 = COL / 2 if sy > 0 else -COL / 2 - GUS_L; P.box(S, -GUS_T / 2, y0, BASE_T, GUS_T, GUS_L, GUS_H)
    P.box(f"node:mount|{M}", -TOP / 2, -TOP / 2, H - TOP_T, TOP, TOP, TOP_T)            # mounting plate: the robot's base sits on its top face
    P.pivot("mount", "fixed", (0, 0, H), axis=(0, 0, 1))
    P.collider("body", -BASE / 2, -BASE / 2, 0, BASE, BASE, H - TOP_T)
    P.collider("mount", -TOP / 2, -TOP / 2, H - TOP_T, TOP, TOP, TOP_T)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="top, mounting face", az=230, el=60)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
