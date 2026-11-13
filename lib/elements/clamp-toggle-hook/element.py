#!/usr/bin/env python3
"""clamp-toggle-hook: generic hook-type toggle clamp (the latch a lid, a door or a fixture plate is drawn shut with: the hook catches a
keeper on the other part and the lever pulls it tight), our own vendor-neutral design of the ETIM 10.0 class EC011973 (Toggle clamp; its
synonyms name the hook type toggle clamp, horizontal and vertical), built unattended (OPERATING.md 12, generic elements; `python
lib/build.py inventory mech` lists the class once no inventory row builds unattended: group EG020054 Clamping tools,
lib/needs-em/mech.md 210). The library's clamp-toggle is the other class of the group (EC003935 Machine toggle clamp, a hold-down);
this is the hook type, its own element. A zinc-plated steel base plate with four M5 holes carries two cheeks; the lever (node `lever`:
two side plates on a pivot pin through the cheeks, a red polyamide handle across their front ends) carries the U-hook (two arms on a
second pin, joined by the catch lip). Lifting the handle turns the lever about the pivot and lifts the hook off the keeper. In the real
clamp the hook swings on its own pin and the lever goes over centre; that linkage is internal mechanism the twin doesn't read: the hook
is drawn riding with the lever. The keeper is the other part's (not drawn). The class values (spec.md, "Class values") are design
inputs; every size below is a design choice. No tensile force is designed or claimed. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "clamp-toggle-hook", "1.0", "device"
TITLE = "toggle clamp, generic, hook type, horizontal, span 88, opening 90 degrees, base 70 x 50 with 4 x M5"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic toggle clamp (ETIM 10.0 EC011973), hook type, horizontal; class values are design inputs "
            "(spec.md); base holes M5 to ISO 273 medium, the screws placed by the host; the keeper and the over-centre linkage not "
            "drawn; every size a design choice; no tensile force claimed; no vendor file opened")
ORIGIN = ("on the base plate's underside (z = 0, the mounting face) under the lever's pivot axis (the line x = 0, z = 14 along y), in "
          "the clamp's centre plane y = 0; the hook reaches toward +x; closed, the lever lies level; the base is fixed, the lever turns "
          "about the pivot axis and lifts the handle and the hook")
COMMAND = "HOOKCLMP"
PARAMS = dict()

BASE_X0, BASE_X1, BASE_W, BASE_T = -30.0, 40.0, 50.0, 3.0    # base plate 70 x 50 x 3 (z 0..3): design choice
HOLE_X, HOLE_Y = (-22.0, 30.0), 17.5                         # 4 x M5 at x -22 / 30, y +-17.5 (52 x 35): design choice
M5_D = 5.5                                                   # M5 clearance, ISO 273 medium H13 (lib/standards/holes.csv)
PZ = 14.0                                                    # the pivot axis: x 0, z 14, along y
CH_X0, CH_X1, CH_Y0, CH_Y1, CH_Z1 = -10.0, 14.0, 13.0, 16.0, 22.0   # cheeks 3.0 thick at y +-13..16, x -10..14, z 3..22
CH_BORE_R, PIN_R = 3.5, 2.5                                  # the cheeks bored Ø7 round the Ø5 pivot pin: 1 clear (features.csv)
PIN_Y = 17.5                                                 # pivot pin y -17.5..17.5: 1.5 proud of the cheeks
LV_Y0, LV_Y1 = 9.0, 12.0                                     # lever side plates 3.0 thick at y +-9..12: 1 clear inside the cheeks
LV_X0, LV_X1, LV_H = -6.0, 70.0, 12.0                        # side plates x -6..70, 12 high round the axis (z 8..20)
HK_X = 24.0                                                  # hook pin Ø5 at x 24 on the axis's level, y +-13.5
HK_PIN_Y = 13.5
HA_Y0, HA_Y1, HA_X0, HA_X1, HA_Z0, HA_Z1 = 5.0, 8.0, 20.0, 96.0, 10.0, 18.0   # hook arms 3.0 thick at y +-5..8: 1 clear of the plates
LIP_X0, LIP_Z0 = 88.0, 2.0                                   # catch lip x 88..96, z 2..10, y +-8: its inner face x 88 = the span
HD_X0, HD_X1, HD_Z1 = 60.0, 110.0, 30.0                      # handle x 60..110, y +-12, z 20..30 on the plates' front ends
OPEN = 90.0                                                  # the lever lifts 90 degrees: the hook clear of the keeper
ZINC, STEEL, GRIP = "M-ZINC", "M-SILVER", "M-RED-PA"

LV_Z0, LV_Z1 = PZ - LV_H / 2, PZ + LV_H / 2
# the cheeks' farthest corner from the pivot axis (the sweep of everything beyond it clears them)
CH_RMAX = max(((x) ** 2 + (z - PZ) ** 2) ** 0.5 for x in (CH_X0, CH_X1) for z in (BASE_T, CH_Z1))
assert CH_Y0 - LV_Y1 == 1.0 and LV_Y0 - HA_Y1 == 1.0 and CH_BORE_R - PIN_R == 1.0
assert PZ - ((LV_X0 ** 2 + (PZ - LV_Z0) ** 2) ** 0.5) > BASE_T + 2.0        # the plates' rear corners sweep 2.5 above the base
assert HK_X - PIN_R > CH_RMAX + 1.0 and HA_X0 ** 2 + (PZ - HA_Z0) ** 2 > (CH_RMAX + 1.0) ** 2   # hook pin and arms beyond the cheeks
assert HA_Z0 > BASE_T and LIP_X0 > BASE_X1 and LV_Z0 > BASE_T + 2.0                          # closed: nothing on the base


def build():
    P = Prims()
    # ---- fixed: base plate with 4 x M5, two cheeks bored 1 clear round the pivot pin
    base = P.box(ZINC, BASE_X0, -BASE_W / 2, 0, BASE_X1 - BASE_X0, BASE_W, BASE_T)                          # base x -30..40
    for x in HOLE_X:
        for sy in (-1, 1):
            P.hole(ZINC, (x, sy * HOLE_Y, -1), (x, sy * HOLE_Y, BASE_T + 1), M5_D / 2, base)                 # M5 clearance
    for sy in (-1, 1):
        y0 = CH_Y0 if sy > 0 else -CH_Y1
        ch = P.box(ZINC, CH_X0, y0, BASE_T, CH_X1 - CH_X0, CH_Y1 - CH_Y0, CH_Z1 - BASE_T)                    # cheek z 3..22
        P.hole(ZINC, (0, y0 - 1, PZ), (0, y0 + CH_Y1 - CH_Y0 + 1, PZ), CH_BORE_R, ch)                        # bored Ø7
    P.collider("base", BASE_X0, -BASE_W / 2, 0, BASE_X1 - BASE_X0, BASE_W, BASE_T)
    P.collider("cheeks", CH_X0, -CH_Y1, BASE_T, CH_X1 - CH_X0, 2 * CH_Y1, CH_Z1 - BASE_T)
    # ---- node lever: pivot pin, two side plates, hook pin, U-hook (two arms + catch lip), handle
    L = lambda m: f"node:lever|{m}"
    P.cyl(L(STEEL), (0, -PIN_Y, PZ), (0, PIN_Y, PZ), PIN_R)                                                  # pivot pin Ø5 x 35
    for sy in (-1, 1):
        y0 = LV_Y0 if sy > 0 else -LV_Y1
        pl = P.box(L(ZINC), LV_X0, y0, LV_Z0, LV_X1 - LV_X0, LV_Y1 - LV_Y0, LV_H)                           # side plate x -6..70
        for x in (0.0, HK_X):
            P.hole(L(ZINC), (x, y0 - 1, PZ), (x, y0 + LV_Y1 - LV_Y0 + 1, PZ), PIN_R, pl)                      # pins pressed in
    P.cyl(L(STEEL), (HK_X, -HK_PIN_Y, PZ), (HK_X, HK_PIN_Y, PZ), PIN_R)                                      # hook pin Ø5 x 27
    for sy in (-1, 1):
        y0 = HA_Y0 if sy > 0 else -HA_Y1
        arm = P.box(L(ZINC), HA_X0, y0, HA_Z0, HA_X1 - HA_X0, HA_Y1 - HA_Y0, HA_Z1 - HA_Z0)                 # hook arm x 20..96
        P.hole(L(ZINC), (HK_X, y0 - 1, PZ), (HK_X, y0 + HA_Y1 - HA_Y0 + 1, PZ), PIN_R, arm)                  # on the hook pin
    P.box(L(ZINC), LIP_X0, -HA_Y1, LIP_Z0, HA_X1 - LIP_X0, 2 * HA_Y1, HA_Z0 - LIP_Z0)                        # catch lip under the arms
    P.box(L(GRIP), HD_X0, -LV_Y1, LV_Z1, HD_X1 - HD_X0, 2 * LV_Y1, HD_Z1 - LV_Z1)                            # handle on the plates
    P.pivot("lever", "rotate", (0, 0, PZ), axis=(0, -1, 0), range=(0, OPEN), unit="deg")                     # + lifts the handle and hook
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
