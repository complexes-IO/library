#!/usr/bin/env python3
"""vise-bench: generic bench vice (the engineer's vice bolted to a workbench's top at its front edge), our own vendor-neutral design
of the ETIM 10.0 class EC002199 (Bench-vice), built unattended (OPERATING.md 12, generic elements; `python lib/build.py inventory
mech` lists the class once no inventory row builds unattended: group EG020054 Clamping tools, lib/needs-em/mech.md). Not the
machine vice of vise-manual / vise-machine (EC002173, low, bolted to a machine table): a tall cast body on a table foot with four
M10 holes (ISO 273 medium), the jaws standing above the bench in front of its edge, so long work hangs down past it. One moving
jaw (node `jaw`: jaw block, exchangeable jaw plate, the rectangular slide bar that runs back through a channel in the body, the
spindle's front end and its T-handle) travels along +x. The spindle inside the slide bar and its nut in the body are internal
mechanism, not drawn and not claimed. The bolts are the bench's: the holes are cut, nothing is placed in them. The class values
(spec.md, "Class values") are design inputs; every size below is a design choice. No clamping force is designed or claimed. No
vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "vise-bench", "1.1", "device"
TITLE = "bench vice, generic, jaws 125 x 50, opening 0 to 100, table foot 118 x 140 with 4 x M10 holes, slide bar 42 x 30"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic bench-vice (ETIM 10.0 EC002199); class values are design inputs (spec.md); table foot holes "
            "M10 to ISO 273 medium; the bolts are the bench's; the spindle and its nut not drawn or claimed; every size a design "
            "choice; no clamping force claimed; no vendor file opened")
ORIGIN = ("the table foot's underside (the seat on the bench top) z = 0; the fixed jaw plate's clamping face x = 0; the jaws' "
          "centre y = 0; the moving jaw opens toward +x, in front of the bench's edge; the jaws' top edges at z = 150")
COMMAND = "VISEBNCH"
PARAMS = dict()

FOOT_X0, FT, FW, FTH = -130.0, -12.0, 140.0, 15.0     # table foot x -130..-12, y -70..70, z 0..15: design choice
BX0, BW, BZ1 = -110.0, 80.0, 120.0                    # body x -110..-12, y -40..40, z 15..120: design choice
JAW_W, JAW_H, JAW_T, JAW_Z0 = 125.0, 50.0, 12.0, 100.0  # jaw plates 125 wide x 50 high (class values) x 12 thick, z 100..150
GAP, TRAVEL = 1.0, 99.0                               # the jaws 1 apart at rest (0); travel 99: opening 1..100 (class value 100)
MB_L, MB_Z0, MB_Z1 = 50.0, 60.0, 140.0                # moving jaw block 50 long (x 13..63 at rest), y -40..40, z 60..140
BAR_W, BAR_Z0, BAR_Z1, BAR_X0 = 42.0, 66.0, 96.0, -128.0  # slide bar 42 x 30 (y +-21, z 66..96), x -128..13 at rest
CH = 1.0                                              # the channel 1 clear of the bar each side: design choice
HOLE_X, HOLE_Y = (-118.0, -24.0), 55.0                # foot holes at x -118 / -24, y +-55 (outside the body): design choice
M10_D = 11.0                                          # M10 clearance, ISO 273 medium H13 (lib/standards/holes.csv)
SP_Z, SP_R, SP_X1 = 81.0, 10.0, 100.0                 # spindle front end Ø20 on the bar's axis z 81, from the block to x 100
HD_X, HD_R, HD_Y = 90.0, 7.0, 90.0                    # T-handle Ø14 along y at x 90, y -90..90: design choice
CAST, STEEL = "M-CAST-BLUE", "M-SILVER"

MB_X0 = GAP + JAW_T                                   # the moving block's back face, 13 at rest
assert FT - (BAR_X0 + TRAVEL) >= 16.0                  # open, the bar still runs 17 inside the body (x -29..-12 at the end)
assert BAR_X0 > FOOT_X0                                # closed, the bar's tail stays over the foot (inside the foot's x)
assert BAR_Z0 - CH - FTH >= 45.0 and BZ1 - (BAR_Z1 + CH) >= 20.0   # the channel's walls in the body
assert JAW_Z0 > BAR_Z1 + CH                            # the slide bar passes under the fixed jaw plate
assert HOLE_Y - M10_D / 2 > BW / 2 + 9.0              # the holes 9.5 clear of the body's sides (a bolt head's room)
assert FW / 2 - HOLE_Y >= M10_D and min(HOLE_X) - FOOT_X0 >= M10_D and FT - max(HOLE_X) >= M10_D   # 12 to 15 from the foot's edges


def build():
    P = Prims()
    foot = P.box(CAST, FOOT_X0, -FW / 2, 0, FT - FOOT_X0, FW, FTH)                                     # table foot
    for x in HOLE_X:
        for sy in (-1, 1):
            P.hole(CAST, (x, sy * HOLE_Y, -1), (x, sy * HOLE_Y, FTH + 1), M10_D / 2, foot)
    body = P.box(CAST, BX0, -BW / 2, FTH, FT - BX0, BW, BZ1 - FTH)                                     # body
    P.cutbox(CAST, BX0 - 1.0, -BAR_W / 2 - CH, BAR_Z0 - CH, FT - BX0 + 2.0, BAR_W + 2 * CH, BAR_Z1 - BAR_Z0 + 2 * CH, body)  # channel
    P.box(STEEL, FT, -JAW_W / 2, JAW_Z0, JAW_T, JAW_W, JAW_H)                                          # fixed jaw plate (x -12..0)
    J = lambda m: f"node:jaw|{m}"
    P.box(J(STEEL), GAP, -JAW_W / 2, JAW_Z0, JAW_T, JAW_W, JAW_H)                                      # moving jaw plate (x 1..13)
    P.box(J(CAST), MB_X0, -BW / 2, MB_Z0, MB_L, BW, MB_Z1 - MB_Z0)                                     # moving jaw block
    P.box(J(CAST), BAR_X0, -BAR_W / 2, BAR_Z0, MB_X0 - BAR_X0, BAR_W, BAR_Z1 - BAR_Z0)                  # slide bar
    P.cyl(J(STEEL), (MB_X0 + MB_L, 0, SP_Z), (SP_X1, 0, SP_Z), SP_R)                                   # spindle's front end
    P.cyl(J(STEEL), (HD_X, -HD_Y, SP_Z), (HD_X, HD_Y, SP_Z), HD_R)                                     # T-handle through it
    P.pivot("jaw", "translate", (GAP, 0, JAW_Z0), axis=(1, 0, 0), range=(0, TRAVEL))
    P.collider("foot", FOOT_X0, -FW / 2, 0, FT - FOOT_X0, FW, FTH)
    P.collider("body", BX0, -BW / 2, FTH, FT - BX0, BW, BZ1 - FTH)
    P.collider("fixed-jaw", FT, -JAW_W / 2, JAW_Z0, JAW_T, JAW_W, JAW_H)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
