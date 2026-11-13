#!/usr/bin/env python3
"""vise-machine: generic machine vise, our own vendor-neutral design of the ETIM 10.0 class EC002173 (Machine vice), built
unattended (OPERATING.md 12, generic elements; inventory row own_design "generic"). A cast body (base, fixed jaw block, rear end
block and four bolting lugs with M12 clearance holes, ISO 273 medium) and one moving jaw (node `jaw`: jaw block and jaw plate)
that slides along +x on the base's top face. Hardened jaw plates 125 x 40 on both jaws. The spindle's square end and its T-handle
stand behind the rear end block; the spindle inside the body, its nut and the guide ways' gibs are internal mechanism, not drawn.
The T-bolts or clamps that hold it to a machine table are the table's (a T-slot standard, ISO 299, is not on file): the lugs' holes
are cut, nothing is placed in them. The class values (spec.md, "Class values") are design inputs; every size below is a design
choice. The folder's record (metadata.json, references/source.txt) names a catalogue vise: no size was taken from it."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "vise-machine", "1.0", "device"
TITLE = "machine vise, generic, jaws 125 x 40, opening 0 to 150, cast body 340 long, 4 x M12 bolting lugs"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic machine vice (ETIM 10.0 EC002173); class values are design inputs (spec.md); bolting holes "
            "M12 to ISO 273 medium; the T-bolts are the machine table's; every size a design choice; no vendor file opened")
ORIGIN = ("the base's underside (the seat on the machine table) z = 0; the fixed jaw plate's clamping face x = 0; the jaws' centre "
          "y = 0; the moving jaw opens toward +x; the jaws' top edges at z = 110")
COMMAND = "VISEMACH"
PARAMS = dict()
BASE_X0, BASE_X1, BASE_W, BASE_H = -90.0, 250.0, 100.0, 60.0   # base x -90..250, y -50..50, z 0..60 (the ways' top z 60): design choice
FJ_X0, FJ_W, FJ_TOP = -18.0, 120.0, 100.0                     # fixed jaw block x -90..-18, y -60..60, z 60..100: design choice
JAW_W, JAW_H, JAW_T, JAW_Z0 = 125.0, 40.0, 18.0, 70.0         # jaw plates 125 wide x 40 high (class values) x 18 thick, z 70..110
GAP = 1.0                                                     # the jaws 1 apart at rest (0): the solids never touch; design choice
MJ_L = 61.0                                                   # moving jaw block 61 long behind its plate (x 19..80 at rest): design choice
TRAVEL = 149.0                                                # jaw translates +x 0..149: opening 1..150 (max. cheeks opening 150)
EB_X0, EB_W = 230.0, 80.0                                     # rear end block x 230..250, y -40..40, z 60..100 (1 clear of the jaw at 149)
LUG_X = (-40.0, 190.0)                                        # lug centres along x (230 apart): design choice
LUG_L, LUG_OUT, LUG_T = 40.0, 30.0, 20.0                      # lugs 40 along x, 30 out from the base's side (y 50..80), 20 thick
LUG_Y = 65.0                                                  # hole centres y +-65 (130 apart): the lugs' middles
M12_D = 13.5                                                  # M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv)
SP_Z, SP_R, SP_X1 = 80.0, 12.5, 298.0                         # spindle end Ø25 on the axis z 80, from the end block to x 298
HD_X, HD_R, HD_Y = 288.0, 8.0, 90.0                           # T-handle Ø16 along y at x 288, y -90..90: design choice

def build():
    P = Prims(); C = "M-CAST-BLUE"; S = "M-SILVER"
    P.box(C, BASE_X0, -BASE_W / 2, 0, BASE_X1 - BASE_X0, BASE_W, BASE_H)                                 # base (the ways on top)
    P.box(C, BASE_X0, -FJ_W / 2, BASE_H, FJ_X0 - BASE_X0, FJ_W, FJ_TOP - BASE_H)                         # fixed jaw block
    P.box(S, FJ_X0, -JAW_W / 2, JAW_Z0, JAW_T, JAW_W, JAW_H)                                             # fixed jaw plate (x -18..0)
    P.box(C, EB_X0, -EB_W / 2, BASE_H, BASE_X1 - EB_X0, EB_W, FJ_TOP - BASE_H)                           # rear end block
    for x in LUG_X:                                                                                      # bolting lugs, holes M12
        for sy in (-1, 1):
            y0 = BASE_W / 2 if sy > 0 else -BASE_W / 2 - LUG_OUT
            lug = P.box(C, x - LUG_L / 2, y0, 0, LUG_L, LUG_OUT, LUG_T)
            P.hole(C, (x, sy * LUG_Y, -1), (x, sy * LUG_Y, LUG_T + 1), M12_D / 2, lug)
    P.cyl(S, (BASE_X1, 0, SP_Z), (SP_X1, 0, SP_Z), SP_R)                                                 # spindle's square end (drawn round)
    P.cyl(S, (HD_X, -HD_Y, SP_Z), (HD_X, HD_Y, SP_Z), HD_R)                                              # T-handle through it
    J = lambda m: f"node:jaw|{m}"                                                                        # the moving jaw
    P.box(J(S), GAP, -JAW_W / 2, JAW_Z0, JAW_T, JAW_W, JAW_H)                                            # moving jaw plate (x 1..19)
    P.box(J(C), GAP + JAW_T, -FJ_W / 2, BASE_H, MJ_L, FJ_W, FJ_TOP - BASE_H)                              # moving jaw block on the ways
    P.pivot("jaw", "translate", (GAP, 0, JAW_Z0), axis=(1, 0, 0), range=(0, TRAVEL))
    P.collider("base", BASE_X0, -BASE_W / 2 - LUG_OUT, 0, BASE_X1 - BASE_X0, BASE_W + 2 * LUG_OUT, BASE_H)
    P.collider("fixed-jaw", BASE_X0, -JAW_W / 2, BASE_H, -BASE_X0, JAW_W, JAW_Z0 + JAW_H - BASE_H)
    P.collider("end-block", EB_X0, -EB_W / 2, BASE_H, BASE_X1 - EB_X0, EB_W, FJ_TOP - BASE_H)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
