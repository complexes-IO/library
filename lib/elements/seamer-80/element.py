#!/usr/bin/env python3
"""seamer-80: generic hand seamer (the sheet-metal worker's seaming pliers: two wide flat blades grip a sheet's edge so it can be
bent, folded into a seam or held taut), our own vendor-neutral design of the ETIM 10.0 class EC004320 (Seaming tool; its synonyms
name the plate seaming device, the plate seaming tool and the plate tensioner), built unattended (OPERATING.md 12, generic elements;
`python lib/build.py inventory mech` lists the class once no inventory row builds unattended: group EG020054 Clamping tools,
lib/needs-em/mech.md). Two zinc-plated steel arms crossed on one pin, as pliers: the fixed arm (the lower blade, its neck, two cheeks
bored for the pressed pin and the upper handle) and the moving arm (node `jaw`: a boss bored 1 clear round the pin between the
cheeks, its neck and the upper blade above the pin's axis, the lower handle below it), each handle with a plastic grip. Squeezing the
handles together closes the blades on the sheet; spreading them turns the moving arm about the pin and opens the blades. The pin's
boss and cheeks follow clamp-spring-25 1.0's pattern. The class values (spec.md, "Class values") are design inputs; every size below
is a design choice. No clamping force is designed or claimed. No vendor file opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "seamer-80", "1.1", "device"
TITLE = "hand seamer, generic, blades 80 wide with a 30 bite, clamping spread 19.7, length 250, two steel arms crossed on a Ø8 pin, plastic grips"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic seaming tool (ETIM 10.0 EC004320), a hand seamer; class values are design inputs (spec.md); "
            "every size a design choice; no clamping force claimed; no vendor file opened")
ORIGIN = ("the pin's axis is the line x = 0, z = 0 along y; the seamer's centre plane y = 0; the blades toward +x, the handles toward "
          "-x; the fixed arm carries the lower blade and the upper handle, the moving arm (node jaw) the upper blade and the lower "
          "handle; the blades' gripping faces 1 apart at rest (closed), either side of z = 0")
COMMAND = "SEAMER"
PARAMS = dict()

PIN_R, PIN_PROUD = 4.0, 0.5                      # pin Ø8, pressed through the cheeks, its ends 0.5 proud of them (clamp-spring-25's)
BOSS_BORE_R = 5.0                                # the moving arm's boss bored Ø10: 1 clear round the pin (features.csv, own)
T = 8.0                                          # every blade, neck and handle bar 8 thick (z): design choice, no edge under 8
FW, MW = 18.0, 10.0                              # the fixed arm's neck and handle bar 18 wide (y +-9), the moving arm's 10 (y +-5)
CH_Y0, CH_Y1 = 6.0, 9.0                          # the fixed arm's cheeks 3.0 thick at y +-6..9: 1 clear of the moving arm's +-5
CH_X0, CH_X1 = -16.0, 14.0                       # cheeks x -16..14: the upper blade's back corner turns to x 15.4 at the swing's end (asserted)
CH_Z0, CH_Z1 = -10.0, 20.0                       # cheeks z -10..20: they carry the pin and join the lower neck to the upper handle
BL_X0, BL_X1, BL_W = 20.0, 50.0, 80.0            # blades x 20..50 (the bite 30), 80 wide (y +-40): class value Width
FACE = 0.5                                       # the blades' gripping faces at z -0.5 and 0.5: 1 apart at rest
NK_X0 = CH_X1                                    # the fixed neck x 14..20, face to face with the cheeks, clear of the boss's sweep (asserted)
BOSS_X, BOSS_Z0, BOSS_Z1 = 7.0, -24.0, FACE + T  # the moving arm's boss x -7..7, z -24..8.5 (joins its neck above and its handle below)
HND_X0 = -200.0                                  # both handles end at x -200: overall length 250 (class value Length)
FH_Z0, MH_Z1 = 16.0, -16.0                       # the fixed (upper) handle bar z 16..24; the moving (lower) handle bar z -24..-16
GR_X1, GR_PAD = -88.0, 2.0                       # plastic grips x -200..-88 (112 long), 2 proud of their bar all round: 28 apart at rest
BAR_X0 = GR_X1 - 2.0                             # each steel handle bar from x -90, its end 2 inside its grip (the grip is the handle's end)
SWING = 22.0                                     # the moving arm turns 22 degrees: the blades' tips then 19.7 apart (class value)
ZINC, STEEL, GRIP = "M-ZINC", "M-SILVER", "M-ORANGE-PA"


def _turn(x, z, deg):                            # a point of the moving arm turned about (0, -1, 0): +x turns to +z
    a = math.radians(deg)
    return x * math.cos(a) - z * math.sin(a), x * math.sin(a) + z * math.cos(a)


SPREAD = _turn(BL_X1, FACE, SWING)[1] + FACE     # 19.69: the upper blade's tip over the lower blade's face at the end of the swing
NECK_IN_ARM = _turn(NK_X0, -FACE - T, -SWING)    # (9.80, -13.1): the fixed neck's lower inner corner seen from the turned arm
assert abs(SPREAD - 19.69) < 0.01
BLADE_BACK = _turn(BL_X0, FACE + T, SWING)       # (15.36, 15.4): the upper blade's back top corner at the end of the swing
assert BLADE_BACK[0] > CH_X1 + 1.0               # 1.36 clear of the cheeks' front faces (validate MOT-010 found 1.0's x 16 hit at 21.4 degrees)
assert NECK_IN_ARM[0] > BOSS_X + 2.5             # the boss's +x face stays 2.8 clear of the fixed neck through the whole swing
assert math.hypot(BOSS_X, BOSS_Z1) < NK_X0       # the boss's upper corners (radius 11.0) never reach the fixed neck
assert BOSS_BORE_R - PIN_R == 1.0 and CH_Y0 - MW / 2 == 1.0     # the node 1 clear of the pin and the cheeks
assert FH_Z0 < CH_Z1 < FH_Z0 + T and CH_Z0 < -FACE - T          # the cheeks reach into the upper handle bar and below the lower neck
assert BOSS_Z0 == MH_Z1 - T                                      # the boss's foot carries the lower handle bar


def build():
    P = Prims()
    # ---- fixed arm: lower blade, neck, cheeks bored for the pin, the pin, upper handle bar and grip
    P.box(ZINC, BL_X0, -BL_W / 2, -FACE - T, BL_X1 - BL_X0, BL_W, T)                                   # lower blade 30 x 80 x 8, face z -0.5
    P.box(ZINC, NK_X0, -FW / 2, -FACE - T, BL_X0 - NK_X0, FW, T)                                       # neck x 14..20 on the blade
    for sy in (-1, 1):
        y0 = CH_Y0 if sy > 0 else -CH_Y1
        ch = P.box(ZINC, CH_X0, y0, CH_Z0, CH_X1 - CH_X0, CH_Y1 - CH_Y0, CH_Z1 - CH_Z0)               # cheek
        P.hole(ZINC, (0, y0 - 1, 0), (0, y0 + CH_Y1 - CH_Y0 + 1, 0), PIN_R, ch)                       # bored Ø8: the pin is pressed in
    P.cyl(STEEL, (0, -CH_Y1 - PIN_PROUD, 0), (0, CH_Y1 + PIN_PROUD, 0), PIN_R)                         # pin Ø8 x 19
    P.box(ZINC, BAR_X0, -FW / 2, FH_Z0, (CH_X0 + 3.0) - BAR_X0, FW, T)                                 # upper handle bar x -90..-13 into the cheeks
    P.box(GRIP, HND_X0, -FW / 2 - GR_PAD, FH_Z0 - GR_PAD, GR_X1 - HND_X0, FW + 2 * GR_PAD, T + 2 * GR_PAD)   # grip 112 x 22 x 12
    P.collider("lower-blade", NK_X0, -BL_W / 2, -FACE - T, BL_X1 - NK_X0, BL_W, T)
    P.collider("upper-handle", HND_X0, -FW / 2 - GR_PAD, FH_Z0 - GR_PAD, (CH_X0 + 3.0) - HND_X0, FW + 2 * GR_PAD, T + 2 * GR_PAD)
    # ---- moving arm (node jaw): boss bored 1 clear round the pin, neck and upper blade, lower handle bar and grip
    J = lambda m: f"node:jaw|{m}"
    bs = P.box(J(ZINC), -BOSS_X, -MW / 2, BOSS_Z0, 2 * BOSS_X, MW, BOSS_Z1 - BOSS_Z0)                  # boss x -7..7, z -24..8.5
    P.hole(J(ZINC), (0, -MW / 2 - 1, 0), (0, MW / 2 + 1, 0), BOSS_BORE_R, bs)                         # bored Ø10
    P.box(J(ZINC), BOSS_X, -MW / 2, FACE, BL_X0 - BOSS_X, MW, T)                                       # neck x 7..20 on the blade
    P.box(J(ZINC), BL_X0, -BL_W / 2, FACE, BL_X1 - BL_X0, BL_W, T)                                     # upper blade 30 x 80 x 8, face z 0.5
    P.box(J(ZINC), BAR_X0, -MW / 2, MH_Z1 - T, -BOSS_X - BAR_X0, MW, T)                                # lower handle bar x -90..-7
    P.box(J(GRIP), HND_X0, -MW / 2 - GR_PAD, MH_Z1 - T - GR_PAD, GR_X1 - HND_X0, MW + 2 * GR_PAD, T + 2 * GR_PAD)   # grip 112 x 14 x 12
    P.pivot("jaw", "rotate", (0, 0, 0), axis=(0, -1, 0), range=(0, SWING), unit="deg")                 # the blades open: +x turns up, the lower handle down
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
