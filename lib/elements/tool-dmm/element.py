#!/usr/bin/env python3
"""tool-dmm: hand-held digital multimeter for the toolbox station, our own design. Display, rotary dial, four test-lead jacks and two
probes parked in side clips; the dial and the probes are named nodes. No measurement category or other rating is printed or claimed."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "tool-dmm", "1.0", "device"
TITLE = "digital multimeter (own design): display, dial, four jacks, two probes in side clips"
TOOLKIT = "1.3"
BASELINE = "our own design (complexes.org): sizes are design choices; the 4 mm test-plug jack figures are NOT ON FILE (Assumption)"
ORIGIN = "lying on a bench: centre of the back face, y = 0; the front faces -y; z up the long side"
COMMAND = "DMM1"
PARAMS = dict()

BODY = (90.0, 40.0, 180.0)                      # x wide, y deep, z tall: design choice (one-hand meter)
DISPLAY = (70.0, 40.0, 55.0)                    # w, h, centre z: design choice
DIAL_PLATE = (70.0, 0.6, 66.0)                  # printed ring of positions under the dial
DIAL = (22.0, 8.0, (0.0, 270.0))                # radius, height, rotation range in degrees: ten positions at 30 (design choice)
JACK_D, JACK_DEPTH, JACK_Z = 8.0, 12.0, -60.0   # 4 mm shrouded test-plug bore (Assumption: the plug's figure is NOT ON FILE)
JACK_X = (-30.0, -10.0, 10.0, 30.0)             # COM, V / ohm, mA, A: pitch 20 (Assumption with the bore)
PROBE = dict(x=51.0, y=-20.0, tip=(0.6, 20.0),   # tip Ø1.2: thinner than 2.5 r, so the gate leaves it sharp (a Ø2 tip's end edge was rejected on the envelope)
 guard=(6.0, 2.0), grip=(4.5, 108.0), boot=(3.0, 15.0), z_top=90.0, pull=150.0)
CLIP_Z = (-20.0, 40.0)                          # two clips per probe on the body's side
LABEL = (60.0, 0.6, 12.0, -78.0)                # w, thickness, h, centre z: complexes.org

def probe(P, name, mat, sx):
    p = PROBE; x = sx * p["x"]; y = p["y"]; z = p["z_top"]
    tr, tl = p["tip"]; gr, gt = p["guard"]; hr, hl = p["grip"]; br, bl = p["boot"]
    P.cyl(f"node:{name}|M-ZINC", (x, y, z), (x, y, z - tl), tr); z -= tl                 # tip at the top
    P.cyl(f"node:{name}|{mat}", (x, y, z), (x, y, z - gt), gr); z -= gt                  # finger guard
    P.cyl(f"node:{name}|{mat}", (x, y, z), (x, y, z - hl), hr); z -= hl                  # grip
    P.cyl(f"node:{name}|{mat}", (x, y, z), (x, y, z - bl), br)                          # boot (the lead comes later)
    P.pivot(name, "translate", (x, y, p["z_top"]), axis=(0, 0, 1), range=(0, p["pull"]))
    W = BODY[0]; xs = sx * W / 2; cw = x - sx * hr - xs                                  # clip from the side face to the grip, touching both
    for zc in CLIP_Z:
        P.box("M-BLACK-PA", min(xs, xs + cw), y - 4.0, zc - 4.0, abs(cw), 8.0, 8.0)

def build():
    P = Prims(); W, D, H = BODY; yf = -D
    body = P.box("M-GREY-PA", -W / 2, -D, -H / 2, W, D, H)
    dw, dh, dz = DISPLAY
    P.box("node:display|M-LENS-DARK", -dw / 2, yf - 1.0, dz - dh / 2, dw, 1.0, dh)
    P.pivot("display", "emissive", (0, yf - 1.0, dz), axis=(0, -1, 0), range=(0, 1))
    pw, pt, ph = DIAL_PLATE
    P.box("M-BLACK-PA", -pw / 2, yf - pt, -ph / 2, pw, pt, ph)
    r, h, rng = DIAL; y0 = yf - pt
    P.cyl("node:dial|M-GREY-PA", (0, y0, 0), (0, y0 - h, 0), r)
    P.box("node:dial|M-WHITE-PA", -2.0, y0 - h - 2.0, 2.0, 4.0, 2.0, 16.0)               # pointer ridge
    P.pivot("dial", "rotate", (0, y0, 0), axis=(0, -1, 0), range=rng, unit="deg")
    for x in JACK_X:
        P.hole("M-GASKET", (x, yf - 1.0, JACK_Z), (x, yf + JACK_DEPTH, JACK_Z), JACK_D / 2, body)
    lw, lt, lh, lz = LABEL
    P.box("M-WHITE-PA", -lw / 2, yf - lt, lz - lh / 2, lw, lt, lh)
    probe(P, "probe-red", "M-RED-PA", 1.0)
    probe(P, "probe-black", "M-BLACK-PA", -1.0)
    px = PROBE["x"] + PROBE["guard"][0]
    P.collider("env", -px, y0 - h - 2.0, -H / 2, 2 * px, D + pt + h + 2.0, H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="right side, red probe in its clips", az=320, el=10)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
