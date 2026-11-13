#!/usr/bin/env python3
"""bracket-angle-strut-41: generic 90-degree angle bracket for the 41 x 41 strut channel, our own vendor-neutral design of the ETIM 10.0
class EC000482 (Fastening element for mounting rail/-profile; synonyms base plate, ceiling bracket, clamp piece, floor console, floor
plate, mounting angle bracket), built unattended (OPERATING.md 12, generic elements; group EG021005 Mounting systems, a tier-2 class,
after console-strut-41, lib/rounds/mech/r152.md). A zinc-plated steel angle, two legs 41 wide and 8 thick at 90 degrees, 90 long from
the outside corner, each with one M12 clearance hole (ISO 273 medium) 50 out from the corner on the leg's centre line: one leg seats on
one channel's open side (the lips' face) or back, the other on a second channel or a frame square to it, one M12 through each hole into
the channel's slot or its channel nut. The leg is as wide as the channel, so its edges lie flush with the channel's walls. The channel
is placed, never redrawn: its figures are read from strut with library.load. The class's features are not on file
(lib/standards/etim/class-features.csv has no EC000482 rows): spec.md gives the design values under plain names, as console-strut-41
does. Every size is a design choice. No load, slip or pull-out claim. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "bracket-angle-strut-41", "1.0", "plate"
TITLE = ("90-degree angle bracket for a 41 x 41 strut channel, generic, zinc-plated steel, two legs 90 x 41 x 8, "
         "one M12 clearance hole in each")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic fastening element for mounting rail/-profile (ETIM 10.0 EC000482), a 90-degree angle bracket "
            "for strut 1.0 (41 x 41 x 2.5): two legs as wide as the channel, each with one M12 clearance hole (ISO 273 medium) on its "
            "centre line, the channel's figures read from strut (library.load); class features not on file, design values under "
            "plain names (spec.md); every size a design choice; no load, slip or pull-out claim; no vendor file opened")
ORIGIN = ("the outside corner: the horizontal leg's seat face z = 0 (it lies on a channel, running +x), the upright leg's seat face "
          "x = 0 (it stands against a second channel or frame, running +z), the bracket's centre plane y = 0")
COMMAND = "BRAS41"
PARAMS = dict()

ST = library.load("strut")                   # strut 1.0: the channel the bracket joins (one home for each figure)
W = ST.W                                     # 41: the channel's width; each leg is as wide (y +-20.5), flush with its walls
SLOT_W = ST.SLOT_W                           # 13.5: the channel's back slots (M12 clearance medium)
OPEN = ST.OPEN                               # 22: the opening between the channel's lips, where a channel nut's bolt passes
T = 8.0                                      # design: each leg's thickness (>= 8, over the gate's 3 to 7 mm free-corner trap)
L = 90.0                                     # design: each leg's length from the outside corner
HOLE_D = 13.5                                # M12 clearance, ISO 273 medium (H13), lib/standards/holes.csv
HC = 50.0                                    # design: each hole's centre, 50 out from the outside corner, on y = 0
IN = 0.5                                     # the upright runs 0.5 into the horizontal leg (one solid joint, strut's way)
MAT = "M-ZINC"                               # zinc-plated steel (strut's layer)

assert HOLE_D == SLOT_W and HOLE_D < OPEN                                           # the hole = the channel's slot width, inside its 22 opening
assert HC - HOLE_D / 2 - T >= 30.0                                                   # 35.25 from a hole's edge to the other leg's inner face (room for a bolt head)
assert L - HC - HOLE_D / 2 >= 30.0                                                   # 33.25 from a hole's edge to its leg's end
assert W / 2 - HOLE_D / 2 >= 13.0                                                    # 13.75 of metal beside each hole
assert min(T, L, W) >= 8.0                                                           # every free edge >= 8 (the gate's 3 to 7 mm trap)


def build():
    P = Prims()
    foot = P.box(MAT, 0, -W / 2, 0, L, W, T)                                                      # the horizontal leg, seat face z = 0
    P.hole(MAT, (HC, 0, -1), (HC, 0, T + 1), HOLE_D / 2, foot)                                     # M12 clearance, through it
    up = P.box(MAT, 0, -W / 2, T - IN, T, W, L - T + IN)                                           # the upright leg, seat face x = 0
    P.hole(MAT, (-1, 0, HC), (T + 1, 0, HC), HOLE_D / 2, up)                                       # M12 clearance, through it
    P.collider("leg-x", 0, -W / 2, 0, L, W, T)
    P.collider("leg-z", 0, -W / 2, T, T, W, L - T)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="behind", az=50, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
