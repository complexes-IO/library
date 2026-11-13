#!/usr/bin/env python3
"""door-shelving-1000: generic door pair for the open front of shelving-steel's bay, our own vendor-neutral design of the ETIM 10.0
class EC004077 (Door (rack element); synonyms rack door, extension door), built unattended (OPERATING.md 12, generic elements; group
EG010340 Storage and racking systems, a tier-2 class walked by name after box-assortment-340x240, lib/rounds/mech/r158.md). Two
jambs, painted steel bars 50 x 20, stand on the floor against the front uprights' front faces, floor to the uprights' tops, joined at
the top by a head 900 x 20 x 40 above the top shelf: the fixed body, one frame. Two leaves, each a painted steel sheet 1.5 folded to a shallow tray (a face 498 wide and 1980 high and a flange 20 deep on its
four edges, turned in toward the bay), hang 2 in front of the jambs with 4 between them. Each leaf turns 0 to 90 degrees outward about
its outer FRONT edge, where a concealed hinge's pivot lies: so at every angle the leaf stays within its bay's width (x -500 to 500),
never comes within 2 of the jambs, and the two leaves' swept spaces stay apart (asserted below), so a bay beside it can carry its own
doors. A finger notch 30 x 120 in each leaf's free edge is the grip. The bay is placed, never redrawn: its width, height and uprights
are read from shelving-steel with library.load. Hinges, lock and the jambs' fixing are the host's assembly: none is drawn and no hole
modelled. The class's features are not on file (lib/standards/etim/class-features.csv has no EC004077 rows): spec.md gives the design
values under plain names, as wall-side-shelving-500 does. Every size is a design choice. No load or safety claim. No vendor file
opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "door-shelving-1000", "1.0", "furniture"
TITLE = ("door pair for the open front of a 1000 wide steel shelving bay, generic, painted steel, two 498 x 1980 sheet leaves 1.5 "
         "on 50 x 20 jambs, each opening 0 to 90 degrees")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic rack door (ETIM 10.0 EC004077), a frame of two jambs 50 x 20 and a head on the front uprights' front faces of "
            "shelving-steel 1.0 (bay 1000 x 500 x 2000, uprights 50 x 50) and two folded sheet leaves 498 x 1980 x 20 in front of "
            "them, each turning 0 to 90 degrees outward about its outer front edge so it never leaves the bay's width; the bay's "
            "figures read from shelving-steel (library.load); class features not on file, design values under plain names "
            "(spec.md); every size a design choice; hinges, lock and fixing not drawn; no load or safety claim; no vendor file opened")
ORIGIN = ("shelving-steel's own origin, so the host places the doors at the bay's origin: the floor z = 0, the middle of the bay's "
          "width x = 0, the front uprights' front faces y = 0; the jambs and leaves in front of that plane, toward -y")
COMMAND = "DRSH1000"
PARAMS = dict()

SS = library.load("shelving-steel")          # shelving-steel 1.0: the bay whose front the doors close (one home for each figure)
W, H, UP = SS.W, SS.H, SS.UP                 # 1000, 2000, 50: the bay's width and height over its uprights, the uprights' section
XO = W / 2                                   # 500: the bay's outside planes x +-500 (the uprights' outer faces)
JD = 20.0                                    # design: the jambs' depth (y -20..0), 50 wide = the uprights' face (x 450..500)
HD = 40.0                                    # design: the head's height (z 1960..2000), between the jambs, above the top shelf (1950)
CL = 2.0                                     # design: the leaves' clear space to the jambs
T = 1.5                                      # design: leaf sheet thickness (under 3: every sheet edge is thin to the gate's fillet check)
F = 20.0                                     # design: the leaves' flange depth (the face included)
GAP = 4.0                                    # design: between the two leaves' free edges
Y1 = -JD - CL                                # -22: the leaves' back (their flanges' edges)
Y0 = Y1 - F                                  # -42: the leaves' front face
Z0, Z1 = 10.0, H - 10.0                      # design: leaves 10 above the floor and 10 below the uprights' tops
LW, LH = XO - GAP / 2, Z1 - Z0               # 498 x 1980 each leaf
SWING = 90.0                                 # design: each leaf opens 0 to 90 degrees outward
NW, NH, NZ = 30.0, 120.0, 1000.0             # design: the finger notch in each free edge, 30 deep, 120 high, centred at z 1000
MAT = "M-STEEL-7035"                         # painted steel, shelving-steel's layer

assert abs(LW - 498.0) < 1e-9 and abs(LH - 1980.0) < 1e-9 and abs(Y0 + 42.0) < 1e-9          # the bay's figures as read
# The swing, worked for the left leaf (the right one mirrors it). Hinge at (-XO, Y0); a leaf point at (dx, dy) from it, dx 0..LW,
# dy 0..F; turned by a in [-90, 0]: x' = dx cos a - dy sin a >= 0 (both terms >= 0), y' = dx sin a + dy cos a <= F.
for k in range(0, 91):
    a = -math.radians(k)
    for dx, dy in ((0, 0), (LW, 0), (0, F), (LW, F)):
        xp, yp = dx * math.cos(a) - dy * math.sin(a), dx * math.sin(a) + dy * math.cos(a)
        assert xp >= -1e-9                                                                      # never past the bay's outside plane
        assert Y0 + yp <= -JD - CL + 1e-9                                                       # never within 2 of the jambs (y >= -20)
assert math.hypot(LW, F) < XO + GAP / 2 - 3.0                                                   # 498.40 < 499: the free corner's sweep
                                                                                                # stays 3.6 short of the other leaf (x 2)
assert NW > F and NH >= 8.0 and Z0 + T < NZ - NH / 2 and NZ + NH / 2 < Z1 - T                   # the notch in the free edge, inside the height
assert T < 3.0 and min(F, JD, UP) >= 8.0                                                        # sheet edges thin, every other free edge >= 8
TRAY = LW * F * LH - (LW - 2 * T) * (F - T) * (LH - 2 * T)                                     # 19720800 - 495 x 18.5 x 1977 = 1616422.5
NOTCH = NH * (NW * T + T * (F - T))                                                             # 120 x (45 + 27.75) = 8730
assert abs(TRAY - 1616422.5) < 1e-6 and abs(NOTCH - 8730.0) < 1e-6
assert H - HD > max(SS.SH_TOPS) and HD >= 8.0                                                    # the head clears the top shelf (1950 < 1960)
HEAD = (W - 2 * UP) * JD * HD                                                                   # 900 x 20 x 40 = 720000
assert abs(2 * (TRAY - NOTCH) + 2 * UP * JD * H + HEAD - 7935385.0) < 1e-6                      # 2 x 1607692.5 + 2 x 2000000 + 720000


def build():
    P = Prims()
    for sx, c in ((-1, "jamb-l"), (1, "jamb-r")):
        x0 = -XO if sx < 0 else XO - UP
        P.box(MAT, x0, -JD, 0, UP, JD, H)                                                        # jamb on the upright's front face, floor to top
        P.collider(c, x0, -JD, 0, UP, JD, H)
    P.box(MAT, -XO + UP, -JD, H - HD, W - 2 * UP, JD, HD)                                       # head between the jambs: one frame
    P.collider("head", -XO + UP, -JD, H - HD, W - 2 * UP, JD, HD)
    for n, c, sx in (("door-l", "leaf-l", -1), ("door-r", "leaf-r", 1)):
        L = f"node:{n}|{MAT}"
        x0 = -XO if sx < 0 else GAP / 2
        lf = P.box(L, x0, Y0, Z0, LW, F, LH)                                                     # the leaf's envelope
        P.cutbox(L, x0 + T, Y0 + T, Z0 + T, LW - 2 * T, F, LH - 2 * T, lf)                       # open toward the bay: the tray
        nx = (-GAP / 2 - NW) if sx < 0 else (GAP / 2 - 1.0)
        P.cutbox(L, nx, Y0 - 1.0, NZ - NH / 2, NW + 1.0, F + 2.0, NH, lf)                        # finger notch in the free edge
        P.pivot(n, "rotate", (sx * XO, Y0, (Z0 + Z1) / 2), axis=(0, 0, 1), range=(0.0, sx * SWING))   # about the outer FRONT edge
        P.collider(c, x0, Y0, Z0, LW, F, LH)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=20), dict(name="behind", az=50, el=20)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
