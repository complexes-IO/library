#!/usr/bin/env python3
"""plc-aio: PLC analogue I/O module, 4 analogue inputs and 2 analogue outputs, each channel 0 ... 10 V or 4 ... 20 mA, 24 V DC, on the
35 mm rail. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC001420 "PLC
analogue I/O-module", built to the class values in spec.md "## Class values"; no maker's datasheet (the vendor file in the folder's
references/ is reference only and was not opened; its record was replaced by this element's, references/source.txt).
What it meets comes from the contracts and elements on file: the rail clip from toolkit/din.py (rail_clip, the 35 x 7.5 rail of
din-rail-35 / EN 60715 TH35-7.5); the input and the supply / output terminals are two placed terminal-plug elements (lib/inventory.csv
made_of "terminal-plug x2"), version pinned (2.0); every other size is a design choice, said so in spec.md.
Not placed in 1.0 (OPERATING.md 12, quality at the source: a host places only common parts past station 6 and models no holes for a
part it will place later): din-clip-35 and led of the inventory's made_of are not built yet. So 1.0 holds to the rail by the
toolkit's rail_clip and its two status lenses are the toolkit's din.led (as servo-drive 1.0).
1.1 (elec-r46): text only (review elec-r33 findings 1 and 4), the geometry is 1.0's.
Modelled from the outside in: a moulded housing on the rail clip, stepped (a base the full height, a front block on it), the two plugs
on the front block's face (x1 the inputs at the top, x2 the supply and the outputs below), two status LEDs and a legend field between
them; the converters, the isolation and the bus inside are not modelled."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "plc-aio", "1.1", "device"
TITLE = "PLC analogue I/O module, 4 AI + 2 AO, 0-10 V / 4-20 mA, 12 bit, 24 V DC, plug-in screw terminals, 35 mm rail (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic PLC analogue I/O-module (ETIM 10.0 EC001420); class values in spec.md; rail clip from "
            "toolkit/din.py (EN 60715 TH35-7.5 rail, din-rail-35); input, supply and output terminals are placed terminal-plug 2.0 "
            "elements; sizes are design choices")
ORIGIN = "rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward -y"
COMMAND = "PLCAIO"
PARAMS = {}

# ---- envelope (design choices; the class values Width / Height / Depth in spec.md)
W, H = 45.0, 100.0                   # width (x 0 ... 45), base height (z -50 ... 50), centred on the rail
BASE_D = 40.0                        # base: y -40 ... 0, the full height
FRONT_D, FRONT_Z = 30.0, 44.0        # front block: y -70 ... -40, z -44 ... 44 (6.0 of the base shows above and below)
# ---- terminals: terminal-plug 2.0 placed on the front block's face, mating face on it, wire entries down (design choices)
PLUG = "2.0"                         # terminal-plug version pinned
X1 = dict(poles=8, x=2.5, z=28.0)    # AI0+ AI0- AI1+ AI1- AI2+ AI2- AI3+ AI3-: the four differential inputs (spec.md Dimensions)
X2 = dict(poles=7, x=5.0, z=-36.0)   # 24V 0V FE AO0 M0 AO1 M1: the module supply, its earth and the two outputs
# ---- LEDs and legend field on the front block's face (design choices)
LEDS = (("led-run", "M-LENS-GREEN", 8.0), ("led-err", "M-LENS-RED", 16.0))
LED_Z = 8.0
LEGEND = (22.0, 42.0, -16.0, 16.0)   # x0, x1, z0, z1

def build():
    P = Prims(); G = "M-GREY-PA"
    din.rail_clip(P, 0, W)                                                                  # the rail latch (toolkit contract)
    P.box(G, 0, -BASE_D, -H / 2, W, BASE_D, H)                                              # housing base on the clip
    y_f = -BASE_D - FRONT_D                                                                 # the front block's face (y -70)
    P.box(G, 0, y_f, -FRONT_Z, W, FRONT_D, 2 * FRONT_Z)                                     # front block on the base
    for tag, X in (("x1", X1), ("x2", X2)):                                                 # input plug, supply / output plug (placed, pinned)
        library.place(P, dict(element="terminal-plug", version=PLUG, tag=tag, parent="", x=X["x"], y=y_f, z=X["z"], yaw=0.0,
                              params=dict(poles=X["poles"])))
    for node, lens, x in LEDS: din.led(P, node, lens, x, y_f, LED_Z)
    lx0, lx1, lz0, lz1 = LEGEND
    P.box("M-WHITE-PA", lx0, y_f - 0.1, lz0, lx1 - lx0, 0.1, lz1 - lz0)                     # legend field (decal: channels, ranges, generic label)
    P.collider("env", 0, y_f - 16.0, -H / 2, W, -y_f + 16.0 + 7.5, H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear rail clip", az=60, el=25),
            dict(name="input plug x1", az=250, el=15, center=(22.5, -78, 30), height=40),
            dict(name="supply and output plug x2", az=230, el=-30, center=(22.5, -78, -36), height=40)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
