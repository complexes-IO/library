#!/usr/bin/env python3
"""op-estop-22-2nc: 22.5 mm emergency-stop operator: Ø40 red mushroom, push-to-latch, twist-to-release, on a 60 x 60 yellow plate, two NC blocks."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import std22, library
from toolkit.prims import Prims

ID, VERSION, CLASS = "op-estop-22-2nc", "1.1", "operator-22"
TITLE = "22.5 mm E-stop, Ø40 mushroom, twist release, yellow plate, 2 NC blocks"
TOOLKIT = "1.3"
BASELINE = "IEC 60947-5-5 / ISO 13850 E-stop on the 22.5 mm cut-out (Rockwell 800F / Siemens 3SU1 class, measured, not shipped)"
ORIGIN = "cut-out centre on the panel front face; panel occupies 0 <= y <= panel_t; mushroom toward -y"
COMMAND = "OPES"
CUTOUT = std22.CUTOUT
PARAMS = dict(panel_t=3.0)
E = std22.ESTOP

def build(panel_t=3.0):
    P = Prims()
    pw, ph, pt = E["plate"]
    yp = P.box("M-YELLOW", -pw / 2, -pt, -ph / 2, pw, pt, ph); P.hole("M-GASKET", (0, -pt - 1, 0), (0, 1, 0), std22.CUTOUT / 2, yp)
    yf = -pt
    P.cyl("M-BLACK-PA", (0, yf, 0), (0, yf - E["collar_h"], 0), E["collar_r"])                                      # collar
    mh = P.cyl("node:self|M-RED", (0, yf - E["collar_h"], 0), (0, yf - E["collar_h"] - E["h"] + 4, 0), E["r"])      # mushroom
    P.hole("M-GASKET", (0, yf - E["collar_h"] + 1, 0), (0, yf - E["collar_h"] - 6.2, 0), E["collar_r"] + 0.3, mh)   # skirt recess: the head slides over the collar for its 6 stroke (1.1)
    P.cyl("node:self|M-RED", (0, yf - E["collar_h"] - E["h"] + 4, 0), (0, yf - E["collar_h"] - E["h"], 0), E["r"] - 4)   # crown
    std22.behind(P, panel_t, 2)
    P.pivot("self", "translate", (0, yf - E["collar_h"], 0), axis=(0, 1, 0), range=(0, 6.0))   # press 6 and latch; twist 45 deg to release
    P.collider("env", -30, yf - E["collar_h"] - E["h"], -39, 60, E["collar_h"] + E["h"] + pt + panel_t + 38, 69)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="behind latch and two NC blocks", az=60, el=20)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
