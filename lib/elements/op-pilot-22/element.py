#!/usr/bin/env python3
"""op-pilot-22: 22.5 mm pilot light, Ø22 domed lens (emissive in the twin), LED lamp block, legend plate."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import std22, library
from toolkit.prims import Prims

ID, VERSION, CLASS = "op-pilot-22", "1.0", "operator-22"
TITLE = "22.5 mm pilot light, domed lens, LED block, legend plate"
TOOLKIT = "1.3"
BASELINE = "IEC 60947-5-1 22.5 mm operator standard (Rockwell 800F / Siemens 3SU1 class, measured, not shipped)"
ORIGIN = "cut-out centre on the panel front face; panel occupies 0 <= y <= panel_t; lens toward -y"
COMMAND = "OPPL"
CUTOUT = std22.CUTOUT
PARAMS = dict(colour="M-LENS-GREEN", legend=True, panel_t=3.0)

def build(colour="M-LENS-GREEN", legend=True, panel_t=3.0):
    P = Prims(); L = std22.LENS
    yf = std22.legend(P) if legend else 0.0
    std22.bezel(P, yf, L["r"] + 0.3)
    P.cyl(f"node:self|{colour}", (0, yf + 2, 0), (0, yf - std22.BEZEL["proud"] - L["dome"] + 2, 0), L["r"])
    P.cyl(f"node:self|{colour}", (0, yf - std22.BEZEL["proud"] - L["dome"] + 2, 0), (0, yf - std22.BEZEL["proud"] - L["dome"], 0), L["r"] - 3)
    std22.behind(P, panel_t, 1)
    P.pivot("self", "emissive", (0, yf - std22.BEZEL["proud"], 0), axis=(0, -1, 0), range=(0, 1))
    P.collider("env", -15, yf - 10, -33, 30, panel_t + 48, 50)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="behind latch and lamp block", az=60, el=20),
            dict(name="white power variant", az=250, el=20, params=dict(colour="M-LENS-WHITE"))]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
