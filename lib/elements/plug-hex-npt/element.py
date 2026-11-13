#!/usr/bin/env python3
"""plug-hex-npt: hex-head plug, one male NPT thread under a wrench hex, closing a female NPT port of the same size (a spare port of
a manifold, a tee's or a cross's unused branch, a receiver's unused tapping: "every port connected or plugged", request pneu-1).
Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC010806 "Hydraulic threaded plug" (synonym
"Hydraulic screw plug"); the class values it is designed to are in spec.md "## Class values". Series and units come from
toolkit/pneu.py (request pneu-1: D1 NPT threads). The male stub is nipple-hex-npt 1.0's and fitting-pushin 2.0's: a plain cylinder
L2 long at the external thread's major diameter at the hand-tight plane, E1 + h, from pneu.NPT (values calculated from ASME
B1.20.1's formulas, EM 2026-11-07); the 1:16 taper and the thread form are not drawn (the library draws threads plain). The head is
nipple-hex-npt's hex (fitting-pushin's flats per thread size, 8 long), so one wrench fits all three. A hex head over a male NPT end is
ASME B16.11's hex-head plug's form, so the head's flats and height are B16.11's figures: a class B line in spec.md (the document
wanted), the hex drawn here a stand-in until it is on file (1.1, review plug-hex-npt-1.0.md finding 1). The joint is a pivot on its
axis at the hex's seat face. No vendor file was opened (pneu-r100)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "plug-hex-npt", "1.1", "connector"
TITLE = "generic hex-head plug, male NPT 1/4"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic hydraulic threaded plug (ETIM 10.0 EC010806), a hex-head plug from hex bar; NPT series from "
            "toolkit/pneu.py D1, male stub from pneu.NPT (calculated from ASME B1.20.1's formulas); the hex head a stand-in for "
            "ASME B16.11's, whose table is a class B document wanted")
ORIGIN = ("joint plane: port-a's seat face (the hex's -y face) y = 0 on the thread's axis (x = z = 0); the stub and the host port "
          "toward -y, the head toward +y")
COMMAND = "PLUG-HEX-NPT"
PARAMS = dict(thread="NPT1/4")

HEX_AF = {"NPT1/8": 14.0, "NPT1/4": 17.0, "NPT3/8": 21.0}   # stand-in for B16.11's head (class B): nipple-hex-npt 1.0's flats per thread size
HEX_L = 8.0                                                # stand-in (class B, B16.11): head length along y (envelope edges >= 8 for the AutoCAD fillet)
HEX_D = 1.12                                               # corners turned to 1.12 x AF (a sharp hex is 1.155 x AF), nipple-hex-npt's
STUB_IN = 0.5                                              # the stub runs 0.5 into the head (one solid joint)
MAT = "M-ZINC"                                             # class value 1: steel, zinc-plated (a design choice for its look)

for _t in HEX_AF:
    assert _t in pneu.THREADS
    _tb = pneu.NPT[_t]["table"]
    assert HEX_AF[_t] > (_tb["E2"] + _tb["h"]) * 25.4      # each head's flats clear its thread's largest major diameter (E2 + h)
    assert HEX_L >= 8.0


def stub(thread):
    """(diameter, length) of the NPT male stub in mm from pneu.NPT: the major diameter at the hand-tight plane, E1 + h, and L2"""
    t = pneu.NPT[thread]["table"]
    return (t["E1"] + t["h"]) * 25.4, pneu.NPT[thread]["length"]


def length(thread="NPT1/4"):
    """overall length, stub end to head top: L2 + head (18.21 for NPT 1/4); class value 11"""
    return stub(thread)[1] + HEX_L


def _hex(P, L, y0, y1, af, d, turn=0.0):
    """a hex prism on the y axis: a cylinder of diameter d with six flats cut at af / 2 (nipple-hex-npt's and fitting-pushin's pattern)"""
    c = P.cyl(L, (0, y0, 0), (0, y1, 0), d / 2.0); lo = min(y0, y1); w = d + 4.0
    for k in range(6):
        t = math.radians(30 + turn + 60 * k); n = (math.sin(t), 0.0, math.cos(t)); tg = (math.cos(t), 0.0, -math.sin(t))
        o = (n[0] * af / 2.0 + tg[0] * w / 2.0, lo - 1.0, n[2] * af / 2.0 + tg[2] * w / 2.0)
        P.cut(L, o, n, (0, 1, 0), (-tg[0], 0.0, -tg[2]), 4.0, abs(y1 - y0) + 2.0, w, c)
    return c


def build(thread="NPT1/4"):
    if thread not in HEX_AF: raise ValueError(f"thread {thread}: one of {', '.join(HEX_AF)} (pneu.THREADS, D1)")
    P = Prims(); af = HEX_AF[thread]
    sd, sl = stub(thread)
    _hex(P, MAT, 0.0, HEX_L, af, af * HEX_D)                                                     # hex head, its seat face on y = 0
    P.cyl(f"node:port-a|{MAT}", (0, -sl, 0), (0, STUB_IN, 0), sd / 2.0)                          # NPT male stub, L2 below y = 0
    P.pivot("port-a", "port", (0, 0, 0), axis=(0, -1, 0), range=(0, 0), unit=thread, gender="male", length=round(sl, 3))
    r = af * HEX_D / 2.0
    P.collider("env", -r, -sl, -r, 2 * r, HEX_L + sl, 2 * r)
    return P


PREVIEWS = [dict(name="three-quarter", az=250, el=25), dict(name="end on port-a", az=250, el=-40),
            dict(name="thread NPT 1/8", az=250, el=25, params=dict(thread="NPT1/8")),
            dict(name="thread NPT 3/8", az=250, el=25, params=dict(thread="NPT3/8"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
