#!/usr/bin/env python3
"""disc-dc: DC switch disconnector, 2 poles (L+ and M of one DC circuit), 25 A, 220 V DC, rotary handle 0 / I, screw terminals, on the
35 mm rail. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC004963
"Switch disconnector (DC)", built to the class values in spec.md "## Class values"; no maker's datasheet. What it meets comes from
the contracts on file: the rail clip from toolkit/din.py (rail_clip, the 35 x 7.5 rail of din-rail-35 / EN 60715 TH35-7.5); every
other size is a design choice, said so in spec.md (no distribution-board front profile is claimed: DIN 43880 is not on file).
Modelled from the outside in: base with the terminal shoulders (line 1, 3 on top; load 2, 4 below), raised front, the rotary handle
(base disc, grip, pointer) turned to the position built, legend label; the contact system inside is not modelled in 1.0."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "disc-dc", "1.0", "device"
TITLE = "DC switch disconnector, 2 poles, 25 A, 220 V DC, rotary handle 0 / I, screw terminals, 35 mm rail (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Switch disconnector (DC) (ETIM 10.0 EC004963); class values in spec.md; rail clip from "
            "toolkit/din.py (EN 60715 TH35-7.5 rail, din-rail-35); sizes are design choices; the terminals' conductor range is open (spec.md)")
ORIGIN = "rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward -y"
COMMAND = "DISCDC"
PARAMS = dict(on=False)

# ---- envelope (design choices; the class values Width / Height / Depth in spec.md)
W, H = 36.0, 90.0                    # width (x 0 ... 36), height (z -45 ... 45), centred on the rail
D_BASE = 42.0                        # base with the terminal shoulders: front face at y -42
RAISED = (1.0, 35.0, 20.0, 22.0)     # raised front x0, x1, depth in front of the shoulders (y -62 ... -42), half height (z -22 ... 22)
# ---- terminals: one per pole end, line on top (1, 3), load below (2, 4) (design choices); the conductor range is open (spec.md)
PITCH = 18.0
TOP, BOT = ("1", "3"), ("2", "4")
HEAD_R, HEAD_T, HEAD_DZ = 2.8, 1.2, 7.0    # screw head radius, height, centre 7.0 in from the end face
ENTRY = (5.5, 10.0, 0.5)                   # wire entry slot: width (x), depth (y), cut into the end face (z)
# ---- rotary handle on the raised front (design choices): OFF with the grip across (x), ON turned 90 degrees clockwise (grip upright)
KNOB_R, KNOB_T = 15.0, 3.0           # base disc Ø30 x 3 on the raised front
GRIP = (8.0, 32.0, 10.0)             # grip: width, length (along x at OFF), depth (y)
POINTER = (6.0, 2.0, 0.2, 1.0)       # white pointer inlay on the grip's face: length (along the grip), width, proud, 1.0 in from the -x end
TURN = 90.0                          # OFF 0, ON 90 (clockwise seen from the front)
LABEL = (3.0, 33.0, -33.0, -24.0)    # legend label on the lower shoulder: x0, x1, z0, z1

def _rot(a, v):
    """v turned by a degrees about +y (clockwise seen from the front, -y)"""
    c, s = math.cos(math.radians(a)), math.sin(math.radians(a))
    return (v[0] * c + v[2] * s, v[1], -v[0] * s + v[2] * c)

def _handle_box(P, layer, a, c, x0, x1, y0, y1, z0, z1):
    """a box of the handle, given at OFF about the handle's axis through c, turned a degrees about it"""
    o = _rot(a, (x0, y0, z0)); o = (o[0] + c[0], o[1] + c[1], o[2] + c[2])
    return P.obox(layer, o, _rot(a, (1, 0, 0)), (0, 1, 0), _rot(a, (0, 0, 1)), x1 - x0, y1 - y0, z1 - z0)

def terminals(P, marks, up, target):
    """two screw clamps on a shoulder (front face y = -D_BASE): the head is the port node t-<mark>; the wire entry is a slot cut into
    the end face (the toolkit's terminal_row shape, din.py, with a named node per terminal)"""
    s = 1 if up else -1; z_edge = s * H / 2; x0 = (W - len(marks) * PITCH) / 2
    for i, mk in enumerate(marks):
        cx = x0 + PITCH * (i + 0.5); cz = z_edge - s * HEAD_DZ; n = f"t-{mk}"
        P.cyl(f"node:{n}|M-ZINC", (cx, -D_BASE, cz), (cx, -D_BASE - HEAD_T, cz), HEAD_R)
        P.pivot(n, "port", (cx, -D_BASE - HEAD_T, cz), axis=(0, -1, 0), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp
        w, d, t = ENTRY; z0 = z_edge - (t if up else 0.0)
        P.cutbox("M-GASKET", cx - w / 2, -D_BASE + 2.0, z0 - (0.0 if up else 1.0), w, d, t + 1.0, target)          # out past the end face
        P.box("M-GASKET", cx - w / 2, -D_BASE + 2.0, z0, w, d, t)                                                  # the dark slot in its cut

def build(on=False):
    P = Prims(); G = "M-GREY-PA"
    base = P.box(G, 0, -D_BASE, -H / 2, W, D_BASE, H)                                       # base with the terminal shoulders
    x0, x1, rd, rz = RAISED; yf = -D_BASE - rd
    P.box(G, x0, yf, -rz, x1 - x0, rd, 2 * rz)                                              # raised front (y -62)
    din.rail_clip(P, 0, W)                                                                  # the rail latch (toolkit contract)
    terminals(P, TOP, True, base); terminals(P, BOT, False, base)
    lx0, lx1, lz0, lz1 = LABEL
    P.box("M-WHITE-PA", lx0, -D_BASE - 0.1, lz0, lx1 - lx0, 0.1, lz1 - lz0)                 # legend label (decal: ratings, poles, generic label)
    # ---- rotary handle: base disc, grip and pointer, turned to the position built (the twin turns it about +y)
    a = TURN if on else 0.0; c = (W / 2, yf, 0.0)
    P.cyl("node:handle|M-BLACK-PA", c, (c[0], yf - KNOB_T, 0.0), KNOB_R)
    gw, gl, gd = GRIP; yk = -KNOB_T
    _handle_box(P, "node:handle|M-BLACK-PA", a, c, -gl / 2, gl / 2, yk - gd, yk, -gw / 2, gw / 2)
    pl, pw, pp, pin = POINTER
    _handle_box(P, "node:handle|M-WHITE-PA", a, c, -gl / 2 + pin, -gl / 2 + pin + pl, yk - gd - pp, yk - gd, -pw / 2, pw / 2)
    P.pivot("handle", "rotate", c, axis=(0, 1, 0), range=(-a, TURN - a))
    yh = yf - KNOB_T - gd - pp
    P.collider("env", 0, yh, -H / 2, W, -yh + 7.5, H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear rail clip", az=60, el=25),
            dict(name="front handle at OFF", az=270, el=0, center=(18, -62, 0), height=60),
            dict(name="handle at ON", az=270, el=0, center=(18, -62, 0), height=60, params=dict(on=True)),
            dict(name="top terminals and wire entries", az=230, el=55, center=(18, -42, 38), height=30)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
