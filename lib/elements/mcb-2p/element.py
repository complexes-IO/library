#!/usr/bin/env python3
"""mcb-2p: miniature circuit breaker, 2-pole, both poles on one handle and one trip (they open together). A generic element (OPERATING.md 12,
EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC000042 "Miniature circuit breaker (MCB)", built to the class values in spec.md
"## Class values"; no maker's datasheet. Inventory row mcb-2p (request panel-1 item 2, the core's answer of 2026-11-11): the control
transformer's primary across two phases, two poles of the mcb family whose figures are on file under mcb-3p-c10.
What it meets comes from elements and the toolkit on file: the body, pole pitch, terminal spacing, rail clip, toggle and pole indicators
are the family's (mcb-3p-c10 1.3, read with library.load, as mcb-1p-c6 builds one pole of it); the 35 mm rail clip is toolkit/din.py.
The one change from the family's body: each terminal screw is a named port node t-<mark> (BEH-020: the twin's probe touches it).
The rated current is not chosen (NEC 430.72(C), the table it is sized by, is not on file): the size goes into the id when it is.
1.1 (elec-r32): text only, geometry as 1.0. behaviour.csv's reset row carries the family's Assumption (A) (trip-free; review
mcb-2p-1.0 finding 1, an ESCAPE: a "design choice" with no rule on a behaviour row), with the line in spec.md's Notes."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "mcb-2p", "1.1", "device"
TITLE = "miniature circuit breaker, 2-pole (one handle, common trip), 35 mm rail"
TOOLKIT = "1.3"
BASELINE = "our own design: generic Miniature circuit breaker (ETIM 10.0 EC000042); body, pitch and terminals the mcb family's on file (mcb-3p-c10 1.3), two poles; rated current not chosen (NEC 430.72(C) NOT ON FILE)"
ORIGIN = "rail device: back face on the rail crown y = 0, rail centreline z = 0, left face of pole 1 x = 0, body toward -y"
COMMAND = "MCB2"
PARAMS = {}
POLES = 2
FAMILY, FAMILY_VERSION = "mcb-3p-c10", "1.3"
MARKS = (("1", "2"), ("3", "4"))               # line (top), load (bottom) per pole: printed on our part, a design choice (spec.md Dimensions)

def build():
    f = library.load(FAMILY, FAMILY_VERSION)
    PITCH, H, D, CLIP, FRONT, SHOULDER, TERM = f.PITCH, f.H, f.D, f.CLIP, f.FRONT, f.SHOULDER, f.TERM
    P = Prims(); W = PITCH * POLES
    P.box("M-GREY-PA", 0, -SHOULDER, -H / 2, W, SHOULDER, H)                                      # base to the shoulder line
    P.box("M-GREY-PA", 0, -FRONT, -22.5, W, FRONT - SHOULDER, 45.0)                               # raised 45 mm front
    din.rail_clip(P, 0, W)
    for i in range(POLES):
        x0 = i * PITCH; cx = x0 + PITCH / 2
        for sz, mk in zip((1, -1), MARKS[i]):                                                     # captive screw terminal per pole, line top, load bottom
            n = f"t-{mk}"; z = sz * TERM / 2
            P.cyl(f"node:{n}|M-ZINC", (cx, -SHOULDER, z), (cx, -SHOULDER - 1.2, z), 2.6)
            P.pivot(n, "port", (cx, -SHOULDER - 1.2, z), axis=(0, -1, 0), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp
            P.box("M-GASKET", cx - 2.3, -SHOULDER + 3, sz * H / 2 - (0.4 if sz > 0 else 0.1), 4.6, 10, 0.5)           # wire entry (the family's)
        din.indicator(P, f"indicator-{i + 1}", x0, PITCH, -FRONT, 14.0)
        P.box("M-WHITE-PA", x0 + 2, -FRONT - 0.2, -20, PITCH - 4, 0.2, 8)                         # label field: complexes.org and the marks
    din.toggle(P, "toggle", 0, W, -FRONT, 0.0)                                                     # one common handle (the family's toggle)
    P.collider("env", 0, -(D - CLIP), -H / 2, W, D, H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="terminals and rail clip", az=60, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
