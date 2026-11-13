#!/usr/bin/env python3
"""profile-angle-alu-40x40x3: generic equal-leg aluminium angle profile, our own vendor-neutral design of the ETIM 10.0 class EC012022
(Angle profile, aluminium), built unattended (OPERATING.md 12, generic elements; `python lib/build.py inventory mech` lists the ETIM
classes in generic.py's group order: EG020017 and EG020054 are done or wait on their standards, lib/needs-em/mech.md, so the first
class of EG019710 Profiles). Plain stock: an extruded equal angle 40 x 40, wall 3, sharp inner and outer corners, anodised, cut to
length (the `length` parameter; a parameter stays out of the id, OPERATING.md 6). No holes: a host that bolts it drills its own and
declares them in its own features.csv. The class values (spec.md, "Class values") are design inputs; the class has no load
feature, so none is claimed, and nothing moves. Every size is a design choice. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "profile-angle-alu-40x40x3", "1.0", "rail"
TITLE = "angle profile, aluminium, generic, equal legs 40 x 40, wall 3, sharp corners, anodised, plain (no holes), cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic angle profile, aluminium (ETIM 10.0 EC012022), an extruded equal-leg angle 40 x 40 x 3 with "
            "sharp corners, anodised, plain stock; class values are design inputs (spec.md); every size a design choice; no load claim; "
            "no vendor file opened")
ORIGIN = ("run start x = 0, the angle's outer corner line y = 0, z = 0 (the heel); the run along +x, one leg along +y (the foot, its "
          "underside z 0), the other along +z (the upright, its outer face y 0)")
COMMAND = "ANGLEALU"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius, set per primitive below (the rail class's 1.0 reads 3 mm walls badly, mech-r69 / r106)

A, B, T = 40.0, 40.0, 3.0                    # leg along y, leg along z, wall: design choices (an equal angle, the class's "Model")
MAT = "M-ALU-ANOD"                           # anodised aluminium (lib/materials.csv al-6063; no temper claimed)

assert A == B and T <= 3.0                                                   # equal legs; the 3.0 wall's edges are "short", skipped by the gate
assert A - T >= 8.0                                                          # the legs' inner faces 37: clear of the 3 to 7 mm free-corner trap
AREA = A * T + (B - T) * T                                                   # the section: two rectangles, no overlap
assert abs(AREA - 231.0) < 1e-9                                              # by hand: 40 x 3 + 37 x 3 = 231 mm²


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 100.0, "length 100 or more"
    body = P.box(MAT, 0, 0, 0, L, A, B)                                      # the angle: one box ...
    P.cutbox(MAT, -1.0, T, T, L + 2.0, A - T + 1.0, B - T + 1.0, body)       # ... less its inside: foot 40 x 3, upright 3 x 40, one solid
    P.collider("foot", 0, 0, 0, L, A, T)
    P.collider("upright", 0, 0, T, L, T, B - T)
    for i in range(len(P)): P.radii[i] = FILLET_R                            # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 20, 20), height=80)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
