#!/usr/bin/env python3
"""hose-guide-roller: a hose guide roller: a flanged spool roller turning between the two cheeks of a U-bracket, screwed down on a
machine's frame where a hose (an air or coolant hose) turns over an edge or runs out to a moving part, so the hose rolls over the
spool instead of rubbing on the edge, and its flanges keep it on the roller. Generic (OPERATING.md 12, EM 2026-11-07): our own
vendor-neutral design of ETIM 10.0 EC010745 "Hose guide" (synonym "Hose guide roller"), the next class of the Hoses group
(EG015510) in generic.next_classes' order after EC004090 (pneu-r118, lib/rounds/pneu/next.md); the class values it is designed to are
in spec.md "## Class values". No dimensional standard shapes a hose guide: its bracket, roller and channel are design choices. Its
two mounting holes are M6 clearance, medium (ISO 273, lib/standards/holes.csv); the screws are the host's (screw-iso4017, not built,
so not placed). One moving part: the roller with its axle stubs (`roller`, rotate about +x, its own axis), turning in plain bores in
the cheeks. No port: it carries no fluid. No vendor file was opened (pneu-r119)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "hose-guide-roller", "1.0", "device"
TITLE = "generic hose guide roller, flanged polyamide spool on a zinc-plated steel U-bracket, for hose to Ø25, two M6 holes"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic hose guide (ETIM 10.0 EC010745), a flanged spool roller between the cheeks of a U-bracket; "
            "mounting holes M6 clearance medium (ISO 273, lib/standards/holes.csv); bracket, roller and channel are design choices")
ORIGIN = ("the centre of the bracket's underside (the mounting face, z = 0); the roller's axis along x at z = 35, the hose running "
          "over it along y, z up")
COMMAND = "HOSE-GUIDE-ROLLER"
PARAMS = dict()

BASE = (90.0, 50.0, 6.0)           # design choice: the bracket's base plate, x by y by thickness, centred on the origin in plan
HOLE_D, HOLE_X = 6.6, 35.0         # M6 clearance, medium (ISO 273 H13: 6.6 to 6.82; holes.csv), at x = ±35 on the base's centre line
CHEEK_T, CHEEK_IN = 5.0, 20.0      # design choice: the two cheeks, 5 thick, inner faces at x = ±20
CHEEK_D, CHEEK_TOP = 40.0, 50.0    # design choice: the cheeks 40 deep (y) and standing to z = 50
AXIS_Z = 35.0                      # design choice: the roller's axis height above the mounting face
HUB_D, HUB_L = 30.0, 30.0          # design choice: the spool's hub (the channel's floor) Ø30, 30 long between the flanges
FLANGE_D, FLANGE_T = 50.0, 4.0     # design choice: the spool's two flanges Ø50, 4 thick
STUB_D = 10.0                      # design choice: the axle stubs Ø10, turning in Ø10 plain bores in the cheeks, face to face
HOSE_MAX = 25.0                    # class value: the largest hose outside diameter the channel takes (30 wide, 10 deep)
MAT_BRACKET, MAT_ROLLER, MAT_AXLE = "M-ZINC", "M-GREY-PA", "M-SILVER"

_X1 = HUB_L / 2                    # 15: hub to flange
_X2 = _X1 + FLANGE_T               # 19: flange's outer face
_GAP = CHEEK_IN - _X2              # 1: running clearance between each flange and its cheek
_X3 = CHEEK_IN + CHEEK_T           # 25: the cheek's outer face, where each stub ends flush
assert _GAP >= 0.5                                                   # the flanges never rub the cheeks
assert AXIS_Z - FLANGE_D / 2 - BASE[2] >= 3.0                        # 4 between the flanges and the base plate
assert CHEEK_TOP - AXIS_Z - STUB_D / 2 >= 3 * CHEEK_T / 2            # 10 of steel above each cheek's bore
assert CHEEK_D / 2 - STUB_D / 2 >= 3 * CHEEK_T / 2                   # 15 beside it
assert HOSE_MAX < HUB_L                                              # the hose fits between the flanges
assert (FLANGE_D - HUB_D) / 2 >= HOSE_MAX / 3                        # the flanges rise 10, over a third of the largest hose's Ø
assert BASE[0] / 2 - HOLE_X - HOLE_D / 2 >= 5.0                      # 6.7 of plate between each hole and the base's end
assert HOLE_X - HOLE_D / 2 - _X3 >= 5.0                              # 6.7 between each hole and its cheek (room for the screw's head)
assert min(BASE[2], CHEEK_T, FLANGE_T) >= 2.5 * 0.5                  # every edge passes the AutoCAD gate's fillet pre-flight


def height(): return AXIS_Z + FLANGE_D / 2                          # 60: the mounting face to the flanges' top


def build():
    P = Prims()
    bx, by, bt = BASE
    base = P.box(MAT_BRACKET, -bx / 2, -by / 2, 0, bx, by, bt)                                      # base plate
    for x in (-HOLE_X, HOLE_X):
        P.hole(MAT_BRACKET, (x, 0, -1.0), (x, 0, bt + 1.0), HOLE_D / 2, base)                         # M6 clearance, through
    for s in (-1, 1):
        x0 = CHEEK_IN if s > 0 else -_X3
        ch = P.box(MAT_BRACKET, x0, -CHEEK_D / 2, bt, CHEEK_T, CHEEK_D, CHEEK_TOP - bt)              # cheek, on the base face to face
        P.hole(MAT_BRACKET, (s * (CHEEK_IN - 1.0), 0, AXIS_Z), (s * (_X3 + 1.0), 0, AXIS_Z), STUB_D / 2, ch)   # axle bore, through
    a = lambda x: (x, 0, AXIS_Z)
    P.cyl(f"node:roller|{MAT_ROLLER}", a(-_X1), a(_X1), HUB_D / 2)                                  # hub: the channel's floor
    for s in (-1, 1):
        P.cyl(f"node:roller|{MAT_ROLLER}", a(s * _X1), a(s * _X2), FLANGE_D / 2)                    # flange, face to face on the hub
        P.cyl(f"node:roller|{MAT_AXLE}", a(s * _X2), a(s * _X3), STUB_D / 2)                        # axle stub, through the cheek's bore
    P.pivot("roller", "rotate", a(0), axis=(1, 0, 0), range=(0, 360), unit="deg")
    P.collider("env", -bx / 2, -by / 2, 0, bx, by, height())
    return P


PREVIEWS = [dict(name="three-quarter", az=250, el=25), dict(name="side", az=270, el=5), dict(name="top", az=250, el=70)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
