#!/usr/bin/env python3
"""teach-pendant: hand-held robot teach pendant for the robot cell, our own design. 7 in class screen, E-stop mushroom, 16 keys and an
enabling bar as named nodes, cable entry at the bottom. Printed on the part: "SIMULATION ONLY. NOT A SAFETY DEVICE" (OPERATING.md 6).
It carries no ratings and makes no safety claim: the E-stop and the enabling bar are simulation inputs only."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import std22, library
from toolkit.prims import Prims

ID, VERSION, CLASS = "teach-pendant", "1.0", "device"
TITLE = "robot teach pendant (simulation only), 7 in screen, E-stop, 16 keys, enabling bar"
TOOLKIT = "1.3"
BASELINE = "our own design (complexes.org): sizes are design choices; E-stop mushroom from toolkit/std22.py; M20 cable entry from lib/standards/holes.csv"
ORIGIN = "hand-held: centre of the back face, y = 0; the screen faces -y; z up the long side"
COMMAND = "TPND"
PARAMS = dict()

BODY = (240.0, 55.0, 300.0)                     # x wide, y deep, z tall: design choice (two-hand grip, 7 in screen above 16 keys)
SCREEN = (155.0, 87.0, 1.0)                     # 7 in diagonal at 16:9 (177.8 mm: 155.0 x 87.2), 1.0 proud: design choice
SCREEN_AT = (-27.5, 78.5)                       # centre x, z
ESTOP_AT = (85.0, 95.0)                         # centre x, z: top right, beside the screen
KEY = (36.0, 18.0, 3.0, 1.0)                    # w (x), h (z), thickness (0.5 in its pocket, 2.5 proud), travel: design choice
KEY_COLS = (-75.0, -25.0, 25.0, 75.0)           # 4 x 4 keys below the screen
KEY_ROWS = (5.0, -21.0, -47.0, -73.0)
POCKET = 1.5                                    # key pocket depth; side clearance 0.2
ENABLE = (3.5, 24.6, 79.6, 1.5)                 # enabling bar on the left side: x thick, y, z, travel (released 0, enabled ~0.75, pressed through 1.5)
LABEL = (200.0, 0.8, 18.0, -133.0)              # white label: w, thickness, h, centre z ("SIMULATION ONLY. NOT A SAFETY DEVICE", complexes.org)
ENTRY = 20.5                                    # M20 x 1.5 cable entry (lib/standards/holes.csv, entry 20.2-20.7); the gland and cable come later
E = std22.ESTOP

def build():
    P = Prims(); W, D, H = BODY; yf = -D
    body = P.box("M-GREY-PA", -W / 2, -D, -H / 2, W, D, H)
    # screen (emissive in the twin)
    sw, sh, st = SCREEN; sx, sz = SCREEN_AT
    P.box("node:screen|M-LENS-DARK", sx - sw / 2, yf - st, sz - sh / 2, sw, st, sh)
    P.pivot("screen", "emissive", (sx, yf - st, sz), axis=(0, -1, 0), range=(0, 1))
    # E-stop: yellow collar on the face, red mushroom (std22 figures), press 6 and latch
    ex, ez = ESTOP_AT
    P.cyl("M-YELLOW", (ex, yf, ez), (ex, yf - E["collar_h"], ez), E["collar_r"])
    y0 = yf - E["collar_h"]
    mh = P.cyl("node:estop|M-RED", (ex, y0, ez), (ex, y0 - E["h"] + 4, ez), E["r"])
    P.hole("M-GASKET", (ex, y0 + 1, ez), (ex, y0 - 6.2, ez), E["collar_r"] + 0.3, mh)               # skirt recess: the head slides over the collar
    P.cyl("node:estop|M-RED", (ex, y0 - E["h"] + 4, ez), (ex, y0 - E["h"], ez), E["r"] - 4)          # crown
    P.pivot("estop", "translate", (ex, y0, ez), axis=(0, 1, 0), range=(0, 6.0))
    # 16 keys, each in its own pocket
    kw, kh, kt, ktr = KEY; n = 0
    for z in KEY_ROWS:
        for x in KEY_COLS:
            n += 1
            P.cutbox("M-GASKET", x - kw / 2 - 0.2, yf, z - kh / 2 - 0.2, kw + 0.4, POCKET, kh + 0.4, body)
            P.box(f"node:key-{n}|M-BLACK-PA", x - kw / 2, yf - (kt - 0.5), z - kh / 2, kw, kt, kh)
            P.pivot(f"key-{n}", "translate", (x, yf - (kt - 0.5), z), axis=(0, 1, 0), range=(0, ktr))
    # enabling bar in a pocket on the left side
    bt, by, bz, btr = ENABLE; xl = -W / 2; yc = -27.5
    P.cutbox("M-GASKET", xl, yc - by / 2 - 0.2, -bz / 2 - 0.2, 3.0, by + 0.4, bz + 0.4, body)
    P.box("node:enable|M-BLACK-PA", xl - 2.0, yc - by / 2, -bz / 2, bt, by, bz)
    P.pivot("enable", "translate", (xl - 2.0, yc, 0.0), axis=(1, 0, 0), range=(0, btr))
    # label on the front, below the keys
    lw, lt, lh, lz = LABEL
    P.box("M-WHITE-PA", -lw / 2, yf - lt, lz - lh / 2, lw, lt, lh)
    # cable entry in the bottom face
    P.hole("M-GASKET", (0, yc, -H / 2 - 1), (0, yc, -H / 2 + 16), ENTRY / 2, body)
    P.collider("env", -W / 2 - 2.0, y0 - E["h"], -H / 2, W + 2.0, D + E["collar_h"] + E["h"], H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="underside left, enabling bar and cable entry", az=200, el=-30)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
