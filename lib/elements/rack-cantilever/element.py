#!/usr/bin/env python3
"""rack-cantilever: generic cantilever rack, our own vendor-neutral design of the ETIM 10.0 class EC004068 (Cantilever rack), built
unattended (OPERATING.md 12, generic elements; inventory row own_design "generic": "cantilever rack"). A single-sided rack for long
stock lying flat (bars, tubes, profiles; lib/machines-factory.txt lines 121 and 122, racks-storage and storage-steel): two columns
1500 apart, each on a floor base that runs forward under the arms, four arms 1000 long on each column, three horizontal ties
between the columns, and four anchor plates with one M12 clearance hole each (ISO 273 medium). One fixed body, no node. The class
values (spec.md, "Class values") are design inputs; every size below is a design choice. No load rating, no safety claim. No
vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "rack-cantilever", "1.0", "furniture"
TITLE = "cantilever rack, generic, single-sided, 2 columns 1500 apart, 4 arm levels 1000 long, 2400 high, 4 x M12 anchor holes"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic cantilever rack (ETIM 10.0 EC004068); class values are design inputs (spec.md); anchor holes "
            "ISO 273 medium for M12; every size a design choice; no load rating, no safety claim; no vendor file opened")
ORIGIN = ("floor plane z = 0, midway between the two columns x = 0, the columns' front faces (the faces the arms spring from) "
          "y = 0; the arms and the loading side toward -y, the columns' backs toward +y")
COMMAND = "RACKCANT"
PARAMS = dict()
COL_X = 750.0                                     # column centres x +-750 (1500 apart): class value (design input)
COL_W, COL_D = 120.0, 200.0                       # column section 120 (x) by 200 (y, 0..200): design choice
H = 2400.0                                        # columns' top above the floor: class value (design input)
BASE_L, BASE_H = 1300.0, 160.0                    # floor base under each column, y -1100..200, z 0..160, the column's width: design choice
ARM_W, ARM_L, ARM_H = 100.0, 1000.0, 100.0        # arms 100 wide, 1000 long (y -1000..0, the class value), 100 deep: design choice
ARM_TOPS = (700.0, 1200.0, 1700.0, 2200.0)        # the arms' top faces, four levels 500 apart: class value 4, heights a design choice
TIE, TIE_Y = 80.0, 60.0                           # ties 80 x 80 between the columns' inner faces, y 60..140: design choice
TIE_Z = (300.0, 1250.0, 2200.0)                   # the ties' undersides: design choice
PL_W, PL_L, PL_T = 80.0, 120.0, 20.0              # anchor plates 80 (x) by 120 (y), 20 thick, on each base's outer side: design choice
PL_Y = (120.0, -1020.0)                           # anchor hole centres along y, rear and front (1140 apart): design choice
M12_D = 13.5                                      # M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv)

def build():
    P = Prims(); S = "M-STEEL-7035"
    for sx, k in ((-1, "l"), (1, "r")):
        cx = sx * COL_X
        P.box(S, cx - COL_W / 2, -(BASE_L - COL_D), 0, COL_W, BASE_L, BASE_H)                # floor base, forward under the arms
        P.box(S, cx - COL_W / 2, 0, BASE_H, COL_W, COL_D, H - BASE_H)                        # column, on the base's rear end
        for top in ARM_TOPS:
            P.box(S, cx - ARM_W / 2, -ARM_L, top - ARM_H, ARM_W, ARM_L, ARM_H)               # arm, its back face on the column's front
        px = cx + COL_W / 2 if sx > 0 else cx - COL_W / 2 - PL_W                             # anchor plate, outside the base
        for y in PL_Y:
            pl = P.box(S, px, y - PL_L / 2, 0, PL_W, PL_L, PL_T)
            P.hole(S, (px + PL_W / 2, y, -1), (px + PL_W / 2, y, PL_T + 1), M12_D / 2, pl)   # M12 anchor hole
        P.collider(f"base-{k}", cx - COL_W / 2, -(BASE_L - COL_D), 0, COL_W, BASE_L, BASE_H)
        P.collider(f"column-{k}", cx - COL_W / 2, 0, BASE_H, COL_W, COL_D, H - BASE_H)
        for i, top in enumerate(ARM_TOPS, 1):
            P.collider(f"arm-{k}{i}", cx - ARM_W / 2, -ARM_L, top - ARM_H, ARM_W, ARM_L, ARM_H)
        for j, y in zip(("b", "f"), PL_Y):
            P.collider(f"anchor-{k}{j}", px, y - PL_L / 2, 0, PL_W, PL_L, PL_T)
    x0 = COL_X - COL_W / 2                                                                   # columns' inner faces: x +-690
    for i, z in enumerate(TIE_Z, 1):
        P.box(S, -x0, TIE_Y, z, 2 * x0, TIE, TIE)                                            # horizontal tie, column to column
        P.collider(f"tie-{i}", -x0, TIE_Y, z, 2 * x0, TIE, TIE)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
