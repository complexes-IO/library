#!/usr/bin/env python3
"""ipc: industrial PC, box form, fanless, 24 V DC, two Ethernet ports, wall-mounted on its back plate. A generic element (OPERATING.md
12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC001413 "Industrial PC", built to the class values in spec.md
"## Class values"; no maker's datasheet (the vendor file in the folder's references/ is reference only and was not opened; the earlier
stub's record is kept verbatim as the end block of references/source.txt, under this element's own, and nothing here is taken from it).
What it meets comes from the standards and elements on file: the four fixing holes are ISO 273 medium clearance for M4
(lib/standards/holes.csv; the inventory's screw-iso7380 x4 is not built, so not placed); the two Ethernet sockets are placed port-rj45
1.0 elements (lib/inventory.csv made_of "port-rj45 x2", past station 6), each seated in a pocket of the housing's front wall, the
opening the host's to cut (port-rj45's spec); the supply terminals a placed terminal-plug 2.0 (made_of "terminal-plug"). Every other
size is a design choice, said so in spec.md.
Not placed in 1.0 (OPERATING.md 12, quality at the source: a host places only common parts past station 6): led and screw-iso7380 of
the inventory's made_of are not built. So the two status lenses are the toolkit's din.led (as plc-aio) and the fixing screws' holes are
modelled, as guard-interlock's.
Modelled from the back out: an aluminium back plate on the wall (the housing's heat spreader) with the four fixing holes in its
corners beyond the housing; the housing on it; on the housing's front face the two sockets, the supply plug, two status lenses and a
legend field. The board, the processor, the memory, the storage and the cooling fins are not modelled."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "ipc", "1.0", "device"
TITLE = "industrial PC, box, fanless, 24 V DC, 2 x Ethernet RJ45, wall mounting (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Industrial PC (ETIM 10.0 EC001413), box form; class values in spec.md; the two Ethernet sockets "
            "are placed port-rj45 1.0 elements, the supply terminals a placed terminal-plug 2.0; fixing holes ISO 273 medium for M4; "
            "sizes are design choices")
ORIGIN = ("wall-mounted device: the back plate's back face on the wall y = 0, x = 0 and z = 0 on the housing's centre; the body toward "
          "-y, the front face (sockets, plug, lenses) at y = -148")
COMMAND = "IPC"
PARAMS = {}

# ---- back plate (design choices: spec.md Dimensions); 8.0 thick keeps every envelope edge >= 8 (the AutoCAD fillet pre-flight)
PL_W, PL_T, PL_H = 110.0, 8.0, 240.0          # x -55 ... 55, y -8 ... 0, z -120 ... 120
FIX = [(sx * 47.5, sz * 110.0) for sz in (1, -1) for sx in (-1, 1)]   # four fixing holes' centres (x, z), beyond the housing
FIX_D = 4.5                                   # ISO 273 medium clearance for M4 (lib/standards/holes.csv), position Ø0.5 (features.csv)
# ---- housing (design choices)
HO_W, HO_D, HO_H = 80.0, 140.0, 200.0         # x -40 ... 40, y -148 ... -8, z -100 ... 100
# ---- Ethernet: port-rj45 1.0 placed twice, front face on the housing's front face, seated in a pocket its own size
RJ45 = "1.0"                                  # port-rj45 version pinned
RJ = library.load("port-rj45", RJ45)
ETH = (("x2", -12.0), ("x3", 12.0))           # LAN1, LAN2: socket centres x; both at z ETH_Z
ETH_Z = 50.0
# ---- supply: terminal-plug 2.0 placed on the front face, poles along +x, wire entries down (design choices)
PLUG = "2.0"                                  # terminal-plug version pinned
X1 = dict(poles=3, x=-7.5, z=-75.0)           # 24V 0V FE
# ---- status lenses and legend field on the front face (design choices)
LEDS = (("led-pwr", "M-LENS-GREEN", -30.0), ("led-run", "M-LENS-YELLOW", -22.0))
LED_Z = 88.0
LEGEND = (-10.0, 34.0, 82.0, 94.0)            # x0, x1, z0, z1

def build():
    P = Prims()
    plate = P.box("M-ALU-ANOD", -PL_W / 2, -PL_T, -PL_H / 2, PL_W, PL_T, PL_H)                      # back plate on the wall
    for fx, fz in FIX:
        P.hole("M-GASKET", (fx, 0.5, fz), (fx, -PL_T - 0.5, fz), FIX_D / 2, plate)                  # M4 fixing holes
    yf = -PL_T - HO_D                                                                               # the front face (y -148)
    housing = P.box("M-ALU-7035", -HO_W / 2, yf, -HO_H / 2, HO_W, HO_D, HO_H)                       # housing on the plate
    for tag, x in ETH:                                                                              # Ethernet sockets (placed, pinned)
        P.cutbox("M-ALU-7035", x - RJ.W / 2, yf - 1.0, ETH_Z - RJ.H / 2, RJ.W, RJ.D + 1.0, RJ.H, housing)
        library.place(P, dict(element="port-rj45", version=RJ45, tag=tag, parent="", x=x, y=yf, z=ETH_Z, yaw=0.0, params={}))
    library.place(P, dict(element="terminal-plug", version=PLUG, tag="x1", parent="", x=X1["x"], y=yf, z=X1["z"], yaw=0.0,
                          params=dict(poles=X1["poles"])))
    for node, lens, x in LEDS: din.led(P, node, lens, x, yf, LED_Z)
    lx0, lx1, lz0, lz1 = LEGEND
    P.box("M-WHITE-PA", lx0, yf - 0.1, lz0, lx1 - lx0, 0.1, lz1 - lz0)                              # legend field (decal: generic label)
    P.collider("env", -PL_W / 2, yf - 16.0, -PL_H / 2, PL_W, -yf + 16.0, PL_H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear: back plate and fixing holes", az=60, el=25),
            dict(name="front: sockets, plug, lenses", az=270, el=0, center=(0, -150, 0), height=230),
            dict(name="supply plug x1", az=240, el=-25, center=(0, -156, -75), height=40)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
