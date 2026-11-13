#!/usr/bin/env python3
"""damping-rod: generic damping rod (a straight rubber-metal rail: the rail-shaped machine mount that carries a machine or a frame
on a rubber block between two steel flats), our own vendor-neutral design of the ETIM 10.0 class EC003749 (Damping rod), built
unattended (OPERATING.md 12, generic elements; `python lib/build.py inventory mech` lists the class as the next mech class once no
inventory row builds unattended and the two classes above it wait for their dimensional standards). The straight sibling of
damping-rod-angle (EC003741): a steel base flat 110 x 200 x 10 with four M10 clearance holes beside the rubber, a rubber block
46 x 190 x 30 bonded on it, and a steel top flat 50 x 200 x 15 bonded on the rubber with two M10 tapped holes for the machine's
foot. A vertical load works the rubber in compression, a side load in shear. The class values (spec.md, "Class values") are design
inputs; the class has no stiffness or load feature, so no load or deflection is claimed and nothing moves in the model. The M10
thread's limits are derived (spec.md, What it meets); the tapped holes are drawn plain at D1. Every other size is a design choice.
No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "damping-rod", "1.1", "device"
TITLE = "damping rod, generic, straight rubber-metal rail, 110 x 200 x 55, rubber block 46 x 190 x 30, 4 x M10 base holes, 2 x M10 tapped"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic damping rod (ETIM 10.0 EC003749), a straight rubber-metal rail; class values are design "
            "inputs (spec.md); base holes at M10's ISO 273 medium clearance; the M10 tapped holes derived (ISO 68-1, ISO 965-1), "
            "drawn plain at D1; every size a design choice; no load, stiffness or deflection claim; no vendor file opened")
ORIGIN = ("the mounting face (the base flat's underside, z = 0) at the rail's centre; y along the rail, x across it; the top flat's "
          "top face, where the machine's foot seats, at z 55")
COMMAND = "DAMPROD"
PARAMS = dict()

W, L, H = 110.0, 200.0, 55.0                     # class values: width (x +-55, the base flat), length (y +-100), height (z 0..55)
BASE_T = 10.0                                    # base flat 110 x 200 x 10: design choice
HOLE_X, HOLE_Y = 42.0, 70.0                      # base holes at x +-42, y +-70: design choice
HOLE_D = 11.0                                    # M10 clearance medium H13 (ISO 273, lib/standards/holes.csv)
RUB_W, RUB_L, RUB_T = 46.0, 190.0, 30.0          # rubber block 46 x 190 x 30: design choice (2 inside the top flat's sides, 5 short of each end)
TOP_W, TOP_T = 50.0, 15.0                        # top flat 50 x 200 x 15: design choice
TAP_Y, TAP_DEPTH = 60.0, 12.0                    # two M10 tapped holes in the top flat at y +-60, 12 deep (blind: 3 of steel over the rubber)
TAP_D1 = 8.3762                                  # M10 x 1.5, 6H: D1 min, derived: derive.thread(10.0, 1.5) (ISO 68-1; ISO 965-1 clause 10)
HEAD_R = 9.0                                     # design: a hexagon head up to Ø18 at the base holes (a design allowance; screw-head standards not on file)
MAT, RUB = "M-ZINC", "M-GASKET"

assert BASE_T + RUB_T + TOP_T == H
assert HOLE_X - HEAD_R >= TOP_W / 2 + 8.0                                  # a bolt head clears the top flat and the rubber by 8 or more
assert W / 2 - HOLE_X - HOLE_D / 2 >= 7.0                                  # 7.5 of steel outside each hole
assert TOP_W - RUB_W == 4.0 and L - RUB_L == 10.0                          # no rubber face coplanar with a steel face (GEO-050)
assert TOP_T - TAP_DEPTH >= 3.0                                            # the tapped holes end in the top flat


def build():
    P = Prims(); hw, hl = W / 2, L / 2
    base = P.box(MAT, -hw, -hl, 0.0, W, L, BASE_T)                                              # base flat, on the floor or frame
    for x in (-HOLE_X, HOLE_X):
        for y in (-HOLE_Y, HOLE_Y):
            P.hole(MAT, (x, y, -1.0), (x, y, BASE_T + 1.0), HOLE_D / 2, base)                  # M10 clearance holes
    P.box(RUB, -RUB_W / 2, -RUB_L / 2, BASE_T, RUB_W, RUB_L, RUB_T)                            # rubber block, bonded both faces
    top = P.box(MAT, -TOP_W / 2, -hl, BASE_T + RUB_T, TOP_W, L, TOP_T)                         # top flat, carries the machine's foot
    for y in (-TAP_Y, TAP_Y):
        P.hole(MAT, (0, y, H - TAP_DEPTH), (0, y, H + 1.0), TAP_D1 / 2, top)                   # M10 tapped holes, plain at D1
    P.collider("body", -hw, -hl, 0.0, W, L, BASE_T + RUB_T)
    P.collider("top", -TOP_W / 2, -hl, BASE_T + RUB_T, TOP_W, L, TOP_T)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="end", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
