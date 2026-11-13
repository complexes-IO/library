#!/usr/bin/env python3
"""op-pb-22-1no: 22.5 mm flush pushbutton operator, momentary, with one contact block and a legend plate."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import std22, library
from toolkit.prims import Prims

ID, VERSION, CLASS = "op-pb-22-1no", "1.1", "operator-22"
TITLE = "22.5 mm flush pushbutton, momentary, 1 contact block, legend plate"
TOOLKIT = "1.3"
BASELINE = "IEC 60947-5-1 22.5 mm operator standard (Rockwell 800F / Siemens 3SU1 class, measured, not shipped)"
ORIGIN = "cut-out centre on the panel front face; panel occupies 0 <= y <= panel_t; cap toward -y"
COMMAND = "OPPB"
CUTOUT = std22.CUTOUT
PARAMS = dict(colour="M-GREEN", legend=True, panel_t=3.0, blocks=1)

def build(colour="M-GREEN", legend=True, panel_t=3.0, blocks=1):
    P = Prims()
    yf = std22.legend(P) if legend else 0.0
    std22.bezel(P, yf, std22.CAP["r"] + 0.3)
    P.cyl(f"node:self|{colour}", (0, yf + 2, 0), (0, yf - std22.BEZEL["proud"] + 0.3, 0), std22.CAP["r"])                   # cap, flush with the bezel
    P.cyl(f"node:self|{colour}", (0, yf - std22.BEZEL["proud"] + 0.3, 0), (0, yf - std22.BEZEL["proud"] - 0.6, 0), std22.CAP["r"] - 1.5)   # cap crown
    std22.behind(P, panel_t, blocks, bore=std22.CAP["r"] + 0.3)                       # the cap travels into the latch bore (1.1)
    P.pivot("self", "translate", (0, yf, 0), axis=(0, 1, 0), range=(0, std22.CAP["travel"]))
    P.collider("env", -15, yf - 4, -33, 30, panel_t + 8 + 30 - yf + 4, 50)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="behind latch and contact block", az=60, el=20),
            dict(name="red stop variant", az=250, el=20, params=dict(colour="M-RED"))]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
