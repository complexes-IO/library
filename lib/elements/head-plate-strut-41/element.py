#!/usr/bin/env python3
"""head-plate-strut-41: generic head plate for the 41 x 41 strut channel, our own vendor-neutral design of the ETIM 10.0 class EC001567
(Head plate for mounting rail/-profile; synonyms head plate for profile rail, head plate for support, floor plate, ceiling bracket),
built unattended (OPERATING.md 12, generic elements; group EG021005 Mounting systems, a tier-2 class, after cap-strut-41,
lib/rounds/mech/r150.md). A zinc-plated steel plate that stands strut 1.0 on a floor (or hangs it from a ceiling): a square plate
120 x 120 x 8 across the channel's end, with four M12 anchor holes outside the channel's outline, and a tab 75 x 41 x 8 welded square
to it under the channel's back. The tab carries a slot 13.5 wide along the run that lies under the channel's first back slot for every
length strut is cut to, so one M12 through both fixes the channel whatever its length. Every channel figure is read from strut with
library.load, so the plate and the channel cannot drift apart. The class's features are not on file (lib/standards/etim/class-features.csv
has no EC001567 rows): spec.md gives the design values under plain names, as cap-strut-41 does. Every size is a design choice. No load,
pull-out or fire claim. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "head-plate-strut-41", "1.0", "plate"
TITLE = ("head plate for a 41 x 41 strut channel, generic, zinc-plated steel, plate 120 x 120 x 8 with 4 x M12 anchor holes, tab "
         "75 x 41 x 8 under the channel's back with a 13.5 slot")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic head plate for mounting rail/-profile (ETIM 10.0 EC001567), a head plate for strut 1.0 (41 x 41 x 2.5): "
            "a square plate across the channel's end with four M12 anchor holes (ISO 273 medium) and a tab under the channel's back whose "
            "slot meets the channel's first back slot at any length, the channel's figures read from strut (library.load); class features "
            "not on file, design values under plain names (spec.md); every size a design choice; no load, pull-out or fire claim; no vendor "
            "file opened")
ORIGIN = ("strut's own frame at its run start: the channel's end face x = 0 (on the plate's face), the centre line y = 0, the back's "
          "outer face z = 0 (on the tab's top face); the channel runs +x from the plate, the plate's outer face (on the floor or ceiling) "
          "at x = -8")
COMMAND = "HPST41"
PARAMS = dict()

ST = library.load("strut")                   # strut 1.0: the channel the plate carries (one home for each figure)
W, H = ST.W, ST.H                            # 41 x 41: the channel's outline
SLOT_W, SLOT_L, PITCH = ST.SLOT_W, ST.SLOT_L, ST.SLOT_PITCH   # 13.5 x 28 slots at 50 in the channel's back
PT = 8.0                                     # design: the plate's thickness (>= 8, over the gate's 3 to 7 mm free-corner trap)
PS = 120.0                                   # design: the plate's side
ZC = H / 2                                   # 20.5: the plate centred on the channel's outline
HOLE_D = 13.5                                # M12 clearance, ISO 273 medium (H13), lib/standards/holes.csv
HOLE_P = 80.0                                # design: the anchor holes' square pitch (y and z), 20 from each edge
TT, TL = 8.0, 75.0                           # design: the tab's thickness (under the back, z -8 .. 0) and length along the run
TW = W                                       # the tab as wide as the channel (y +-20.5), flush with its walls
IN = 0.5                                     # the tab runs 0.5 into the plate (one solid joint, a weld, strut's way)
MAT = "M-ZINC"                               # zinc-plated steel (strut's layer)


def first_slot(length):
    """the x of strut 1.0's first back slot centre for a run of `length` (strut's build(): the slots centred on the length)"""
    rows = int((length - PITCH) // PITCH) + 1 if length >= PITCH else 0
    return (length - (rows - 1) * PITCH) / 2 if rows else None


X0S = [first_slot(L) for L in [50 + 0.5 * k for k in range(0, 2000)]]          # every length 50 to 1049.5, in 0.5 steps
X_LO, X_HI = min(X0S), max(X0S)                                                   # 25 .. 49.75: where the first slot's centre falls
TS_X0, TS_X1 = 18.0, 57.0                    # design: the tab's slot along x, 13.5 wide (y +-6.75), over every first-slot centre +- 6.75
TS_W = HOLE_D                                # the tab slot's width: M12 clearance medium, as the channel's back slot
assert abs(X_LO - 25.0) < 1e-9 and X_HI < 50.0, (X_LO, X_HI)                       # by hand: L - (rows - 1) * 50 lies in [50, 100), halved
assert TS_X0 <= X_LO - HOLE_D / 2 and TS_X1 >= 50.0 + HOLE_D / 2                  # an M12's clearance circle fits the tab slot at any first slot
assert TS_W == SLOT_W and TL - TS_X1 >= 8.0                                       # the two slots the same width; 18 of tab beyond the slot
yh = HOLE_P / 2
assert yh - HOLE_D / 2 > W / 2 + 12.0                                             # the anchor holes outside the channel's outline (33.25 > 20.5 + 12, room for a washer)
assert PS / 2 - yh == 20.0 and PS / 2 - yh - HOLE_D / 2 >= 13.0 and ZC - PS / 2 < -TT   # 20 from each hole's centre to the edge (13.25 of metal); the plate covers the tab's underside
assert PT >= 8.0 and TT >= 8.0 and TW >= 8.0 and TL >= 8.0                         # every free edge >= 8 (the gate's 3 to 7 mm trap)


def build():
    P = Prims()
    plate = P.box(MAT, -PT, -PS / 2, ZC - PS / 2, PT, PS, PS)                                       # the plate across the channel's end
    for y in (-yh, yh):
        for z in (ZC - yh, ZC + yh):
            P.hole(MAT, (-PT - 1, y, z), (1, y, z), HOLE_D / 2, plate)                              # M12 anchor hole, through the plate
    tab = P.box(MAT, -IN, -TW / 2, -TT, TL + IN, TW, TT)                                            # the tab under the channel's back, welded
    P.cutbox(MAT, TS_X0, -TS_W / 2, -TT - 1, TS_X1 - TS_X0, TS_W, TT + 2, tab)                       # its slot, through
    P.collider("plate", -PT, -PS / 2, ZC - PS / 2, PT, PS, PS)
    P.collider("tab", 0, -TW / 2, -TT, TL, TW, TT)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="behind", az=50, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
