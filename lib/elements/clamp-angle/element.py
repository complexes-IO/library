#!/usr/bin/env python3
"""clamp-angle: generic angle clamp (the corner clamp that holds two workpieces at a right angle for gluing, screwing or welding a
frame's corner), our own vendor-neutral design of the ETIM 10.0 class EC002144 (Angle clamp; the class's synonyms name the corner
and mitre clamp), built unattended (OPERATING.md 12, generic elements; `python lib/build.py inventory mech` lists the class once no
inventory row builds unattended: the first class of group EG020054 Clamping tools whose shape no dimensional standard fixes,
lib/needs-em/mech.md). A cast base 120 x 120 carries two fences at 90 degrees (the fixed jaws, their faces the planes y = 0 and
x = 0) and two spindle posts. Each workpiece lies against its fence and is pressed onto it by a steel pad on a screw spindle that
runs through its post's bore and ends in a T-handle: two moving nodes, `pad-a` (+y) and `pad-b` (+x). The two spindles cross in
plan at different heights, so neither pad's sweep meets the other's spindle; and each pad sits farther from the corner than the
other pad's whole stroke reaches, so the two pads never meet whatever each is set to (2.0, review mech-r124 finding 1). The spindles are drawn plain (their thread and the
nut in the post are internal mechanism, not drawn and not claimed). The class values (spec.md, "Class values") are design inputs;
every size is a design choice. No clamping force is designed or claimed. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "clamp-angle", "2.0", "device"
TITLE = "angle clamp, generic, 90 degree corner, two screw pads, clamping spread 30, jaws 100 x 40, base 120 x 120"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic angle clamp (ETIM 10.0 EC002144); class values are design inputs (spec.md); two screw "
            "spindles drawn plain, their thread and nut not drawn or claimed; every size a design choice; no clamping force "
            "claimed; no vendor file opened")
ORIGIN = ("the base's underside z = 0 at the jaws' inside corner: fence a's clamping face is the plane y = 0 (its workpiece runs "
          "along +x), fence b's the plane x = 0 (its workpiece runs along +y); pad-a opens toward +y, pad-b toward +x")
COMMAND = "CLAMPANG"
PARAMS = dict()

B0, B1, BT = -20.0, 100.0, 10.0          # base x and y -20..100, z 0..10: design choice
FT, JL, JW = 20.0, 100.0, 40.0           # fences 20 thick; jaw length 100 from the corner; jaw width 40 (z 10..50): class values
GAP, TRAVEL = 1.0, 29.0                  # each pad 1 off its fence at rest (0); travel 29: clamping spread 1..30 (class value 30)
PT, PL, PZ0, PZ1 = 10.0, 36.0, 11.0, 41.0  # pads 10 thick, 36 long (42..78 along their fence), z 11..41 (1 above the base): design
POST_T, POST_L, POST_Z1 = 15.0, 36.0, 50.0  # posts 15 thick, 36 wide (42..78), z 10..50: design choice
POST_N = 70.0                            # each post's near face 70 from its fence: design choice
SA_Z, SB_Z, SP_R, BORE_R = 20.0, 34.0, 6.0, 7.0  # spindle a on z 20, spindle b on z 34, both Ø12 in Ø14 bores: design choice
SP_C = 60.0                              # both spindles on the pads' middle line (x 60 for a, y 60 for b): the pads 42..78, 2 past
                                         # the other pad's whole stroke (GAP + TRAVEL + PT = 40); 2.0, review mech-r124 finding 1
SP_END, HD_AT, HD_R, HD_H = 95.0, 92.0, 5.0, 25.0  # spindle ends 95 from the fence; T-handle Ø10 at 92, 50 long: design choice
CAST, STEEL = "M-CAST-BLUE", "M-SILVER"

assert GAP + TRAVEL + PT < SP_C - SP_R - 2.0               # each pad's back stops clear of the other spindle at the end of its travel
assert (SB_Z - SP_R) - (SA_Z + SP_R) >= 2.0                # the spindles cross 2 apart in z
assert SA_Z - BORE_R - BT >= 3.0 and POST_Z1 - (SB_Z + BORE_R) >= 3.0   # the bores' walls in the posts
assert GAP + TRAVEL + PT + 2.0 <= SP_C - PL / 2           # each pad 2 clear of the other pad's whole stroke: both may be open
assert GAP + TRAVEL + PT + 2.0 <= SP_C - POST_L / 2       # each post 2 clear of the other pad's whole stroke
assert SP_C + SP_R + 2.0 <= POST_N and POST_N + POST_T < HD_AT - HD_R  # the posts clear of the crossing spindle and of the handles
assert SP_C + HD_H < HD_AT - HD_R                          # handle a ends 2 short of handle b's line (and b of a's)


def build():
    P = Prims()
    P.box(CAST, B0, B0, 0, B1 - B0, B1 - B0, BT)                                                 # base
    P.box(CAST, B0, -FT, BT, B1 - B0, FT, JW)                                                    # fence a (face y 0), x -20..100
    P.box(CAST, -FT, 0, BT, FT, B1, JW)                                                          # fence b (face x 0), y 0..100
    pa = P.box(CAST, SP_C - POST_L / 2, POST_N, BT, POST_L, POST_T, POST_Z1 - BT)                # post a, y 70..85
    P.hole(CAST, (SP_C, POST_N - 1.0, SA_Z), (SP_C, POST_N + POST_T + 1.0, SA_Z), BORE_R, pa)   # spindle a's bore (along y)
    pb = P.box(CAST, POST_N, SP_C - POST_L / 2, BT, POST_T, POST_L, POST_Z1 - BT)                # post b, x 70..85
    P.hole(CAST, (POST_N - 1.0, SP_C, SB_Z), (POST_N + POST_T + 1.0, SP_C, SB_Z), BORE_R, pb)   # spindle b's bore (along x)
    A = lambda m: f"node:pad-a|{m}"
    P.box(A(STEEL), SP_C - PL / 2, GAP, PZ0, PL, PT, PZ1 - PZ0)                                  # pad a, y 1..11 at rest
    P.cyl(A(STEEL), (SP_C, GAP + PT, SA_Z), (SP_C, SP_END, SA_Z), SP_R)                          # spindle a
    P.cyl(A(STEEL), (SP_C - HD_H, HD_AT, SA_Z), (SP_C + HD_H, HD_AT, SA_Z), HD_R)                # handle a, along x
    P.pivot("pad-a", "translate", (SP_C, GAP, SA_Z), axis=(0, 1, 0), range=(0, TRAVEL))
    Bn = lambda m: f"node:pad-b|{m}"
    P.box(Bn(STEEL), GAP, SP_C - PL / 2, PZ0, PT, PL, PZ1 - PZ0)                                 # pad b, x 1..11 at rest
    P.cyl(Bn(STEEL), (GAP + PT, SP_C, SB_Z), (SP_END, SP_C, SB_Z), SP_R)                         # spindle b
    P.cyl(Bn(STEEL), (HD_AT, SP_C - HD_H, SB_Z), (HD_AT, SP_C + HD_H, SB_Z), HD_R)               # handle b, along y
    P.pivot("pad-b", "translate", (GAP, SP_C, SB_Z), axis=(1, 0, 0), range=(0, TRAVEL))
    P.collider("base", B0, B0, 0, B1 - B0, B1 - B0, BT)
    P.collider("fence-a", B0, -FT, BT, B1 - B0, FT, JW)
    P.collider("fence-b", -FT, 0, BT, FT, B1, JW)
    P.collider("post-a", SP_C - POST_L / 2, POST_N, BT, POST_L, POST_T, POST_Z1 - BT)
    P.collider("post-b", POST_N, SP_C - POST_L / 2, BT, POST_T, POST_L, POST_Z1 - BT)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="work", az=60, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
