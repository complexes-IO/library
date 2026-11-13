#!/usr/bin/env python3
"""hose-coolant-seg-npt: a segmented (joint) coolant hose for a lathe or a mill: a hex base with one male NPT stub, screwed into a
machine's coolant outlet (coolant-pump's line, a manifold's port), then a stack of snap-together plastic segments, each a ball-like
body on a neck, that the operator bends by hand to aim the coolant at the cut, and a round nozzle at the free end.
Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC010441 "Coolant hose for lathe/miller"
(synonyms "Joint and coolant hose", "Joint flexible coolant hose"); the class values it is designed to are in spec.md "## Class
values". No dimensional standard shapes a segmented coolant hose (each system's segments are its own); the base's thread takes its
series from toolkit/pneu.py (request pneu-1: D1 NPT threads) and its stub is nipple-hex-npt 1.0's and plug-hex-npt's: a plain
cylinder L2 long at E1 + h from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07). The segments are drawn
straight, at rest: the hand-set bend is not modelled (nothing the twin reads), so the hose is one fixed body with one port. The
coolant passage is not drawn. The nozzle's outlet discharges to the cut, so it is no port. No vendor file was opened (pneu-r117)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "hose-coolant-seg-npt", "1.0", "connector"
TITLE = "generic segmented coolant hose, male NPT 1/4 base, 16 segments"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic coolant hose for lathe/miller (ETIM 10.0 EC010441), a segmented joint hose on a hex base with "
            "a round nozzle; NPT series from toolkit/pneu.py D1, male stub from pneu.NPT (calculated from ASME B1.20.1's formulas); "
            "segment sizes our design choices")
ORIGIN = ("joint plane: port-a's seat face (the base hex's -y face) y = 0 on the hose's axis (x = z = 0); the stub and the host "
          "port toward -y, the hose and nozzle toward +y, drawn straight")
COMMAND = "HOSE-COOLANT-SEG-NPT"
PARAMS = dict(thread="NPT1/4", segments=16)

HEX_AF = {"NPT1/4": 17.0, "NPT3/8": 21.0}   # design: nipple-hex-npt 1.0's flats per thread size, so one wrench fits
HEX_L = 8.0                                  # design: base hex length along y (envelope edges >= 8 for the AutoCAD fillet pre-flight)
HEX_D = 1.06                                 # design: corners turned to 1.06 x AF (cap-hex-npt's, so the Godot envelope rounding holds)
STUB_IN = 0.5                                # the stub runs 0.5 into the hex (one solid joint), plug-hex-npt's
BALL_D, BALL_L = 16.0, 10.0                  # design: each segment's ball-like body, Ø16 x 10 along y
NECK_D, NECK_L = 10.0, 6.0                   # design: each segment's neck, Ø10 x 6 between bodies (runs 0.5 into each)
PITCH = BALL_L + NECK_L                      # 16 per segment
NOZ_D, NOZ_L = 10.0, 10.0                    # design: the nozzle's body after the last segment's neck
TIP_D, TIP_L = 6.0, 8.0                      # design: the nozzle's round tip, Ø6 x 8 (its outlet face the coolant's exit)
SEG_MIN, SEG_MAX = 4, 40                     # design: the shortest and longest stack built
MAT = "M-BLUE"                               # class value: acetal (POM) segments and base, blue (a design choice for its look)

for _t in HEX_AF:
    assert _t in pneu.THREADS
    _tb = pneu.NPT[_t]["table"]
    assert HEX_AF[_t] > (_tb["E2"] + _tb["h"]) * 25.4      # each hex's flats clear its thread's largest major diameter (E2 + h)
    assert HEX_AF[_t] > BALL_D                             # the hex is the widest part, so the envelope is the hex's
    assert round(HEX_AF[_t] * HEX_D) - HEX_AF[_t] <= 1.5   # Godot's catalogue envelope rounding (cap-hex-npt, pneu-r106)
assert NECK_D < BALL_D and TIP_D < NOZ_D and min(NECK_D, TIP_D) >= 2.5 * 0.5 * 2   # every wall well above the fillet's 1.25
assert HEX_L >= 8.0


def stub(thread):
    """(diameter, length) of the NPT male stub in mm from pneu.NPT: the major diameter at the hand-tight plane, E1 + h, and L2"""
    t = pneu.NPT[thread]["table"]
    return (t["E1"] + t["h"]) * 25.4, pneu.NPT[thread]["length"]


def length(segments=16):
    """seat face to nozzle tip along y: hex + segments x pitch + nozzle (the stub below y = 0 not counted); class value length"""
    return HEX_L + segments * PITCH + NECK_L + NOZ_L + TIP_L


def _hex(P, L, y0, y1, af, d, turn=0.0):
    """a hex prism on the y axis: a cylinder of diameter d with six flats cut at af / 2 (nipple-hex-npt's and plug-hex-npt's pattern)"""
    c = P.cyl(L, (0, y0, 0), (0, y1, 0), d / 2.0); lo = min(y0, y1); w = d + 4.0
    for k in range(6):
        t = math.radians(30 + turn + 60 * k); n = (math.sin(t), 0.0, math.cos(t)); tg = (math.cos(t), 0.0, -math.sin(t))
        o = (n[0] * af / 2.0 + tg[0] * w / 2.0, lo - 1.0, n[2] * af / 2.0 + tg[2] * w / 2.0)
        P.cut(L, o, n, (0, 1, 0), (-tg[0], 0.0, -tg[2]), 4.0, abs(y1 - y0) + 2.0, w, c)
    return c


def build(thread="NPT1/4", segments=16):
    if thread not in HEX_AF: raise ValueError(f"thread {thread}: one of {', '.join(HEX_AF)} (pneu.THREADS, D1)")
    segments = int(segments)
    if not SEG_MIN <= segments <= SEG_MAX: raise ValueError(f"segments {segments}: {SEG_MIN} to {SEG_MAX}")
    P = Prims(); af = HEX_AF[thread]
    sd, sl = stub(thread)
    _hex(P, MAT, 0.0, HEX_L, af, af * HEX_D)                                                     # base hex, its seat face on y = 0
    P.cyl(f"node:port-a|{MAT}", (0, -sl, 0), (0, STUB_IN, 0), sd / 2.0)                          # NPT male stub, L2 below y = 0
    y = HEX_L
    for _ in range(segments):                                                                    # neck, then body, per segment
        P.cyl(MAT, (0, y - 0.5, 0), (0, y + NECK_L + 0.5, 0), NECK_D / 2.0)
        P.cyl(MAT, (0, y + NECK_L, 0), (0, y + PITCH, 0), BALL_D / 2.0)
        y += PITCH
    P.cyl(MAT, (0, y - 0.5, 0), (0, y + NECK_L + 0.5, 0), NECK_D / 2.0)                          # the nozzle's neck
    y += NECK_L
    P.cyl(MAT, (0, y, 0), (0, y + NOZ_L, 0), NOZ_D / 2.0)                                        # nozzle body
    P.cyl(MAT, (0, y + NOZ_L - 0.5, 0), (0, y + NOZ_L + TIP_L, 0), TIP_D / 2.0)                  # nozzle tip
    assert abs(y + NOZ_L + TIP_L - length(segments)) < 1e-9
    P.pivot("port-a", "port", (0, 0, 0), axis=(0, -1, 0), range=(0, 0), unit=thread, gender="male", length=round(sl, 3))
    r = af * HEX_D / 2.0
    P.collider("env", -r, -sl, -r, 2 * r, length(segments) + sl, 2 * r)
    return P


PREVIEWS = [dict(name="three-quarter", az=250, el=25), dict(name="base", az=250, el=-40),
            dict(name="short", az=250, el=25, params=dict(segments=4)),
            dict(name="npt38", az=250, el=25, params=dict(thread="NPT3/8"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
