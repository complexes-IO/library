#!/usr/bin/env python3
"""clamp-bar-300: generic bar clamp (the F-style screw clamp a fitter or joiner sets across work to hold it while glue sets or while
it is drilled), our own vendor-neutral design of the ETIM 10.0 class EC002200 (Glue clamp; its synonyms name the bar clamp and the
screw clamp), built unattended (OPERATING.md 12, generic elements; `python lib/build.py inventory mech` lists the class once no
inventory row builds unattended: group EG020054 Clamping tools, lib/needs-em/mech.md). A steel bar with a fixed cast arm at its end;
a sliding cast arm (node `jaw`) runs along the bar in a channel 1 clear of it and carries the screw spindle, its pressure pad and its
wooden handle. The sliding arm's own lock on the bar (it tilts and grips) and the screw's own stroke are internal mechanism the twin
doesn't read: not drawn, not claimed; the node's travel is the clamp's whole chucking range. The class values (spec.md, "Class
values") are design inputs; every size below is a design choice. No clamping force is designed or claimed. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "clamp-bar-300", "1.1", "device"
TITLE = "bar clamp, generic, chucking range 1 to 300, overhang 90, bar 25 x 10 x 380, sliding arm with screw, pad Ø24 and wooden handle"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic glue clamp (ETIM 10.0 EC002200), an F-style bar clamp; class values are design inputs (spec.md); "
            "the sliding arm's lock and the screw's stroke not drawn or claimed; every size a design choice; no clamping force "
            "claimed; no vendor file opened")
ORIGIN = ("the fixed arm's clamping face x = 0; the bar's underside z = 0 (the bar runs along +x above it, the arms hang down to "
          "z -110); the clamp's centre plane y = 0; the screw's axis at z -90; the sliding arm opens toward +x")
COMMAND = "CLAMPBAR"
PARAMS = dict()

BAR_L, BAR_T, BAR_H = 380.0, 10.0, 25.0          # bar x 0..380, y -5..5, z 0..25: design choice
FA_T, FA_W = 20.0, 26.0                          # fixed arm x -20..0, y -13..13: design choice
ARM_Z0, ARM_Z1 = -110.0, 35.0                    # both arms z -110..35 (they reach 110 below the bar, 10 above it)
SA_T, SA_W = 25.0, 22.0                          # sliding arm 25 along x, y -11..11: design choice
CH = 1.0                                         # the sliding arm's channel 1 clear of the bar on every side: design choice
SCREW_Z = -90.0                                  # the screw's axis 90 below the bar's underside: the class value overhang length
GAP, TRAVEL = 1.0, 299.0                         # the pad 1 from the fixed jaw at rest; travel 299: opening 1..300 (class value)
PAD_R, PAD_T = 12.0, 10.0                        # pressure pad Ø24 x 10: design choice
SP_R, SP_L = 6.0, 30.0                           # spindle Ø12, 30 showing between the pad and the arm at rest: design choice
HD_R, HD_L = 12.0, 80.0                          # wooden handle Ø24 x 80 behind the sliding arm: design choice
CAST, STEEL, WOOD = "M-CAST-BLUE", "M-SILVER", "M-BROWN"

SA_X0 = GAP + PAD_T + SP_L                       # the sliding arm's front face, 41 at rest
SA_X1 = SA_X0 + SA_T                             # its back face, 66 at rest
assert BAR_L - (SA_X1 + TRAVEL) >= 10.0           # open, the bar still runs 15 beyond the sliding arm
assert SA_W / 2 - (BAR_T / 2 + CH) >= 5.0 and ARM_Z1 - (BAR_H + CH) >= 9.0   # the channel's side walls 5, its roof 9
assert SCREW_Z - PAD_R - ARM_Z0 >= 8.0 and FA_W / 2 > max(PAD_R, HD_R, SA_W / 2)   # the pad above the arms' feet; y extremes on the fixed arm
assert min(FA_T, FA_W, BAR_T, BAR_H, SA_T, SA_W) >= 8.0   # every box edge 8 or longer (the gate's fillet rule, device r 0.5)


def build():
    P = Prims()
    P.box(CAST, -FA_T, -FA_W / 2, ARM_Z0, FA_T, FA_W, ARM_Z1 - ARM_Z0)                                  # fixed arm (its +x face the jaw)
    P.box(STEEL, 0, -BAR_T / 2, 0, BAR_L, BAR_T, BAR_H)                                                 # bar
    J = lambda m: f"node:jaw|{m}"
    arm = P.box(J(CAST), SA_X0, -SA_W / 2, ARM_Z0, SA_T, SA_W, ARM_Z1 - ARM_Z0)                         # sliding arm
    P.cutbox(J(CAST), SA_X0 - 1.0, -BAR_T / 2 - CH, -CH, SA_T + 2.0, BAR_T + 2 * CH, BAR_H + 2 * CH, arm)    # its channel round the bar
    P.cyl(J(STEEL), (GAP, 0, SCREW_Z), (GAP + PAD_T, 0, SCREW_Z), PAD_R)                                 # pressure pad
    P.cyl(J(STEEL), (GAP + PAD_T, 0, SCREW_Z), (SA_X0, 0, SCREW_Z), SP_R)                                # spindle
    P.cyl(J(WOOD), (SA_X1, 0, SCREW_Z), (SA_X1 + HD_L, 0, SCREW_Z), HD_R)                                # handle
    P.pivot("jaw", "translate", (GAP, 0, SCREW_Z), axis=(1, 0, 0), range=(0, TRAVEL))
    P.collider("fixed-arm", -FA_T, -FA_W / 2, ARM_Z0, FA_T, FA_W, ARM_Z1 - ARM_Z0)
    P.collider("bar", 0, -BAR_T / 2, 0, BAR_L, BAR_T, BAR_H)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
