#!/usr/bin/env python3
"""slide-profile-product: generic product line slide profile, plastic, our own vendor-neutral design of the ETIM 10.0 class EC010731
(Product line slide profile, plastic), built unattended (OPERATING.md 12, generic elements; `python lib/build.py inventory mech` lists
the machine-element classes in order: EC011968 Gear wheel before it waits on the gear standards and EC010448 Plastic ball on a sphere
solid, lib/needs-em/mech.md). The strip the goods of a product line slide along as they pass on a conveyor: a plastic guide strip 12
thick and 40 high bonded on the outer face of a galvanized steel mounting angle 50 x 60 x 3, whose foot screws to the conveyor's
frame with M6 clearance holes (ISO 273 medium), so the strip's face stands as the line's side guide. Cut to length (the `length`
parameter; a parameter stays out of the id, OPERATING.md 6). slide-profile-flat-belt's sibling (EC010730): the same plastic, the same
galvanized mounting, the same holes. The class values (spec.md, "Class values") are design inputs; the class has no load, speed or
friction feature, so none is claimed and nothing moves in the model (the goods and the conveyor are the host's). Every size is a design
choice. No vendor file was opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "slide-profile-product", "1.1", "rail"
TITLE = "product line slide profile, plastic, generic, guide strip 12 x 40 on a 50 x 60 x 3 mounting angle, M6 foot holes, cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic product line slide profile, plastic (ETIM 10.0 EC010731), a PE-UHMW guide strip on the outer face "
            "of a galvanized steel mounting angle whose foot carries M6 holes at ISO 273 medium clearance; class values are design "
            "inputs (spec.md); every size a design choice; no load, speed or friction claim; no vendor file opened")
ORIGIN = ("run start x = 0, the angle's outer corner line y = 0 (the upright leg's face the strip is bonded to), the foot's underside "
          "z = 0 (the mounting face, on the frame); the run along +x, the foot toward +y, the strip's guide face toward -y at y -12")
COMMAND = "SLIDEPROFPL"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                                   # the gate's radius, set per primitive below (the rail class's 1.0 reads 10 mm edges short, mech-r69 / r106)

ST, SH, SZ = 12.0, 40.0, 15.0                    # the guide strip 12 thick (y), 40 high (z), its underside 15 over the frame: design choices
AT, FOOT, LEG = 3.0, 50.0, 60.0                  # the mounting angle 3 thick, foot 50 (y), upright leg 60 high (z): design choices (3.0: the gate's "short" edge)
HOLE_D = 6.6                                     # M6 clearance medium H13 (ISO 273, lib/standards/holes.csv)
HOLE_Y = 30.0                                    # the holes' line in the foot, y 30: design: an M6 head up to Ø10.5 clears the upright leg's
                                                 # inner face (y 3) by 21.75 and the foot's edge (y 50) by 14.75 (a design allowance; screw-head
                                                 # standards not on file)
END = 50.0                                       # the end holes 50 in from each end; between them at most HOLE_PITCH apart
HOLE_PITCH = 450.0
MAT_P = "M-WHITE-PA"                             # the guide strip, appearance only (white): PE-UHMW (spec.md; no PE layer in godot/qa/materials)
MAT_A = "M-GALV"                                 # the mounting angle, galvanized steel

assert SZ + SH <= LEG and SZ >= 8.0                                        # the strip on the upright leg, under its top, 15 over the foot
assert ST >= 8.0 and SH >= 8.0                                             # the strip's end edges 12 and 40 (clear of the fillet trap: 3 to 7)
assert HOLE_Y - 5.25 - AT >= 2.0 and FOOT - HOLE_Y - 5.25 >= 2.0           # the screw head clears the upright leg and the foot's edge
assert FOOT - HOLE_Y - HOLE_D / 2 >= 1.5 * AT                              # DFM-010: hole edge distance 1.5 t or more
assert AT <= 3.0                                                         # the angle's 3.0 edges "short", skipped by the gate


def hole_xs(L):
    """the holes' x positions: END in from each end, evenly between at most HOLE_PITCH apart"""
    n = int(math.ceil((L - 2 * END) / HOLE_PITCH)) + 1
    return [END + k * (L - 2 * END) / (n - 1) for k in range(n)]


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 200.0, "length 200 or more"
    foot = P.box(MAT_A, 0, 0, 0, L, FOOT, LEG)                                           # the mounting angle: one box ...
    P.cutbox(MAT_A, -1.0, AT, AT, L + 2.0, FOOT - AT + 1.0, LEG - AT + 1.0, foot)        # ... less its inside: foot 50 x 3, upright leg 3 x 60, one solid
    P.box(MAT_P, 0, -ST, SZ, L, ST, SH)                                                  # the guide strip, bonded on the leg's outer face
    for x in hole_xs(L):
        P.hole(MAT_A, (x, HOLE_Y, -1.0), (x, HOLE_Y, AT + 1.0), HOLE_D / 2, foot)        # M6 clearance through the foot
    P.collider("guide", 0, -ST, 0, L, ST + AT, LEG)
    P.collider("foot", 0, AT, 0, L, FOOT - AT, AT)
    for i in range(len(P)): P.radii[i] = FILLET_R                                        # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 19, 30), height=120)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
