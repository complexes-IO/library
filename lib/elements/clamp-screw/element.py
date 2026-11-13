#!/usr/bin/env python3
"""clamp-screw: the screw clamp of a terminal (a terminal block, a contactor or relay terminal), as its own element: the cage the wire goes
through, the clamping screw (rotate, with its torque window) and the clamp's contact zone. toolkit/contact.py terminate() decides what
it makes of a wire end: inserted how far, stripped how long, the screw at what torque, the size inside its range or not.
Frame: the mouth at the origin on the wire axis, the wire inserted along +y, the screw head toward -z. Brief: references/measure.md."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "clamp-screw", "1.1", "contact"
TITLE = "screw clamp (cage, M3 screw), with wire range, strip length and torque window"
TOOLKIT = "1.3"
BASELINE = "own design: cage 5.1 x 10.4 x 7.5 and screw head Ø4.0 from the term-4mm STEP read-back (references of term-4mm); wire range 22-10 AWG on file (McMaster 7641K21 page); torque, strip length and grip NOT ON FILE (Assumption)"
ORIGIN = "the mouth of the cage on the wire axis; the wire goes in along +y; the screw head toward -z"
COMMAND = "CLAMP"
PARAMS = dict(size_min=0.33, size_max=5.26, torque_min=0.5, torque_max=0.8, strip=10.0, condition="ok", cage_w=5.1)
CAGE = (5.1, 7.5, 10.4)          # x across, y along the wire, z along the screw (term-4mm STEP read-back: 5.1 x 10.4 x 7.5)
WINDOW = (4.0, 5.0)              # the wire window, x and z: takes a 6 mm2 conductor (Ø2.8) with room
GRIP = 5.0                       # mm of bare conductor the clamp needs under it for a reliable contact (Assumption)

def build(size_min=0.33, size_max=5.26, torque_min=0.5, torque_max=0.8, strip=10.0, condition="ok", cage_w=5.1):
    """cage_w: 5.1 in a 6.0 feed-through block, 4.5 in a 5.0 ground block (the ground STEP's clamp parts are 4.5 wide)"""
    P = Prims(); _, L, h = CAGE; w = cage_w; wx = min(WINDOW[0], w - 1.0); wz = WINDOW[1]; z0 = -wz / 2 - 3.9                                       # cage bottom: 3.9 of thread under the window
    mat = "M-CU-CORRODED" if condition == "corroded" else "M-ZINC"
    cage = P.box(f"node:self|{mat}", -w / 2, 0, z0, w, L, h)
    P.cutbox("M-GASKET", -wx / 2, -1.0, -wz / 2, wx, L + 2.0, wz, cage)                                    # the window, through along the wire
    P.hole("M-GASKET", (0, L / 2, z0 - 1.0), (0, L / 2, -wz / 2), 1.5, cage)                                # the screw's thread (M3)
    P.cyl("node:screw|M-ZINC", (0, L / 2, z0 - 0.6), (0, L / 2, -wz / 2), 1.5)                              # screw shank, its tip at the window floor (open)
    P.cyl("node:screw|M-ZINC", (0, L / 2, z0 - 3.0), (0, L / 2, z0 - 0.6), 2.0)                             # head Ø4.0 (STEP read-back)
    P.pivot("screw", "rotate", (0, L / 2, 0), axis=(0, 0, 1), range=(0, 720), unit="deg", lead=0.5, torque=(torque_min, torque_max))
    P.pivot("self", "contact", (0, 0, 0), axis=(0, 1, 0), range=(0.5, L), unit="mm", gender="clamp", size_min=size_min, size_max=size_max,
            grip=GRIP, strip=strip, window=(wx, wz), torque=(torque_min, torque_max), condition=condition)
    P.collider("env", -w / 2, 0, z0 - 3.0, w, L, h + 3.0)
    return P

PREVIEWS = [dict(name="clamp", az=230, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
