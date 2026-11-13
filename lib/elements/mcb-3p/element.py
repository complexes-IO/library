#!/usr/bin/env python3
"""mcb-3p: miniature circuit breaker, 3-pole, the three poles on one handle and one trip (they open together). A generic element
(OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC000042 "Miniature circuit breaker (MCB)", built to the
class values in spec.md "## Class values"; no maker's datasheet. Inventory row mcb-3p (request panel-6 item 1b; own_design generic by
request elec-13, the core's answer of 2026-11-13): the press-hydraulic panel's motor branch breaker (q3), three poles of the mcb family
whose figures are on file under mcb-3p-c10.
What it meets comes from elements and the toolkit on file: the body, pole pitch, terminal spacing, rail clip, toggle and pole indicators
are the family's (mcb-3p-c10 1.5, read with library.load, as mcb-2p builds two poles of it); the 35 mm rail clip is toolkit/din.py.
Each terminal screw is a named port node t-<mark> (BEH-020), its pivot at the wire entry's mouth on the end face, axis the way the wire
goes in, as the family's 1.4 (PIN-002: a screw clamp, gender none).
The rated current is not chosen (NEC 430.52, Table 430.52, the table the motor branch's breaker is sized by, is not on file): the size
goes into the id when it is (OPERATING.md 6; the library's rename)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "mcb-3p", "1.1", "device"
TITLE = "miniature circuit breaker, 3-pole (one handle, common trip), 35 mm rail"
TOOLKIT = "1.3"
BASELINE = "our own design: generic Miniature circuit breaker (ETIM 10.0 EC000042); body, pitch and terminals the mcb family's on file (mcb-3p-c10 1.5), three poles; rated current not chosen (NEC 430.52 NOT ON FILE)"
ORIGIN = "rail device: back face on the rail crown y = 0, rail centreline z = 0, left face of pole 1 x = 0, body toward -y"
COMMAND = "MCB3G"
PARAMS = {}
POLES = 3
FAMILY, FAMILY_VERSION = "mcb-3p-c10", "1.5"
MARKS = (("1", "2"), ("3", "4"), ("5", "6"))   # line (top), load (bottom) per pole: printed on our part, a design choice (spec.md Dimensions)

def build():
    f = library.load(FAMILY, FAMILY_VERSION)
    PITCH, H, D, CLIP, FRONT, SHOULDER, TERM = f.PITCH, f.H, f.D, f.CLIP, f.FRONT, f.SHOULDER, f.TERM
    P = Prims(); W = PITCH * POLES
    P.box("M-GREY-PA", 0, -SHOULDER, -H / 2, W, SHOULDER, H)                                      # base to the shoulder line
    P.box("M-GREY-PA", 0, -FRONT, -22.5, W, FRONT - SHOULDER, 45.0)                               # raised 45 mm front
    din.rail_clip(P, 0, W)                                                                         # the library's contract for the 35 x 7.5 rail (EN 60715 TH35-7.5)
    for i in range(POLES):
        x0 = i * PITCH; cx = x0 + PITCH / 2
        for sz, mk in zip((1, -1), MARKS[i]):                                                     # captive screw terminal per pole, line top, load bottom
            n = f"t-{mk}"
            P.cyl(f"node:{n}|M-ZINC", (cx, -SHOULDER, sz * TERM / 2), (cx, -SHOULDER - 1.2, sz * TERM / 2), 2.6)
            P.box("M-GASKET", cx - 2.3, -SHOULDER + 3, sz * H / 2 - (0.4 if sz > 0 else 0.1), 4.6, 10, 0.5)   # wire entry (the family's)
            P.pivot(n, "port", (cx, -SHOULDER + 8.0, sz * H / 2), axis=(0, 0, -sz), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp; at the entry's mouth, axis in
        din.indicator(P, f"indicator-{i + 1}", x0, PITCH, -FRONT, 14.0)
        P.box("M-WHITE-PA", x0 + 2, -FRONT - 0.2, -20, PITCH - 4, 0.2, 8)                         # label field: complexes.org and the marks
    din.toggle(P, "toggle", 0, W, -FRONT, 0.0)                                                     # one common handle (the family's toggle; swing class C)
    P.collider("env", 0, -(D - CLIP), -H / 2, W, D, H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="terminals and rail clip", az=60, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
