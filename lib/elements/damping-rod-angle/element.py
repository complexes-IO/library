#!/usr/bin/env python3
"""damping-rod-angle: generic rubber-metal slanting rail (an angle damping rod: the rail-shaped machine mount that carries a machine
or a frame on two inclined rubber layers), our own vendor-neutral design of the ETIM 10.0 class EC003741 (Angle damping rod,
"Rubber-metal slanting rail"), built unattended (OPERATING.md 12, generic elements). A steel base 140 x 160 x 10 with four M10
clearance holes carries a holder with a 90-degree V-groove along the rail; two rubber layers 10 thick lie on the groove's faces, and
a steel wedge rests on them, its 90-degree ridge down in the groove, two M10 tapped holes in its top face for the machine's foot.
A vertical load presses the wedge into the V, so the rubber works in compression and shear at once. The class values (spec.md,
"Class values") are design inputs; the class has no stiffness or load feature, so no load or deflection is claimed and nothing
moves in the model. The M10 thread's limits are derived (spec.md, What it meets); the tapped holes are drawn plain at D1. Every
other size is a design choice. No vendor file was opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "damping-rod-angle", "1.1", "device"
TITLE = "angle damping rod, generic, rubber-metal slanting rail, 140 x 160 x 80, 90-degree V, 4 x M10 base holes, 2 x M10 tapped"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic angle damping rod (ETIM 10.0 EC003741), a rubber-metal slanting rail; class values are design "
            "inputs (spec.md); base holes at M10's ISO 273 medium clearance; the M10 tapped holes derived (ISO 68-1, ISO 965-1), "
            "drawn plain at D1; every size a design choice; no load, stiffness or deflection claim; no vendor file opened")
ORIGIN = ("the mounting face (the base's underside, z = 0) at the rail's centre; y along the rail, x across it; the wedge's top face, "
          "where the machine's foot seats, at z 80")
COMMAND = "DAMPRODANG"
PARAMS = dict()

W, L, H = 140.0, 160.0, 80.0                     # class values: total width (x +-70), length (y +-80), total height (z 0..80)
BASE_T = 10.0                                    # base plate 140 x 160 x 10: design choice
HOLE_X, HOLE_Y = 56.0, 60.0                      # base holes at x +-56, y +-60: design choice
HOLE_D = 11.0                                    # M10 clearance medium H13 (ISO 273, lib/standards/holes.csv)
HOLD_X, HOLD_TOP = 42.0, 50.0                    # the holder x +-42, from the base to z 50: design choice
IN = 0.5                                         # the holder runs 0.5 into the base (one solid joint)
APEX = 18.0                                      # the V-groove's bottom line at z 18, its faces at 45 degrees: design choice
GROOVE = HOLD_TOP - APEX                         # 32: the groove's half-width at the holder's top (a 90-degree V)
RUB_T = 10.0                                     # rubber layers 10 thick on each groove face: design choice
RUB_L = 150.0                                    # rubber 150 along y (y +-75), 5 short of each steel end: design choice
RUB_A0 = 12.0                                    # each layer starts 12 up its face from the groove's bottom line, so the two never meet
WEDGE_X = GROOVE                                 # the wedge x +-32, as wide as the groove's mouth: design choice
TAP_Y, TAP_DEPTH = 45.0, 15.0                    # two M10 tapped holes in the wedge's top at y +-45, 15 deep: design choice
TAP_D1 = 8.3762                                  # M10 x 1.5, 6H: D1 min, derived: derive.thread(10.0, 1.5) (ISO 68-1; ISO 965-1 clause 10)
S = math.sqrt(0.5)                               # sin 45 = cos 45
RISE = RUB_T / S                                 # 14.142: the wedge's faces lie RUB_T off the groove's faces, 14.142 higher at any x
RIDGE = APEX + RISE                              # 32.142: the wedge's ridge line
SLOPE = GROOVE / S                               # 45.255: the groove's face from the bottom line to the holder's top, along the slope
MAT, RUB = "M-ZINC", "M-GASKET"

assert HOLE_X - HOLE_D / 2 >= HOLD_X + 8.0 and W / 2 - HOLE_X - HOLE_D / 2 >= 8.0    # the holes clear the holder and the base's edge
assert APEX - BASE_T >= 8.0                                                          # 8 of steel under the groove's bottom
assert HOLD_X - GROOVE >= 8.0                                                        # 8 lips beside the groove's mouth
assert RUB_A0 > RUB_T                                                                # the two layers stay apart at the bottom
assert H - TAP_DEPTH > RIDGE + WEDGE_X                                               # the tapped holes end in the wedge's full width
assert RIDGE + WEDGE_X - HOLD_TOP >= 8.0                                             # the wedge's lower corners stand 8+ over the lips


def build():
    P = Prims(); hw, hl = W / 2, L / 2
    base = P.box(MAT, -hw, -hl, 0.0, W, L, BASE_T)                                              # base plate
    for x in (-HOLE_X, HOLE_X):
        for y in (-HOLE_Y, HOLE_Y):
            P.hole(MAT, (x, y, -1.0), (x, y, BASE_T + 1.0), HOLE_D / 2, base)                  # M10 clearance holes
    hold = P.box(MAT, -HOLD_X, -hl, BASE_T - IN, 2 * HOLD_X, L, HOLD_TOP - BASE_T + IN)         # holder on the base
    # the 90-degree V-groove: one cut whose two faces meet at the bottom line (0, z APEX); the region above both 45-degree faces
    P.cut(MAT, (0.0, -hl - 10.0, APEX), (S, 0, S), (0, 1, 0), (-S, 0, S), 80.0, L + 20.0, 80.0, hold)
    # the two rubber layers on the groove's faces, 10 thick, bonded to the holder below and the wedge above
    a0, ln = RUB_A0, SLOPE - RUB_A0
    P.obox(RUB, (a0 * S, -RUB_L / 2, APEX + a0 * S), (S, 0, S), (0, 1, 0), (-S, 0, S), ln, RUB_L, RUB_T)    # right layer
    P.obox(RUB, (-a0 * S, RUB_L / 2, APEX + a0 * S), (-S, 0, S), (0, -1, 0), (S, 0, S), ln, RUB_L, RUB_T)   # left layer
    # the wedge: a box cut below its two 45-degree faces (each RUB_T off the groove's face), its ridge down at z RIDGE
    wb = RIDGE - 1.0
    wedge = P.box(MAT, -WEDGE_X, -hl, wb, 2 * WEDGE_X, L, H - wb)
    P.cut(MAT, (60.0, -hl - 20.0, RIDGE + 60.0), (-S, 0, -S), (0, 1, 0), (S, 0, -S), 100.0, L + 40.0, 60.0, wedge)   # under the right face
    P.cut(MAT, (-60.0, hl + 20.0, RIDGE + 60.0), (S, 0, -S), (0, -1, 0), (-S, 0, -S), 100.0, L + 40.0, 60.0, wedge)  # under the left face
    for y in (-TAP_Y, TAP_Y):
        P.hole(MAT, (0, y, H - TAP_DEPTH), (0, y, H + 1.0), TAP_D1 / 2, wedge)                 # M10 tapped holes, plain at D1
    P.collider("body", -hw, -hl, 0.0, W, L, HOLD_TOP)
    P.collider("wedge", -WEDGE_X, -hl, RIDGE, 2 * WEDGE_X, L, H - RIDGE)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="end", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
