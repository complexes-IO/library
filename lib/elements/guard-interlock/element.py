#!/usr/bin/env python3
"""guard-interlock: position switch with guard locking and a separate tongue actuator (an interlocking device for a movable guard), two
N.C. safety contacts (11-12 closed while the actuator is in; 21-22 closed while it is in and locked), the guard locking applied by a
spring and released by a 24 V DC solenoid (A1-A2: power to unlock), AC-15 2 A at 230 V / DC-13 1 A at 24 V, plastic housing 40 x 40 x 92
with a 30 high head, M20 x 1.5 cable entry. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the
ETIM 10.0 class EC002593 "Position switch with guard locking", built to the class values in spec.md "## Class values"; no maker's
datasheet (the folder's earlier stub is reference only and was not used; its record is kept as references/source.txt's end block).
A safety-function class (lib/inventory.csv safety yes): the element is held at station 7 for EM's "Safety sign-off" (OPERATING.md 13).
What it meets comes from the standards on file: the four fixing holes (two in the switch's top block, two in the actuator) are ISO 273
medium clearance for M5 (lib/standards/holes.csv; the inventory's screw-iso4762 x4, not built, not placed) and the cable entry is
M20 x 1.5 tapped, its minor diameter derived (derive.thread, ISO 68-1 / ISO 965-1). The interlocking standard (ISO 14119) and the
contact standard (IEC 60947-5-1) are not in lib/standards/sources.csv: nothing is taken from them, every size is a design choice.
Not placed in this version (OPERATING.md 12, quality at the source): receptacle-m12 (the inventory's made_of; not past station 6, so
the cable-entry form, as limit-switch), the installer's cable gland, and the mechanism inside the head (locking bolt, solenoid,
contact block).
Modelled from the outside in: limit-switch's housing frame scaled up (a base block with the cable entry, two side walls, a back wall, a
top block with the two fixing holes) round a terminal compartment closed by a front cover; six terminal screw heads on the back wall
(the port nodes t-11, t-12, t-21, t-22, t-A1, t-A2); the head on top with the actuator's slot in its front face; the actuator (node
`actuator`: the tongue and its mounting block, fixed to the guard), which slides out of the slot toward -y as the guard opens."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "guard-interlock", "1.0", "device"
TITLE = "position switch with guard locking, tongue actuator, spring lock / 24 V DC solenoid release, 2 N.C. (11-12, 21-22), AC-15 2 A 230 V, M20 x 1.5 entry (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Position switch with guard locking (ETIM 10.0 EC002593); class values in spec.md; fixing holes "
            "ISO 273 medium for M5 (lib/standards/holes.csv); cable entry M20 x 1.5 derived (ISO 68-1 / ISO 965-1); housing, head and "
            "actuator sizes are design choices; the terminals' conductor range and torque and the solenoid's operating limits are open "
            "(spec.md); a safety-function class held for EM's safety sign-off")
ORIGIN = "the housing's back (mounting) face y = 0, x = 0 the centreline, z = 0 the base's bottom face (cable entry), body toward -y"
COMMAND = "GUARDLK"
PARAMS = {}

# ---- housing (design choices: spec.md Dimensions)
W, D = 40.0, 40.0                    # housing 40 wide (x ±20), 40 deep (y -40 ... 0)
BASE_H = 10.0                        # base block z 0 ... 10, carries the cable entry
TOP = (80.0, 92.0)                   # top block z 80 ... 92, carries the two fixing holes
WALL, BACK, COVER = 4.0, 4.0, 3.0    # side walls x ±16 ... ±20, back wall y -4 ... 0, front cover y -40 ... -37 (z 10 ... 80)
# ---- what it meets (standards on file)
FIX_D = 5.5                          # ISO 273 medium clearance for M5 (lib/standards/holes.csv; features.csv)
FIX = ((-12.0, 86.0), (12.0, 86.0))  # (x, z) of the switch's two fixing holes, through y: design choice
ENTRY_D = 18.3762                    # M20 x 1.5 internal thread's minor diameter D1, derived: derive.thread(20.0, 1.5) (ISO 68-1, ISO 965-1)
ENTRY = (0.0, -20.0)                 # (x, y) of the entry's axis, up through the base into the compartment
# ---- terminals (design choices; their conductor range and torque NOT ON FILE (B): IEC 60947-1)
HEAD_R, HEAD_T = 2.2, 1.2            # terminal screw heads Ø4.4 x 1.2 on the back wall's front face (y -4)
TERMS = (("t-11", -8.0, 66.0), ("t-12", -8.0, 46.0), ("t-21", 0.0, 66.0), ("t-22", 0.0, 46.0),
         ("t-A1", 8.0, 66.0), ("t-A2", 8.0, 46.0))     # node, x, z
LABEL = (-12.0, 12.0, 20.0, 38.0)    # label field on the cover: x0, x1, z0, z1 (decal)
# ---- head and actuator (design choices)
HEAD = (92.0, 122.0)                 # head z 92 ... 122, full section
SLOT = (7.0, 103.0, 111.0, -15.0)    # actuator slot in the head's front face: half width x, z from ... to, its floor at y -15
TONGUE = (6.0, 104.0, 110.0, -17.0)  # tongue: half width x, z from ... to, its tip at y -17 (1 clear each side, 2 at the floor)
BLOCK = (16.0, 98.0, 116.0, 10.0)    # actuator's mounting block: half width x, z from ... to, depth in y (y -54 ... -44, 4 in front of the head)
GAP = 4.0                            # the block's back face to the head's front face, actuator in
ACT_FIX = ((-11.0, 107.0), (11.0, 107.0))   # (x, z) of the actuator's two fixing holes, through y into the guard: design choice (an M5
                                            # ISO 4762 head, Ø8.5, seats beside the tongue: x 6.75 ... 15.25 inside the block's ±16)
TRAVEL = 40.0                        # the actuator withdraws 40 toward -y as the guard opens (the tongue's tip then 0 in front of the head ... clear)

def build():
    P = Prims(); G = "M-GREY-PA"; Y = "M-YELLOW-PA"
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
    head = P.box(Y, -w, -D, h0, W, D, h1 - h0)                                             # head
    sw, s0, s1, sf = SLOT
    P.cutbox("M-GASKET", -sw, -D - 1.0, s0, 2 * sw, sf + D + 1.0, s1 - s0, head)          # the actuator's slot, from the front face to y -15
    tw, t0, t1, tt = TONGUE; bw, b0, b1, bd = BLOCK
    yb = -D - GAP                                                                          # the block's back face (y -44)
    P.box("node:actuator|M-SILVER", -tw, yb, t0, 2 * tw, tt - yb, t1 - t0)                 # tongue (the node's first box: poses.py)
    blk = P.box("node:actuator|M-ZINC-CAST", -bw, yb - bd, b0, 2 * bw, bd, b1 - b0)        # mounting block, fixed to the guard
    for fx, fz in ACT_FIX:                                                                 # two M5 clearance holes into the guard, ISO 273 medium
        P.hole("M-GASKET", (fx, yb + 0.5, fz), (fx, yb - bd - 0.5, fz), FIX_D / 2, blk)
    P.pivot("actuator", "translate", (0, yb, (t0 + t1) / 2), axis=(0, -1, 0), range=(0, TRAVEL), unit="mm")
    P.collider("env", -w, yb - bd, 0.0, W, bd + GAP + D, h1)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear and fixing holes", az=60, el=20),
            dict(name="front, actuator in", az=270, el=0),
            dict(name="head and actuator slot", az=300, el=30, center=(0, -40, 107), height=40),
            dict(name="underside and cable entry", az=230, el=-50, center=(0, -20, 5), height=50),
            dict(name="front cover and label", az=270, el=0, center=(0, -20, 29), height=50)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
