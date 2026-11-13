#!/usr/bin/env python3
"""vise-manual: generic manual machine vise for a drilling machine or a saw, our own vendor-neutral design of the ETIM 10.0 class
EC002173 (Machine vice; the class's synonyms name the drilling machine vice), built unattended (OPERATING.md 12, generic elements;
inventory row own_design "generic": drill-pillar, drill-radial, saw-circular-metal). The small, low sibling of vise-machine (jaws
125 x 40, opening 150, M12): jaws 100 x 30, opening 100, a cast body 238 long with four bolting lugs for M10 (ISO 273 medium) and
one moving jaw (node `jaw`: jaw block and jaw plate) that slides along +x on the base's top face. The spindle's end and its
T-handle stand behind the rear end block; the spindle inside the body, its nut and the ways' gibs are internal mechanism, not
drawn. The T-bolts or clamps that hold it to a machine table are the table's (a T-slot standard, ISO 299, is not on file): the
lugs' holes are cut, nothing is placed in them. The class values (spec.md, "Class values") are design inputs; every size below is
a design choice. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "vise-manual", "1.0", "device"
TITLE = "machine vise, manual, generic, jaws 100 x 30, opening 0 to 100, cast body 238 long, 4 x M10 bolting lugs"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic machine vice (ETIM 10.0 EC002173); class values are design inputs (spec.md); bolting holes "
            "M10 to ISO 273 medium; the T-bolts are the machine table's; every size a design choice; no vendor file opened")
ORIGIN = ("the base's underside (the seat on the machine table) z = 0; the fixed jaw plate's clamping face x = 0; the jaws' centre "
          "y = 0; the moving jaw opens toward +x; the jaws' top edges at z = 65")
COMMAND = "VISEMAN"
PARAMS = dict()
BASE_X0, BASE_X1, BASE_W, BASE_H = -60.0, 178.0, 80.0, 30.0   # base x -60..178, y -40..40, z 0..30 (the ways' top z 30): design choice
FJ_X0, FJ_W, FJ_TOP = -12.0, 96.0, 55.0                       # fixed jaw block x -60..-12, y -48..48, z 30..55: design choice
JAW_W, JAW_H, JAW_T, JAW_Z0 = 100.0, 30.0, 12.0, 35.0         # jaw plates 100 wide x 30 high (class values) x 12 thick, z 35..65
GAP = 1.0                                                     # the jaws 1 apart at rest (0): the solids never touch; design choice
MJ_L = 45.0                                                   # moving jaw block 45 long behind its plate (x 13..58 at rest): design choice
TRAVEL = 99.0                                                 # jaw translates +x 0..99: opening 1..100 (max. cheeks opening 100)
EB_X0, EB_W = 158.0, 60.0                                     # rear end block x 158..178, y -30..30, z 30..55 (1 clear of the jaw at 99)
LUG_X = (-30.0, 140.0)                                        # lug centres along x (170 apart): design choice
LUG_L, LUG_OUT, LUG_T = 36.0, 25.0, 15.0                      # lugs 36 along x, 25 out from the base's side (y 40..65), 15 thick
LUG_Y = 52.5                                                  # hole centres y +-52.5 (105 apart): the lugs' middles
M10_D = 11.0                                                  # M10 clearance, ISO 273 medium H13 (lib/standards/holes.csv)
SP_Z, SP_R, SP_X1 = 42.5, 10.0, 220.0                         # spindle end Ø20 on the axis z 42.5, from the end block to x 220
HD_X, HD_R, HD_Y = 210.0, 6.0, 70.0                           # T-handle Ø12 along y at x 210, y -70..70: design choice

def build():
    P = Prims(); C = "M-CAST-BLUE"; S = "M-SILVER"
    P.box(C, BASE_X0, -BASE_W / 2, 0, BASE_X1 - BASE_X0, BASE_W, BASE_H)                                 # base (the ways on top)
    P.box(C, BASE_X0, -FJ_W / 2, BASE_H, FJ_X0 - BASE_X0, FJ_W, FJ_TOP - BASE_H)                         # fixed jaw block
    P.box(S, FJ_X0, -JAW_W / 2, JAW_Z0, JAW_T, JAW_W, JAW_H)                                             # fixed jaw plate (x -12..0)
    P.box(C, EB_X0, -EB_W / 2, BASE_H, BASE_X1 - EB_X0, EB_W, FJ_TOP - BASE_H)                           # rear end block
    for x in LUG_X:                                                                                      # bolting lugs, holes M10
        for sy in (-1, 1):
            y0 = BASE_W / 2 if sy > 0 else -BASE_W / 2 - LUG_OUT
            lug = P.box(C, x - LUG_L / 2, y0, 0, LUG_L, LUG_OUT, LUG_T)
            P.hole(C, (x, sy * LUG_Y, -1), (x, sy * LUG_Y, LUG_T + 1), M10_D / 2, lug)
    P.cyl(S, (BASE_X1, 0, SP_Z), (SP_X1, 0, SP_Z), SP_R)                                                 # spindle's end (drawn round)
    P.cyl(S, (HD_X, -HD_Y, SP_Z), (HD_X, HD_Y, SP_Z), HD_R)                                              # T-handle through it
    J = lambda m: f"node:jaw|{m}"                                                                        # the moving jaw
    P.box(J(S), GAP, -JAW_W / 2, JAW_Z0, JAW_T, JAW_W, JAW_H)                                            # moving jaw plate (x 1..13)
    P.box(J(C), GAP + JAW_T, -FJ_W / 2, BASE_H, MJ_L, FJ_W, FJ_TOP - BASE_H)                              # moving jaw block on the ways
    P.pivot("jaw", "translate", (GAP, 0, JAW_Z0), axis=(1, 0, 0), range=(0, TRAVEL))
    P.collider("base", BASE_X0, -BASE_W / 2 - LUG_OUT, 0, BASE_X1 - BASE_X0, BASE_W + 2 * LUG_OUT, BASE_H)
    P.collider("fixed-jaw", BASE_X0, -JAW_W / 2, BASE_H, -BASE_X0, JAW_W, JAW_Z0 + JAW_H - BASE_H)
    P.collider("end-block", EB_X0, -EB_W / 2, BASE_H, BASE_X1 - EB_X0, EB_W, FJ_TOP - BASE_H)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
