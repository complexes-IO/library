#!/usr/bin/env python3
"""rack-sheet-vertical: a vertical sheet storage rack, our own design (OPERATING.md 12, own designs; inventory row own_design
"yes": "vertical sheet storage rack"; lib/machines-factory.txt line 122, storage-steel, lists it beside rack-cantilever and
rack-bar). Sheets stand on edge on a base plate in eight slots between nine upright dividers, each divider a frame of a front
post, a back post, a middle bar and a top bar; two back rails tie the dividers along x. A sheet goes in from the front or from
above and leans on a divider. One fixed body, no node, no hole: the rack's fixing to the floor is the assembly's (anchor-bolt).
Every size is a design choice. No load rating, no sheet format claim, no safety claim. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "rack-sheet-vertical", "1.1", "furniture"
TITLE = "vertical sheet rack 1600 x 1200 x 1500, base plate 20, nine upright dividers, eight slots 155 wide, sheets stood on edge"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; every size a design choice; no load rating, "
            "no sheet format claim, no safety claim; no vendor file opened")
ORIGIN = ("floor plane z = 0 at the centre of the rack's footprint x = 0, y = 0; the front (the side a sheet goes in from) "
          "toward -y; the slots follow one another along x, each sheet's face in a y-z plane")
COMMAND = "SHEETRACK"
PARAMS = dict()
W, D = 1600.0, 1200.0                             # footprint 1600 (x) by 1200 (y): design choice
BASE_T = 20.0                                     # base plate 20 thick (z 0..20); 20, not 10: a 10 edge between two free
                                                  # corners read 89 % at the fillet gate (rack-bar 1.0's first run)
BAR = 40.0                                        # every post, bar and rail 40 x 40: design choice
TOP = 1500.0                                      # dividers' top, 1500 above the floor: design choice
SLOTS = 8                                         # eight slots, nine dividers: design choice
MID_Z = 720.0                                     # middle bar's underside, z 720..760: design choice
LOW_Z = 240.0                                     # lower back rail's underside, z 240..280: design choice

def dividers():
    """x of each divider's left face: nine dividers 40 thick, the outer two flush with the base plate's ends."""
    clear = (W - (SLOTS + 1) * BAR) / SLOTS                                                 # 155 clear between dividers
    return [-W / 2 + i * (clear + BAR) for i in range(SLOTS + 1)], clear

def build():
    P = Prims(); S = "M-STEEL-7035"
    xs, clear = dividers()
    yf, yb = -D / 2, D / 2 - 2 * BAR                                                        # front post y -600..-560, back post
                                                                                            # y 520..560; back rails y 560..600
    P.box(S, -W / 2, -D / 2, 0, W, D, BASE_T)                                               # base plate: the sheets stand on it
    for x in xs:
        P.box(S, x, yf, BASE_T, BAR, BAR, TOP - BASE_T)                                     # front post
        P.box(S, x, yb, BASE_T, BAR, BAR, TOP - BASE_T)                                     # back post
        P.box(S, x, yf + BAR, MID_Z, BAR, yb - yf - BAR, BAR)                               # middle bar, post to post
        P.box(S, x, yf + BAR, TOP - BAR, BAR, yb - yf - BAR, BAR)                           # top bar, post to post
    for z in (LOW_Z, TOP - BAR):
        P.box(S, -W / 2, yb + BAR, z, W, BAR, BAR)                                          # back rail, behind the back posts
    P.collider("base", -W / 2, -D / 2, 0, W, D, BASE_T)
    for i, x in enumerate(xs, 1):
        P.collider(f"divider-{i}", x, yf, BASE_T, BAR, yb + BAR - yf, TOP - BASE_T)        # the divider's plane a sheet leans on
    P.collider("rail-low", -W / 2, yb + BAR, LOW_Z, W, BAR, BAR)
    P.collider("rail-top", -W / 2, yb + BAR, TOP - BAR, W, BAR, BAR)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="top", az=180, el=60)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
