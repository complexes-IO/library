#!/usr/bin/env python3
"""head-rivet-c-hyd: a rivet setting head, a cylinder-driven fixture: a C-frame (a column at the back, a lower arm with the anvil, an
upper arm that seats the cylinder) whose placed cylinder pushes the upper die down the die axis onto the rivet standing on the
anvil. The riveter (lib/machines-factory.txt line 67) mounts it on its welded frame and works it from its foot switch through its
valve. lib/inventory.csv row `head-rivet-c-hyd` (own_design yes, "pneumatic rivet setting head"; used_by riveter). Our own design
(OPERATING.md 12, own designs; core watch 2026-11-11, request pneu-11's answer item 3: "a cylinder-driven setting head is a
fixture, not the hand-held tool EC004037 describes. It places a cylinder that is on file (a common part) and models its own body;
the rivet sizes it takes are design choices"). The cylinder placed is hyd-cylinder-da-40 1.1 (bom.csv, tag `cyl`; OPERATING.md 12,
foundation first: the only plain double-acting cylinder on file past station 6; the pneumatic ISO 15552 cylinder of the inventory
is not built, ISO 15552 not on file), read through library.load so the seat cannot drift from it: it stands on the upper arm's top
face by its head cap, its gland nose in the arm's bore, rolled 90 degrees about its own y so the rod points down (-z) and its ports
face +x (a placed instance touches its host and never overlaps it, GEO-020: the cap flush on the arm, the cup's top face on the
rod's end face). That seat locates the cylinder and does not retain it against the setting reaction: the mounting to the
upper arm is hyd-cylinder-da-40's open figure (ISO 6020-2 mounting styles, class B, spec.md Open figures; review head-rivet-1.0.md
finding 1), drawn with the cylinder's 2.0. The die cup is pressed on the rod's plain end (no rod-end thread is on file: hyd-cylinder-da-40's open figure) and so is
part of the rod's node (`cyl.rod`, translate -z, 0 to the stroke; its states and poses are hyd-cylinder-da-40's own behaviour.csv, carried
by the placed part); at full stroke the upper die stops 3 above the anvil's face (the least set-head height, a design choice), so
the dies never meet. Frame, arms, anvil, dies, cup and the seat are design choices. No rating
of its own (no ratings.csv): no setting force or rivet size is claimed; the force available is the cylinder's own figure. The
cylinder's two ports (`cyl.port-cap`, `cyl.port-rod`, unit hyd-port) are its own, with its own open figures (its spec.md)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "head-rivet-c-hyd", "1.2", "device"
TITLE = "rivet setting head, own design, C-frame fixture driven by hyd-cylinder-da-40 1.1 placed, daylight 203, throat 60"
TOOLKIT = "1.3"
BASELINE = ("our own design (inventory own_design yes; request pneu-11's answer item 3: a cylinder-driven setting head is a fixture, "
            "not the hand-held tool EC004037); C-frame with anvil and die cup, driven by hyd-cylinder-da-40 1.1 placed from file (bom.csv; "
            "OPERATING.md 12 common parts; its figures read through library.load); frame, arms, anvil, dies, cup and the cylinder's "
            "seat are design choices; no rating of its own; no vendor file opened")
ORIGIN = ("the frame's underside (the mounting plane z = 0) on the die axis (x = y = 0); the column at -x, the throat open toward +x, "
          "the cylinder above with its rod down the die axis and its ports facing +x")
COMMAND = "HEAD-RIVET"
PARAMS = dict()

HC = library.load("hyd-cylinder-da-40")           # hyd-cylinder-da-40 1.1 (bom.csv pins the version): the figures the seat and the die travel follow
CYL_TAG, ROLL = "cyl", 90.0                 # the cylinder rolled 90 about its own y: its +x (rod) -> -z, its +z (ports) -> +x (toolkit/prims.py rotation_yp)
STROKE = HC.STROKE                          # 200: the die travel is the cylinder's stroke
GAP = 3.0                                   # design choice: at full stroke the upper die stops 3 above the anvil's face (the least set-head height)
COL_X, FRAME_Y = (-110.0, -60.0), 100.0     # design choices: the column at the back, 50 thick, the frame 100 wide
ARM_X = (COL_X[1] - 0.5, 60.0)              # the arms from 0.5 into the column to the throat's end (throat 60 from the die axis)
LOWER_T, ARM_T = 40.0, 38.0                 # design choices: the lower arm; the upper arm (the cylinder's seat)
HOLDER_D, HOLDER_H = 40.0, 20.0             # design choice: the anvil holder on the lower arm
DIE_D, DIE_H = 16.0, 10.0                   # design choice: the two dies, Ø16 x 10 (solid rivets up to Ø6 by design; no size or force rating claimed)
CUP_D, CUP_H = 30.0, 30.0                   # design choice: the die cup pressed on the rod's plain end
CUP_CLEAR, NOSE_CLEAR = 2.0, 1.0            # design choices: the cup's top 2 below the upper arm at rest; the arm's bore 1 clear round the gland nose
IN = 0.5                                    # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_FRAME, MAT_HOLDER, MAT_DIE = "M-STEEL-7035", "M-GALV", "M-SILVER"

Z_HOLDER = (LOWER_T - IN, LOWER_T - IN + HOLDER_H)         # 39.5 to 59.5: the anvil holder, 0.5 into the lower arm
Z_ANVIL = Z_HOLDER[1] - IN + DIE_H                         # 69: the anvil's (lower die's) face
Z_DIE = Z_ANVIL + STROKE + GAP                             # 272: the upper die's face at rest (daylight 203)
Z_CUP = (Z_DIE + DIE_H - IN, Z_DIE + DIE_H - IN + CUP_H)   # 281.5 to 311.5: the die cup, the die 0.5 into it
Z0 = Z_CUP[1] + HC.X_ROD[1]                                # 651.5: the cylinder's origin (its rear cap's back face) so the rod's end meets the cup's top face
Z_CAP = Z0 - HC.X_HEAD[1]                                  # 351.5: the head cap's front face, which seats on the upper arm's top face
Z_ARM = (Z_CAP - ARM_T, Z_CAP)                             # 313.5 to 351.5: the upper arm, the cap flush on its top (a placed instance touches its host, never overlaps it: GEO-020)
BORE_D = HC.GLAND_D + 2 * NOSE_CLEAR                       # 38: the arm's bore round the gland nose, the rod through it
assert HC.VERSION == "1.1" and HC.ROD_OUT > 0 and HC.X_GLAND < HC.X_ROD[1]
assert Z_ARM[0] - Z_CUP[1] >= CUP_CLEAR                    # the cup clears the arm at rest
assert Z0 - HC.X_GLAND >= Z_ARM[0] + 10.0                  # the gland nose stays inside the arm's bore, 10 above its underside
assert BORE_D > HC.ROD_D + 2 * HC.ROD_CLEAR and CUP_D > HC.ROD_D and DIE_D < CUP_D
assert HC.CAP / 2.0 + 5.0 <= ARM_X[1] and HC.CAP / 2.0 + 5.0 <= FRAME_Y / 2.0        # the cap on the arm, 5 of arm round it
assert Z0 - (HC.X_HEAD[0] + HC.X_HEAD[1]) / 2.0 - HC.SPOT_D / 2.0 > Z_ARM[1] + 5.0    # the rod-end port's spot face clear above the arm
assert Z_DIE - STROKE - Z_ANVIL == GAP and Z_CUP[0] - STROKE > Z_HOLDER[1] + 5.0      # the dies never meet; the cup clears the holder at full stroke
assert HOLDER_D > DIE_D and HOLDER_D / 2.0 + 5.0 <= ARM_X[1] and ARM_X[0] + 5.0 <= -HOLDER_D / 2.0


def build():
    P = Prims(); y0 = -FRAME_Y / 2.0
    P.box(MAT_FRAME, COL_X[0], y0, 0.0, COL_X[1] - COL_X[0], FRAME_Y, Z_ARM[1])                           # column, the mounting plane its underside
    P.box(MAT_FRAME, ARM_X[0], y0, 0.0, ARM_X[1] - ARM_X[0], FRAME_Y, LOWER_T)                            # lower arm, 0.5 into the column
    arm = P.box(MAT_FRAME, ARM_X[0], y0, Z_ARM[0], ARM_X[1] - ARM_X[0], FRAME_Y, ARM_T)                   # upper arm, the cylinder's seat
    P.hole(MAT_FRAME, (0, 0, Z_ARM[1] + 1.0), (0, 0, Z_ARM[0] - 1.0), BORE_D / 2.0, arm)                  # its bore: the gland nose and the rod
    P.cyl(MAT_HOLDER, (0, 0, Z_HOLDER[0]), (0, 0, Z_HOLDER[1]), HOLDER_D / 2.0)                            # anvil holder
    P.cyl(MAT_DIE, (0, 0, Z_HOLDER[1] - IN), (0, 0, Z_ANVIL), DIE_D / 2.0)                                 # anvil (the lower die)
    row = next(r for r in library.own_bom(sys.modules[__name__]) if r["tag"] == CYL_TAG)                 # the cylinder, placed per bom.csv
    assert row["element"] == HC.ID and abs(row["z"] - Z0) < 1e-6 and abs(row["roll"] - ROLL) < 1e-6 and row["x"] == row["y"] == 0.0
    base = len(P); library.place(P, row)
    for i in range(base, len(P)):                                                                        # the child's colliders named for its nodes here
        L, k, q = P[i]
        if L.startswith("collider:"): P[i] = (f"collider:{CYL_TAG}.{L[9:]}", k, q)
    P.cyl(f"node:{CYL_TAG}.rod|{MAT_HOLDER}", (0, 0, Z_CUP[1]), (0, 0, Z_CUP[0]), CUP_D / 2.0)            # die cup on the rod's end face (touching, GEO-020), rides with the rod
    P.cyl(f"node:{CYL_TAG}.rod|{MAT_DIE}", (0, 0, Z_DIE + DIE_H), (0, 0, Z_DIE), DIE_D / 2.0)             # upper die, 0.5 into the cup
    P.collider("body", COL_X[0], y0, 0.0, ARM_X[1] - COL_X[0], FRAME_Y, Z0)
    P.collider(f"{CYL_TAG}.rod", -CUP_D / 2.0, -CUP_D / 2.0, Z_DIE, CUP_D, CUP_D, Z_CUP[1] - Z_DIE)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="throat", az=0, el=10), dict(name="dies", az=45, el=15)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
