#!/usr/bin/env python3
"""clamp-girder-200: generic beam clamp for workshop (girder clamp), our own vendor-neutral design of the ETIM 10.0 class EC004751
(Beam clamp for workshop; synonyms Beam clamp, Beam lifting clamp, Chain hoist flange clamp, Girder clamp, Scissor clamp), built
unattended (OPERATING.md 12, generic elements; group EG010320 Lifting equipment, a tier-2 class walked by name after group EG010340,
lib/rounds/mech/r171.md). It grips the bottom flange of an I-beam and gives a fixed point under it to hang a chain hoist from: two
painted steel C-jaws hook over the flange's edges, their lips bearing on the flange's top face; a bright-steel spindle runs across under
the flange through bores in both jaws' lower parts and through a load plate hanging midway between them, whose eye takes the hoist's hook
or shackle; a T-handle on the spindle's end turns it. The -y jaw is fixed on the spindle; the +y jaw (node `jaw`) is wound out along +y
to pass the flange's edge when the clamp is fitted, and back in to grip. The spindle's thread, its nut in the jaw, the load plate's
centring and the retention of the spindle are internal mechanism, not drawn (the spindle is drawn plain, no thread is claimed).
Sized to beam-runway 1.1's flange (200 x 20, read with library.load, fit asserted): a host clamps it where no trolley runs. No element
is placed or redrawn. The class's features are not on file (lib/standards/etim/class-features.csv has no EC004751 rows): spec.md gives
the design values under plain names, as ramp-loading-150 does. Every size is a design choice; no standard is claimed. No load
capacity, proof load or safety claim (a lifting attachment's working load limit is not stated). No vendor file opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "clamp-girder-200", "1.0", "furniture"
TITLE = ("beam clamp (girder clamp), generic, for a flange 200 x 20 (beam-runway 1.1's), two painted steel C-jaws 80 wide, the +y jaw "
         "wound out 0 to 40 on a spindle Ø20, load plate with a Ø30 eye 95 under the flange")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic beam clamp for workshop (ETIM 10.0 EC004751), two painted steel C-jaws 80 wide hooking over an "
            "I-beam's bottom flange 200 x 20 (beam-runway 1.1's, read with library.load, fit asserted), lips 24 over the flange's top, 8 "
            "clear of its edges; a plain bright-steel spindle Ø20 through Ø22 bores in both jaws and in a load plate 20 thick with a Ø30 "
            "eye; the +y jaw a translate node 0 to 40; class features not on file, design values under plain names (spec.md); every size "
            "a design choice; no thread, load capacity, proof load or safety claim; no vendor file opened")
ORIGIN = ("the flange's underside z = 0 on the beam's centre line y = 0, the clamp's middle x = 0 (beam-runway's frame: a host places it "
          "at the beam's own origin moved along x); the beam's length along x; the jaws' lips rest on the flange's top face z = 20")
COMMAND = "CLGIR200"
PARAMS = dict()

BEAM_V = "1.1"
BR = library.load("beam-runway", BEAM_V)        # the beam whose bottom flange it grips (the fit)
FW, FT = BR.FLG_W, BR.FLG_T                     # 200, 20: the flange's width and thickness
WEB = BR.WEB_T                                  # 20: the web the lips stay clear of

W = 80.0                                        # design: the jaws' and the load plate's width along the beam (x -40 to 40)
JT = 16.0                                       # design: the jaws' side walls and lips, 16 thick
SIDE = 8.0                                      # design: the side walls 8 clear of the flange's edges at rest
LIP = 24.0                                      # design: the lips reach 24 in over the flange's top from its edges
LOW_H = 36.0                                    # design: the jaws' lower parts 36 deep, the spindle in their middle
GAP_UNDER = 24.0                                # design: 24 clear between the flange's underside and the jaws' lower parts
TRAVEL = 40.0                                   # design: the +y jaw winds out 0 to 40 along +y
RS, RB = 10.0, 11.0                             # design: the spindle Ø20, the bores Ø22 (1 clear all round)
PT, PZ0, PZ1 = 20.0, -120.0, -20.0              # design: the load plate 20 thick (y -10 to 10), z -120 to -20
RE, ZE = 15.0, -95.0                            # design: the eye Ø30 across the plate (axis y) at z -95
RH, HY, HL = 6.0, 176.0, 80.0                   # design: the T-handle Ø12 along z at y 176, 80 long, centred on the spindle

YO = FW / 2 + SIDE + JT                         # 124: the jaws' outer faces at rest
YS = FW / 2 + SIDE                              # 108: the side walls' inner faces
YL = FW / 2 - LIP                               # 76: the lips' inner edges (and the jaws' inner faces)
ZT = FT + JT                                    # 36: the jaws' top faces (lips 16 thick on the flange's top z 20)
ZL1 = -GAP_UNDER                                # -24: the lower parts' top faces
ZL0 = ZL1 - LOW_H                               # -60: the jaws' undersides
ZS = (ZL0 + ZL1) / 2                            # -42: the spindle's axis
Y_END = HY + 8.0                                # 184: the spindle's +y end, 8 past the handle's axis
Y_BEG = -YO - 10.0                              # -134: the spindle's -y end, 10 past the fixed jaw's outer face
MAT, ST = "M-YELLOW", "M-SILVER"               # painted steel in beam-runway's yellow (no marking claim); the spindle bright steel

assert YL > WEB / 2 + 50                                                             # the lips stay 66 clear of the web
assert YL + TRAVEL > FW / 2 + 10                                                     # wound out, the +y lip clears the flange's edge by 16
assert HY - RH > YO + TRAVEL + 5                                                     # the handle (y 170 to 182) clears the jaw wound out (164)
assert Y_END > HY + RH                                                               # the spindle reaches through the handle
assert PZ1 <= -20 and PZ1 - (ZS + RB) >= 10                                         # the load plate 20 under the flange, 11 of wall over its bore
assert ZE - RE - PZ0 >= 10 and ZS - RB - (ZE + RE) >= 10                             # 10 of plate under the eye, 31 between eye and bore
assert ZS - RB - ZL0 >= 7 and ZL1 - (ZS + RB) >= 7                                   # 7 of wall round the jaws' bores
assert PT / 2 < YL                                                                   # the load plate between the jaws' inner faces
# Volume by hand (the yellow parts): a jaw 80 x 48 x 96 less its opening 80 x 32 x 44 less its bore Ø22 x 48; the load plate 80 x 20 x 100
# less its bore Ø22 x 20 and its eye Ø30 x 20.
JAW_V = W * (YO - YL) * (ZT - ZL0) - W * (YS - YL) * (FT - ZL1) - math.pi * RB ** 2 * (YO - YL)
PLATE_V = W * PT * (PZ1 - PZ0) - math.pi * RB ** 2 * PT - math.pi * RE ** 2 * PT
assert abs(JAW_V - 237753.6) < 0.1 and abs(PLATE_V - 138260.2) < 0.1


def build():
    P = Prims()
    J = lambda m: f"node:jaw|{m}"
    a = P.box(MAT, -W / 2, -YO, ZL0, W, YO - YL, ZT - ZL0)                                    # the fixed jaw (-y), a C open toward +y
    P.cutbox(MAT, -W / 2 - 1.0, -YS, ZL1, W + 2.0, YS - YL + 1.0, FT - ZL1, a)              # its opening: y -108 to -75, z -24 to 20
    P.hole(MAT, (0.0, -YO - 1.0, ZS), (0.0, -YL + 1.0, ZS), RB, a)                         # its bore
    b = P.box(J(MAT), -W / 2, YL, ZL0, W, YO - YL, ZT - ZL0)                                  # the moving jaw (+y), a C open toward -y
    P.cutbox(J(MAT), -W / 2 - 1.0, YL - 1.0, ZL1, W + 2.0, YS - YL + 1.0, FT - ZL1, b)       # its opening: y 75 to 108, z -24 to 20
    P.hole(J(MAT), (0.0, YL - 1.0, ZS), (0.0, YO + 1.0, ZS), RB, b)                          # its bore
    P.pivot("jaw", "translate", (0.0, YL, FT), axis=(0, 1, 0), range=(0, TRAVEL))
    p = P.box(MAT, -W / 2, -PT / 2, PZ0, W, PT, PZ1 - PZ0)                                    # the load plate, midway
    P.hole(MAT, (0.0, -PT / 2 - 1.0, ZS), (0.0, PT / 2 + 1.0, ZS), RB, p)                   # its bore for the spindle
    P.hole(MAT, (0.0, -PT / 2 - 1.0, ZE), (0.0, PT / 2 + 1.0, ZE), RE, p)                   # its eye for the hoist's hook
    P.cyl(ST, (0.0, Y_BEG, ZS), (0.0, Y_END, ZS), RS)                                         # the spindle, plain
    P.cyl(ST, (0.0, HY, ZS - HL / 2), (0.0, HY, ZS + HL / 2), RH)                             # the T-handle through its end
    P.collider("jaw-fixed", -W / 2, -YO, ZL0, W, YO - YL, ZT - ZL0)
    P.collider("load-plate", -W / 2, -PT / 2, PZ0, W, PT, PZ1 - PZ0)
    P.collider("spindle", -RS, Y_BEG, ZS - RS, 2 * RS, Y_END - Y_BEG, 2 * RS)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="end", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
