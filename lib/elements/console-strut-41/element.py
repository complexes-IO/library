#!/usr/bin/env python3
"""console-strut-41: generic rail console for the 41 x 41 strut channel, our own vendor-neutral design of the ETIM 10.0 class EC010933
(Rail console; synonyms cantilever arm, clap console, industry support, rail console set, screw on angle, support for wall rail), built
unattended (OPERATING.md 12, generic elements; group EG021005 Mounting systems, a tier-2 class, after head-plate-strut-41,
lib/rounds/mech/r151.md). A zinc-plated steel cantilever arm on its own wall plate that carries strut 1.0 laid across its top: a plate
80 x 160 x 8 with two M12 anchor holes, above and below the arm, and an arm 300 long welded square to it, an inverted U 41 wide and 80
deep (a top 8 thick on two webs 8 thick, open below). The top carries a slot 13.5 wide along the arm, so one M12 through it and one of
the channel's back slots fixes the channel anywhere from 66.75 to 283.25 out from the wall; the nut goes in the 25 between the webs. The
channel is placed, never redrawn: its figures are read from strut with library.load. The class's features are not on file
(lib/standards/etim/class-features.csv has no EC010933 rows): spec.md gives the design values under plain names, as head-plate-strut-41
does. Every size is a design choice. No load, deflection or pull-out claim. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "console-strut-41", "1.1", "plate"
TITLE = ("rail console for a 41 x 41 strut channel, generic, zinc-plated steel, wall plate 80 x 160 x 8 with 2 x M12 anchor holes, "
         "arm 300 long, inverted U 41 x 80 with a 13.5 slot along its top")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic rail console (ETIM 10.0 EC010933), a cantilever arm for strut 1.0 (41 x 41 x 2.5) laid across its "
            "top: a wall plate with two M12 anchor holes (ISO 273 medium) and an inverted-U arm whose top slot takes one M12 through one "
            "of the channel's back slots, the channel's figures read from strut (library.load); class features not on file, design "
            "values under plain names (spec.md); every size a design choice; no load, deflection or pull-out claim; no vendor file opened")
ORIGIN = ("the wall face of the plate x = 0 (the arm runs +x from the wall), the arm's centre plane y = 0, the arm's top face z = 0 "
          "(the seat: the channel's back lies on it, the channel running along y)")
COMMAND = "CNST41"
PARAMS = dict()

ST = library.load("strut")                   # strut 1.0: the channel the console carries (one home for each figure)
W = ST.W                                     # 41: the channel's width, here along the arm (the channel crosses it)
SLOT_W = ST.SLOT_W                           # 13.5: the channel's back slots (M12 clearance medium)
PT = 8.0                                     # design: the wall plate's thickness (>= 8, over the gate's 3 to 7 mm free-corner trap)
PW = 80.0                                    # design: the wall plate's width (y +-40)
PZ0, PZ1 = -120.0, 40.0                      # design: the wall plate from z -120 to 40 (160 tall)
HOLE_D = 13.5                                # M12 clearance, ISO 273 medium (H13), lib/standards/holes.csv
HZ = (20.0, -100.0)                          # design: the two anchor holes on y = 0, one above the arm, one below it
AL = 300.0                                   # design: the arm's reach from the plate's face (x 8) to its end (x 308; 308 from the wall face)
AW = W                                       # the arm as wide as the channel (y +-20.5)
AD = 80.0                                    # design: the arm's depth, z -80 .. 0
TT = 8.0                                     # design: the top's thickness (z -8 .. 0)
WT = 8.0                                     # design: each web's thickness (y 12.5 .. 20.5 and its mirror)
GAP = AW - 2 * WT                            # 25: the clear between the webs, for the M12 nut under the top
IN = 0.5                                     # the arm runs 0.5 into the plate (one solid joint, a weld, strut's way)
TS_X0, TS_X1 = 60.0, 290.0                   # design: the top's slot along x, 13.5 wide (y +-6.75)
TS_W = SLOT_W                                # the slot's width: the channel's back slot width, M12 clearance medium
MAT = "M-ZINC"                               # zinc-plated steel (strut's layer)

AX1 = PT + AL                                # 308: the arm's end
assert TS_W == HOLE_D and TS_W / 2 < GAP / 2                                       # the slot within the gap between the webs
assert GAP == 25.0                                                                 # design: the clear for the M12's nut under the top (the nut is the host's, not drawn, not sized here)
assert TS_X0 + TS_W / 2 - W / 2 >= PT + 30.0                                       # the channel at its nearest (bolt at x 66.75) starts 46.25 out: clear of the anchor's head on the plate
assert AX1 - (TS_X1 - TS_W / 2 + W / 2) >= 0.0 and AX1 - TS_X1 >= 18.0             # at its farthest (bolt at x 283.25) the channel ends at 303.75, on the arm (308); 18 of top beyond the slot
assert HZ[0] - HOLE_D / 2 >= 12.0 and PZ1 - HZ[0] == 20.0                           # the upper hole 13.25 above the arm's top (room for a washer), 20 from the plate's top edge
assert -AD - (HZ[1] + HOLE_D / 2) >= 12.0 and HZ[1] - PZ0 == 20.0                   # the lower hole 13.25 below the webs, 20 from the plate's bottom edge
assert PW / 2 - HOLE_D / 2 >= 13.0 and PW > AW                                     # 33.25 of metal beside each hole; the plate wider than the arm
assert min(PT, TT, WT, AW, AD, PW) >= 8.0                                          # every free edge >= 8 (the gate's 3 to 7 mm trap)


def build():
    P = Prims()
    plate = P.box(MAT, 0, -PW / 2, PZ0, PT, PW, PZ1 - PZ0)                                         # the wall plate
    for z in HZ:
        P.hole(MAT, (-1, 0, z), (PT + 1, 0, z), HOLE_D / 2, plate)                                   # M12 anchor hole, through the plate
    arm = P.box(MAT, PT - IN, -AW / 2, -AD, AL + IN, AW, AD)                                        # the arm, welded to the plate
    P.cutbox(MAT, PT - IN - 1, -GAP / 2, -AD - 1, AL + IN + 2, GAP, AD - TT + 1, arm)               # open below: the inverted U
    P.cutbox(MAT, TS_X0, -TS_W / 2, -TT - 1, TS_X1 - TS_X0, TS_W, TT + 2, arm)                      # the top's slot, through
    P.collider("plate", 0, -PW / 2, PZ0, PT, PW, PZ1 - PZ0)
    P.collider("arm", PT, -AW / 2, -AD, AL, AW, AD)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="behind", az=50, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
