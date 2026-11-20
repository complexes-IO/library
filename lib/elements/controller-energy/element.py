#!/usr/bin/env python3
"""controller-energy: energy management controller, one RS-485 port to the plant's meters and one Ethernet port to the plant's
network, 24 V DC, on the 35 mm rail; it reads and reports, and has no power path of its own. A generic element (OPERATING.md 12,
EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC002758 "Energy management controller", built to the class
values in spec.md "## Class values"; no maker's datasheet, no product matched, nothing downloaded.
The reading of the class is the lane's (elec-r63, spec.md "Class choice"): the class's features cover both a controller and a unit
that carries the load (rated currents, reductions); this element is the controller alone, so every load-path feature reads "none".
What it meets comes from the contracts and elements on file: the rail clip from toolkit/din.py (rail_clip, the 35 x 7.5 rail of
din-rail-35 / EN 60715 TH35-7.5); the RS-485 and the supply terminals are two placed terminal-plug elements, version pinned (2.0);
the Ethernet socket is a placed port-rj45 1.0 (past station 6), seated in a pocket of the front block its own size, the opening
the host's to cut (port-rj45's spec). Every other size is a design choice, said so in spec.md.
Not placed in 1.0 (OPERATING.md 12, quality at the source: a host places only common parts past station 6 and models no holes for a
part it will place later): din-clip-35 and led are not built yet. So 1.0 holds to the rail by the toolkit's rail_clip and its two
status lenses are the toolkit's din.led (as daq 1.0 and plc-aio 1.1).
Modelled from the outside in: daq 1.0's stepped moulded housing on the rail clip (a base the full height, a front block on it), the
RS-485 plug x1 at the top of the front block's face, the supply plug x2 and the Ethernet socket x3 side by side below, two status
LEDs and a legend field between them; the processor, the isolation and the network electronics inside are not modelled."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "controller-energy", "1.0", "device"
TITLE = "energy management controller, 1 x RS-485, 1 x Ethernet RJ45, 24 V DC, plug-in screw terminals, 35 mm rail (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Energy management controller (ETIM 10.0 EC002758), a controller with no power path; class "
            "values in spec.md; rail clip from toolkit/din.py (EN 60715 TH35-7.5 rail, din-rail-35); RS-485 and supply terminals "
            "are placed terminal-plug 2.0 elements, the Ethernet socket a placed port-rj45 1.0; sizes are design choices")
ORIGIN = "rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward -y"
COMMAND = "CTRLENERGY"
PARAMS = {}

# ---- envelope (design choices, daq 1.0's housing; the class values Width / Height / Depth in spec.md)
W, H = 45.0, 100.0                   # width (x 0 ... 45), base height (z -50 ... 50), centred on the rail
BASE_D = 40.0                        # base: y -40 ... 0, the full height
FRONT_D, FRONT_Z = 30.0, 44.0        # front block: y -70 ... -40, z -44 ... 44 (6.0 of the base shows above and below)
# ---- terminals: terminal-plug 2.0 placed on the front block's face, mating face on it, wire entries down (design choices)
PLUG = "2.0"                         # terminal-plug version pinned
X1 = dict(poles=3, x=4.0, z=28.0)    # A B COM: the RS-485 pair and its signal common (spec.md Dimensions)
X2 = dict(poles=3, x=4.0, z=-36.0)   # 24V 0V FE: the supply and its functional earth
# ---- Ethernet: port-rj45 1.0 placed once, front face on the front block's face, seated in a pocket its own size
RJ45 = "1.0"                         # port-rj45 version pinned
RJ = library.load("port-rj45", RJ45)
X3 = dict(x=32.0, z=-32.0)           # the socket's centre: x 24 ... 40, z -39 ... -25 (5.0 clear of x2's body and of the block's edges)
# ---- LEDs and legend field on the front block's face (design choices)
LEDS = (("led-run", "M-LENS-GREEN", 8.0), ("led-err", "M-LENS-RED", 16.0))
LED_Z = 8.0
LEGEND = (22.0, 42.0, -16.0, 16.0)   # x0, x1, z0, z1

assert RJ.D + 1.0 < FRONT_D, "the socket's pocket must end inside the front block"
assert X2["x"] + 5.0 * X2["poles"] + 5.0 <= X3["x"] - RJ.W / 2, "5.0 between the supply plug and the socket"
assert X3["x"] + RJ.W / 2 + 5.0 <= W and X3["z"] - RJ.H / 2 - 5.0 >= -FRONT_Z, "5.0 of wall round the socket's pocket"

def build():
    P = Prims(); G = "M-GREY-PA"
    din.rail_clip(P, 0, W)                                                                  # the rail latch (toolkit contract)
    P.box(G, 0, -BASE_D, -H / 2, W, BASE_D, H)                                              # housing base on the clip
    y_f = -BASE_D - FRONT_D                                                                 # the front block's face (y -70)
    front = P.box(G, 0, y_f, -FRONT_Z, W, FRONT_D, 2 * FRONT_Z)                             # front block on the base
    P.cutbox(G, X3["x"] - RJ.W / 2, y_f - 1.0, X3["z"] - RJ.H / 2, RJ.W, RJ.D + 1.0, RJ.H, front)   # the socket's pocket
    library.place(P, dict(element="port-rj45", version=RJ45, tag="x3", parent="", x=X3["x"], y=y_f, z=X3["z"], yaw=0.0, params={}))
    for tag, X in (("x1", X1), ("x2", X2)):                                                 # RS-485 plug, supply plug (placed, pinned)
        library.place(P, dict(element="terminal-plug", version=PLUG, tag=tag, parent="", x=X["x"], y=y_f, z=X["z"], yaw=0.0,
                              params=dict(poles=X["poles"])))
    for node, lens, x in LEDS: din.led(P, node, lens, x, y_f, LED_Z)
    lx0, lx1, lz0, lz1 = LEGEND
    P.box("M-WHITE-PA", lx0, y_f - 0.1, lz0, lx1 - lx0, 0.1, lz1 - lz0)                     # legend field (decal: ports, supply, generic label)
    P.collider("env", 0, y_f - 16.0, -H / 2, W, -y_f + 16.0 + 7.5, H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear rail clip", az=60, el=25),
            dict(name="RS-485 plug x1", az=250, el=15, center=(22.5, -78, 30), height=40),
            dict(name="supply plug x2 and Ethernet socket x3", az=250, el=-20, center=(22.5, -78, -34), height=40)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
