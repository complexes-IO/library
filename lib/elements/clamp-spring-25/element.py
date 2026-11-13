#!/usr/bin/env python3
"""clamp-spring-25: generic spring clamp (the hand clamp a joiner squeezes open and lets close on an edge or a glued joint; a spring
round its pin holds the jaws shut), our own vendor-neutral design of the ETIM 10.0 class EC004294 (Spring clamp; its synonyms name
the edge clamp for gluing and the joint gluer), built unattended (OPERATING.md 12, generic elements; `python lib/build.py inventory
mech` lists the class once no inventory row builds unattended: group EG020054 Clamping tools, lib/needs-em/mech.md). Two zinc-plated
steel arms on one pin: the lower arm (fixed: jaw bar, handle bar and two cheeks bored for the pressed pin) and the upper arm (node
`jaw`: a boss bored 1 clear round the pin between the cheeks, its jaw bar and its handle bar), each jaw with a plastic pad. Squeezing
the handles turns the upper arm about the pin and opens the jaws. The spring round the pin is internal mechanism the twin doesn't
read: not drawn, not claimed. The class values (spec.md, "Class values") are design inputs; every size below is a design choice. No
clamping force is designed or claimed. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "clamp-spring-25", "1.1", "device"
TITLE = "spring clamp, generic, clamping range 25, overhang 54, two steel arms on a Ø8 pin, plastic pads 16 x 24"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic spring clamp (ETIM 10.0 EC004294), a hand spring clamp; class values are design inputs "
            "(spec.md); the spring round the pin not drawn or claimed; every size a design choice; no clamping force claimed; no "
            "vendor file opened")
ORIGIN = ("the pin's axis is the line x = 0, z = 0 along y; the clamp's centre plane y = 0; the jaws toward +x, the handles toward "
          "-x; the lower arm is fixed, the upper arm turns about the pin; the pads' clamping faces 1 apart at rest, either side of z = 0")
COMMAND = "CLAMPSPR"
PARAMS = dict()

PIN_R, PIN_PROUD = 4.0, 0.5                      # pin Ø8, pressed through the cheeks, its ends 0.5 proud of them
BOSS_BORE_R = 5.0                                # the upper arm's boss bored Ø10: 1 clear round the pin (features.csv, own)
BAR_T = 8.0                                      # every arm bar 8 thick (z): design choice
LW, UW = 18.0, 10.0                              # lower bars 18 wide (y +-9), the upper arm 10 wide (y +-5)
CH_Y0, CH_Y1 = 6.0, 9.0                          # the lower arm's cheeks 3.0 thick at y +-6..9: 1 clear of the upper arm's +-5
CH_X, CH_Z0, CH_Z1 = 14.0, -30.0, 6.0            # cheeks x -14..14, z -30..6 (they carry the pin and join both lower bars)
JAW_X0, JAW_X1 = 11.0, 70.0                      # the lower jaw bar x 11..70: 11 beyond the boss's swept corners (radius 9.9)
HND_X0 = -110.0                                  # both handle bars end at x -110
LJ_Z1, LH_Z1 = -3.5, -26.0                       # lower jaw bar's top z -3.5 (z -11.5..-3.5); lower handle bar's top z -26
UJ_Z0, UH_Z0 = 3.5, 26.0                         # upper jaw bar's underside z 3.5 (3.5..11.5); upper handle bar's underside z 26
BOSS_X, BOSS_Z0, BOSS_Z1 = 7.0, -7.0, 34.0       # the upper arm's boss x -7..7, z -7..34 (joins its two bars)
PAD_X0, PAD_X1, PAD_W, PAD_T = 52.0, 68.0, 24.0, 3.0   # pads 16 x 24 x 3.0, faces at z -0.5 and 0.5: 1 apart at rest
SWING = 24.0                                     # the upper arm turns 24 degrees: the handles' ends then 5 apart, the pads' centres 25.4
ZINC, STEEL, PAD = "M-ZINC", "M-SILVER", "M-ORANGE-PA"
OVERHANG = PAD_X1 - CH_X                         # 54: the class value Overhang length, the pads' tips back to the cheeks' front faces,
                                                 # where work wider than the 12 between the cheeks stops (review clamp-spring-25-1.0 finding 1)
assert OVERHANG == 54.0

assert (BOSS_X ** 2 + BOSS_Z0 ** 2) ** 0.5 + 1.0 < JAW_X0       # the boss's lower corners sweep clear of the lower jaw bar
assert LJ_Z1 + PAD_T == -0.5 and UJ_Z0 - PAD_T == 0.5           # the pads' faces 1 apart at rest
assert BOSS_BORE_R - PIN_R == 1.0 and CH_Y0 - UW / 2 == 1.0     # the node 1 clear of the pin and the cheeks


def build():
    P = Prims()
    # ---- lower arm (fixed): jaw bar, handle bar, two cheeks bored for the pin, the pin, the lower pad
    P.box(ZINC, JAW_X0, -LW / 2, LJ_Z1 - BAR_T, JAW_X1 - JAW_X0, LW, BAR_T)                           # jaw bar x 11..70
    P.box(ZINC, HND_X0, -LW / 2, LH_Z1 - BAR_T, -JAW_X0 - HND_X0, LW, BAR_T)                          # handle bar x -110..-11
    for sy in (-1, 1):
        y0 = CH_Y0 if sy > 0 else -CH_Y1
        ch = P.box(ZINC, -CH_X, y0, CH_Z0, 2 * CH_X, CH_Y1 - CH_Y0, CH_Z1 - CH_Z0)                    # cheek
        P.hole(ZINC, (0, y0 - 1, 0), (0, y0 + CH_Y1 - CH_Y0 + 1, 0), PIN_R, ch)                       # bored Ø8: the pin is pressed in
    P.cyl(STEEL, (0, -CH_Y1 - PIN_PROUD, 0), (0, CH_Y1 + PIN_PROUD, 0), PIN_R)                         # pin Ø8 x 19
    P.box(PAD, PAD_X0, -PAD_W / 2, LJ_Z1, PAD_X1 - PAD_X0, PAD_W, PAD_T)                               # lower pad
    P.collider("lower-jaw", JAW_X0, -LW / 2, LJ_Z1 - BAR_T, JAW_X1 - JAW_X0, LW, BAR_T + PAD_T)
    P.collider("lower-handle", HND_X0, -LW / 2, LH_Z1 - BAR_T, -JAW_X0 - HND_X0, LW, BAR_T)
    # ---- upper arm (node jaw): boss bored 1 clear round the pin, jaw bar, handle bar, the upper pad
    J = lambda m: f"node:jaw|{m}"
    bs = P.box(J(ZINC), -BOSS_X, -UW / 2, BOSS_Z0, 2 * BOSS_X, UW, BOSS_Z1 - BOSS_Z0)                  # boss x -7..7, z -7..34
    P.hole(J(ZINC), (0, -UW / 2 - 1, 0), (0, UW / 2 + 1, 0), BOSS_BORE_R, bs)                         # bored Ø10
    P.box(J(ZINC), BOSS_X, -UW / 2, UJ_Z0, JAW_X1 - BOSS_X, UW, BAR_T)                                 # jaw bar x 7..70
    P.box(J(ZINC), HND_X0, -UW / 2, UH_Z0, -BOSS_X - HND_X0, UW, BAR_T)                                # handle bar x -110..-7
    P.box(J(PAD), PAD_X0, -PAD_W / 2, UJ_Z0 - PAD_T, PAD_X1 - PAD_X0, PAD_W, PAD_T)                    # upper pad
    P.pivot("jaw", "rotate", (0, 0, 0), axis=(0, -1, 0), range=(0, SWING), unit="deg")                 # the jaws open: +x turns up
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
