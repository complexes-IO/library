#!/usr/bin/env python3
"""bar-depth-support-1067: generic depth support bar for one beam level of pallet-rack, our own vendor-neutral design of the ETIM 10.0
class EC004078 (Depth support bar (rack element); synonyms rack front-to-rear support, rack push-through protection), built unattended
(OPERATING.md 12, generic elements; group EG010340 Storage and racking systems, a tier-2 class, after guard-upright-80,
lib/rounds/mech/r154.md). A zinc-plated steel bar laid front to rear across a level's front and back beams: an inverted U 40 wide and
30 high (a top 8 thick on two webs 8 thick, open below), its webs bearing on the beams' tops, and at each end a lip 8 thick hanging 60
down outside the beam's outer face, 2 clear of it, so the bar cannot slide off front or back. The beams are placed, never redrawn: the
frame depth and the beam section are read from pallet-rack with library.load. Where along the beams the bar sits is the host's
assembly. The class's features are not on file (lib/standards/etim/class-features.csv has no EC004078 rows): spec.md gives the design
values under plain names, as guard-upright-80 does. Every size is a design choice. No load, deflection or push-through claim; no
safety claim. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "bar-depth-support-1067", "1.0", "furniture"
TITLE = ("depth support bar for a 1067 deep pallet rack frame, generic, zinc-plated steel, inverted U 40 x 30, "
         "end lips hooking over the front and back beams")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic depth support bar (ETIM 10.0 EC004078), laid front to rear across one beam level of "
            "pallet-rack 1.1 (frame depth 1067, beams 50 deep x 120 high): an inverted-U bar 40 x 30 whose webs bear on the beams' "
            "tops and whose end lips hang 60 down outside the beams' outer faces, 2 clear, the rack's figures read from pallet-rack "
            "(library.load); class features not on file, design values under plain names (spec.md); every size a design choice; no "
            "load, deflection, push-through or safety claim; no vendor file opened")
ORIGIN = ("the front beam's outer face y = 0, the beams' top face z = 0 (the bar's webs bear on it), the bar's centre plane x = 0; "
          "the bar runs +y from the aisle toward the back beam; the host places it anywhere along the beams")
COMMAND = "BDS1067"
PARAMS = dict()

PR = library.load("pallet-rack")             # pallet-rack 1.1: the rack whose beams carry the bar (one home for each figure)
DEPTH = PR.DEPTH                             # 1067: the frame's depth, the front beam's outer face to the back beam's outer face
BEAM_D, BEAM_H = PR.BEAM_D, PR.BEAM_H        # 50 x 120: the beams' section (depth along y, height)
W = 40.0                                     # design: the bar's width (x +-20)
H = 30.0                                     # design: the bar's height above the beams' tops (z 0 .. 30)
TT = 8.0                                     # design: the top's thickness (z 22 .. 30)
WT = 8.0                                     # design: each web's thickness (x 12 .. 20 and its mirror); the webs bear on the beams
GAP = W - 2 * WT                             # 24: the clear between the webs
CL = 2.0                                     # design: the lips' clear space to the beams' outer faces
LT = 8.0                                     # design: the lips' thickness along y
LD = 60.0                                    # design: how far each lip hangs below the beams' tops
IN = 0.5                                     # the bar runs 0.5 into each lip (one solid joint, a weld, guard-upright-80's way)
MAT = "M-ZINC"                               # zinc-plated steel (strut's layer)

Y0, Y1 = -CL, DEPTH + CL                     # -2 .. 1069: the bar between the lips' inner faces
BL = Y1 - Y0 + 2 * IN                        # 1072: the bar's drawn length, 0.5 into each lip
assert GAP == 24.0 and WT <= GAP                                                    # two webs and a clear between them
assert LD < BEAM_H and LD >= 8.0                                                    # the lips end 60 down the beams' 120 face, above their underside
assert CL > 0.0                                                                     # the lips never touch the beams: the bar is laid on, not forced
assert DEPTH - 2 * BEAM_D > 0.0                                                     # 967 clear between the beams' inner faces: the bar spans it
assert min(W, H, TT, WT, LT, LD, GAP) >= 8.0                                        # every free edge >= 8 (the gate's 3 to 7 mm trap)
VOL_BAR = (W * H - GAP * (H - TT)) * BL                                             # 672 x 1072 = 720384
VOL_LIPS = 2 * W * LT * (LD + H)                                                    # 2 x 40 x 8 x 90 = 57600
VOL_OVER = 2 * (W * H - GAP * (H - TT)) * IN                                        # the joints' overlaps, 672
assert abs(VOL_BAR - 720384.0) < 1e-6 and abs(VOL_LIPS - 57600.0) < 1e-6 and abs(VOL_OVER - 672.0) < 1e-6


def build():
    P = Prims()
    bar = P.box(MAT, -W / 2, Y0 - IN, 0, W, BL, H)                                                 # the bar, y -2.5 .. 1069.5
    P.cutbox(MAT, -GAP / 2, Y0 - IN - 1, -1, GAP, BL + 2, H - TT + 1, bar)                         # open below: the inverted U
    P.box(MAT, -W / 2, Y0 - LT, -LD, W, LT, LD + H)                                                 # front lip, y -10 .. -2
    P.box(MAT, -W / 2, Y1, -LD, W, LT, LD + H)                                                      # back lip, y 1069 .. 1077
    P.collider("bar", -W / 2, Y0, 0, W, Y1 - Y0, H)
    P.collider("lip-front", -W / 2, Y0 - LT, -LD, W, LT, LD + H)
    P.collider("lip-back", -W / 2, Y1, -LD, W, LT, LD + H)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="end", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
