#!/usr/bin/env python3
"""thermostat-enc: enclosure thermostat on the 35 mm rail, our own design. A housing with a setpoint dial on its front and two screw
terminals at the bottom; the dial is a named node. The rail clip and the terminals are the toolkit's rail-device parts (toolkit/din.py)
on file; the housing and dial sizes are design choices. No switching rating, temperature range or approval mark is printed or claimed."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "thermostat-enc", "1.1", "device"
TITLE = "enclosure thermostat (own design), 35 mm rail: setpoint dial, two screw terminals"
TOOLKIT = "1.3"
BASELINE = "our own design (complexes.org): housing and dial sizes are design choices; rail clip and screw terminals from toolkit/din.py on file"
ORIGIN = "rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward -y"
COMMAND = "TSTE"
PARAMS = dict()

BODY = (35.0, 40.0, 60.0)                       # x wide, y deep off the rail crown, z tall: design choice (two narrow rail modules)
CLIP = 7.5                                      # din.rail_clip's lips behind the crown (toolkit/din.py)
SCALE = (26.0, 0.6, 26.0, 6.0)                  # w, thickness, h, centre z: the printed setpoint scale under the dial (design choice)
DIAL = (10.0, 6.0, (0.0, 270.0))                # radius, height, rotation range in degrees (design choice; no temperatures claimed)
POINTER = (2.0, 1.5, 7.0)                       # w, proud, length from the dial's centre: a ridge on the dial's face, inside its radius
TERMS = (2, 12.0)                               # two screw terminals at the bottom, pitch 12 (design choice), din.terminal_row's figures
LABEL = (25.0, 0.2, 8.0, 23.0)                  # w, thickness, h, centre z: complexes.org
LEGEND = (25.0, 0.2, 4.0, -18.0)                # w, thickness, h, centre z: terminal numbers 1 and 2 above the screws (1.1, design choice)

def build():
    P = Prims(); W, D, H = BODY; yf = -D
    hb = P.box("M-GREY-PA", 0.0, -D, -H / 2, W, D, H)                                        # housing (1.1: the wire entries are cut into it)
    din.rail_clip(P, 0.0, W, CLIP)
    sw, st, sh, sz = SCALE
    P.box("M-WHITE-PA", W / 2 - sw / 2, yf - st, sz - sh / 2, sw, st, sh)                   # setpoint scale (decal: marks, no figures)
    r, h, rng = DIAL; y0 = yf - st; cx = W / 2
    P.cyl("node:dial|M-BLACK-PA", (cx, y0, sz), (cx, y0 - h, sz), r)
    pw, pp, pl = POINTER
    P.box("node:dial|M-WHITE-PA", cx - pw / 2, y0 - h - pp, sz, pw, pp, pl)                  # pointer ridge, from the centre up
    P.pivot("dial", "rotate", (cx, y0, sz), axis=(0, -1, 0), range=rng, unit="deg")
    n, pitch = TERMS
    din.terminal_row(P, W / 2 - n * pitch / 2, yf, -H / 2, n, pitch, up=False, target=hb)  # slots recessed in the end face (request elec-2)
    lw, lt, lh, lz = LABEL
    P.box("M-WHITE-PA", W / 2 - lw / 2, yf - lt, lz - lh / 2, lw, lt, lh)                   # label field (decal: complexes.org)
    gw, gt, gh, gz = LEGEND
    P.box("M-WHITE-PA", W / 2 - gw / 2, yf - gt, gz - gh / 2, gw, gt, gh)                   # terminal legend field (decal: 1, 2)
    P.collider("env", 0.0, y0 - h - pp, -H / 2, W, D + st + h + pp + CLIP, H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="rail clip and terminals", az=60, el=25)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
