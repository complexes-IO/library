#!/usr/bin/env python3
"""cross-street-npt: street cross, a square steel block with one female NPT port and one male NPT stub in line on the run and two
opposed female NPT ports on the branch at a right angle, all four of one size: it screws straight into a female port (a manifold's,
a receiver's, a valve's) and splits it in three without a nipple, where cross-block-npt 1.1 needs one.
Generic (OPERATING.md 12, EM 2026-11-07; autopilot.md 2.b2): our own vendor-neutral design of ETIM 10.0 EC003026 "Fitting with 4
connections" (synonyms "Ball piece with 4 connections", "Angle fitting"), the next class of EG015540 in pneu's order that builds
after tee-street-npt's EC003025. The block cross's all-female threaded form is cross-block-npt's (EC010805), so this element is the
form that differs: one end male (tee-street-npt 1.1's step from tee-block-npt). Machined from square bar, a form no dimensional
standard shapes, which is why it is generic; the block's section and length are design choices (the block form is the reason, not
whether a standard is on file: review tee-block-npt-1.0.md finding 2). Series and units come from toolkit/pneu.py (request pneu-1:
D1 NPT threads). The three female ports are cross-block-npt's (a blind bore E1 + h, L2 + 2 deep, from pneu.NPT through a land 0.2
proud, the pivot on the land's outer face); the male stub is plug-hex-npt 1.0's (a plain cylinder L2 long at E1 + h, 0.5 into the
block, the pivot on the seat face). Values from pneu.NPT are calculated from ASME B1.20.1's formulas (EM 2026-11-07). The flow
passages where the bores meet and through the stub are not drawn (cross-block-npt's way). No vendor file was opened (pneu-r110)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "cross-street-npt", "1.0", "connector"
TITLE = "generic street cross, female NPT 1/4 run end and two branches, male NPT 1/4 run end, square steel bar"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic fitting with 4 connections (ETIM 10.0 EC003026), a street cross machined from square bar; NPT "
            "series from toolkit/pneu.py D1, female ports bored at E1 + h and the male stub at E1 + h from pneu.NPT (calculated from "
            "ASME B1.20.1's formulas); the block's section and length are design choices")
ORIGIN = ("where the run and branch axes meet, on their plane (z = 0): port-a (female) toward -x and port-b (the male stub's seat "
          "face) toward +x on the run, port-c (female) toward +y and port-d (female) toward -y on the branch")
COMMAND = "CROSS-STREET-NPT"
PARAMS = dict(thread="NPT1/4")

SECTION = {"NPT1/8": 22.0, "NPT1/4": 28.0, "NPT3/8": 28.0}   # cross-block-npt's square bar side (y and z): opposed branch bores
HALF_A = {"NPT1/8": 17.0, "NPT1/4": 23.0, "NPT3/8": 24.0}    # cross-block-npt's half run: the female run end's face at x = -HALF_A
LAND = {"NPT1/8": 14.0, "NPT1/4": 18.0, "NPT3/8": 21.0}      # cross-block-npt's square land round each female bore (the port node)
LAND_T = 0.2                                                 # each land 0.2 proud of its face (GEO-050), cross-block-npt's
STUB_IN = 0.5                                                # the stub runs 0.5 into the block (one solid joint), plug-hex-npt's
WALL = 3.0                                                   # design choice: at least 3 mm of steel round and between bores
MAT = "M-ZINC"                                               # steel, zinc-plated (cross-block-npt's)


def bore(thread="NPT1/4"):
    """(diameter, depth) of a female port in mm from pneu.NPT: E1 + h, the male's major diameter at the hand-tight plane, and
    L2 + 2, a run-out past the male's effective thread (tank 2.0)"""
    t = pneu.NPT[thread]["table"]
    return (t["E1"] + t["h"]) * 25.4, pneu.NPT[thread]["length"] + 2.0


def stub(thread="NPT1/4"):
    """(diameter, length) of the male stub in mm from pneu.NPT: E1 + h and L2 (plug-hex-npt's)"""
    t = pneu.NPT[thread]["table"]
    return (t["E1"] + t["h"]) * 25.4, pneu.NPT[thread]["length"]


for _t in SECTION:
    assert _t in pneu.THREADS
    _d, _l = bore(_t); _a, _h = SECTION[_t], HALF_A[_t]; _sd, _sl = stub(_t); _tb = pneu.NPT[_t]["table"]
    assert _l >= pneu.NPT[_t]["engagement"]                  # deeper than a male's make-up (L1 + L3)
    assert _a - _d >= 2 * WALL                               # steel round each bore across the section
    assert _h - _l - _d / 2 >= WALL                          # the run bore's floor stays clear of the branch bores' sides
    assert _a / 2 - _d / 2 >= WALL                           # the stub end's block wall past the branch bores (x = +a / 2)
    assert _a - 2 * _l >= WALL                               # the two opposed branch bores' floors keep steel between them
    assert _d + 2.0 < LAND[_t] < _a                          # the land rings its bore, inside the face
    assert _a > (_tb["E2"] + _tb["h"]) * 25.4                # the stub's seat face is wider than the female's mouth (E2 + h)
    assert _a >= 8.0 and _sl >= 6.0                          # envelope edges >= 8 (the AutoCAD fillet pre-flight)


def length(thread="NPT1/4"):
    """overall length along the run, port-a's land face to the stub's end (47.405 for NPT 1/4)"""
    return HALF_A[thread] + LAND_T + SECTION[thread] / 2 + stub(thread)[1]


def _female(P, body, name, d, c, thread):
    """a female NPT port on the face at distance c whose outward normal is d (a unit vector in x or y): the plain bore into the
    body, its land (the node) with the bore through it, and the pivot on the land's outer face, its axis out of the block
    (cross-block-npt 1.1's _port)"""
    dx, dy = d; bd, bl = bore(thread); h = LAND[thread] / 2
    P.hole("M-GASKET", (dx * (c + 1.0), dy * (c + 1.0), 0), (dx * (c - bl), dy * (c - bl), 0), bd / 2, body)
    if dx:
        x0 = c if dx > 0 else -c - LAND_T
        f = P.box(f"node:{name}|{MAT}", x0, -h, -h, LAND_T, 2 * h, 2 * h)
    else:
        y0 = c if dy > 0 else -c - LAND_T
        f = P.box(f"node:{name}|{MAT}", -h, y0, -h, 2 * h, LAND_T, 2 * h)
    e = c + LAND_T
    P.hole("M-GASKET", (dx * (e + 1.0), dy * (e + 1.0), 0), (dx * (c - 1.0), dy * (c - 1.0), 0), bd / 2, f)
    P.pivot(name, "port", (dx * e, dy * e, 0), axis=(dx, dy, 0), range=(0, 0), unit=thread, gender="female")


def build(thread="NPT1/4"):
    if thread not in SECTION: raise ValueError(f"thread {thread}: one of {', '.join(SECTION)} (pneu.THREADS, D1)")
    P = Prims(); a, ha = SECTION[thread], HALF_A[thread]; sd, sl = stub(thread)
    body = P.box(MAT, -ha, -a / 2, -a / 2, ha + a / 2, a, a)            # the square bar, the run along x, its +x end square on the branch
    _female(P, body, "port-a", (-1, 0), ha, thread)                     # run end a, -x, female (the class's connection 1)
    _female(P, body, "port-c", (0, 1), a / 2, thread)                   # branch c, +y, female (connection 3), at 90° to the run
    _female(P, body, "port-d", (0, -1), a / 2, thread)                  # branch d, -y, female (connection 4), opposite c
    x0 = a / 2                                                          # the male end's seat face, the block's +x face
    P.cyl(f"node:port-b|{MAT}", (x0 - STUB_IN, 0, 0), (x0 + sl, 0, 0), sd / 2.0)   # run end b, +x, NPT male stub L2 long
    P.pivot("port-b", "port", (x0, 0, 0), axis=(1, 0, 0), range=(0, 0), unit=thread, gender="male", length=round(sl, 3))
    e, f = ha + LAND_T, a / 2 + LAND_T
    P.collider("env", -e, -f, -a / 2, e + x0 + sl, 2 * f, a)
    return P


PREVIEWS = [dict(name="three-quarter", az=250, el=25), dict(name="male end port-b", az=110, el=20),
            dict(name="thread NPT 1/8", az=250, el=25, params=dict(thread="NPT1/8")),
            dict(name="thread NPT 3/8", az=250, el=25, params=dict(thread="NPT3/8"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
