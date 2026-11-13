#!/usr/bin/env python3
"""joystick-22: joystick control switch, two actuation directions (up / down), spring return to 0, one N.O. contact per direction,
front mounting through the 22.5 mm cut-out. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the
ETIM 10.0 class EC000632 "Control switch, Joystick", built to the class values in spec.md "## Class values"; no maker's datasheet.
What it meets comes from the contracts on file: the Ø22.5 cut-out, the legend plate, the Ø29.7 front ring, the Ø30 x 8 latch and the
22 x 30 x 25 contact blocks are the library's 22 mm contract (toolkit/std22.py; lib/standards/holes.csv); every other size is a
design choice, said so in spec.md. The anti-rotation feature is not on file and is not modelled (spec.md). Modelled from the outside
in: legend plate, front ring with a fork (the gate that keeps the lever in its one plane), the lever on its hub (the node that tilts),
a body through the cut-out, the latch and two contact blocks with one screw-clamp port per terminal; the return spring and the
linkage from the lever to the blocks are not modelled in 1.0."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, std22
from toolkit.prims import Prims

ID, VERSION, CLASS = "joystick-22", "1.1", "operator-22"
TITLE = "joystick control switch, 2 directions (up / down), spring return to 0, 1 NO per direction, 22.5 mm front mounting, screw terminals (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Control switch, Joystick (ETIM 10.0 EC000632); class values in spec.md; the 22.5 cut-out, legend "
            "plate, front ring, latch and contact blocks from toolkit/std22.py (lib/standards/holes.csv); other sizes are design choices; "
            "the anti-rotation feature and the terminals' conductor range are open (spec.md)")
ORIGIN = "cut-out centre on the panel front face; panel occupies 0 <= y <= panel_t; lever toward -y"
COMMAND = "JOY22"
CUTOUT = std22.CUTOUT
PARAMS = dict(panel_t=3.0, legend=True, tilt=0.0)

# ---- front (design choices; Class values 3, 4 and 13 to 15 in spec.md)
BORE_R = 6.0                           # the front ring's bore behind the hub (Ø12.0, features.csv): the linkage's way through
FORK = (6.5, 10.0, 10.0, 6.0)          # fork cheeks on the ring's face: inner x, outer x, depth (y), half height (z)
HUB = (6.0, 4.5, 5.5)                  # lever hub along x: half length, radius, axis this far in front of the ring's face
ROD_R, ROD_L = 3.0, 30.5               # lever rod Ø6.0, from the pivot axis to the knob
KNOB = (8.0, 12.0, 6.0, 2.0)           # knob Ø16.0 x 12.0, then a cap Ø12.0 x 2.0: the tip 44.5 from the pivot axis
TILT = 20.0                            # the lever's travel each way from 0 (degrees); -20 = up, +20 = down
# ---- through the panel and behind it
BODY_R = 11.0                          # Ø22.0 body through the cut-out: 0.3 under the cut-out's smallest Ø22.3 (holes.csv); design choice
LATCH, BLOCK = std22.LATCH, std22.BLOCK
MARKS = (("13", "14"), ("23", "24"))   # contact block per direction: up (13-14), down (23-24); each 1 N.O.
HEAD_R, HEAD_T, HEAD_DX, HEAD_DZ = 2.2, 1.5, 6.0, 4.0   # the block's terminal screws as std22.behind draws them (x +-6, 4 above the block's centre)
ENTRY = (5.0, 4.0, 0.5, 4.5)           # wire entry slot: width (y), height (z), cut into the side face (x), centre 4.5 in front of the back face

def _lever(t, d):
    """the point on the lever's axis d mm from the pivot, the lever tilted t degrees about +x (positive tilts the knob down)"""
    return (0.0, -d * math.cos(math.radians(t)), -d * math.sin(math.radians(t)))

def blocks(P, y0):
    """the contact blocks behind the latch (std22's block and its place: the first centred on the axis, the next below it); each block's
    two terminal screws are port nodes t-<mark>, with the wire entry a slot cut into the block's side face beside each screw"""
    w, d, h = BLOCK["w"], BLOCK["d"], BLOCK["h"]; yb = y0 + d; ew, eh, ed, ein = ENTRY
    for b, marks in enumerate(MARKS):
        z0 = -h / 2 - b * (h + 1); zt = z0 + h / 2 + HEAD_DZ
        body = P.box("M-BLACK-PA", -w / 2, y0, z0, w, d, h)
        for side, mk in zip((-1, 1), marks):
            cx = side * HEAD_DX; n = f"t-{mk}"
            P.cyl(f"node:{n}|M-ZINC", (cx, yb, zt), (cx, yb + HEAD_T, zt), HEAD_R)
            P.pivot(n, "port", (cx, yb + HEAD_T, zt), axis=(0, 1, 0), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp
            xf = side * w / 2; yc = yb - ein
            P.cutbox("M-GASKET", xf - (ed if side > 0 else 1.0), yc - ew / 2, zt - eh / 2, ed + 1.0, ew, eh, body)     # out past the side face
            P.box("M-GASKET", xf - (ed if side > 0 else 0.0), yc - ew / 2, zt - eh / 2, ed, ew, eh)                     # the dark slot in its cut

def build(panel_t=3.0, legend=True, tilt=0.0):
    P = Prims(); B = "M-BLACK-PA"
    yf = std22.legend(P) if legend else 0.0                                                    # legend plate (its own Ø22.5 hole)
    std22.bezel(P, yf, BORE_R)                                                                  # Ø29.7 front ring, 3.0 proud
    yr = yf - std22.BEZEL["proud"]                                                              # the ring's front face
    xi, xo, fd, fz = FORK
    for s in (-1, 1):                                                                           # fork cheeks: the gate of the one plane
        P.box("M-ZINC", xi if s > 0 else -xo, yr - fd, -fz, xo - xi, fd, 2 * fz)
    P.cyl(B, (0, yf, 0), (0, panel_t, 0), BODY_R)                                               # body through the legend and the cut-out
    P.cyl(B, (0, panel_t, 0), (0, panel_t + LATCH["h"], 0), LATCH["r"])                         # mounting latch behind the panel
    blocks(P, panel_t + LATCH["h"])
    # ---- the lever: hub on the pivot axis (x), rod, knob and cap; tilted t degrees about +x
    hl, hr, hy = HUB; py = yr - hy; t = float(tilt)
    def at(d): p = _lever(t, d); return (p[0], py + p[1], p[2])
    P.cyl("node:self|M-BLACK-PA", (-hl, py, 0), (hl, py, 0), hr)
    P.cyl("node:self|M-BLACK-PA", at(0.0), at(ROD_L), ROD_R)
    kr, kl, cr, cl = KNOB
    P.cyl("node:self|M-BLACK-PA", at(ROD_L), at(ROD_L + kl), kr)
    P.cyl("node:self|M-BLACK-PA", at(ROD_L + kl), at(ROD_L + kl + cl), cr)
    P.pivot("self", "rotate", (0, py, 0), axis=(1, 0, 0), range=(-TILT - t, TILT - t))
    tip = py - (ROD_L + kl + cl); zb = -BLOCK["h"] / 2 - (BLOCK["h"] + 1); xw = LATCH["r"]                  # the latch is the widest part (legend 30 wide)
    zt = std22.LEGEND["h"] * 0.35 if legend else LATCH["r"]                                     # the legend plate's top, else the latch's
    P.collider("env", -xw, tip, zb, 2 * xw, panel_t + LATCH["h"] + BLOCK["d"] + HEAD_T - tip, zt - zb)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear latch blocks and terminals", az=60, el=20),
            dict(name="side lever up", az=180, el=0, params=dict(tilt=-20.0)),
            dict(name="fork and hub", az=230, el=35, center=(0, -9, 0), height=30),
            dict(name="side lever down", az=180, el=0, params=dict(tilt=20.0))]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
