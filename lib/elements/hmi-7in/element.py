#!/usr/bin/env python3
"""hmi-7in: operator panel (HMI), 7 in colour touchscreen 800 x 480, 24 V DC, Ethernet, mounted in a panel cut-out and held by four
clamps. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC011541
"Display/operator panel", built to the class values in spec.md "## Class values"; no maker's datasheet (the vendor file in the
folder's references/ is reference only and was not opened; the earlier stub's record is kept verbatim as the end block of
references/source.txt, under this element's own).
What it meets comes from the elements on file: the four panel clamps are placed panel-clamp 1.2 elements (lib/inventory.csv made_of
"panel-clamp x4"; released), and the housing cuts the slot panel-clamp defines (its properties.csv: slot 10.4 x 7.0, at least 3.0
deep, its bearing face 30.0 behind the bezel's seating face); the supply terminals are a placed terminal-plug 2.0 (made_of
"terminal-plug"). Every other size is a design choice, said so in spec.md.
Not placed in 1.0 (OPERATING.md 12, quality at the source: a host places only common parts past station 6 and models no holes for a
part it will place later): port-rj45 and led of the inventory's made_of are not built yet. So 1.0 has no Ethernet socket modelled
(the class value says Ethernet; the socket comes with port-rj45, a later version) and its status lens is the toolkit's din.led.
Modelled from the outside in: the bezel on the panel's front face with the display (an emissive node, `screen`) and a status lens;
the housing through the cut-out with the four clamp slots in its top and bottom walls; the clamps in them; the supply plug on the
housing's back face. The display's cell, the touch sensor, the controller board and the power supply inside are not modelled."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "hmi-7in", "1.1", "device"
TITLE = "operator panel (HMI), 7 in colour touchscreen 800 x 480, 24 V DC, Ethernet, panel cut-out mount with 4 clamps (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Display/operator panel (ETIM 10.0 EC011541); class values in spec.md; the four clamps are placed "
            "panel-clamp 1.2 elements in the slot it defines, the supply terminals a placed terminal-plug 2.0; sizes are design choices")
ORIGIN = "cut-out centre on the panel front face; the bezel's seating face y = 0, the housing toward +y through the panel, display toward -y"
COMMAND = "HMI7IN"
PARAMS = {}

# ---- the display (design: 7 in diagonal, 800 x 480 square pixels, so 5:3; spec.md Class values 2 / 3 and Dimensions)
DIAG = 7.0 * 25.4                                   # 177.8 mm, the inventory's 7 in, a design input (EC011541 has no display-size feature; 1 in = 25.4 mm exactly)
SCR_W = DIAG * 5 / math.sqrt(5 ** 2 + 3 ** 2)        # 152.46: the active area's width (Pythagoras on the 5:3 aspect)
SCR_H = DIAG * 3 / math.sqrt(5 ** 2 + 3 ** 2)        # 91.48: its height
SCR_T, SCR_Z = 0.5, 6.0                              # the screen's face 0.5 proud of the bezel; its centre z 6 above the cut-out centre
# ---- bezel and housing (design choices)
BEZ_W, BEZ_H, BEZ_D = 200.0, 150.0, 8.0              # bezel x -100 ... 100, z -75 ... 75, y -8 ... 0 (its back face seats on the panel)
HOU_W, HOU_H, HOU_D = 186.0, 132.0, 50.0             # housing x -93 ... 93, z -66 ... 66, y 0 ... 50 through the cut-out
CUTOUT_RECT = (187.0, 133.0)                         # the panel's cut-out (w along x, h along z): the housing with 0.5 a side
# ---- the clamps: panel-clamp 1.2 placed in four slots, two in the top wall, two in the bottom (design: positions; the slot is the clamp's)
CLAMP = "1.2"                                        # panel-clamp version pinned
CL = library.load("panel-clamp", CLAMP)
SLOT_W, SLOT_L, SLOT_D = CL.HOOK_Y + 0.4, CL.HOOK_Z + 1.0, 3.0   # 10.4 x 7.0, 3.0 deep: panel-clamp properties.csv slot_width / slot_length / slot_depth_min
SEAT = CL.SEAT_Z                                     # 30.0: the slot's rear (bearing) face behind the bezel's seating face (slot_seat_distance)
CLAMP_X = (-60.0, 60.0)
# ---- supply plug: terminal-plug 2.0 placed on the housing's back face, body toward +y, wire entries down (design choices)
PLUG = "2.0"                                         # terminal-plug version pinned
X1 = dict(poles=3, x=80.0, z=-50.0)                  # 24V 0V FE; yaw 180 puts its poles along -x from x 80 (x 65 ... 80)
# ---- status lens and legend field on the bezel (design choices)
LED = ("led-run", "M-LENS-GREEN", 88.0, -62.0)
LEGEND = (-90.0, -30.0, -68.0, -56.0)                # x0, x1, z0, z1 on the bezel's face

def build():
    P = Prims(); B = "M-BLACK-PA"
    yf = -BEZ_D                                                                             # the bezel's front face (y -8)
    P.box(B, -BEZ_W / 2, yf, -BEZ_H / 2, BEZ_W, BEZ_D, BEZ_H)                               # bezel on the panel's front face
    housing = P.box("M-GREY-PA", -HOU_W / 2, 0.0, -HOU_H / 2, HOU_W, HOU_D, HOU_H)         # housing through the cut-out
    P.box("node:screen|M-LENS-DARK", -SCR_W / 2, yf - SCR_T, SCR_Z - SCR_H / 2, SCR_W, SCR_T, SCR_H)   # display / touch face
    P.pivot("screen", "emissive", (0.0, yf - SCR_T, SCR_Z), axis=(0, -1, 0), range=(0, 1))
    node, lens, lx, lz = LED; din.led(P, node, lens, lx, yf, lz)
    gx0, gx1, gz0, gz1 = LEGEND
    P.box("M-WHITE-PA", gx0, yf - 0.1, gz0, gx1 - gx0, 0.1, gz1 - gz0)                      # legend field (decal: generic label)
    zt = HOU_H / 2
    for k, (x, side) in enumerate([(x, s) for s in (1, -1) for x in CLAMP_X], start=1):
        zw = side * zt                                                                       # the wall's outer face (z +66 top, -66 bottom)
        z0 = zw - SLOT_D if side > 0 else zw                                                 # slot: blind, SLOT_D into the wall
        P.cutbox("M-GREY-PA", x - SLOT_W / 2, SEAT - SLOT_L, z0, SLOT_W, SLOT_L, SLOT_D, housing)
        # panel-clamp's frame: x out of the wall (here +-z), z toward the panel (here -y), origin on the slot's bearing face
        rot = dict(yaw=90.0, roll=-90.0) if side > 0 else dict(yaw=-90.0, roll=90.0)
        n0 = len(P)
        library.place(P, dict(element="panel-clamp", version=CLAMP, tag=f"clamp-{k}", parent="", x=x, y=SEAT, z=zw,
                              pitch=0.0, params={}, **rot))
        for i in range(n0, len(P)):                                                          # the clamp's own collider `body` joins this
            if P[i][0] == "collider:body": P[i] = ("collider:env",) + tuple(P[i][1:])        # element's `env` (no second collider named
                                                                                             # like the host's body node)
    library.place(P, dict(element="terminal-plug", version=PLUG, tag="x1", parent="", x=X1["x"], y=HOU_D, z=X1["z"], yaw=180.0,
                          params=dict(poles=X1["poles"])))
    P.collider("env", -BEZ_W / 2, yf - SCR_T, -BEZ_H / 2, BEZ_W, HOU_D + 16.0 - yf + SCR_T, BEZ_H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear clamps and plug", az=60, el=25),
            dict(name="supply plug x1", az=60, el=-20, center=(72.5, 58, -50), height=40)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
