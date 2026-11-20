#!/usr/bin/env python3
"""stack-light: signal tower (stack light) with three continuous-light elements, green, yellow and red from the base up, Ø50, each
lit from its own terminal at 24 V DC against a common 0 V. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral
design of the ETIM 10.0 class EC001042 "Signal tower complete", built to the class values in spec.md "## Class values"; no maker's
datasheet (the folder's earlier stub is reference only and was not used; its record is kept unread at the end of
references/source.txt). Not a safety-function device.
What it meets comes from the standards on file: the two fixing holes are ISO 273 medium clearance for M4 (lib/standards/holes.csv) and
the cable entry is M20 x 1.5 tapped, its minor diameter derived (derive.thread, ISO 68-1 / ISO 965-1). Every other size is a design
choice, said so in spec.md.
Not placed in this version (OPERATING.md 12, quality at the source): receptacle-m12 and led of the inventory's made_of are not past
station 6 (led is not built), so this is the cable-entry form with screw clamps, and each light element is drawn here as one lit
node; screw-iso7380 is not built, so the two fixing holes stand open.
Modelled from the mounting face up: the base as a frame (a floor block with the cable entry, two fixing ears, two side walls, a back
wall and a top block) round a terminal compartment closed by a front cover; four terminal screw heads on the back wall (the port
nodes t-C, t-1, t-2, t-3); the three light elements (nodes lamp-green, lamp-yellow, lamp-red) stacked face to face on the top block,
and a cap. Nothing moves."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "stack-light", "1.0", "device"
TITLE = "signal tower, 3 continuous-light elements green / yellow / red, Ø50, 24 V DC, terminals C 1 2 3, base 60 x 60 with two M4 ears, M20 x 1.5 entry (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Signal tower complete (ETIM 10.0 EC001042); class values in spec.md; fixing holes ISO 273 medium "
            "for M4 (lib/standards/holes.csv); cable entry M20 x 1.5 derived (ISO 68-1 / ISO 965-1); base, light element and cap sizes "
            "are design choices; the terminals' conductor range and torque are open (spec.md)")
ORIGIN = "the base's bottom (mounting) face z = 0, x = 0 and y = 0 the tower's axis (the cable entry's axis), front cover toward -y"
COMMAND = "STACKLT"
PARAMS = {}

# ---- base (design choices: spec.md Dimensions)
W, D = 60.0, 60.0                    # base 60 x 60 (x ±30, y ±30)
FLOOR_H = 8.0                        # floor block z 0 ... 8, carries the cable entry
TOP = (40.0, 48.0)                   # top block z 40 ... 48, carries the light elements
WALL, BACK, COVER = 4.0, 4.0, 3.0    # side walls x ±26 ... ±30, back wall y 26 ... 30, front cover y -30 ... -27 (z 8 ... 40)
EAR = (20.0, 8.0)                    # fixing ears: 20 out from each side (x ±30 ... ±50), full depth, z 0 ... 8
# ---- what it meets (standards on file)
FIX_D = 4.5                          # ISO 273 medium clearance for M4 (lib/standards/holes.csv; features.csv)
FIX_X = 40.0                         # the two fixing holes at x ±40, y 0, through the ears (z): design choice
ENTRY_D = 18.3762                    # M20 x 1.5 internal thread's minor diameter D1, derived: derive.thread(20.0, 1.5) (ISO 68-1, ISO 965-1)
# ---- terminals (design choices; their conductor range and torque NOT ON FILE (B): IEC 60947-1)
HEAD_R, HEAD_T = 2.2, 1.2            # terminal screw heads Ø4.4 x 1.2 on the back wall's front face (y 26)
TERM_Z = 24.0
TERMS = (("t-C", -15.0), ("t-1", -5.0), ("t-2", 5.0), ("t-3", 15.0))   # node, x
LABEL = (-20.0, 20.0, 14.0, 34.0)    # label field on the cover: x0, x1, z0, z1 (decal)
# ---- light elements and cap (design choices)
LAMP_R, LAMP_H = 25.0, 40.0          # each light element Ø50 x 40
LAMPS = (("lamp-green", "M-LENS-GREEN"), ("lamp-yellow", "M-LENS-YELLOW"), ("lamp-red", "M-LENS-RED"))   # from the base up
CAP_H = 8.0                          # cap Ø50 x 8 on the top element

def build():
    P = Prims(); G = "M-GREY-PA"; K = "M-BLACK-PA"
    w, d = W / 2, D / 2; z0, z1 = TOP; yb = d - BACK
    floor = P.box(G, -w, -d, 0.0, W, D, FLOOR_H)                                           # floor block
    P.hole("M-GASKET", (0, 0, -0.5), (0, 0, FLOOR_H + 0.5), ENTRY_D / 2, floor)            # M20 x 1.5 cable entry (minor Ø, derived)
    el, eh = EAR
    for sx in (-1, 1):                                                                     # fixing ears, one M4 clearance hole each
        ear = P.box(G, w if sx > 0 else -w - el, -d, 0.0, el, D, eh)
        P.hole("M-GASKET", (sx * FIX_X, 0, -0.5), (sx * FIX_X, 0, eh + 0.5), FIX_D / 2, ear)
    hw = z0 - FLOOR_H
    for sx in (-1, 1):                                                                     # side walls
        P.box(G, sx * w - (WALL if sx > 0 else 0.0), -d + COVER, FLOOR_H, WALL, D - COVER, hw)
    P.box(G, -w + WALL, yb, FLOOR_H, W - 2 * WALL, BACK, hw)                               # back wall (terminals on its front face)
    P.box(G, -w, -d, FLOOR_H, W, COVER, hw)                                                # front cover over the compartment
    P.box(G, -w, -d, z0, W, D, z1 - z0)                                                    # top block
    for n, x in TERMS:                                                                     # terminal screw heads: the port nodes
        P.cyl(f"node:{n}|M-ZINC", (x, yb, TERM_Z), (x, yb - HEAD_T, TERM_Z), HEAD_R)
        P.pivot(n, "port", (x, yb - HEAD_T, TERM_Z), axis=(0, -1, 0), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp
    x0, x1, lz0, lz1 = LABEL
    P.box("M-WHITE-PA", x0, -d - 0.6, lz0, x1 - x0, 0.6, lz1 - lz0)                        # label field on the cover (decal)
    z = z1
    for n, m in LAMPS:                                                                     # light elements, face to face
        P.cyl(f"node:{n}|{m}", (0, 0, z), (0, 0, z + LAMP_H), LAMP_R)
        P.pivot(n, "emissive", (0, 0, z), axis=(0, 0, 1), range=(0, 1)); z += LAMP_H
    P.cyl(K, (0, 0, z), (0, 0, z + CAP_H), LAMP_R)                                         # cap
    P.collider("env", -w - el, -d - 0.6, 0.0, W + 2 * el, D + 0.6, z + CAP_H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear", az=60, el=20),
            dict(name="front", az=270, el=0),
            dict(name="underside, cable entry and fixing holes", az=230, el=-50, center=(0, 0, 5), height=80),
            dict(name="front cover and label", az=270, el=0, center=(0, -30, 24), height=56)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
