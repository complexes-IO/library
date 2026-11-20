#!/usr/bin/env python3
"""diode-rail-3a: diode module on the 35 mm rail, one rectifier diode between two plug-in screw terminals (A anode, K cathode), 3 A,
250 V. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC004667 "Discrete
electronic component", built to the class value in spec.md "## Class values"; no maker's datasheet, no product matched, no vendor file
(the folder is new: the class is one of the "etim" lines of `python lib/build.py inventory elec`, no inventory row).
What it meets comes from the contracts and elements on file: the rail clip from toolkit/din.py (rail_clip, the 35 x 7.5 rail of
din-rail-35 / EN 60715 TH35-7.5); the two terminals are one placed terminal-plug element, version pinned (2.0). Every other size is
a design choice, said so in spec.md.
Not placed in 1.0 (OPERATING.md 12, quality at the source: a host places only common parts past station 6 and models no holes for a
part it will place later): din-clip-35 is not built yet, so 1.0 holds to the rail by the toolkit's rail_clip.
Modelled from the outside in: psu-ac-24v-2a5 1.0's stepped moulded housing at one narrow module's width (a base the full height, a
front block on it), the plug x1 at the foot of the front block's face and a legend field above it; the diode inside and its board
are not modelled."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "diode-rail-3a", "1.0", "device"
TITLE = "diode module, one rectifier diode A to K, 3 A 250 V, plug-in screw terminals, 35 mm rail (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Discrete electronic component (ETIM 10.0 EC004667); class values in spec.md; rail clip from "
            "toolkit/din.py (EN 60715 TH35-7.5 rail, din-rail-35); the terminals are a placed terminal-plug 2.0 element; sizes are "
            "design choices")
ORIGIN = "rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward -y"
COMMAND = "DIODER"
PARAMS = {}

# ---- envelope (design choices: psu-ac-24v-2a5 1.0's housing at one narrow module's width)
W, H = 18.0, 80.0                    # width (x 0 ... 18), base height (z -40 ... 40), centred on the rail
BASE_D = 40.0                        # base: y -40 ... 0, the full height
FRONT_D, FRONT_Z = 20.0, 34.0        # front block: y -60 ... -40, z -34 ... 34 (6.0 of the base shows above and below)
# ---- terminals: terminal-plug 2.0 placed on the front block's face, mating face on it, wire entries down (design choices)
PLUG = "2.0"                         # terminal-plug version pinned
X1 = dict(poles=2, x=4.0, z=-22.0)   # A K: pole 1 the anode, pole 2 the cathode (spec.md Dimensions)
# ---- legend field on the front block's face (design choice)
LEGEND = (2.0, 16.0, 0.0, 28.0)      # x0, x1, z0, z1

def build():
    P = Prims(); G = "M-GREY-PA"
    din.rail_clip(P, 0, W)                                                                  # the rail latch (toolkit contract)
    P.box(G, 0, -BASE_D, -H / 2, W, BASE_D, H)                                              # housing base on the clip
    y_f = -BASE_D - FRONT_D                                                                 # the front block's face (y -60)
    P.box(G, 0, y_f, -FRONT_Z, W, FRONT_D, 2 * FRONT_Z)                                     # front block on the base
    library.place(P, dict(element="terminal-plug", version=PLUG, tag="x1", parent="", x=X1["x"], y=y_f, z=X1["z"], yaw=0.0,
                          params=dict(poles=X1["poles"])))                                  # the A K plug (placed, pinned)
    lx0, lx1, lz0, lz1 = LEGEND
    P.box("M-WHITE-PA", lx0, y_f - 0.1, lz0, lx1 - lx0, 0.1, lz1 - lz0)                     # legend field (decal: diode symbol, ratings, generic label)
    P.collider("env", 0, y_f - 16.0, -H / 2, W, -y_f + 16.0 + 7.5, H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear rail clip", az=60, el=25),
            dict(name="plug x1", az=250, el=-20, center=(9.0, -68, -20), height=40)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
