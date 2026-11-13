#!/usr/bin/env python3
"""panel-light: enclosure LED light bar with a door switch, our own design. An aluminium bar screwed to the inner face of the enclosure's
top door-frame flange (two ISO 7380 screws), a row of LED windows into a light channel, and a door-switch plunger the closing door presses.
2.0 (elec-r31; review panel-light-1.0 re-reads, finding 1): 1.0 sat on the back panel, 270 short of the door. The mounting face is now the
door-frame flange (enc-fs-1524x1829x305: FL 30 tall, T 1.9, its inner face looking into the cabinet); the bar (28 tall) sits on the flange
2 below the roof sheet, the door switch is a block seated under the bar's right end, below the flange's edge, and its plunger leaves the
back-face plane there toward the door (+y), 32 proud (the bar's own end face with a fourth opening would not mesh: the block is the
switch's own body): the shut
door's inner skin (DOOR_RET 25 − DOOR_T 1.9 = 23.1 in front of the flange's front face, 25.0 in front of its inner face) presses it 7. The
origin's face and the plunger's axis changed: a major. The led element and the screws are not built yet: their holes are modelled and the
parts are placed in a later version (EM rule 2026-11-05)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "panel-light", "2.1", "device"
TITLE = "enclosure LED light bar with door switch (own design), 300 long, two M4 screws, on the top door-frame flange"
TOOLKIT = "1.3"
BASELINE = "our own design (complexes.org): sizes are design choices; M4 clearance holes per ISO 273 (lib/standards/holes.csv); the LED's figures are NOT ON FILE (Assumption)"
ORIGIN = "surface-mount device: back face (on the flange's inner face), left mounting hole centre; body toward -y; the bar runs along +x; the plunger toward +y below the flange's edge"
COMMAND = "PLIT"
PARAMS = dict()

BAR = (-15.0, 300.0, 25.0, 28.0)               # x start, length, depth (y), height (z): design choice (2.0: 28 tall, z -16 to 12, the whole bar on the 30 flange)
BAR_Z = (-16.0, 12.0)                           # the bar's z: the hole line 12 below the top
MOUNT_X = (0.0, 270.0)                          # two M4 screws (ISO 7380), on the hole line z = 0
MOUNT_D = 4.5                                   # ISO 273 medium for M4 (lib/standards/holes.csv)
CHANNEL = (20.0, 230.0, 10.0, 16.0)             # light channel from the back face: x start, length, depth, height (z -8 to 8: on the flange)
LED_D, LED_X0, LED_PITCH, LED_N = 5.2, 35.0, 25.0, 9    # LED windows (Assumption: a 5 mm LED; the led element is NOT ON FILE)
SWITCH = dict(x=258.0, z=-22.0, bore_d=8.4, bore_depth=10.0, r=4.0, inside=2.0, proud=32.0, travel=7.0)   # door-switch plunger: design choice (2.0: in the switch block below the flange's edge, 32 proud toward the door)
BLOCK = (246.0, 24.0, -28.0, 12.0)              # the door-switch block under the bar's right end: x start, length, z start, height (y as the bar): design choice

def build():
    P = Prims(); x0, L, D, H = BAR; yf = -D; z0, z1 = BAR_Z
    bar = P.box("M-ALU-ANOD", x0, -D, z0, L, D, H)
    bx, bl, bz, bh = BLOCK
    blk = P.box("M-BLACK-PA", bx, -D, bz, bl, D, bh)                                                                  # the switch block, seated under the bar
    for x in MOUNT_X:
        P.hole("M-GASKET", (x, yf - 1.0, 0), (x, 1.0, 0), MOUNT_D / 2, bar)
    cx, cl, cd, ch = CHANNEL
    P.cutbox("M-GASKET", cx, -cd, -ch / 2, cl, cd, ch, bar)
    P.box("node:lamp|M-LENS-WHITE", cx + 0.1, -cd + 0.1, -ch / 2 + 0.1, cl - 0.2, cd - 0.2, ch - 0.2)
    P.pivot("lamp", "emissive", (cx + cl / 2, -cd, 0), axis=(0, -1, 0), range=(0, 1))
    for i in range(LED_N):
        x = LED_X0 + i * LED_PITCH
        P.hole("M-GASKET", (x, yf - 1.0, 0), (x, -cd + 0.5, 0), LED_D / 2, bar)
    s = SWITCH
    P.hole("M-GASKET", (s["x"], 1.0, s["z"]), (s["x"], -s["bore_depth"], s["z"]), s["bore_d"] / 2, blk)                 # bore from the block's back-face plane
    P.cyl("node:door-switch|M-ZINC", (s["x"], -s["inside"], s["z"]), (s["x"], s["proud"], s["z"]), s["r"])               # plunger out toward the door (+y)
    P.pivot("door-switch", "translate", (s["x"], s["proud"], s["z"]), axis=(0, -1, 0), range=(0, s["travel"]))        # pressed into the block
    P.collider("env", x0, yf, bz, L, D + s["proud"], z1 - bz)
    return P

PREVIEWS = [dict(name="front three-quarter: light channel windows", az=250, el=20), dict(name="back: mounting face, plunger toward the door", az=70, el=10)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
