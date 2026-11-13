#!/usr/bin/env python3
"""profile-angle-pvc-30x30x3: generic equal-leg plastic angle profile, our own vendor-neutral design of the ETIM 10.0 class EC010681
(Plastic angle profile), built unattended (OPERATING.md 12, generic elements; the EG019710 Profiles classes in generic.py's order by
name, after the I-profiles of mech-r134). An extruded rigid PVC equal angle 30 x 30, wall 3, sharp inner and outer corners, white,
not perforated: an edge trim, corner guard or light cover angle. Plain stock, cut to length (the `length` parameter; a parameter
stays out of the id, OPERATING.md 6); no holes: a host that fixes it drills its own and declares them in its own features.csv. Every
size is a design choice (no dimensional standard shapes a plastic angle). The class values (spec.md, "Class values") are design
inputs; the class has no load or temperature feature, so none is claimed, and nothing moves. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "profile-angle-pvc-30x30x3", "1.0", "rail"
TITLE = "angle profile, plastic, generic, rigid PVC equal legs 30 x 30, wall 3, sharp corners, white, not perforated, cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic plastic angle profile (ETIM 10.0 EC010681), an extruded rigid PVC equal-leg angle 30 x 30 x 3 "
            "with sharp corners, white, not perforated, plain stock; class values are design inputs (spec.md); every size a design "
            "choice; no load, temperature or fire claim; no vendor file opened")
ORIGIN = ("run start x = 0, the angle's outer corner line y = 0, z = 0 (the heel); the run along +x, one leg along +y (the foot, its "
          "underside z 0), the other along +z (the upright, its outer face y 0)")
COMMAND = "ANGLEPVC"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius, set per primitive below (as the other thin-walled profiles, mech-r106 / r131)

A, B, T = 30.0, 30.0, 3.0                    # leg along y, leg along z, wall: design choices (an equal angle, the class's "Model")
MAT = "M-WHITE-PVC"                          # rigid PVC, white (lib/materials.csv pvc; render layer M-WHITE-PVC)

assert A == B and T <= 3.0                                                   # equal legs; the 3.0 wall's edges are "short", skipped by the gate
assert A - T >= 8.0                                                          # the legs' inner faces 27: clear of the 3 to 7 mm free-corner trap (mech-r69)
AREA = A * T + (B - T) * T                                                   # the section: two rectangles, no overlap
assert abs(AREA - 171.0) < 1e-9                                              # by hand: 30 x 3 + 27 x 3 = 171 mm²


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 100.0, "length 100 or more"
    body = P.box(MAT, 0, 0, 0, L, A, B)                                      # the angle: one box ...
    P.cutbox(MAT, -1.0, T, T, L + 2.0, A - T + 1.0, B - T + 1.0, body)       # ... less its inside: foot 30 x 3, upright 3 x 30, one solid
    P.collider("foot", 0, 0, 0, L, A, T)
    P.collider("upright", 0, 0, T, L, T, B - T)
    for i in range(len(P)): P.radii[i] = FILLET_R                            # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 15, 15), height=60)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
