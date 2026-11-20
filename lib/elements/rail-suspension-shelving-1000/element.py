#!/usr/bin/env python3
"""rail-suspension-shelving-1000: generic suspension rail for the back of a 1000 wide steel shelving bay, our own vendor-neutral design
of the ETIM 10.0 class EC004080 (Suspension rail (rack element); synonyms Suspension rail for stand rack, Wall rail), built unattended
(OPERATING.md 12, generic elements; group EG010340 Storage and racking systems, a tier-2 class walked by name after
shelf-pullout-shelving-1000, lib/rounds/mech/r160.md). It spans the bay between the inner faces of its two rear uprights, above one of
its shelves, so open-fronted bins hang on it by their rear hooks in front of the bay's back. The rail is one painted steel sheet 2.0
formed to a hook profile: a web 80 high in the plane of the bay's back, a channel 16 wide and 13 deep along its top front edge (its
floor 2.0, its front lip turned up), open on top, into which a bin's hook drops. Two end plates 3 x 40 x 80 close it and stand against
the rear uprights' inner faces: one fixed body. The rail's top stands 30 under the shelf above, so a hook lifts out over the lip. The
bay is placed, never redrawn: its width, depth, uprights and shelf heights are read from shelving-steel with library.load. The end
plates' fixing to the uprights is the host's assembly: none is drawn and no hole is modelled (shelving-steel's uprights carry none).
The class's features are not on file (lib/standards/etim/class-features.csv has no EC004080 rows): spec.md gives the design values
under plain names, as shelf-pullout-shelving-1000 does. Every size is a design choice. No load or safety claim. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "rail-suspension-shelving-1000", "1.0", "furniture"
TITLE = ("suspension rail for the back of a 1000 wide steel shelving bay, generic, painted steel sheet 2.0, a hook profile 20 x 80 "
         "between two end plates on the rear uprights")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic suspension rail (ETIM 10.0 EC004080), a painted steel sheet 2.0 formed to a hook profile 20 x 80 "
            "(a web in the plane of the bay's back and an open channel 16 wide along its top front edge for bins' rear hooks) between "
            "two end plates 3 x 40 x 80 on the inner faces of the rear uprights of shelving-steel 1.0 (bay 1000 x 500 x 2000, uprights "
            "50 x 50, shelves 40 deep, 450 apart), its top 30 under the shelf above; the bay's figures read from shelving-steel "
            "(library.load); class features not on file, design values under plain names (spec.md); every size a design choice; fixing "
            "not drawn; no load or safety claim; no vendor file opened")
ORIGIN = ("shelving-steel's own x and y, so the host places the rail at the bay's origin raised to a shelf's top face: the top face of "
          "the shelf below the rail z = 0, the middle of the bay's width x = 0, the front uprights' front faces y = 0; the bay's depth "
          "toward +y, its back at y = 500; the bins hang on the rail's front, toward -y")
COMMAND = "RSUS1000"
PARAMS = dict()

SS = library.load("shelving-steel")          # shelving-steel 1.0: the bay whose rear uprights carry the rail (one home for each figure)
W, D, UP, SH_T = SS.W, SS.D, SS.UP, SS.SH_T  # 1000, 500, 50, 40: the bay's width and depth, the uprights' section, the shelves' depth
XI = W / 2 - UP                              # 450: the uprights' inner faces x +-450
YB0, YB1 = D - UP, D                         # 450 to 500: the rear uprights' depth band
CLEAR_UP = min(b - a for a, b in zip(SS.SH_TOPS, SS.SH_TOPS[1:])) - SH_T   # 410: the clear height between a shelf and the one above
EP_T, EP_W = 3.0, 40.0                       # design: end plates 3 thick (x), 40 wide (y)
EP_Y0 = YB0 + 5.0                            # design: the end plates y 455 to 495, 5 inside the rear uprights' front and back faces
XE = XI - EP_T                               # 447: the end plates' inner faces x +-447 (the rail's ends)
T = 2.0                                      # design: the rail's sheet thickness (under 3: every section edge is thin to the fillet check)
H = 80.0                                     # design: the rail's height (the web), z Z0 to Z0 + 80
Z0 = 300.0                                   # design: the rail's bottom 300 above the shelf below, so its top stands at 380
RY1 = 490.0                                  # design: the web's back face y 490, 5 in front of the end plates' back edges
RY0 = RY1 - 20.0                             # 470: the profile's front, 20 deep over the lip
CH_Z = 60.0                                  # design: the channel's floor z 60 to 62 above the rail's bottom
LIP = 75.0                                   # design: the lip's top 75 above the rail's bottom, 13 above the channel's floor
MAT = "M-STEEL-7035"                         # painted steel, shelving-steel's layer

TOP = Z0 + H                                 # 380: the rail's top
assert abs(XI - 450.0) < 1e-9 and abs(YB0 - 450.0) < 1e-9 and abs(CLEAR_UP - 410.0) < 1e-9          # the bay's figures as read
assert YB0 < EP_Y0 and EP_Y0 + EP_W < YB1 and EP_Y0 <= RY0 and RY1 <= EP_Y0 + EP_W                  # plates on the uprights, rail on them
assert CLEAR_UP - TOP >= 2 * (LIP - CH_Z - T)                                                      # 30 >= 26: a hook lifts out over the lip
# The profile (y, z from the rail's bottom): web y 488 to 490, z 0 to 80; channel floor y 470 to 488, z 60 to 62; lip y 470 to 472,
# z 62 to 75. Every section edge is 2 (the sheet) or 13 and more; the end plates' edges 3, 40 and 80: none falls in the 3 to 7 trap.
SECTION = 20 * H - (RY1 - T - RY0 - T) * (H - CH_Z - T) - (RY1 - T - RY0) * CH_Z - T * (H - LIP)        # 1600 - 288 - 1080 - 10
assert abs(SECTION - (T * H + (RY1 - T - RY0) * T + T * (LIP - CH_Z - T))) < 1e-9 and abs(SECTION - 222.0) < 1e-9
assert min(RY1 - T - RY0, LIP - CH_Z - T, LIP - CH_Z, H - CH_Z - T, CH_Z) >= 8.0                    # section edges 18, 13, 15, 18, 60
# (the web's 5 above the lip's top is a gap across the channel, not an edge: the lip's top face is 2 wide, the web's front face 18 high)
RAIL = 2 * XE * SECTION                                                                             # 894 x 222 = 198468
PLATE = EP_T * EP_W * H                                                                             # 3 x 40 x 80 = 9600
assert abs(RAIL - 198468.0) < 1e-6 and abs(RAIL + 2 * PLATE - 217668.0) < 1e-6


def build():
    P = Prims()
    r = P.box(MAT, -XE, RY0, Z0, 2 * XE, RY1 - RY0, H)                                         # the profile's envelope, end plate to end plate
    P.cutbox(MAT, -XE - 1.0, RY0 + T, Z0 + CH_Z + T, 2 * XE + 2.0, RY1 - T - RY0 - T, H - CH_Z, r)   # the channel, open on top
    P.cutbox(MAT, -XE - 1.0, RY0 - 1.0, Z0 - 1.0, 2 * XE + 2.0, RY1 - T - RY0 + 1.0, CH_Z + 1.0, r)  # in front of the web, under the floor
    P.cutbox(MAT, -XE - 1.0, RY0 - 1.0, Z0 + LIP, 2 * XE + 2.0, T + 1.0, H - LIP + 1.0, r)          # above the lip
    P.collider("hook-rail", -XE, RY0, Z0, 2 * XE, RY1 - RY0, H)
    for sx, c in ((-1, "end-l"), (1, "end-r")):
        x0 = -XI if sx < 0 else XE
        P.box(MAT, x0, EP_Y0, Z0, EP_T, EP_W, H)                                                # end plate on the rear upright's inner face
        P.collider(c, x0, EP_Y0, Z0, EP_T, EP_W, H)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
