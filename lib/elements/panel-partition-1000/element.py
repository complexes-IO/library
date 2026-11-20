#!/usr/bin/env python3
"""panel-partition-1000: generic element for a storage partition (a grate panel of a partition wall or storage cage), for posts 1000
apart, our own vendor-neutral design of the ETIM 10.0 class EC004103 (Element for storage partition; synonyms grate partition,
storage partition element, storage partition system), built unattended (OPERATING.md 12, generic elements; group EG010340 Storage and
racking systems, walked by name, lib/rounds/mech/r165.md). The second of the partition set: it bolts between two post-partition-2000
1.0 posts (foundation first: the post is built and gated), and every figure it meets is read from that element with library.load (the
tabs' fixing heights, the tab hole's offset from the post's axis, the tabs' +y face, the panel gap), so each has one home. A welded
frame of painted steel tube 20 x 20 x 2 (two full-width rails, two stiles between them, a middle rail) filled with vertical flat bars
2 x 20 at 50 pitch, 930 wide and 1850 high (z 100 to 1950), on the partition's line y -10 to 10; each stile carries three M8
clearance holes (ISO 273 medium) on the post's tab holes. The post is not placed or redrawn: the partition is the host's assembly.
The class's features are not on file (lib/standards/etim/class-features.csv has no EC004103 rows): spec.md gives the design values under
plain names, as post-partition-2000 does. Every size is a design choice. No load, impact, reach-through or safety claim: a partition
is no guard here (ISO 13857 distances are not claimed). No vendor file opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "panel-partition-1000", "1.0", "furniture"
TITLE = ("element for a storage partition, generic, grate panel 930 x 1850 for posts 1000 apart, painted steel tube frame 20 x 20 x 2 "
         "with vertical flat bars 2 x 20 at 50 pitch, six M8 fixing holes")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic element for storage partition (ETIM 10.0 EC004103), a grate panel for post-partition-2000 1.0 "
            "posts 1000 apart: a welded frame of painted steel tube 20 x 20 x 2, 930 wide (x +-465, 10 clear of each post's face) and "
            "1850 high (z 100 to 1950), two full-width rails, two stiles between them and a middle rail at z 1050, filled with 17 "
            "vertical flat bars 2 x 20 at 50 pitch; each stile with three M8 clearance holes (ISO 273 medium) along y at x +-455, z "
            "250, 1050, 1850, the post's tab holes; the frame on y -10 to 10 against the tabs' +y faces; the post's figures read with "
            "library.load; class features not on file, design values under plain names (spec.md); every size a design choice; the "
            "posts, screws, nuts and washers not drawn; no load, impact, reach-through or safety claim; no vendor file opened")
ORIGIN = ("the floor at the middle of the bay between two posts: z = 0 the floor (the posts' floor plates' undersides), x = 0 halfway "
          "between the posts' axes (x -500 and 500), y = 0 the partition's centre plane; the panel runs along x")
COMMAND = "PPNL1000"
PARAMS = dict()

POST_V = "1.0"
PO = library.load("post-partition-2000", POST_V)  # the post (one home for each figure the panel meets)
PITCH = 1000.0                                  # design: the posts' axes 1000 apart (the panel's module, its id's size)
TB = 20.0                                       # design: the frame tube's section 20 x 20 (the post's interface: a frame tube 20 wide, 20 deep)
T = 2.0                                         # design: the tube's wall
IN = 0.5                                        # each joint runs 0.5 into the part it meets (one body, a weld; the post's way)
X1 = PITCH / 2 - PO.UP / 2 - PO.PANEL_GAP       # 465: the frame's end, 10 clear of the post's face
XS = PITCH / 2 - PO.TAB_HOLE_X                  # 455: the stiles' axes, on the post's tab holes
Y0, Y1 = PO.TAB_Y1, PO.TAB_Y1 + TB              # -10, 10: the frame against the tabs' +y faces, centred on the partition's line
Z0, Z1 = 100.0, 1950.0                          # design: the frame's bottom 100 above the floor, its top 50 under the post's top
ZM = PO.TAB_Z[1]                                # 1050: the middle rail's axis, at the middle fixing height
HOLE_D = PO.TAB_HOLE_D                          # 9: M8 clearance, ISO 273 medium (H13), lib/standards/holes.csv, the post's
BAR_T, BAR_P, BAR_N = 2.0, 50.0, 17             # design: vertical flat bars 2 thick (x) x 20 deep (y), 50 pitch, 17 of them
BAR_X = [BAR_P * (i - (BAR_N - 1) / 2) for i in range(BAR_N)]   # -400 .. 400
MAT = "M-STEEL-7035"                            # painted steel, the post's layer

assert abs(X1 - 465.0) < 1e-9 and abs(XS - 455.0) < 1e-9 and Y0 == -10.0 and Y1 == 10.0 and ZM == 1050.0
assert abs((X1 - TB / 2) - XS) < 1e-9                                                       # each stile centred on the post's tab hole
assert abs(Y0 + Y1) < 1e-9                                                                  # the panel centred on the partition's line
assert Z0 + TB < min(PO.TAB_Z) - PO.TAB_H / 2 and max(PO.TAB_Z) + PO.TAB_H / 2 < Z1 - TB      # every tab meets a stile, clear of the rails
assert Z1 <= PO.H and Z0 > PO.FT                                                            # under the post's top, clear of its floor plate
assert TB / 2 - HOLE_D / 2 >= 5.0                                                           # 5.5 from a hole's edge to the stile's sides
assert X1 - TB + T <= XS - HOLE_D / 2 and XS + HOLE_D / 2 <= X1 - T                         # each hole inside the bore's x span: it cuts the two y walls only (the middle rail ends at 445.5, clear of it)
assert (X1 - TB) - (BAR_X[-1] + BAR_T / 2) >= 40.0 and BAR_P - BAR_T == 48.0                # 44 clear at the stiles, 48 between bars
# Every edge is 2 (a wall, a bar's thickness), 20 or more: none falls in the gate's 3 to 7 mm free-corner fillet trap.
assert min(TB, Z0) >= 8.0 and T <= 2.0 and BAR_T <= 2.0
# Volume by hand: two rails 930 long, two stiles from 0.5 in the bottom rail to 0.5 in the top rail less three M8 holes through two
# walls each, a middle rail 891 long (0.5 into each stile), 17 bars in two runs each 0.5 into the rails they meet. Tube section 20² − 16².
SEC = TB * TB - (TB - 2 * T) ** 2
RAIL = SEC * 2 * X1
STILE = SEC * (Z1 - Z0 - 2 * TB + 2 * IN) - 3 * 2 * math.pi * (HOLE_D / 2) ** 2 * T
MID = SEC * (2 * (X1 - TB) + 2 * IN)
BARS = BAR_N * BAR_T * TB * ((ZM - TB / 2 - (Z0 + TB) + 2 * IN) + ((Z1 - TB) - (ZM + TB / 2) + 2 * IN))
VOL = 2 * RAIL + 2 * STILE + MID + BARS
assert abs(RAIL - 133920.0) < 1e-6 and abs(STILE - 260020.6) < 0.1 and abs(MID - 128304.0) < 1e-6 and abs(BARS - 1218560.0) < 1e-6
assert abs(VOL - 2134745.2) < 0.1


def build():
    P = Prims()
    for z0 in (Z0, Z1 - TB):                                                                   # the bottom and top rails, full width
        r = P.box(MAT, -X1, Y0, z0, 2 * X1, TB, TB)
        P.cutbox(MAT, -X1 - 1.0, Y0 + T, z0 + T, 2 * X1 + 2.0, TB - 2 * T, TB - 2 * T, r)       # its bore, open at both ends
    for sx in (-1, 1):                                                                         # the stiles, 0.5 into each rail
        x0 = sx * X1 if sx < 0 else X1 - TB
        s = P.box(MAT, x0, Y0, Z0 + TB - IN, TB, TB, Z1 - Z0 - 2 * TB + 2 * IN)
        P.cutbox(MAT, x0 + T, Y0 + T, Z0 + TB - IN - 1.0, TB - 2 * T, TB - 2 * T, Z1 - Z0 - 2 * TB + 2 * IN + 2.0, s)
        for z in PO.TAB_Z:
            P.hole(MAT, (sx * XS, Y0 - 1.0, z), (sx * XS, Y1 + 1.0, z), HOLE_D / 2, s)        # M8 clearance on the post's tab hole
    m = P.box(MAT, -(X1 - TB) - IN, Y0, ZM - TB / 2, 2 * (X1 - TB) + 2 * IN, TB, TB)           # the middle rail, 0.5 into each stile
    P.cutbox(MAT, -(X1 - TB) - IN - 1.0, Y0 + T, ZM - TB / 2 + T, 2 * (X1 - TB) + 2 * IN + 2.0, TB - 2 * T, TB - 2 * T, m)
    for x in BAR_X:                                                                            # the flat bars, two runs, 0.5 into the rails
        P.box(MAT, x - BAR_T / 2, Y0, Z0 + TB - IN, BAR_T, TB, ZM - TB / 2 - (Z0 + TB) + 2 * IN)
        P.box(MAT, x - BAR_T / 2, Y0, ZM + TB / 2 - IN, BAR_T, TB, (Z1 - TB) - (ZM + TB / 2) + 2 * IN)
    P.collider("grate", -X1, Y0, Z0, 2 * X1, TB, Z1 - Z0)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="behind", az=50, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
