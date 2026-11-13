#!/usr/bin/env python3
"""overload-electronic: electronic motor overload relay, self-powered, 0.4 ... 2.0 A, trip class 10, 1 N.O. + 1 N.C., separate
mounting on the 35 mm rail. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class
EC001080 "Electronic overload relay", built to the class values in spec.md "## Class values"; no maker's datasheet. What it meets
comes from the contracts on file: the rail clip from toolkit/din.py (rail_clip, the 35 x 7.5 rail of din-rail-35 / EN 60715
TH35-7.5); every other size is a design choice, said so in spec.md. Modelled from the outside in: housing, main terminals L1-L3 in
and T1-T3 out, the auxiliary block 95-98, the current-setting dial, the reset button and the trip indicator; the current sensing
and trip electronics inside are not modelled in 1.0."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "overload-electronic", "1.1", "device"
TITLE = "electronic overload relay, self-powered, 0.4-2.0 A, class 10, 1 NO + 1 NC, screw terminals, 35 mm rail (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Electronic overload relay (ETIM 10.0 EC001080); class values in spec.md; rail clip from "
            "toolkit/din.py (EN 60715 TH35-7.5 rail, din-rail-35); sizes are design choices; the terminals' conductor range is open (spec.md)")
ORIGIN = "rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward -y"
COMMAND = "OLEL"
PARAMS = dict(setting=0.0, pressed=False)

# ---- envelope (design choices; the class values Width / Height / Depth in spec.md)
W, H = 45.0, 90.0                    # width (x), height (z): z -45 ... 45, centred on the rail
D_BASE = 46.0                        # base and main terminal shoulders: front face at y -46
D = 76.0                             # front face at y -76; 83.5 overall with the 7.5 behind the crown (din.rail_clip)
FH = (2.0, 43.0, -28.0, 18.0)        # front housing x0, x1, z0, z1 (y -76 ... -46)
AUX = (2.0, 43.0, 18.0, 28.0, -66.0)  # auxiliary block x0, x1, z0, z1, front face y (to the shoulder at -46)
# ---- terminals (design choices: pitch, head, entry); the conductor range is open (spec.md)
MAIN_X = (9.5, 22.5, 35.5)           # 13.0 pitch, centred
AUX_X = (9.0, 18.0, 27.0, 36.0)      # 9.0 pitch, centred
MAIN = dict(r=2.8, t=1.2, dz=7.0, entry=(5.0, 10.0, 0.5))
AUXT = dict(r=2.0, t=1.2, dz=5.0, entry=(3.2, 8.0, 0.5))
# ---- front: dial, reset button, trip indicator, legend (design choices)
DIAL = (13.0, 4.0, 6.0, 1.0)         # x, z, radius, proud of the face
SPAN = 270.0                         # dial travel over the setting range 0.4 ... 2.0 A
BTN = (30.0, 4.0, 7.2, 1.0, 5.0)     # x, z, square side, proud, length; in an 8.0 square pocket 7.0 deep
PRESS = 2.0                          # reset button stroke
POCKET = (8.0, 7.0)
LEGEND = (5.0, 40.0, -25.0, -15.0)   # x0, x1, z0, z1

def terminals(P, xs, marks, y_face, z_edge, up, target, r, t, dz, entry):
    """screw clamps on a shoulder (front face y_face): the head is the port node t-<mark>; the wire entry is a slot cut into the end
    face z_edge (the toolkit's terminal_row shape, din.py, with a named node per terminal)"""
    s = 1 if up else -1
    for cx, mk in zip(xs, marks):
        cz = z_edge - s * dz; n = f"t-{mk}"
        P.cyl(f"node:{n}|M-ZINC", (cx, y_face, cz), (cx, y_face - t, cz), r)
        P.pivot(n, "port", (cx, y_face - t, cz), axis=(0, -1, 0), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp
        w, d, sl = entry; z0 = z_edge - (sl if up else 0.0)
        P.cutbox("M-GASKET", cx - w / 2, y_face + 2.0, z0 - (0.0 if up else 1.0), w, d, sl + 1.0, target)       # out past the end face
        P.box("M-GASKET", cx - w / 2, y_face + 2.0, z0, w, d, sl)                                               # the dark slot in its cut

def build(setting=0.0, pressed=False):
    """setting: the dial's angle (0 ... SPAN deg); pressed: the reset button at the end of its stroke"""
    P = Prims(); G = "M-GREY-PA"
    base = P.box(G, 0, -D_BASE, -H / 2, W, D_BASE, H)                                       # base with the main terminal shoulders
    x0, x1, z0, z1 = FH
    fh = P.box(G, x0, -D, z0, x1 - x0, D - D_BASE, z1 - z0)                               # front housing
    ax0, ax1, az0, az1, ay = AUX
    ab = P.box(G, ax0, ay, az0, ax1 - ax0, -D_BASE - ay, az1 - az0)                        # auxiliary block above it, set back
    din.rail_clip(P, 0, W)                                                                  # the rail latch (toolkit contract)
    terminals(P, MAIN_X, ("L1", "L2", "L3"), -D_BASE, H / 2, True, base, **MAIN)           # line in, top
    terminals(P, MAIN_X, ("T1", "T2", "T3"), -D_BASE, -H / 2, False, base, **MAIN)         # motor out, bottom
    terminals(P, AUX_X, ("95", "96", "97", "98"), ay, az1, True, ab, **AUXT)               # auxiliary contacts on the block's face
    # current-setting dial with its pointer (one node), turning about the y axis
    dx, dzc, dr, dp = DIAL
    P.cyl("node:dial-ir|M-BLACK-PA", (dx, -D, dzc), (dx, -D - dp, dzc), dr)
    a = math.radians(setting); ux, uz = math.sin(a), math.cos(a)                            # pointer direction in x-z (0 deg = up)
    P.obox("node:dial-ir|M-WHITE-PA", (dx - 0.6 * uz + 0.5 * ux, -D - dp, dzc + 0.6 * ux + 0.5 * uz), (ux, 0, uz), (0, -1, 0), (uz, 0, -ux), 4.8, 0.3, 1.2)   # right-handed axes
    P.pivot("dial-ir", "rotate", (dx, -D, dzc), axis=(0, 1, 0), range=(0, SPAN))     # +angle turns it clockwise seen from the front, as `setting`
    # reset button in its pocket, pressing toward the mounting plane (+y)
    bx, bz, bs, bp, bl = BTN; ps, pd = POCKET
    P.cutbox("M-GASKET", bx - ps / 2, -D - 0.5, bz - ps / 2, ps, pd + 0.5, ps, fh)
    yb = -D - bp + (PRESS if pressed else 0.0)
    P.box("node:btn-reset|M-BLUE", bx - bs / 2, yb, bz - bs / 2, bs, bl, bs)
    P.pivot("btn-reset", "translate", (bx, -D - bp, bz), axis=(0, 1, 0), range=(0, PRESS))
    din.indicator(P, "ind-trip", bx - 4.0, 8.0, -D, -10.0)                                  # trip indicator window (red / green in the twin)
    lx0, lx1, lz0, lz1 = LEGEND
    P.box("M-WHITE-PA", lx0, -D - 0.1, lz0, lx1 - lx0, 0.1, lz1 - lz0)                       # legend field (decal: class, range, generic label)
    P.collider("env", 0, -D - DIAL[3] - 0.3, -H / 2, W, D + DIAL[3] + 0.3 + 7.5, H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear rail clip", az=60, el=25),
            dict(name="face dial reset and trip indicator", az=255, el=10, center=(22.5, -76, -2), height=56),
            dict(name="set dial at full scale, reset pressed", az=245, el=10, center=(22.5, -76, 2), height=24, params=dict(setting=270.0, pressed=True)),
            dict(name="top line and auxiliary terminals", az=230, el=55, center=(22.5, -56, 34), height=34)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
