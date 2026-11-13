#!/usr/bin/env python3
"""shelf-pullout-shelving-1000: generic pull-out shelf for a shelf of shelving-steel's bay, our own vendor-neutral design of the ETIM 10.0
class EC004083 (Rack pull-out shelf), built unattended (OPERATING.md 12, generic elements; group EG010340 Storage and racking systems, a
tier-2 class walked by name after door-shelving-1000, lib/rounds/mech/r159.md). It stands on the top face of any of the bay's five
shelves, between the uprights. The fixed body: two slide rails, painted steel bars 12 x 45 along the bay's depth, each 1 inside its
uprights' inner faces, with a groove 6 deep and 25 high along its inner face, joined behind by a tie 874 x 20 x 10 under the grooves:
one frame. The moving part, node `tray`: a painted steel sheet 1.5 folded to an open tray 868 x 420 x 60, 5 above the shelf and 3 inside
the rails, with a runner 8 x 21 on each side that rides in its rail's groove (1 clear at the groove's bottom, 2 above and below it).
The tray pulls out 0 to 280 toward -y, out of the bay's front; at full travel each runner keeps 150 of its 420 in its rail (asserted):
a three-quarter extension. A finger notch 120 x 30 in the tray's front wall is the grip. The bay is placed, never redrawn: its width,
uprights and shelf heights are read from shelving-steel with library.load. Balls, stops and the rails' fixing to the shelf are the host's
assembly: none is drawn and no hole modelled. The class's features are not on file (lib/standards/etim/class-features.csv has no
EC004083 rows): spec.md gives the design values under plain names, as door-shelving-1000 does. Every size is a design choice. No load
or safety claim. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "shelf-pullout-shelving-1000", "1.0", "furniture"
TITLE = ("pull-out shelf for a shelf of a 1000 wide steel shelving bay, generic, painted steel, a 868 x 420 x 60 sheet tray on two "
         "grooved rails, pulling out 0 to 280")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic rack pull-out shelf (ETIM 10.0 EC004083), two grooved slide rails 12 x 45 joined by a rear tie on "
            "the top face of a shelf of shelving-steel 1.0 (bay 1000 x 500 x 2000, uprights 50 x 50, shelves 40 deep, 450 apart) and an "
            "open sheet tray 868 x 420 x 60 whose side runners ride in the rails' grooves, pulling out 0 to 280 toward the bay's front, "
            "so each runner keeps 150 of its length in its rail; the bay's figures read from shelving-steel (library.load); class "
            "features not on file, design values under plain names (spec.md); every size a design choice; balls, stops and fixing not "
            "drawn; no load or safety claim; no vendor file opened")
ORIGIN = ("shelving-steel's own x and y, so the host places the shelf at the bay's origin raised to a shelf's top face: the shelf's top "
          "face z = 0, the middle of the bay's width x = 0, the front uprights' front faces y = 0; the bay's depth toward +y; the tray "
          "pulls out toward -y")
COMMAND = "SHPO1000"
PARAMS = dict()

SS = library.load("shelving-steel")          # shelving-steel 1.0: the bay whose shelf carries the pull-out (one home for each figure)
W, D, UP, SH_T = SS.W, SS.D, SS.UP, SS.SH_T  # 1000, 500, 50, 40: the bay's width and depth, the uprights' section, the shelves' depth
XI = W / 2 - UP                              # 450: the uprights' inner faces x +-450 (the shelves span between them)
CU = 1.0                                     # design: the rails' clear space to the uprights' inner faces
RW, RH = 12.0, 45.0                          # design: the rails' section, 12 wide (x) and 45 high
XR = XI - CU                                 # 449: the rails' outer faces x +-449
XRI = XR - RW                                # 437: the rails' inner faces x +-437
RY0, RY1 = 20.0, D - 20.0                    # design: the rails from y 20 to 480, 20 inside the shelf's front and back edges
GD, GZ0, GZ1 = 6.0, 10.0, 35.0               # design: the groove 6 deep from the rail's inner face, z 10 to 35 (lips 10 thick, web 6)
TIE_Y, TIE_H = 20.0, 10.0                    # design: the rear tie 20 deep, 10 high, under the grooves, y 460 to 480
CT = 3.0                                     # design: the tray's clear space to the rails' inner faces
XT = XRI - CT                                # 434: the tray's outer side faces x +-434
TY0, TY1 = 30.0, 450.0                       # design: the tray from y 30 to 450 (420 deep), 10 in front of the tie
TZ0, TZ1 = 5.0, 65.0                         # design: the tray 5 above the shelf's top face, 60 high
T = 1.5                                      # design: tray sheet thickness (under 3: every sheet edge is thin to the gate's fillet check)
RN_W = 8.0                                   # design: the runners 8 wide (x 434 to 442), 1 short of the groove's bottom at 443
RN_Z0, RN_Z1 = GZ0 + 2.0, GZ1 - 2.0          # 12 to 33: the runners 2 clear of the groove's lips
TRAVEL = 280.0                               # design: the tray pulls out 0 to 280 toward -y
NW, ND = 120.0, 30.0                         # design: the finger notch in the front wall, 120 wide, 30 down from the rim
MAT = "M-STEEL-7035"                         # painted steel, shelving-steel's layer

assert abs(XR - 449.0) < 1e-9 and abs(XRI - 437.0) < 1e-9 and abs(XT - 434.0) < 1e-9          # the bay's figures as read
assert XT + RN_W < XRI + GD and abs((XRI + GD) - (XT + RN_W) - 1.0) < 1e-9                     # runner 1 short of the groove's bottom
assert RN_Z1 - RN_Z0 >= 8.0 and RN_W >= 8.0 and min(RW, RH, TIE_Y, TIE_H, GZ0, RH - GZ1) >= 8.0  # every free edge >= 8 (none 3 to 7)
assert TIE_H <= GZ0 and TY1 < RY1 - TIE_Y                                                       # the tie under the grooves, behind the tray
# The travel: at full travel (-280) the runners span y TY0 - TRAVEL .. TY1 - TRAVEL = -250 .. 170; the rails start at y 20, so each
# runner keeps 170 - 20 = 150 of its 420 in its rail; at rest the tray stays 10 behind the rails' front ends and 10 before the tie.
ENGAGED = (TY1 - TRAVEL) - RY0
assert abs(ENGAGED - 150.0) < 1e-9 and ENGAGED >= (TY1 - TY0) / 3                              # a third of the runner kept in its rail
assert TZ1 < min(b - a for a, b in zip(SS.SH_TOPS, SS.SH_TOPS[1:])) - SH_T                     # 65 < 410: clears the shelf above
assert NW >= 8.0 and ND < TZ1 - TZ0 - T                                                         # the notch inside the front wall
RAIL = RW * (RY1 - RY0) * RH - GD * (RY1 - RY0) * (GZ1 - GZ0)                                   # 248400 - 69000 = 179400
TIE = 2 * XRI * TIE_Y * TIE_H                                                                   # 874 x 20 x 10 = 174800
TRAY = 2 * XT * (TY1 - TY0) * (TZ1 - TZ0) - (2 * XT - 2 * T) * (TY1 - TY0 - 2 * T) * (TZ1 - TZ0 - T)   # 21873600 - 21101242.5
NOTCH = NW * T * ND                                                                             # 120 x 1.5 x 30 = 5400
RUNNER = RN_W * (TY1 - TY0) * (RN_Z1 - RN_Z0)                                                   # 8 x 420 x 21 = 70560
assert abs(RAIL - 179400.0) < 1e-6 and abs(TRAY - 772357.5) < 1e-6 and abs(RUNNER - 70560.0) < 1e-6
assert abs(2 * RAIL + TIE + TRAY - NOTCH + 2 * RUNNER - 1441677.5) < 1e-6


def build():
    P = Prims()
    for sx, c in ((-1, "rail-l"), (1, "rail-r")):
        x0 = -XR if sx < 0 else XRI
        r = P.box(MAT, x0, RY0, 0, RW, RY1 - RY0, RH)                                            # slide rail on the shelf's top face
        gx = -XRI - GD if sx < 0 else XRI
        P.cutbox(MAT, gx, RY0 - 1.0, GZ0, GD, RY1 - RY0 + 2.0, GZ1 - GZ0, r)                     # groove along its inner face
        P.collider(c, x0, RY0, 0, RW, RY1 - RY0, RH)
    P.box(MAT, -XRI, RY1 - TIE_Y, 0, 2 * XRI, TIE_Y, TIE_H)                                     # rear tie between the rails: one frame
    P.collider("tie", -XRI, RY1 - TIE_Y, 0, 2 * XRI, TIE_Y, TIE_H)
    L = f"node:tray|{MAT}"
    tr = P.box(L, -XT, TY0, TZ0, 2 * XT, TY1 - TY0, TZ1 - TZ0)                                  # the tray's envelope
    P.cutbox(L, -XT + T, TY0 + T, TZ0 + T, 2 * XT - 2 * T, TY1 - TY0 - 2 * T, TZ1 - TZ0, tr)     # open on top: the tray
    P.cutbox(L, -NW / 2, TY0 - 1.0, TZ1 - ND, NW, T + 2.0, ND + 1.0, tr)                       # finger notch in the front wall
    for sx in (-1, 1):
        x0 = -XT - RN_W if sx < 0 else XT
        P.box(L, x0, TY0, RN_Z0, RN_W, TY1 - TY0, RN_Z1 - RN_Z0)                                 # runner in its rail's groove
    P.pivot("tray", "translate", (0, TY0, TZ0), axis=(0, -1, 0), range=(0, TRAVEL))             # pulls out toward the bay's front
    P.collider("pan", -XT, TY0, TZ0, 2 * XT, TY1 - TY0, TZ1 - TZ0)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="behind", az=50, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
