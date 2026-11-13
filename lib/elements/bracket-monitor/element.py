#!/usr/bin/env python3
"""bracket-monitor: wall-mounted display bracket with a tilting head (node `tilt`) and a 100 x 100 display hole pattern. Our own
design (EM r4 rule). What it meets: the surface it is screwed to (4 x M6, ISO 273 medium Ø6.6) and a display's rear hole pattern
(100 x 100, 4 x M4, ISO 273 medium Ø4.5: the pattern and the M4 screw size are one Assumption (B), the VESA standard's text is not
on file; ISO 273 gives the Ø4.5 hole for the chosen M4 only). 1.1: text only (review 1.0 finding 1), the part unchanged."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "bracket-monitor", "1.1", "furniture"
TITLE = "display bracket, wall plate and tilting 100 x 100 head"
TOOLKIT = "1.3"
BASELINE = "our own design (EM r4 rule, 2026-11-05): no product matched; screws to ISO 273 medium clearance; display pattern 100 x 100 an Assumption"
ORIGIN = "surface mount: the wall plate's back face y = 0 on the mounting surface, its centre x = 0, z = 0; the arm toward -y"
COMMAND = "BRKMON"
PARAMS = dict()
WP, WT = 150.0, 4.0              # wall plate 150 x 150 x 4: design choice
WP_PITCH, WP_D = 120.0, 6.6      # 4 x M6 at 120 x 120 (design choice); Ø6.6 = M6 clearance, ISO 273 medium H13
ARM_W, ARM_L = 40.0, 200.0       # arm 40 x 40 section, reaching 200 from the plate face to the hinge axis: design choice
AXIS_Y = -(WT + ARM_L)           # the tilt axis (along x) at y = -204, z = 0
KN_R, KN_L = 12.0, 60.0          # hinge knuckle on the arm: Ø24 x 60, design choice
HEAD, HT = 120.0, 4.0            # head plate 120 x 120 x 4, its back face 16 from the axis: design choice
HEAD_Y = AXIS_Y - 16.0
VESA, VESA_D = 100.0, 4.5        # display pattern 100 x 100 and its 4 x M4 screws (Assumption (B): VESA MIS-D text not on file); Ø4.5 ISO 273 medium H13 for an M4
TILT = (-20.0, 20.0)             # tilt range in degrees: design choice

def build():
    P = Prims()
    wp = P.box("M-STEEL-7035", -WP / 2, -WT, -WP / 2, WP, WT, WP)                                     # wall plate
    for sx in (-1, 1):
        for sz in (-1, 1):
            x, z = sx * WP_PITCH / 2, sz * WP_PITCH / 2
            P.hole("M-STEEL-7035", (x, 1, z), (x, -WT - 1, z), WP_D / 2, wp)
    P.box("M-STEEL-7035", -ARM_W / 2, AXIS_Y, -ARM_W / 2, ARM_W, ARM_L, ARM_W)                     # arm, plate face to the axis
    P.cyl("M-STEEL-7035", (-KN_L / 2, AXIS_Y, 0), (KN_L / 2, AXIS_Y, 0), KN_R)                      # knuckle
    # the tilting head: plate, two ears and two sleeves beside the knuckle (0.5 axial gap), all node `tilt`
    T = "node:tilt|M-STEEL-7035"
    hp = P.box(T, -HEAD / 2, HEAD_Y - HT, -HEAD / 2, HEAD, HT, HEAD)
    for sx in (-1, 1):
        for sz in (-1, 1):
            x, z = sx * VESA / 2, sz * VESA / 2
            P.hole(T, (x, HEAD_Y + 1, z), (x, HEAD_Y - HT - 1, z), VESA_D / 2, hp)
    for sx in (-1, 1):
        x0 = KN_L / 2 + 0.5 if sx > 0 else -KN_L / 2 - 0.5 - 14.0
        P.cyl(T, (x0, AXIS_Y, 0), (x0 + 14.0, AXIS_Y, 0), KN_R)                                     # sleeve on the axis
        P.box(T, x0, HEAD_Y, -KN_R, 14.0, AXIS_Y - HEAD_Y, 2 * KN_R)                                # ear from the sleeve to the plate
    P.pivot("tilt", "rotate", (0, AXIS_Y, 0), axis=(1, 0, 0), range=TILT)
    P.collider("body", -WP / 2, AXIS_Y, -WP / 2, WP, -AXIS_Y, WP)
    P.collider("tilt", -HEAD / 2, HEAD_Y - HT, -HEAD / 2, HEAD, AXIS_Y + KN_R - (HEAD_Y - HT), HEAD)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=20), dict(name="side, tilt axis", az=270, el=0)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
