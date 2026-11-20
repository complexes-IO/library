#!/usr/bin/env python3
"""door-partition-1000: generic single door for a storage partition (a grate partition wall, a storage cage), for posts 1000 apart,
our own vendor-neutral design of the ETIM 10.0 class EC004105 (Door for storage partition; synonyms single door, storage partition
door, storage partition single door), built unattended (OPERATING.md 12, generic elements; group EG010340 Storage and racking systems,
walked by name, lib/rounds/mech/r166.md). The third of the partition set: it bolts between two post-partition-2000 1.0 posts in place
of a panel-partition-1000 1.0 (foundation first: both are built and gated), and every figure it meets is read with library.load (the
post's tab heights, tab hole offset, tab faces, tab reach and panel gap; the panel's frame tube, wall, fixing stiles, top rail and floor
gap), so each has one home. The fixed body is a door frame of painted steel tube 20 x 20 x 2, the panel's: two stiles with three M8
clearance holes (ISO 273 medium) each on the posts' tab holes, joined at the top by a full-width head; no sill, so the opening is clear
from the floor. The leaf, node `door`, is a welded grate of the same tube (rails, stiles, a middle rail) with 17 vertical flat bars 2 x
20 at 50 pitch, 860 wide (x +-430, 5 inside the posts' tabs) and 1820 high (z 100 to 1920, 10 under the head); it turns 0 to 90
degrees toward +y (away from the tabs) about a vertical axis on the left stile's inner front edge (x -445, y 10), and its sweep stays
clear of the frame and of both posts' tabs at every angle (asserted below). Hinges, lock and screws are the host's assembly: none is
drawn. The class's features are not on file (lib/standards/etim/class-features.csv has no EC004105 rows): spec.md gives the design
values under plain names, as panel-partition-1000 does. Every size is a design choice. No load, impact, reach-through or safety claim:
a partition is no guard here (ISO 13857 distances are not claimed). No vendor file opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "door-partition-1000", "1.0", "furniture"
TITLE = ("single door for a storage partition, generic, for posts 1000 apart, painted steel tube frame 20 x 20 x 2 with six M8 "
         "fixing holes and a grate leaf 860 x 1820 of flat bars 2 x 20 at 50 pitch, opening 0 to 90 degrees")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic door for storage partition (ETIM 10.0 EC004105), a single hinged door for post-partition-2000 1.0 "
            "posts 1000 apart: a fixed frame of painted steel tube 20 x 20 x 2 (two stiles at x +-445 to 465 with three M8 clearance "
            "holes (ISO 273 medium) each at x +-455, z 250, 1050, 1850, the posts' tab holes, and a full-width head at z 1930 to 1950, "
            "no sill) on y -10 to 10 against the tabs' +y faces; a leaf (node door) of the same tube, 860 wide (x +-430) and 1820 high "
            "(z 100 to 1920), with a middle rail and 17 vertical flat bars 2 x 20 at 50 pitch, turning 0 to 90 degrees toward +y about "
            "the left stile's inner front edge (x -445, y 10); the post's and panel-partition-1000 1.0's figures read with "
            "library.load; class features not on file, design values under plain names (spec.md); every size a design choice; the "
            "posts, hinges, lock, screws, nuts and washers not drawn; no load, impact, reach-through or safety claim; no vendor file "
            "opened")
ORIGIN = ("the floor at the middle of the bay between two posts, panel-partition-1000's origin: z = 0 the floor (the posts' floor "
          "plates' undersides), x = 0 halfway between the posts' axes (x -500 and 500), y = 0 the partition's centre plane; the door "
          "runs along x and opens toward +y")
COMMAND = "DRPT1000"
PARAMS = dict()

POST_V, PANEL_V = "1.0", "1.0"
PO = library.load("post-partition-2000", POST_V)    # the post (its tabs: the fixing interface)
PN = library.load("panel-partition-1000", PANEL_V)  # the panel this door stands in for (its frame: one home for each figure)
PITCH = PN.PITCH                                # 1000: the posts' axes at x +-500
TB, T, IN = PN.TB, PN.T, PN.IN                  # 20, 2, 0.5: the frame tube's section and wall, each joint 0.5 into the part it meets
X1, XS = PN.X1, PN.XS                           # 465, 455: the frame's ends (10 clear of the posts' faces), the stiles' axes on the tab holes
Y0, Y1 = PN.Y0, PN.Y1                           # -10, 10: the frame against the tabs' +y faces, centred on the partition's line
Z0, Z1 = PN.Z0, PN.Z1                           # 100, 1950: the frame's bottom (the panel's floor gap) and its top
ZM = PN.ZM                                      # 1050: the leaf's middle rail, at the panel's
HOLE_D = PN.HOLE_D                              # 9: M8 clearance, ISO 273 medium (H13), lib/standards/holes.csv, the post's
BAR_T, BAR_P, BAR_N = PN.BAR_T, PN.BAR_P, PN.BAR_N   # 2, 50, 17: the panel's flat bars
BAR_X = PN.BAR_X                                # -400 .. 400
XI = X1 - TB                                    # 445: the fixed stiles' inner faces, the door's opening x +-445
TABX = PITCH / 2 - PO.UP / 2 - PO.TAB_R         # 435: the posts' tabs' inner ends (the tabs at x +-435 to 475, y -18 to -10)
LX = TABX - 5.0                                 # 430: design: the leaf's ends, 5 inside the tabs' ends (so the closed leaf never rubs a tab)
LZ0, LZ1 = Z0, Z1 - TB - 10.0                   # 100, 1920: design: the leaf at the frame's bottom, 10 under the head
HX, HY = -XI, Y1                                # (-445, 10): the hinge axis, the left stile's inner front edge (z vertical)
SWING = 90.0                                    # design: the leaf opens 0 to 90 degrees toward +y
CL = 2.0                                        # design: the least clear space the swept leaf keeps to the frame and the tabs
MAT = "M-STEEL-7035"                            # painted steel, the post's and panel's layer
LEAF = f"node:door|{MAT}"

assert PITCH == 1000.0 and X1 == 465.0 and XS == 455.0 and Y0 == -10.0 and Y1 == 10.0 and Z0 == 100.0 and Z1 == 1950.0
assert XI == 445.0 and TABX == 435.0 and LX == 430.0 and LZ1 == 1920.0 and ZM == 1050.0
assert PO.TAB_Y1 == Y0 and PO.TAB_Y0 < Y0                                                   # the tabs lie on the -y side of the frame
assert Z1 <= PO.H and Z0 > PO.FT                                                            # under the post's top, clear of its floor plate
assert Z0 + 20.0 < min(PO.TAB_Z) - PO.TAB_H / 2 and max(PO.TAB_Z) + PO.TAB_H / 2 < Z1 - TB   # every tab meets a fixed stile, under the head
assert TB / 2 - HOLE_D / 2 >= 5.0                                                           # 5.5 from a hole's edge to the stile's sides
assert XI + T <= XS - HOLE_D / 2 and XS + HOLE_D / 2 <= X1 - T                              # each hole inside the bore's x span: two y walls only
assert LX - TB - (BAR_X[-1] + BAR_T / 2) >= 8.0                                              # 9 clear at the leaf's stiles, 48 between bars
assert LZ0 + TB < ZM - TB / 2 and ZM + TB / 2 < LZ1 - TB                                     # the middle rail between the leaf's rails
# The swing. A leaf point at (dx, dy) from the hinge axis, dx = XI - LX .. XI + LX (15 .. 875), dy = -20 .. 0, turned by a in 0..90
# degrees: x' = dx cos a - dy sin a, y' = dx sin a + dy cos a (both linear in dx, dy: the leaf's section is a rectangle, so its four
# corners bound it). Asserted for every degree: (1) never past the hinge stile's inner face (x >= -445), and within 2 of that plane only
# at y >= 12, 2 in front of the stile; (2) never past y = -10, the tabs' +y faces, and within 2 of that plane only at |x| <= 433, 2 inside
# the tabs' ends; (3) the free edge never within 2 of the other stile's inner face (x <= 443); (4) under the head at every angle (the axis
# is vertical, so z never changes: z 1920 < 1930).
DX0, DX1 = XI - LX, XI + LX
assert DX0 == 15.0 and DX1 == 875.0
for k in range(0, int(SWING) + 1):
    a = math.radians(k)
    for dx in (DX0, DX1):
        for dy in (-TB, 0.0):
            x = HX + dx * math.cos(a) - dy * math.sin(a)
            y = HY + dx * math.sin(a) + dy * math.cos(a)
            assert x >= -XI - 1e-9 and y >= Y0 - 1e-9 and x <= XI - CL                        # (1), (2), (3) on the corners
    for i in range(0, int((DX1 - DX0) / 5.0) + 1):                                              # (1) and (2) along the leaf's faces, every 5
        dx = DX0 + 5.0 * i
        for dy in (-TB, 0.0):
            x = HX + dx * math.cos(a) - dy * math.sin(a)
            y = HY + dx * math.sin(a) + dy * math.cos(a)
            assert not (x < -XI + CL and y < Y1 + CL)                                           # clear of the hinge stile
            assert not (y < Y0 + CL and abs(x) > TABX - CL)                                     # clear of both posts' tabs
assert LZ1 + 10.0 == Z1 - TB                                                                  # (4)
# Every edge is 2 (a wall, a bar's thickness), 20 or more: none falls in the gate's 3 to 7 mm free-corner fillet trap.
assert min(TB, Z0) >= 8.0 and T <= 2.0 and BAR_T <= 2.0
# Volume by hand, the tube section 20² − 16² = 144. Fixed: two stiles from z 100 to 1930.5 (0.5 into the head) less three M8 holes
# through two walls each, the head 930 long. The leaf: two rails 860 long, two stiles 0.5 into each rail, a middle rail 821 long (0.5
# into each stile), 17 bars in two runs each 0.5 into the rails they meet. The joints' 0.5 overlaps are counted in both parts.
SEC = TB * TB - (TB - 2 * T) ** 2
F_STILE = SEC * (Z1 - TB + IN - Z0) - 3 * 2 * math.pi * (HOLE_D / 2) ** 2 * T
F_HEAD = SEC * 2 * X1
L_RAIL = SEC * 2 * LX
L_STILE = SEC * (LZ1 - LZ0 - 2 * TB + 2 * IN)
L_MID = SEC * (2 * (LX - TB) + 2 * IN)
L_BARS = BAR_N * BAR_T * TB * ((ZM - TB / 2 - (LZ0 + TB) + 2 * IN) + ((LZ1 - TB) - (ZM + TB / 2) + 2 * IN))
FIXED = 2 * F_STILE + F_HEAD
LEAFV = 2 * L_RAIL + 2 * L_STILE + L_MID + L_BARS
assert abs(F_STILE - 262828.6) < 0.1 and abs(F_HEAD - 133920.0) < 1e-6 and abs(FIXED - 659577.2) < 0.1
assert abs(L_RAIL - 123840.0) < 1e-6 and abs(L_STILE - 256464.0) < 1e-6 and abs(L_MID - 118224.0) < 1e-6
assert abs(L_BARS - 1198160.0) < 1e-6 and abs(LEAFV - 2076992.0) < 1e-6
VOL = FIXED + LEAFV
assert abs(VOL - 2736569.2) < 0.1


def build():
    P = Prims()
    for sx, c in ((-1, "frame-l"), (1, "frame-r")):                                             # the fixed stiles, 0.5 into the head
        x0 = -X1 if sx < 0 else XI
        s = P.box(MAT, x0, Y0, Z0, TB, TB, Z1 - TB + IN - Z0)
        P.cutbox(MAT, x0 + T, Y0 + T, Z0 - 1.0, TB - 2 * T, TB - 2 * T, Z1 - TB + IN - Z0 + 1.0, s)   # its bore, open below
        for z in PO.TAB_Z:
            P.hole(MAT, (sx * XS, Y0 - 1.0, z), (sx * XS, Y1 + 1.0, z), HOLE_D / 2, s)        # M8 clearance on the post's tab hole
        P.collider(c, x0, Y0, Z0, TB, TB, Z1 - TB - Z0)
    h = P.box(MAT, -X1, Y0, Z1 - TB, 2 * X1, TB, TB)                                           # the head, full width: one frame
    P.cutbox(MAT, -X1 - 1.0, Y0 + T, Z1 - TB + T, 2 * X1 + 2.0, TB - 2 * T, TB - 2 * T, h)     # its bore, open at both ends
    P.collider("head", -X1, Y0, Z1 - TB, 2 * X1, TB, TB)
    for z0 in (LZ0, LZ1 - TB):                                                                 # the leaf's rails, full width
        r = P.box(LEAF, -LX, Y0, z0, 2 * LX, TB, TB)
        P.cutbox(LEAF, -LX - 1.0, Y0 + T, z0 + T, 2 * LX + 2.0, TB - 2 * T, TB - 2 * T, r)
    for sx in (-1, 1):                                                                         # the leaf's stiles, 0.5 into each rail
        x0 = -LX if sx < 0 else LX - TB
        s = P.box(LEAF, x0, Y0, LZ0 + TB - IN, TB, TB, LZ1 - LZ0 - 2 * TB + 2 * IN)
        P.cutbox(LEAF, x0 + T, Y0 + T, LZ0 + TB - IN - 1.0, TB - 2 * T, TB - 2 * T, LZ1 - LZ0 - 2 * TB + 2 * IN + 2.0, s)
    m = P.box(LEAF, -(LX - TB) - IN, Y0, ZM - TB / 2, 2 * (LX - TB) + 2 * IN, TB, TB)          # the middle rail, 0.5 into each stile
    P.cutbox(LEAF, -(LX - TB) - IN - 1.0, Y0 + T, ZM - TB / 2 + T, 2 * (LX - TB) + 2 * IN + 2.0, TB - 2 * T, TB - 2 * T, m)
    for x in BAR_X:                                                                            # the flat bars, two runs, 0.5 into the rails
        P.box(LEAF, x - BAR_T / 2, Y0, LZ0 + TB - IN, BAR_T, TB, ZM - TB / 2 - (LZ0 + TB) + 2 * IN)
        P.box(LEAF, x - BAR_T / 2, Y0, ZM + TB / 2 - IN, BAR_T, TB, (LZ1 - TB) - (ZM + TB / 2) + 2 * IN)
    P.pivot("door", "rotate", (HX, HY, (LZ0 + LZ1) / 2), axis=(0, 0, 1), range=(0.0, SWING))   # about the left stile's inner front edge
    P.collider("leaf", -LX, Y0, LZ0, 2 * LX, TB, LZ1 - LZ0)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="behind", az=50, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
