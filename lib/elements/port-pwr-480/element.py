#!/usr/bin/env python3
"""port-pwr-480: IEC 60309 pin-and-sleeve receptacle, 3P+E 480 V 20 A, red, hinged cap, wall mount. Brief: references/measure.md
(plate 79 x 79, 4 x Ø5.2 on 60 x 60, cap Ø78.5 x 22.7, depth 60 + 46 + 22.2)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din, sweep as SW
from toolkit.prims import Prims

ID, VERSION, CLASS = "port-pwr-480", "1.1", "connector"
TITLE = "pin-and-sleeve receptacle 3P+E 480 V 20 A, IP67, hinged cap, 79 mm square flange"
TOOLKIT = "1.3"
BASELINE = "Bryant C420R7WA class via AutomationDirect (2-D drawing p. 1; instruction sheet p. 2); IEC 60309-2 7 h, red for 480 V"
ORIGIN = "cut-out centre class: plate centre on the wall's front face y = 0, cap and socket toward -y, rear body toward +y"
COMMAND = "P480"
CUTOUT = 52.0                        # wall clearance hole: NOT ON FILE, the rear body Ø plus 2 (Assumption)
PARAMS = dict(open=False)
PL, PT, HP = 79.0, 4.0, 60.0         # plate, thickness (from the STEP class, Assumption), hole pattern
BODY_D, REAR, CAP_R, CAP_H = 46.0, 22.2, 39.25, 22.7

def build(open=False):
    P = Prims()
    pl = P.box("M-RED-PA", -PL / 2, -PT, -PL / 2, PL, PT, PL)
    for sx in (-1, 1):
        for sz in (-1, 1):
            P.hole("M-GASKET", (sx * HP / 2, -PT - 1, sz * HP / 2), (sx * HP / 2, 1, sz * HP / 2), 2.6, pl)
            P.cyl("M-ZINC", (sx * HP / 2, -PT, sz * HP / 2), (sx * HP / 2, -PT - 2.0, sz * HP / 2), 4.0)
    P.cyl("M-RED-PA", (0, -PT, 0), (0, -PT - BODY_D, 0), 26.0)                                     # body to the socket face
    P.cyl("node:self|M-BLACK-PC", (0, -PT - BODY_D + 0.8, 0), (0, -PT - BODY_D - 0.2, 0), 22.0)      # socket face (3P+E at 7 h: decal)
    P.pivot("self", "port", (0, -PT - BODY_D, 0), axis=(0, -1, 0), range=(0, 0), unit="480V-3P+E")
    hz = 30.0; hy = -PT - BODY_D                                                                     # cap hinge at the top of the face
    P.cyl("node:cap|M-RED-PA", (0, hy, 0), (0, hy - CAP_H, 0), CAP_R)
    P.box("node:cap|M-RED-PA", -12, hy - CAP_H + 2, hz - 2, 24, 8, 12)                               # hinge knuckle
    P.pivot("cap", "rotate", (0, hy, hz + 4), axis=(1, 0, 0), range=(0, -100))                      # open angle from the STEP (~100), outward (1.1: was inward)
    P.cyl("M-RED-PA", (0, 0, 0), (0, REAR, 0), 24.0)                                                 # rear body through the wall
    P.collider("env", -PL / 2, hy - CAP_H, -PL / 2, PL, CAP_H + BODY_D + PT + REAR, PL)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="rear body", az=60, el=20)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
