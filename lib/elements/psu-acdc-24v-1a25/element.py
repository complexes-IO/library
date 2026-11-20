#!/usr/bin/env python3
"""psu-acdc-24v-1a25: AC/DC power supply, 120 V AC single-phase in, two outputs: 24 V AC 1.25 A and 24 V DC 1.25 A (60 W in all),
not stabilised, on the 35 mm rail. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0
class EC002542 "AC/DC-power supply", built to the class values in spec.md "## Class values"; no maker's datasheet, no product matched,
no vendor file (the folder is new: the class is one of the "etim" lines of `python lib/build.py inventory elec`, no inventory row).
What it meets comes from the contracts and elements on file: the rail clip from toolkit/din.py (rail_clip, the 35 x 7.5 rail of
din-rail-35 / EN 60715 TH35-7.5); the input and the two outputs' terminals are three placed terminal-plug elements, version pinned
(2.0). Every other size is a design choice, said so in spec.md.
Not placed in 1.0 (OPERATING.md 12, quality at the source: a host places only common parts past station 6 and models no holes for a
part it will place later): din-clip-35 and led are not built yet. So 1.0 holds to the rail by the toolkit's rail_clip and its two
status lenses are the toolkit's din.led (as psu-ac-24v-2a5 1.0).
Modelled from the outside in: psu-ac-24v-2a5 1.0's stepped moulded housing on the rail clip (a base the full height, a front block on
it), the input plug x1 at the top of the front block's face, the AC output plug x2 and the DC output plug x3 side by side at its
foot, two status LEDs and a legend field between them; the transformer, its windings, the rectifier, the smoothing and any
protection inside are not modelled."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "psu-acdc-24v-1a25", "1.0", "device"
TITLE = ("AC/DC power supply, 120 V AC in, 24 V AC 1.25 A and 24 V DC 1.25 A out (60 W), not stabilised, plug-in screw terminals, "
         "35 mm rail (complexes.org generic)")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic AC/DC-power supply (ETIM 10.0 EC002542); class values in spec.md; rail clip from toolkit/din.py "
            "(EN 60715 TH35-7.5 rail, din-rail-35); input and output terminals are placed terminal-plug 2.0 elements; sizes are "
            "design choices")
ORIGIN = "rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward -y"
COMMAND = "PSUACDC"
PARAMS = {}

# ---- envelope (design choices, psu-ac-24v-2a5 1.0's housing; the class values Width / Height / Depth in spec.md)
W, H = 45.0, 100.0                   # width (x 0 ... 45), base height (z -50 ... 50), centred on the rail
BASE_D = 40.0                        # base: y -40 ... 0, the full height
FRONT_D, FRONT_Z = 30.0, 44.0        # front block: y -70 ... -40, z -44 ... 44 (6.0 of the base shows above and below)
# ---- terminals: terminal-plug 2.0 placed on the front block's face, mating face on it, wire entries down (design choices)
PLUG = "2.0"                         # terminal-plug version pinned
X1 = dict(poles=3, x=4.0, z=28.0)    # L N PE: the 120 V AC input and the protective earth (spec.md Dimensions)
X2 = dict(poles=2, x=4.0, z=-36.0)   # AC1 AC2: the 24 V AC output
X3 = dict(poles=2, x=28.0, z=-36.0)  # +V -V: the 24 V DC output, 14.0 to the right of x2's body
# ---- LEDs and legend field on the front block's face (design choices)
LEDS = (("led-ac", "M-LENS-GREEN", 8.0), ("led-dc", "M-LENS-GREEN", 15.0))
LED_Z = 8.0
LEGEND = (22.0, 42.0, -16.0, 16.0)   # x0, x1, z0, z1

def build():
    P = Prims(); G = "M-GREY-PA"
    din.rail_clip(P, 0, W)                                                                  # the rail latch (toolkit contract)
    P.box(G, 0, -BASE_D, -H / 2, W, BASE_D, H)                                              # housing base on the clip
    y_f = -BASE_D - FRONT_D                                                                 # the front block's face (y -70)
    P.box(G, 0, y_f, -FRONT_Z, W, FRONT_D, 2 * FRONT_Z)                                     # front block on the base
    for tag, X in (("x1", X1), ("x2", X2), ("x3", X3)):                                     # input plug, AC and DC output plugs (placed, pinned)
        library.place(P, dict(element="terminal-plug", version=PLUG, tag=tag, parent="", x=X["x"], y=y_f, z=X["z"], yaw=0.0,
                              params=dict(poles=X["poles"])))
    for node, lens, x in LEDS: din.led(P, node, lens, x, y_f, LED_Z)
    lx0, lx1, lz0, lz1 = LEGEND
    P.box("M-WHITE-PA", lx0, y_f - 0.1, lz0, lx1 - lx0, 0.1, lz1 - lz0)                     # legend field (decal: ratings, terminal diagram, generic label)
    P.collider("env", 0, y_f - 16.0, -H / 2, W, -y_f + 16.0 + 7.5, H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear rail clip", az=60, el=25),
            dict(name="input plug x1", az=250, el=15, center=(22.5, -78, 30), height=40),
            dict(name="output plugs x2 x3", az=250, el=-20, center=(22.5, -78, -34), height=40)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
