#!/usr/bin/env python3
"""cross-block-npt: block cross, four female NPT ports of one size in a cross (two in line on the run, two opposed on the branch at
a right angle) in a square steel bar, joining four male NPT ends (nipples, push-in fittings' stubs, a gauge's stub) where one line
splits in three. Generic (OPERATING.md 12, EM 2026-11-07; autopilot.md 2.b2: the next ETIM class `inventory pneu` lists that builds):
our own vendor-neutral design of ETIM 10.0 EC010805 "Hydraulic threaded cross piece"; the class values it is designed to are in
spec.md "## Class values". tee-block-npt 1.0's four-port sibling: the same run, ports and lands, with a `port-d` on -y. Machined from
square bar (a block cross), not a forged fitting (ASME B16.11's): a form no dimensional standard shapes, which is why it is generic;
the block's section and length are design choices. The two branch bores face each other across the section, so the section is deeper
than the tee's (asserted: 3 of steel between their floors). Series and units come from toolkit/pneu.py (request pneu-1: D1 NPT
threads). Each port is valve-ball-32's: a blind bore at the male's major diameter at the hand-tight plane, E1 + h, L2 + 2 deep (tank
2.0's rule), from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07), through a land 0.2 proud of the face
(the port node), the pivot on the land's outer face (filter-air 3.0's rule). The flow passages where the bores meet are not drawn
(valve-ball-32's way). No vendor file was opened (pneu-r99)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "cross-block-npt", "1.1", "connector"
TITLE = "generic block cross, four female NPT 1/4 ports in a cross, square steel bar"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic hydraulic threaded cross piece (ETIM 10.0 EC010805), a block cross machined from square bar; "
            "NPT series from toolkit/pneu.py D1, female ports bored at E1 + h from pneu.NPT (calculated from ASME B1.20.1's "
            "formulas); the block's section and length are design choices")
ORIGIN = ("the block's centre, on the plane of the four port axes (z = 0): port-a toward -x and port-b toward +x on the run, "
          "port-c toward +y and port-d toward -y on the branch")
COMMAND = "CROSS-BLOCK-NPT"
PARAMS = dict(thread="NPT1/4")

SECTION = {"NPT1/8": 22.0, "NPT1/4": 28.0, "NPT3/8": 28.0}   # design choices: the square bar's side (y and z) per thread size
RUN = {"NPT1/8": 34.0, "NPT1/4": 46.0, "NPT3/8": 48.0}       # design choices: the block's length along the run (x), tee-block-npt's
LAND = {"NPT1/8": 14.0, "NPT1/4": 18.0, "NPT3/8": 21.0}      # design choices: the square land round each bore (the port node)
LAND_T = 0.2                                                 # each land 0.2 proud of its face (GEO-050), valve-ball-32's fields
WALL = 3.0                                                   # design choice: at least 3 mm of steel between bores and round each
MAT = "M-ZINC"                                               # class values 1 and 2: steel, zinc-plated


def bore(thread="NPT1/4"):
    """(diameter, depth) of a female port in mm from pneu.NPT: E1 + h, the male's major diameter at the hand-tight plane, and
    L2 + 2, a run-out past the male's effective thread (tank 2.0)"""
    t = pneu.NPT[thread]["table"]
    return (t["E1"] + t["h"]) * 25.4, pneu.NPT[thread]["length"] + 2.0


for _t in SECTION:
    assert _t in pneu.THREADS
    _d, _l = bore(_t); _a, _r = SECTION[_t], RUN[_t]
    assert _l >= pneu.NPT[_t]["engagement"]                  # deeper than a male's make-up (L1 + L3)
    assert _a - _d >= 2 * WALL                               # steel round each bore across the section
    assert _r / 2 - _l - _d / 2 >= WALL                      # the run bores' floors stay clear of the branch bores' sides
    assert _a - 2 * _l >= WALL                               # the two opposed branch bores' floors keep steel between them
    assert _d + 2.0 < LAND[_t] < _a                          # the land rings its bore, inside the face
    assert _a >= 8.0                                         # every envelope edge >= 8 (the AutoCAD fillet pre-flight)


def length(thread="NPT1/4"):
    """overall length along the run, land face to land face (46.4 for NPT 1/4)"""
    return RUN[thread] + 2 * LAND_T


def _port(P, body, name, d, thread):
    """a female NPT port on the face whose outward normal is d (a unit vector in x or y): the plain bore into the body, its land
    (the node) with the bore through it, and the pivot on the land's outer face, its axis out of the block"""
    dx, dy = d; bd, bl = bore(thread); h = LAND[thread] / 2
    c = RUN[thread] / 2 if dx else SECTION[thread] / 2
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
    P = Prims(); a, r = SECTION[thread], RUN[thread]
    body = P.box(MAT, -r / 2, -a / 2, -a / 2, r, a, a)                  # the square bar, the run along x
    _port(P, body, "port-a", (-1, 0), thread)                           # run end a, -x (the class's connection 1)
    _port(P, body, "port-b", (1, 0), thread)                            # run end b, +x (connection 2), opposite a
    _port(P, body, "port-c", (0, 1), thread)                            # branch c, +y (connection 3), at 90° to the run
    _port(P, body, "port-d", (0, -1), thread)                           # branch d, -y (connection 4), opposite c
    e, f = r / 2 + LAND_T, a / 2 + LAND_T
    P.collider("env", -e, -f, -a / 2, 2 * e, 2 * f, a)
    return P


PREVIEWS = [dict(name="three-quarter", az=250, el=25), dict(name="branch port-c", az=90, el=15),
            dict(name="thread NPT 1-8", az=250, el=25, params=dict(thread="NPT1/8")),
            dict(name="thread NPT 3-8", az=250, el=25, params=dict(thread="NPT3/8"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
