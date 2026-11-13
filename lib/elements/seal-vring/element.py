#!/usr/bin/env python3
"""seal-vring: an all-rubber V-ring seal, the axial lip seal stretched onto a rotating shaft (a pump's, a gearbox's, a motor's), where it
turns with the shaft and its lip runs against a counterface across the shaft (a housing's face, a bearing cover), keeping splash, dust
and grease out of the bearing. Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC010422 "V-ring
seal"; the class values it is designed to are in spec.md "## Class values". No dimensional standard on file sizes a V-ring
(lib/standards/sources.csv has none): its section and its bore's stretch on the shaft are design choices (spec.md Dimensions). The
ring lies flat, its axis on z, the lip toward +z. The toolkit's primitives have no cone, so the lip's flare is drawn as two rings
stepped outward (an appearance, class C). Nothing moves on its own and nothing connects: no port, no node. No vendor file was opened
(pneu-r104)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "seal-vring", "1.0", "connector-part"
TITLE = "generic V-ring seal, NBR, for a 40 mm shaft"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic V-ring seal (ETIM 10.0 EC010422), an all-rubber axial lip seal stretched onto the shaft; its "
            "section, its lip's steps and its bore's stretch on the shaft are design choices")
ORIGIN = "the centre of the body's back face (z = 0) on the shaft axis; the ring lies flat, its axis along +z, the lip toward +z"
COMMAND = "SEAL-VRING"
PARAMS = dict(shaft=40.0)

SHAFTS = (30.0, 40.0, 50.0)          # design choices: the shaft diameters built, mm
STRETCH = 0.90                       # design choice: the free bore is 0.90 x the shaft, so the ring grips the shaft and turns with it
BODY_H, BODY_W = 5.0, 5.0            # design choices: the body's radial height and axial width, mm
LIP1 = (3.0, 6.5, 3.0)               # design choices: the lip's root ring: inner and outer radius over the bore radius, axial width
LIP2 = (5.5, 9.0, 3.0)               # design choices: the lip's tip ring, stepped outward over the root ring
MAT = "M-GASKET"                     # class value: NBR, black (the black rubber material on file)

for _a, _b, _w in (LIP1, LIP2):
    assert _b - _a >= 3.0 and _w >= 3.0            # every ring's wall at least 3 (the fillet pre-flight's 2.5 r with margin)
assert LIP1[0] < BODY_H < LIP1[1]                  # the root ring stands on the body's front face (z = BODY_W) and overhangs it
assert LIP1[0] < LIP2[0] < LIP1[1] < LIP2[1]       # the tip ring stands on the root ring and overhangs it: the lip flares outward


def bore(shaft=40.0):
    """the free bore: STRETCH x the shaft (36.0 for a 40 shaft)"""
    return STRETCH * float(shaft)


def build(shaft=40.0):
    shaft = float(shaft)
    if shaft not in SHAFTS: raise ValueError(f"shaft {shaft:g}: one of {', '.join(f'{s:g}' for s in SHAFTS)} mm")
    r0 = bore(shaft) / 2.0
    P = Prims()
    body = P.cyl(MAT, (0, 0, 0), (0, 0, BODY_W), r0 + BODY_H)                            # the body, gripping the shaft
    P.hole(MAT, (0, 0, -1.0), (0, 0, BODY_W + 1.0), r0, body)                           # its bore, on the shaft
    z = BODY_W
    for a, b, w in (LIP1, LIP2):                                                         # the lip's two rings, each on the last face to face
        ring = P.cyl(MAT, (0, 0, z), (0, 0, z + w), r0 + b)
        P.hole(MAT, (0, 0, z - 1.0), (0, 0, z + w + 1.0), r0 + a, ring)
        z += w
    ro = r0 + LIP2[1]
    P.collider("env", -ro, -ro, 0, 2 * ro, 2 * ro, z)
    return P


PREVIEWS = [dict(name="three-quarter, 40 shaft", az=250, el=35), dict(name="side", az=200, el=5),
            dict(name="30 shaft", az=250, el=35, params=dict(shaft=30.0)),
            dict(name="50 shaft", az=250, el=35, params=dict(shaft=50.0))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
