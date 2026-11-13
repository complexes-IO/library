#!/usr/bin/env python3
"""tensioner-strap-16: generic strapping device (the hand strap tensioner a packer sets on a strapped load and pumps by its lever to
pull the strap tight), our own vendor-neutral design of the ETIM 10.0 class EC003373 (Strapping device; its synonyms name the strap
tensioner and the hand tensioner), built unattended (OPERATING.md 12, generic elements; `python lib/build.py inventory mech` lists
the class once no inventory row builds unattended: group EG020054 Clamping tools, lib/needs-em/mech.md). A zinc-plated steel sole
plate carries a hardened grip plate and two cheeks; between the cheeks a knurled feed wheel on its shaft, 1.5 above the grip plate:
the strap's path. The lever (node `lever`: two side plates outside the cheeks, a handle bar across their rear ends, the shaft pressed
in them and the feed wheel on it) turns about the shaft's axis. On the working stroke the ratchet couples wheel and lever, so the
wheel turns with the lever and draws the strap in; the ratchet and pawl, the feed wheel's spring loading and the gripper for the
strap's lower layer are internal mechanism the twin doesn't read: not drawn, not claimed. The class values (spec.md, "Class values")
are design inputs; every size below is a design choice. No strap tension is designed or claimed. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "tensioner-strap-16", "1.0", "device"
TITLE = "strapping device, generic, hand strap tensioner for plastic strap 12 to 16 wide, feed wheel Ø30, lever 210, sole 160 x 40"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic strapping device (ETIM 10.0 EC003373), a hand strap tensioner; class values are design inputs "
            "(spec.md); the ratchet, the feed wheel's spring loading and the lower layer's gripper not drawn or claimed; every size a "
            "design choice; no strap tension claimed; no vendor file opened")
ORIGIN = ("on the sole plate's underside (z = 0, the face that stands on the load) under the feed wheel's axis; the strap's centre "
          "plane y = 0; the feed wheel's axis is the line x = 0, z = 24.5 along y; the lever toward -x; the sole is fixed, the lever "
          "turns about the wheel's axis and lifts its handle")
COMMAND = "TENSSTRP"
PARAMS = dict()

SOLE_X0, SOLE_X1, SOLE_W, SOLE_T = -110.0, 50.0, 40.0, 6.0   # sole plate 160 x 40 x 6 (z 0..6): design choice
GRIP_X, GRIP_W, GRIP_T = 12.0, 16.0, 2.0                     # hardened grip plate x -12..12, y +-8, z 6..8 under the wheel
GAP = 1.5                                                    # the strap's path between the grip plate and the wheel (design)
WHL_R, WHL_W = 15.0, 16.0                                    # feed wheel Ø30 x 16 (y +-8): as wide as the widest strap
Z_AX = SOLE_T + GRIP_T + GAP + WHL_R                         # the wheel's axis z 24.5
CH_Y0, CH_Y1, CH_X, CH_Z1 = 9.0, 12.0, 20.0, 40.0            # cheeks 3.0 thick at y +-9..12, x -20..20, z 6..40: 1 clear of the wheel
SH_R, SH_Y = 5.0, 17.5                                       # shaft Ø10, y -17.5..17.5: 1.5 proud of the lever plates
CH_BORE_R = 6.0                                              # the cheeks bored Ø12: 1 clear round the shaft (features.csv, own)
LV_Y0, LV_Y1 = 13.0, 16.0                                    # lever side plates 3.0 thick at y +-13..16: 1 clear of the cheeks
LV_X0, LV_X1, LV_H = -200.0, 10.0, 16.0                      # lever plates x -200..10, 16 high round the axis (z 16.5..32.5)
HB_X1 = -186.0                                               # handle bar x -200..-186 across the plates (y +-13)
SWING = 60.0                                                 # the lever lifts its handle 60 degrees: one working stroke
ZINC, STEEL = "M-ZINC", "M-SILVER"

LV_Z0, LV_Z1 = Z_AX - LV_H / 2, Z_AX + LV_H / 2
assert Z_AX == 24.5 and CH_Y0 - WHL_W / 2 == 1.0 and LV_Y0 - CH_Y1 == 1.0 and CH_BORE_R - SH_R == 1.0
assert ((LV_X1 ** 2 + (Z_AX - LV_Z0) ** 2) ** 0.5) + 1.0 < Z_AX - SOLE_T - GRIP_T   # the plates' front corners sweep clear of the sole
assert CH_Z1 - Z_AX > WHL_R and Z_AX - SH_R - CH_BORE_R > SOLE_T                    # the cheeks hold the wheel's outline and the bore


def build():
    P = Prims()
    # ---- fixed: sole plate, grip plate, two cheeks bored 1 clear round the shaft
    P.box(ZINC, SOLE_X0, -SOLE_W / 2, 0, SOLE_X1 - SOLE_X0, SOLE_W, SOLE_T)                                 # sole x -110..50
    P.box(STEEL, -GRIP_X, -GRIP_W / 2, SOLE_T, 2 * GRIP_X, GRIP_W, GRIP_T)                                  # grip plate z 6..8
    for sy in (-1, 1):
        y0 = CH_Y0 if sy > 0 else -CH_Y1
        ch = P.box(ZINC, -CH_X, y0, SOLE_T, 2 * CH_X, CH_Y1 - CH_Y0, CH_Z1 - SOLE_T)                       # cheek z 6..40
        P.hole(ZINC, (0, y0 - 1, Z_AX), (0, y0 + CH_Y1 - CH_Y0 + 1, Z_AX), CH_BORE_R, ch)                   # bored Ø12
    P.collider("sole", SOLE_X0, -SOLE_W / 2, 0, SOLE_X1 - SOLE_X0, SOLE_W, SOLE_T + GRIP_T)
    P.collider("cheeks", -CH_X, -CH_Y1, SOLE_T, 2 * CH_X, 2 * CH_Y1, CH_Z1 - SOLE_T)
    # ---- node lever: feed wheel, shaft, two side plates (the shaft pressed in them), handle bar
    L = lambda m: f"node:lever|{m}"
    P.cyl(L(STEEL), (0, -WHL_W / 2, Z_AX), (0, WHL_W / 2, Z_AX), WHL_R)                                    # feed wheel Ø30 x 16
    P.cyl(L(STEEL), (0, -SH_Y, Z_AX), (0, SH_Y, Z_AX), SH_R)                                               # shaft Ø10 x 35
    for sy in (-1, 1):
        y0 = LV_Y0 if sy > 0 else -LV_Y1
        pl = P.box(L(ZINC), LV_X0, y0, LV_Z0, LV_X1 - LV_X0, LV_Y1 - LV_Y0, LV_H)                         # side plate x -200..10
        P.hole(L(ZINC), (0, y0 - 1, Z_AX), (0, y0 + LV_Y1 - LV_Y0 + 1, Z_AX), SH_R, pl)                     # bored Ø10: shaft pressed in
    P.box(L(ZINC), LV_X0, -LV_Y0, LV_Z0, HB_X1 - LV_X0, 2 * LV_Y0, LV_H)                                   # handle bar between the plates
    P.pivot("lever", "rotate", (0, 0, Z_AX), axis=(0, 1, 0), range=(0, SWING), unit="deg")                 # -x lifts: the handle up
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
