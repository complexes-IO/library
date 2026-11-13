#!/usr/bin/env python3
"""strip-rubber-cord-10: generic rubber cord, our own vendor-neutral design of the ETIM 10.0 class EC010643 (Rubber cord), built
unattended (OPERATING.md 12, generic elements; the EG019710 Profiles classes in generic.py's order by name, after
strip-rubber-bumper-40x22, mech-r139). A solid black EPDM round cord Ø10, no hollow core: the cord a machine lays in a groove as a
seal or a buffer, or bonds into a ring. Plain stock, cut to length (the `length` parameter; a parameter stays out of the id,
OPERATING.md 6). Not an O-ring: no ring, no ISO 3601 size is claimed, and the DIN 7715 tolerance class is "not stated". The class
values (spec.md, "Class values") are design inputs; no hardness, temperature or fire figure is claimed, and nothing moves. Every size
is a design choice. No vendor file was opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "strip-rubber-cord-10", "1.0", "rail"
TITLE = "Rubber cord, generic, solid EPDM, diameter 10, no hollow core, black, plain, cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic rubber cord (ETIM 10.0 EC010643), solid EPDM round cord D10, no hollow core, black, plain stock; "
            "class values are design inputs (spec.md); the diameter a design choice; DIN 7715 tolerance class not stated; not an O-ring; "
            "no hardness, temperature or fire claim; no vendor file opened")
ORIGIN = "run start x = 0, the cord's axis along +x at y = 0, z = 0 (the cord's centre line)"
COMMAND = "RUBBERCORD"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius, set per primitive below (as the other profiles, mech-r106 / r131)

D = 10.0                                     # the cord's diameter (class feature Diameter): a design choice
R = D / 2.0
MAT = "M-GASKET"                             # EPDM, solid, black (lib/materials.csv epdm; render layer M-GASKET, the library's black rubber)

assert D >= 8.0                                                              # the end faces' round edges (circumference 31.4) clear the 3 to 7 mm trap
AREA = math.pi * R * R
assert abs(AREA - 78.54) < 0.01                                              # by hand: π 5² = 78.54 mm²


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 100.0, "length 100 or more"
    P.cyl(MAT, (0, 0, 0), (L, 0, 0), R)                                                       # the cord, Ø10, solid
    P.collider("cord", 0, -R, -R, L, D, D)
    for i in range(len(P)): P.radii[i] = FILLET_R                                            # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 0, 0), height=30)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
