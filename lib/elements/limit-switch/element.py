#!/usr/bin/env python3
"""limit-switch: end (position) switch with a roller lever, one N.C. and one N.O. contact (11-12, 23-24), slow action, AC-15 3 A at
230 V / DC-13 2 A at 24 V, plastic housing 30 x 30 x 80 with an M20 x 1.5 cable entry. A generic element (OPERATING.md 12, EM
2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC000030 "End switch", built to the class values in spec.md
"## Class values"; no maker's datasheet (the folder's earlier stub is reference only and was not used; its record is replaced by this
element's, references/source.txt). Not a safety-function device: no forced (positive) opening is claimed (Class values 14 and 28).
What it meets comes from the standards on file: the two fixing holes are ISO 273 medium clearance for M5 (lib/standards/holes.csv) and
the cable entry is M20 x 1.5 tapped, its minor diameter derived (derive.thread, ISO 68-1 / ISO 965-1). The housing's form follows
no standard on file (the standard form of a position switch's housing and fixing pattern, EN 50047, is not in
lib/standards/sources.csv): every other size is a design choice, said so in spec.md.
Not placed in this version (OPERATING.md 12, quality at the source): the installer's cable gland in the entry (no gland element past
station 6 is pinned here) and the contact block's springs and bridges inside.
Modelled from the outside in: the housing as a frame (a base block with the cable entry, two side walls, a back wall, a top block
with the two fixing holes) round a terminal compartment closed by a front cover; four terminal screw heads on the back wall (the port
nodes t-11, t-12, t-23, t-24); the rotary head on top; the lever (node `lever`: its shaft, arm and roller), which swings ±45° in the
front plane about the head's shaft."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "limit-switch", "1.1", "device"
TITLE = "end switch, roller lever, 1 N.C. + 1 N.O. (11-12, 23-24), AC-15 3 A 230 V, DC-13 2 A 24 V, housing 30 x 30 x 80, M20 x 1.5 entry (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic End switch (ETIM 10.0 EC000030); class values in spec.md; fixing holes ISO 273 medium for M5 "
            "(lib/standards/holes.csv); cable entry M20 x 1.5 derived (ISO 68-1 / ISO 965-1); housing, head and lever sizes are design "
            "choices; the terminals' conductor range and torque are open (spec.md)")
ORIGIN = "the housing's back (mounting) face y = 0, x = 0 the centreline, z = 0 the base's bottom face (cable entry), body toward -y"
COMMAND = "LIMITSW"
PARAMS = {}

# ---- housing (design choices: spec.md Dimensions)
W, D = 30.0, 30.0                    # housing 30 wide (x ±15), 30 deep (y -30 ... 0)
BASE_H = 10.0                        # base block z 0 ... 10, carries the cable entry
TOP = (48.0, 60.0)                   # top block z 48 ... 60, carries the two fixing holes
WALL, BACK, COVER = 4.0, 4.0, 3.0    # side walls x ±11 ... ±15, back wall y -4 ... 0, front cover y -30 ... -27 (z 10 ... 48)
# ---- what it meets (standards on file)
FIX_D = 5.5                          # ISO 273 medium clearance for M5 (lib/standards/holes.csv; features.csv)
FIX = ((-8.0, 54.0), (8.0, 54.0))    # (x, z) of the two fixing holes, through y: design choice (EN 50047's pattern not on file)
ENTRY_D = 18.3762                    # M20 x 1.5 internal thread's minor diameter D1, derived: derive.thread(20.0, 1.5) (ISO 68-1, ISO 965-1)
ENTRY = (0.0, -15.0)                 # (x, y) of the entry's axis, up through the base into the compartment
# ---- terminals (design choices; their conductor range and torque NOT ON FILE (B): IEC 60947-1)
HEAD_R, HEAD_T = 2.2, 1.2            # terminal screw heads Ø4.4 x 1.2 on the back wall's front face (y -4)
TERMS = (("t-11", -5.0, 36.0), ("t-12", -5.0, 22.0), ("t-23", 5.0, 36.0), ("t-24", 5.0, 22.0))   # node, x, z
LABEL = (-10.0, 10.0, 28.0, 44.0)    # label field on the cover: x0, x1, z0, z1 (decal)
# ---- head and lever (design choices)
HEAD = (60.0, 80.0)                  # rotary head z 60 ... 80, full section
SHAFT = (70.0, 3.0, 6.0)             # lever shaft: axis height z, radius, length out of the head's front face (y -30 ... -36)
ARM = (8.0, 4.0, 64.0, 102.0)        # arm: width (x), thickness (y -40 ... -36), z from ... to
ROLLER = (9.0, 8.0)                  # roller Ø18 x 8 (y -48 ... -40), axis at the arm's top end (z 102)
TRAVEL = 45.0                        # the lever swings ±45° in the front plane (x-z); the contacts change over at its operating point

def build():
    P = Prims(); G = "M-GREY-PA"; K = "M-BLACK-PA"
    w = W / 2; ztop0, ztop1 = TOP; yi = -BACK
    base = P.box(G, -w, -D, 0.0, W, D, BASE_H)                                             # base block
    ex, ey = ENTRY
    P.hole("M-GASKET", (ex, ey, -0.5), (ex, ey, BASE_H + 0.5), ENTRY_D / 2, base)          # M20 x 1.5 cable entry (minor Ø, derived)
    hw = ztop0 - BASE_H
    for sx in (-1, 1):                                                                     # side walls
        P.box(G, sx * w - (WALL if sx > 0 else 0.0), -D + COVER, BASE_H, WALL, D - COVER, hw)
    P.box(G, -w + WALL, yi, BASE_H, W - 2 * WALL, BACK, hw)                                # back wall (terminals on its front face)
    P.box(G, -w, -D, BASE_H, W, COVER, hw)                                                 # front cover over the compartment
    top = P.box(G, -w, -D, ztop0, W, D, ztop1 - ztop0)                                     # top block
    for fx, fz in FIX:                                                                     # two M5 clearance holes, ISO 273 medium
        P.hole("M-GASKET", (fx, 0.5, fz), (fx, -D - 0.5, fz), FIX_D / 2, top)
    for n, x, z in TERMS:                                                                  # terminal screw heads: the port nodes
        P.cyl(f"node:{n}|M-ZINC", (x, yi, z), (x, yi - HEAD_T, z), HEAD_R)
        P.pivot(n, "port", (x, yi - HEAD_T, z), axis=(0, -1, 0), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp
    x0, x1, z0, z1 = LABEL
    P.box("M-WHITE-PA", x0, -D - 0.6, z0, x1 - x0, 0.6, z1 - z0)                           # label field on the cover (decal)
    h0, h1 = HEAD
    P.box(K, -w, -D, h0, W, D, h1 - h0)                                                    # rotary head
    zs, rs, ls = SHAFT; aw, at, a0, a1 = ARM; rr, rl = ROLLER
    ya = -D - ls                                                                           # the arm's back face (y -36)
    P.box(f"node:lever|M-ZINC-CAST", -aw / 2, ya - at, a0, aw, at, a1 - a0)                # arm (the node's first box: poses.py)
    P.cyl("node:lever|M-SILVER", (0, -D, zs), (0, ya, zs), rs)                             # lever shaft out of the head
    P.cyl(f"node:lever|{K}", (0, ya - at, a1), (0, ya - at - rl, a1), rr)                  # roller on the arm's front face
    P.pivot("lever", "rotate", (0, -D, zs), axis=(0, 1, 0), range=(-TRAVEL, TRAVEL))
    P.collider("env", -w, ya - at - rl, 0.0, W, at + rl + ls + D, a1 + rr)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear and fixing holes", az=60, el=20),
            dict(name="front, lever at rest", az=270, el=0),
            dict(name="underside and cable entry", az=230, el=-50, center=(0, -15, 5), height=40),
            dict(name="front cover and label", az=270, el=0, center=(0, -15, 29), height=44)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
