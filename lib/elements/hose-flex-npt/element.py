#!/usr/bin/env python3
"""hose-flex-npt: a flexible connecting hose, a rubber core under a stainless wire braid, with a crimped ferrule and a hex end
fitting at each end, each end a male NPT stub: it joins two female NPT ports that move against each other or don't line up (a
valve on a moving carriage, a machine's coolant or air line across a hinge, a gauge set off a vibrating pump). Generic
(OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC004090 "Flexible connecting hose
(plastic/silicone/rubber core)"; the class values it is designed to are in spec.md "## Class values". No dimensional standard on
file shapes a braided connecting hose's section or its crimped ends; the end threads take their series from toolkit/pneu.py
(request pneu-1: D1 NPT threads) and each stub is nipple-hex-npt 1.1's: a plain cylinder L2 long at E1 + h from pneu.NPT (values
calculated from ASME B1.20.1's formulas, EM 2026-11-07). The hose is drawn straight, at rest: the bend it takes in a machine is
not modelled (nothing the twin reads), so it is one fixed body with two ports. The bore is not drawn. No vendor file was opened
(pneu-r118)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "hose-flex-npt", "1.0", "connector"
TITLE = "generic braided connecting hose, male NPT 1/4 both ends, 300 long"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic flexible connecting hose, plastic/silicone/rubber core (ETIM 10.0 EC004090), a rubber core "
            "under a stainless wire braid with a crimped hex end fitting at each end; NPT series from toolkit/pneu.py D1, male "
            "stubs from pneu.NPT (calculated from ASME B1.20.1's formulas); the hose, ferrule and hex sizes are design choices")
ORIGIN = ("joint plane: port-a's seat face (the first hex's -y face) y = 0 on the hose's axis (x = z = 0); port-a's host port "
          "toward -y, the hose toward +y, drawn straight, port-b's seat face at y = length")
COMMAND = "HOSE-FLEX-NPT"
PARAMS = dict(thread="NPT1/4", length=300)

HEX_AF = {"NPT1/4": 17.0, "NPT3/8": 21.0}    # design: nipple-hex-npt 1.1's flats per thread size, so one wrench fits
HEX_L = 8.0                                  # design: end hex length along y (envelope edges >= 8 for the AutoCAD fillet pre-flight)
HEX_D = 1.06                                 # design: corners turned to 1.06 x AF (cap-hex-npt's, so the Godot envelope rounding holds)
STUB_IN = 0.5                                # each stub runs 0.5 into its hex (one solid joint), nipple-hex-npt's
FER_D = {"NPT1/4": 15.0, "NPT3/8": 19.0}     # design: the crimped ferrule's Ø per end size, 2 under the hex's flats
FER_L = 22.0                                 # design: the ferrule's length along y (runs 0.5 into the hex)
HOSE_D = {"NPT1/4": 12.0, "NPT3/8": 16.0}    # design: the braided hose's outside Ø per end size, drawn solid
LEN_MIN, LEN_MAX = 100.0, 1500.0             # design: the shortest and longest hose built, seat face to seat face
MAT_END = "M-ZINC"                           # class value: end fittings and ferrules, zinc-plated steel
MAT_HOSE = "M-SILVER"                        # class value: the stainless steel wire braid over the rubber core

for _t in HEX_AF:
    assert _t in pneu.THREADS
    _tb = pneu.NPT[_t]["table"]
    assert HEX_AF[_t] > (_tb["E2"] + _tb["h"]) * 25.4      # each hex's flats clear its thread's largest major diameter (E2 + h)
    assert HOSE_D[_t] < FER_D[_t] < HEX_AF[_t]             # the hex is the widest part, so the envelope is the hex's
    assert round(HEX_AF[_t] * HEX_D) - HEX_AF[_t] <= 1.5   # Godot's catalogue envelope rounding (cap-hex-npt, pneu-r106)
    assert HOSE_D[_t] >= 2.5 * 0.5 * 2                     # every section well above the fillet pre-flight's 1.25
assert HEX_L >= 8.0 and LEN_MIN >= 2 * (HEX_L + FER_L) + 20.0   # the shortest hose keeps 20 of bare hose between its ferrules


def stub(thread):
    """(diameter, length) of the NPT male stub in mm from pneu.NPT: the major diameter at the hand-tight plane, E1 + h, and L2"""
    t = pneu.NPT[thread]["table"]
    return (t["E1"] + t["h"]) * 25.4, pneu.NPT[thread]["length"]


def overall(thread="NPT1/4", length=300):
    """stub end to stub end along y: L2 + seat-to-seat length + L2 (320.42 for the default)"""
    return float(length) + 2 * stub(thread)[1]


def _hex(P, L, y0, y1, af, d, turn=0.0):
    """a hex prism on the y axis: a cylinder of diameter d with six flats cut at af / 2 (nipple-hex-npt's and plug-hex-npt's pattern)"""
    c = P.cyl(L, (0, y0, 0), (0, y1, 0), d / 2.0); lo = min(y0, y1); w = d + 4.0
    for k in range(6):
        t = math.radians(30 + turn + 60 * k); n = (math.sin(t), 0.0, math.cos(t)); tg = (math.cos(t), 0.0, -math.sin(t))
        o = (n[0] * af / 2.0 + tg[0] * w / 2.0, lo - 1.0, n[2] * af / 2.0 + tg[2] * w / 2.0)
        P.cut(L, o, n, (0, 1, 0), (-tg[0], 0.0, -tg[2]), 4.0, abs(y1 - y0) + 2.0, w, c)
    return c


def build(thread="NPT1/4", length=300):
    if thread not in HEX_AF: raise ValueError(f"thread {thread}: one of {', '.join(HEX_AF)} (pneu.THREADS, D1)")
    L = float(length)
    if not LEN_MIN <= L <= LEN_MAX: raise ValueError(f"length {length}: {LEN_MIN:g} to {LEN_MAX:g} (seat face to seat face)")
    P = Prims(); af = HEX_AF[thread]; fd = FER_D[thread]; hd = HOSE_D[thread]
    sd, sl = stub(thread)
    _hex(P, MAT_END, 0.0, HEX_L, af, af * HEX_D)                                                 # end a's hex, port-a's seat face on y = 0
    P.cyl(f"node:port-a|{MAT_END}", (0, -sl, 0), (0, STUB_IN, 0), sd / 2.0)                      # NPT male stub a, L2 below y = 0
    P.cyl(MAT_END, (0, HEX_L - 0.5, 0), (0, HEX_L + FER_L, 0), fd / 2.0)                         # ferrule a
    P.cyl(MAT_HOSE, (0, HEX_L + FER_L - 0.5, 0), (0, L - HEX_L - FER_L + 0.5, 0), hd / 2.0)      # the braided hose, straight
    P.cyl(MAT_END, (0, L - HEX_L - FER_L, 0), (0, L - HEX_L + 0.5, 0), fd / 2.0)                 # ferrule b
    _hex(P, MAT_END, L - HEX_L, L, af, af * HEX_D)                                               # end b's hex, port-b's seat face on y = L
    P.cyl(f"node:port-b|{MAT_END}", (0, L - STUB_IN, 0), (0, L + sl, 0), sd / 2.0)               # NPT male stub b, L2 past y = L
    P.pivot("port-a", "port", (0, 0, 0), axis=(0, -1, 0), range=(0, 0), unit=thread, gender="male", length=round(sl, 3))
    P.pivot("port-b", "port", (0, L, 0), axis=(0, 1, 0), range=(0, 0), unit=thread, gender="male", length=round(sl, 3))
    r = af * HEX_D / 2.0
    P.collider("env", -r, -sl, -r, 2 * r, overall(thread, L), 2 * r)
    return P


PREVIEWS = [dict(name="three-quarter", az=250, el=25), dict(name="end", az=250, el=-40),
            dict(name="short", az=250, el=25, params=dict(length=100)),
            dict(name="npt38", az=250, el=25, params=dict(thread="NPT3/8"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
