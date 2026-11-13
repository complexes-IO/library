#!/usr/bin/env python3
"""port-rj45: an RJ45 (8P8C modular) Ethernet socket, the device side of a twisted-pair joint: an insulating housing with the plug's
opening in its front face and eight female spring contacts on the opening's top face. A generic element (OPERATING.md 12, EM 2026-11-07):
our own vendor-neutral design of ETIM 10.0 EC001121 "Modular connector", built to the class values in spec.md "## Class values"; no
maker's datasheet and no product is matched. A common part (lib/inventory.csv row port-rj45, own_design generic: "RJ45 Ethernet socket
(IEC 60603-7)"): hmi-7in, ipc, eth-switch-din, power-meter, ups-rack and gateway-fieldbus list it in their made_of.
What it meets: the mating plug's face. The opening, the latch slot and the contacts' pitch and order are IEC 60603-7's (the 8-way
modular connector's mating interface), and that standard is not on file (lib/standards/sources.csv has no row): NOT ON FILE (B), drawn to
the design layout in spec.md, so a maker's plug is not claimed to fit. The host places it behind its wall with the front face on the
wall's outer face and cuts the wall's opening itself (the host's figure).
Modelled: the housing (one solid, the opening and the latch slot cut into its front face), the eight contacts (each a port node, gender
female). Not modelled: a metal shield (this design is unshielded), the contacts' tails into the host's board, link / activity LEDs (led
is not built: OPERATING.md 12, quality at the source), the board-lock pegs. Nothing moves."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "port-rj45", "1.0", "connector"
TITLE = "RJ45 (8P8C) Ethernet socket, unshielded, 8 female contacts, front opening (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Modular connector (ETIM 10.0 EC001121), an 8P8C RJ45 socket; class values in spec.md; the mating "
            "face (opening, latch slot, contact pitch and order) NOT ON FILE (B): IEC 60603-7, drawn to a design layout; every other "
            "size a design choice")
ORIGIN = ("the housing's front face y = 0 (the face that sits on the host's wall's outer face), x = 0 and z = 0 on the housing's centre; "
          "the mating plug toward -y, the housing behind the front face (inside the host) toward +y")
COMMAND = "RJ45P"
PARAMS = {}

# ---- housing (design choices: spec.md Dimensions)
W, H, D = 16.0, 14.0, 21.0            # x -8 ... 8, z -7 ... 7, y 0 ... 21
# ---- the plug's opening (design layout: the mating face NOT ON FILE (B), IEC 60603-7; spec.md)
OPEN_W, OPEN_Z0, OPEN_Z1 = 11.8, -3.0, 5.0     # the opening 11.8 wide, z -3.0 ... 5.0 (8.0 high)
SLOT_W, SLOT_Z0 = 6.0, -5.5                    # the latch slot under it, 6.0 wide, z -5.5 ... -3.0 (2.5)
OPEN_D = 15.0                                  # both 15.0 deep from the front face (y 0 ... 15); the back wall 6.0
# ---- contacts (design layout, as the opening)
N, PITCH = 8, 1.0                     # eight contacts at a 1.0 pitch, contact 1 at x -3.5 (left, seen from the front, the slot down)
CW, CH = 0.5, 0.6                     # each 0.5 wide, 0.6 thick, on the opening's top face (z 4.4 ... 5.0)
CY0, CY1 = 5.0, 13.0                  # from y 5.0 (the tip, the port node) to y 13.0

def contacts():
    """[(mark, x)] of the eight contacts, contact 1 at -x"""
    return [(str(k + 1), round(-(N - 1) * PITCH / 2 + k * PITCH, 4)) for k in range(N)]

def build():
    P = Prims()
    hs = P.box("M-BLACK-PA", -W / 2, 0.0, -H / 2, W, D, H)                                       # housing, front face y 0
    P.cutbox("M-GASKET", -OPEN_W / 2, -1.0, OPEN_Z0, OPEN_W, OPEN_D + 1.0, OPEN_Z1 - OPEN_Z0, hs)  # the plug's opening
    P.cutbox("M-GASKET", -SLOT_W / 2, -1.0, SLOT_Z0, SLOT_W, OPEN_D + 1.0, OPEN_Z0 - SLOT_Z0 + 0.5, hs)  # the latch slot, into it
    for mark, x in contacts():                                                                   # contacts on the top face
        node = f"c-{mark}"
        P.box(f"node:{node}|M-GOLD", x - CW / 2, CY0, OPEN_Z1 - CH, CW, CY1 - CY0, CH)
        P.pivot(node, "port", (x, CY0, OPEN_Z1 - CH / 2), axis=(0, -1, 0), range=(0, 0), unit="rj45", gender="female")
    P.collider("env", -W / 2, 0.0, -H / 2, W, D, H)
    return P

PREVIEWS = [dict(name="three-quarter", az=250, el=25), dict(name="mating face", az=270, el=0, center=(0, 0, 0), height=18)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
