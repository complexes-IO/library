#!/usr/bin/env python3
"""nipple-hex-npt: hex nipple, straight, one male NPT thread at each end of a wrench hex, joining two female NPT ports of the same
size face to face (a drain valve hung under a receiver's drain port, a gauge stood off a port). Generic (OPERATING.md 12, EM
2026-11-07): our own vendor-neutral design of ETIM 10.0 EC010803 "Hydraulic nipple, 2 connections"; the class values it is
designed to are in spec.md "## Class values". Series and units come from toolkit/pneu.py (request pneu-1: D1 NPT threads). Each
male stub is fitting-pushin 2.0's: a plain cylinder L2 long at the external thread's major diameter at the hand-tight plane,
E1 + h, from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07); the 1:16 taper and the thread form are not
drawn (the library draws threads plain). The hex's flats are fitting-pushin's per thread size, so one wrench fits both; its
length and the flow bore (not drawn) are design choices. Each joint is a pivot on its axis at a hex face. No vendor file was
opened (pneu-r97)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "nipple-hex-npt", "1.1", "connector"
TITLE = "generic hex nipple, straight, male NPT 1/4 both ends"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic hydraulic nipple, 2 connections (ETIM 10.0 EC010803), a straight hex nipple; NPT series from "
            "toolkit/pneu.py D1, male stubs from pneu.NPT (calculated from ASME B1.20.1's formulas); the hex and its length are "
            "design choices")
ORIGIN = ("joint plane: port-a's seat face (the hex's -y face) y = 0 on the thread's axis (x = z = 0); port-a's host port toward -y, "
          "port-b's toward +y")
COMMAND = "NIPPLE-HEX-NPT"
PARAMS = dict(thread="NPT1/4")

HEX_AF = {"NPT1/8": 14.0, "NPT1/4": 17.0, "NPT3/8": 21.0}   # design choices: fitting-pushin 2.0's wrench flats per thread size
HEX_L = 8.0                                                # design choice: hex length along y (envelope edges >= 8 for the AutoCAD fillet)
HEX_D = 1.12                                               # corners turned to 1.12 x AF (a sharp hex is 1.155 x AF), fitting-pushin's
STUB_IN = 0.5                                              # each stub runs 0.5 into the hex (one solid joint)
MAT = "M-ZINC"                                             # class value 1: steel; the zinc plating a design choice (no class value)

for _t in HEX_AF:
    assert _t in pneu.THREADS
    _tb = pneu.NPT[_t]["table"]
    assert HEX_AF[_t] > (_tb["E2"] + _tb["h"]) * 25.4      # each hex's flats clear its thread's largest major diameter (E2 + h)
    assert HEX_L >= 8.0


def stub(thread):
    """(diameter, length) of the NPT male stub in mm from pneu.NPT: the major diameter at the hand-tight plane, E1 + h, and L2"""
    t = pneu.NPT[thread]["table"]
    return (t["E1"] + t["h"]) * 25.4, pneu.NPT[thread]["length"]


def length(thread="NPT1/4"):
    """overall length, stub end to stub end: L2 + hex + L2 (28.41 for NPT 1/4)"""
    return 2 * stub(thread)[1] + HEX_L


def _hex(P, L, y0, y1, af, d, turn=0.0):
    """a hex prism on the y axis: a cylinder of diameter d with six flats cut at af / 2 (fitting-pushin's and gland-m20's pattern)"""
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
    _hex(P, MAT, 0.0, HEX_L, af, af * HEX_D)                                                     # hex, port-a's seat face on y = 0
    P.cyl(f"node:port-a|{MAT}", (0, -sl, 0), (0, STUB_IN, 0), sd / 2.0)                          # NPT male stub a, L2 below y = 0
    P.cyl(f"node:port-b|{MAT}", (0, HEX_L - STUB_IN, 0), (0, HEX_L + sl, 0), sd / 2.0)           # NPT male stub b, L2 above the hex
    P.pivot("port-a", "port", (0, 0, 0), axis=(0, -1, 0), range=(0, 0), unit=thread, gender="male", length=round(sl, 3))
    P.pivot("port-b", "port", (0, HEX_L, 0), axis=(0, 1, 0), range=(0, 0), unit=thread, gender="male", length=round(sl, 3))
    r = af * HEX_D / 2.0
    P.collider("env", -r, -sl, -r, 2 * r, HEX_L + 2 * sl, 2 * r)
    return P


PREVIEWS = [dict(name="three-quarter", az=250, el=25), dict(name="end on port-a", az=250, el=-40),
            dict(name="thread NPT 1/8", az=250, el=25, params=dict(thread="NPT1/8")),
            dict(name="thread NPT 3/8", az=250, el=25, params=dict(thread="NPT3/8"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
