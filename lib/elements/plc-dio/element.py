#!/usr/bin/env python3
"""plc-dio: PLC digital I/O module, 8 digital inputs and 8 digital outputs, 24 V DC, on the 35 mm rail. A generic element (OPERATING.md 12,
EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC001419 "PLC digital I/O-module", built to the class values in
spec.md "## Class values"; no maker's datasheet (the vendor file in the folder's references/ is reference only and was not opened; its
record was replaced by this element's, references/source.txt).
What it meets comes from the contracts and elements on file: the rail clip from toolkit/din.py (rail_clip, the 35 x 7.5 rail of
din-rail-35 / EN 60715 TH35-7.5); the input and the output terminals are two placed terminal-plug elements (lib/inventory.csv made_of
"terminal-plug x2"), version pinned (2.0); every other size is a design choice, said so in spec.md.
Not placed in 1.0 (OPERATING.md 12, quality at the source: a host places only common parts past station 6 and models no holes for a
part it will place later): din-clip-35 and led of the inventory's made_of are not built yet. So 1.0 holds to the rail by the
toolkit's rail_clip and its 16 channel lenses and two status lenses are the toolkit's din.led (as plc-aio 1.0).
The same body as plc-aio 1.0 (a stepped moulded housing on the rail clip), 60 wide for two 10- and 11-pole plugs: x1 the module supply
and the inputs at the top, x2 the output supply and the outputs below; a row of input LEDs, a row of output LEDs, two status LEDs and
a legend field between them; the input circuits, the output switches and the bus inside are not modelled."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "plc-dio", "1.0", "device"
TITLE = "PLC digital I/O module, 8 DI + 8 DO, 24 V DC, transistor outputs 0.5 A, plug-in screw terminals, 35 mm rail (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic PLC digital I/O-module (ETIM 10.0 EC001419); class values in spec.md; rail clip from "
            "toolkit/din.py (EN 60715 TH35-7.5 rail, din-rail-35); input and output terminals are placed terminal-plug 2.0 "
            "elements; sizes are design choices")
ORIGIN = "rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward -y"
COMMAND = "PLCDIO"
PARAMS = {}

# ---- envelope (design choices; the class values Width / Height / Depth in spec.md)
W, H = 60.0, 100.0                   # width (x 0 ... 60: the 11-pole plug's 55 and 2.5 each side), base height (z -50 ... 50)
BASE_D = 40.0                        # base: y -40 ... 0, the full height (as plc-aio 1.0)
FRONT_D, FRONT_Z = 30.0, 44.0        # front block: y -70 ... -40, z -44 ... 44 (as plc-aio 1.0)
# ---- terminals: terminal-plug 2.0 placed on the front block's face, mating face on it, wire entries down (design choices)
PLUG = "2.0"                         # terminal-plug version pinned
X1 = dict(poles=11, x=2.5, z=28.0)   # 24V 0V FE DI0 ... DI7: the module supply, its functional earth and the eight inputs
X2 = dict(poles=10, x=5.0, z=-36.0)  # 24VO 0VO DO0 ... DO7: the output supply and the eight outputs
# ---- LEDs and legend field on the front block's face (design choices)
CH_X0, CH_PITCH = 17.5, 5.0          # channel lenses: x 17.5 ... 52.5, one above each pole pitch
DI_Z, DO_Z = 14.0, -18.0             # the input row under x1, the output row over x2
STATUS = (("led-run", "M-LENS-GREEN", 6.0), ("led-err", "M-LENS-RED", 12.0))
STATUS_Z = -2.0
LEGEND = (17.0, 55.0, -10.0, 6.0)    # x0, x1, z0, z1

def build():
    P = Prims(); G = "M-GREY-PA"
    din.rail_clip(P, 0, W)                                                                  # the rail latch (toolkit contract)
    P.box(G, 0, -BASE_D, -H / 2, W, BASE_D, H)                                              # housing base on the clip
    y_f = -BASE_D - FRONT_D                                                                 # the front block's face (y -70)
    P.box(G, 0, y_f, -FRONT_Z, W, FRONT_D, 2 * FRONT_Z)                                     # front block on the base
    for tag, X in (("x1", X1), ("x2", X2)):                                                 # input plug, output plug (placed, pinned)
        library.place(P, dict(element="terminal-plug", version=PLUG, tag=tag, parent="", x=X["x"], y=y_f, z=X["z"], yaw=0.0,
                              params=dict(poles=X["poles"])))
    for k in range(8):                                                                      # channel LEDs: inputs above, outputs below
        din.led(P, f"led-di{k}", "M-LENS-YELLOW", CH_X0 + CH_PITCH * k, y_f, DI_Z)
        din.led(P, f"led-do{k}", "M-LENS-YELLOW", CH_X0 + CH_PITCH * k, y_f, DO_Z)
    for node, lens, x in STATUS: din.led(P, node, lens, x, y_f, STATUS_Z)
    lx0, lx1, lz0, lz1 = LEGEND
    P.box("M-WHITE-PA", lx0, y_f - 0.1, lz0, lx1 - lx0, 0.1, lz1 - lz0)                     # legend field (decal: channels, ratings, generic label)
    P.collider("env", 0, y_f - 16.0, -H / 2, W, -y_f + 16.0 + 7.5, H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear rail clip", az=60, el=25),
            dict(name="input plug x1", az=250, el=15, center=(30, -78, 30), height=40),
            dict(name="output plug x2", az=230, el=-30, center=(30, -78, -36), height=40)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
