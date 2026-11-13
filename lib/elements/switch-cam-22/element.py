#!/usr/bin/env python3
"""switch-cam-22: control switch (cam switch), 1-0-2, two poles, knob on a 48 x 48 front shield, front mounting through the 22.5 mm
cut-out, a stack of two contact chambers behind the panel. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral
design of the ETIM 10.0 class EC002611 "Control switch", built to the class values in spec.md "## Class values"; no maker's datasheet.
What it meets comes from the contracts on file: the Ø22.5 cut-out (toolkit/std22.py CUTOUT, lib/standards/holes.csv) and the Ø30 x 8
mounting latch behind the panel (std22.LATCH); every other size is a design choice, said so in spec.md. The anti-rotation feature
is not on file and is not modelled (spec.md). Modelled from the outside in: front shield, knob (the node that turns), a body through
the cut-out, the latch, and two contact chambers with one screw-clamp port per terminal; the cam shaft and contacts inside are not
modelled in 1.0."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, std22
from toolkit.prims import Prims

ID, VERSION, CLASS = "switch-cam-22", "1.1", "operator-22"
TITLE = "control switch 1-0-2, 2 poles, 10 A, 440 V AC, knob on a 48 x 48 front shield, 22.5 mm front mounting, screw terminals (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Control switch (ETIM 10.0 EC002611); class values in spec.md; the 22.5 cut-out and the mounting "
            "latch from toolkit/std22.py (lib/standards/holes.csv); sizes are design choices; the anti-rotation feature and the "
            "terminals' conductor range are open (spec.md)")
ORIGIN = "cut-out centre on the panel front face; panel occupies 0 <= y <= panel_t; knob toward -y"
COMMAND = "SWCAM"
CUTOUT = std22.CUTOUT
PARAMS = dict(panel_t=3.0, position=0)

# ---- front (design choices; Class values 15 and 16 in spec.md)
SHIELD = (48.0, 48.0, 3.0)             # front shield: width (x), height (z), thickness (y)
KNOB_R, KNOB_T = 16.0, 4.0             # knob base Ø32 x 4 on the shield
GRIP = (8.0, 32.0, 12.0)               # thumb grip on the knob base: width (x), length (z), depth (y); the pointer end is up at position 0
POINTER = (2.0, 7.0, 0.2, 8.0)         # white pointer inlay on the grip's face: width, length, proud, from z 8 up
STEP = 45.0                            # knob angle between positions: 1 at -45, 0 at 0, 2 at +45 (clockwise seen from the front)
# ---- through the panel and behind it
BODY_R = 11.0                          # Ø22.0 body through the cut-out: 0.3 under the cut-out's smallest Ø22.3 (holes.csv); design choice
LATCH = std22.LATCH                    # Ø30 x 8 mounting latch behind the panel (the library's 22 mm contract)
CH = (32.0, 15.0, 40.0)                # contact chamber: width (x), depth (y), height (z); one pole per chamber
POLES = 2
HEAD_R, HEAD_T, HEAD_DX = 2.2, 1.2, 8.0   # terminal screw head radius, height; centres at x -8 / +8 on the top and bottom faces
ENTRY = (5.0, 4.0, 0.5, 4.5)           # wire entry slot: width (y), height (z), cut into the side face (x), centre 4.5 in from the top / bottom

def _rot(a, v):
    """v turned by a degrees about +y (clockwise seen from the front, -y)"""
    c, s = math.cos(math.radians(a)), math.sin(math.radians(a))
    return (v[0] * c + v[2] * s, v[1], -v[0] * s + v[2] * c)

def _knob_box(P, layer, a, x0, x1, y0, y1, z0, z1):
    """a box of the knob, given at position 0, turned a degrees about the knob's axis"""
    o = _rot(a, (x0, y0, z0))
    return P.obox(layer, o, _rot(a, (1, 0, 0)), (0, 1, 0), _rot(a, (0, 0, 1)), x1 - x0, y1 - y0, z1 - z0)

def chamber(P, k, y0):
    """contact chamber k (one pole): a housing with four screw clamps, two on the top face and two on the bottom; contact a (position 1)
    on the left (x < 0), contact b (position 2) on the right. The head is the port node t-<mark>; the wire entry is a slot cut into the
    side face under it."""
    w, d, h = CH; yc = y0 + d / 2
    body = P.box("M-GREY-PA", -w / 2, y0, -h / 2, w, d, h)
    marks = {(-1, 1): 4 * k + 1, (-1, -1): 4 * k + 2, (1, 1): 4 * k + 3, (1, -1): 4 * k + 4}   # (side, up): terminal mark
    ew, eh, ed, ein = ENTRY
    for (side, up), mk in sorted(marks.items(), key=lambda kv: kv[1]):
        cx = side * HEAD_DX; zf = up * h / 2; n = f"t-{mk}"
        P.cyl(f"node:{n}|M-ZINC", (cx, yc, zf), (cx, yc, zf + up * HEAD_T), HEAD_R)
        P.pivot(n, "port", (cx, yc, zf + up * HEAD_T), axis=(0, 0, up), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp
        zc = zf - up * ein; xf = side * w / 2
        P.cutbox("M-GASKET", xf - (ed if side > 0 else 1.0), yc - ew / 2, zc - eh / 2, ed + 1.0, ew, eh, body)       # out past the side face
        P.box("M-GASKET", xf - (ed if side > 0 else 0.0), yc - ew / 2, zc - eh / 2, ed, ew, eh)                       # the dark slot in its cut
    return body

def build(panel_t=3.0, position=0):
    P = Prims(); B = "M-BLACK-PA"
    sw, sh, st = SHIELD
    P.box(B, -sw / 2, -st, -sh / 2, sw, st, sh)                                                # front shield on the panel face
    P.cyl(B, (0, 0, 0), (0, panel_t, 0), BODY_R)                                                # body through the cut-out
    P.cyl(B, (0, panel_t, 0), (0, panel_t + LATCH["h"], 0), LATCH["r"])                         # mounting latch behind the panel
    y = panel_t + LATCH["h"]
    for k in range(POLES): chamber(P, k, y + k * CH[1])
    # ---- knob: base disc and thumb grip, turned to the position built (the twin turns it about +y)
    a = {0: 0.0, 1: -STEP, 2: STEP}[int(position)]
    yk = -st - KNOB_T
    P.cyl("node:self|M-BLACK-PA", (0, -st, 0), (0, yk, 0), KNOB_R)
    gw, gl, gd = GRIP
    _knob_box(P, "node:self|M-BLACK-PA", a, -gw / 2, gw / 2, yk - gd, yk, -gl / 2, gl / 2)
    pw, pl, pp, pz = POINTER
    _knob_box(P, "node:self|M-WHITE-PA", a, -pw / 2, pw / 2, yk - gd - pp, yk - gd, pz, pz + pl)
    P.pivot("self", "rotate", (0, -st, 0), axis=(0, 1, 0), range=(-STEP - a, STEP - a))
    P.collider("env", -sw / 2, yk - gd - pp, -sh / 2, sw, gd + pp + KNOB_T + st + panel_t + LATCH["h"] + POLES * CH[1], sh)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear chambers and terminals", az=60, el=25),
            dict(name="front knob at 0", az=270, el=0, center=(0, -10, 0), height=56),
            dict(name="position 2", az=270, el=0, center=(0, -10, 0), height=56, params=dict(position=2)),
            dict(name="top terminal row and wire entries", az=210, el=50, center=(0, 26, 20), height=40)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
