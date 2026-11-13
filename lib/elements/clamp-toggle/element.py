#!/usr/bin/env python3
"""clamp-toggle: generic vertical hold-down toggle clamp, our own vendor-neutral design of the ETIM 10.0 class EC003935 (Machine
toggle clamp), built unattended (OPERATING.md 12, generic elements). A flanged base with 4 x M5 holes, a two-plate frame, and one
lever (node `arm`: the clamping arm with the handle) that swings open about the pivot. The spindle is a screw with two nuts, never
generic: its M8 hole is cut through the arm and the parts are placed in a later version. Holes: ISO 273 medium (lib/standards/
holes.csv). The class values (spec.md, "Class values") are design inputs; every size below is a design choice. In this model the
handle and the arm are one lever on one pivot: the toggle link of a real clamp is not drawn (spec.md, Mechanism)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "clamp-toggle", "1.0", "device"
TITLE = "toggle clamp, generic, vertical hold-down, 2.5 kN, flanged base 4 x M5, spindle hole M8"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic machine toggle clamp (ETIM 10.0 EC003935); class values are design inputs (spec.md); "
            "base holes M5 and spindle hole M8 to ISO 273 medium; spindle and nuts placed later; every size a design choice")
ORIGIN = ("the mounting face (the base's underside) z = 0, the centre of the base's four-hole pattern x = 0, y = 0; clamped, the arm "
          "reaches toward +x and the handle stands up; opening swings the arm up and the handle back toward -x")
COMMAND = "TOGCLAMP"
PARAMS = dict()
BASE_X, BASE_Y, BASE_T = 64.0, 44.0, 3.0       # flanged base 64 x 44 x 3: design choice
HOLE_X, HOLE_Y = 24.0, 14.0                    # 4 x M5 at +-24, +-14 (48 x 28): design choice
M5_D = 5.5                                     # M5 clearance, ISO 273 medium H13 (lib/standards/holes.csv)
M8_D = 9.0                                     # M8 clearance for the spindle, ISO 273 medium H13 (lib/standards/holes.csv)
PIVOT = (0.0, 30.0)                            # pivot axis (x, z), along y: design choice
FRAME_X, FRAME_TOP, PLATE_T = 12.0, 38.0, 3.0  # frame plates x -12..12, up to z 38, 3 thick: design choice
GAP = 8.5                                      # plates' inner faces at y = +-8.5 (0.5 clear of the 16-wide arm): design choice
JOURNAL_R, BORE_R = 3.0, 3.1                   # pivot journal Ø6 in the arm's Ø6.2 bore (features.csv): design choice
HEAD_R, HEAD_T = 5.0, 1.5                      # the journal's riveted heads Ø10 x 1.5: design choice
HUB_R, ARM_W, ARM_H = 7.0, 16.0, 8.0           # arm hub r 7; arm bar 16 wide, 8 deep, level with the pivot: design choice
ARM_TIP, SPINDLE_AT = 62.0, 50.0               # arm tip x 62; spindle axis x 50 (50 from the pivot): design choice
HANDLE_W, HANDLE_D, HANDLE_TOP = 10.0, 8.0, 100.0   # handle bar 10 x 8, up to z 100: design choice
GRIP_R, GRIP_Z = 7.0, (62.0, 102.0)            # grip Ø14 from z 62 to 102: design choice
OPEN = 95.0                                    # opening angle: the arm just past vertical, so the open clamp stays open (design choice)

def build():
    P = Prims(); Z, G = "M-ZINC", "M-RED-PA"; px, pz = PIVOT
    base = P.box(Z, -BASE_X / 2, -BASE_Y / 2, 0, BASE_X, BASE_Y, BASE_T)                                  # flanged base
    for sx in (-1, 1):
        for sy in (-1, 1):
            x, y = sx * HOLE_X, sy * HOLE_Y
            P.hole(Z, (x, y, -1), (x, y, BASE_T + 1), M5_D / 2, base)
    for s in (-1, 1):                                                                                      # frame plates
        P.box(Z, -FRAME_X, GAP if s > 0 else -GAP - PLATE_T, BASE_T, 2 * FRAME_X, PLATE_T, FRAME_TOP - BASE_T)
    yo = GAP + PLATE_T                                                                                     # 11.5: the plates' outer faces
    P.cyl(Z, (px, -yo, pz), (px, yo, pz), JOURNAL_R)                                                       # pivot journal through both plates
    for s in (-1, 1): P.cyl(Z, (px, s * yo, pz), (px, s * (yo + HEAD_T), pz), HEAD_R)                      # riveted heads
    A = lambda m: f"node:arm|{m}"                                                                          # the lever: arm, hub, handle, grip
    hub = P.cyl(A(Z), (px, -ARM_W / 2, pz), (px, ARM_W / 2, pz), HUB_R)
    P.hole(Z, (px, -ARM_W / 2 - 1, pz), (px, ARM_W / 2 + 1, pz), BORE_R, hub)                              # the hub's bore on the journal
    bar = P.box(A(Z), px + 5.0, -ARM_W / 2, pz - ARM_H / 2, ARM_TIP - px - 5.0, ARM_W, ARM_H)               # arm bar, from inside the hub
    P.hole(Z, (SPINDLE_AT, 0, pz - ARM_H / 2 - 1), (SPINDLE_AT, 0, pz + ARM_H / 2 + 1), M8_D / 2, bar)      # spindle hole M8 (spindle later)
    P.box(A(Z), px - HANDLE_D / 2, -HANDLE_W / 2, pz + 5.0, HANDLE_D, HANDLE_W, HANDLE_TOP - pz - 5.0)      # handle bar, from inside the hub
    P.cyl(A(G), (px, 0, GRIP_Z[0]), (px, 0, GRIP_Z[1]), GRIP_R)                                            # grip
    P.pivot("arm", "rotate", (px, 0, pz), axis=(0, -1, 0), range=(0, OPEN), unit="deg")                    # + opens: arm up, handle back
    P.collider("body", -BASE_X / 2, -BASE_Y / 2, 0, BASE_X, BASE_Y, BASE_T)
    P.collider("frame", -FRAME_X, -yo - HEAD_T, BASE_T, 2 * FRAME_X, 2 * (yo + HEAD_T), FRAME_TOP - BASE_T)
    P.collider("arm", px - HUB_R, -ARM_W / 2, pz - HUB_R, ARM_TIP - px + HUB_R, ARM_W, 2 * HUB_R)
    P.collider("handle", px - GRIP_R, -GRIP_R, pz + HUB_R, 2 * GRIP_R, 2 * GRIP_R, GRIP_Z[1] - pz - HUB_R)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
