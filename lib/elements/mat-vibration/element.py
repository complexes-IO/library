#!/usr/bin/env python3
"""mat-vibration: generic vibration absorber mat (the loose rubber pad laid under a machine's feet, a bench or a cabinet so the floor
takes less of its vibration and the machine doesn't walk), our own vendor-neutral design of the ETIM 10.0 class EC011715 (Vibration
absorber mat), built unattended (OPERATING.md 12, generic elements; `python lib/build.py inventory mech` lists the class once no
inventory row builds unattended and the machine-element classes above it wait for a dimensional standard or a toolkit primitive,
lib/needs-em/mech.md). A 500 x 500 NBR mat 16 thick: a 10 core with 3 high ribs on both faces, 10 wide at a 25 pitch, the top ribs
along x and the bottom ribs along y, so two mats stacked lie rib across rib (the class's Stackable feature). The class values
(spec.md, "Class values") are design inputs; the class's Max. load is not stated, so no load or deflection is claimed and nothing
moves in the model. Every size is a design choice. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "mat-vibration", "1.0", "device"
TITLE = "vibration absorber mat, generic, NBR 500 x 500 x 16, ribbed both faces, ribs crossed for stacking"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic vibration absorber mat (ETIM 10.0 EC011715), NBR, 500 x 500 x 16 ribbed both faces; class "
            "values are design inputs (spec.md); every size a design choice; no load, deflection or damping claim; no vendor file "
            "opened")
ORIGIN = ("the floor face (the bottom ribs' underside, z = 0) at the mat's centre; the top ribs run along x, the bottom ribs along "
          "y; the top ribs' top face, where a machine's foot stands, at z 16")
COMMAND = "VIBMAT"
PARAMS = dict()

L, W = 500.0, 500.0                              # class values: length (x +-250) and width (y +-250)
CORE_T = 10.0                                    # the core sheet 10 thick: design choice
RIB_H, RIB_W, PITCH, N = 3.0, 10.0, 25.0, 20     # ribs 3 high, 10 wide, at 25 centres, 20 a face: design choice
T = CORE_T + 2 * RIB_H                           # class value: thickness 16
MAT = "M-GASKET"

assert T == 16.0
assert (N - 1) * PITCH + RIB_W <= W - 10.0                                 # the outer ribs 7.5 in from the mat's edges
assert RIB_H <= 3.0 and RIB_W >= 8.0 and CORE_T >= 8.0                     # the fillet gate's trap: no free-corner edge of 3 to 7 (mech-r101)
C0 = -(N - 1) * PITCH / 2                                                  # the first rib's centre line, -237.5


def build():
    P = Prims(); hl, hw = L / 2, W / 2
    P.box(MAT, -hl, -hw, RIB_H, L, W, CORE_T)                                                   # core sheet
    for i in range(N):
        c = C0 + i * PITCH
        P.box(MAT, -hl, c - RIB_W / 2, RIB_H + CORE_T, L, RIB_W, RIB_H)                         # top rib, along x
        P.box(MAT, c - RIB_W / 2, -hw, 0.0, RIB_W, W, RIB_H)                                    # bottom rib, along y
    P.collider("body", -hl, -hw, 0.0, L, W, T)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="end", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
