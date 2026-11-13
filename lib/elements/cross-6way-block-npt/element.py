#!/usr/bin/env python3
"""cross-6way-block-npt: six-way block cross, six female NPT ports of one size in a steel bar: two in line on the run (x), two
opposed on the branch (y) and two opposed on the side branch (z), joining six male NPT ends where one line splits in five (a supply
to four valves and a gauge, or a header that ties lines from three directions). Generic (OPERATING.md 12, EM 2026-11-07;
autopilot.md 2.b2: the next ETIM class in pneu's order that builds): our own vendor-neutral design of ETIM 10.0 EC010367 "Fitting
with 6 connections" (synonym "Ball piece with 6 connections"); the class values it is designed to are in spec.md "## Class values".
cross-side-block-npt 1.0's six-port sibling: the same run, section, ports and lands, with a `port-f` on -z, so the block reaches as
far below the ports' plane as above it (top() each way, the side bore's WALL rule mirrored). Machined from bar (a block), not a
casting or a forging: a form no dimensional standard shapes, which is why it is generic; the block's sizes are design choices.
Series and units come from toolkit/pneu.py (request pneu-1: D1 NPT threads). Each port is cross-block-npt's: a blind bore at E1 +
h, L2 + 2 deep, from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07), through a land 0.2 proud of the face
(the port node), the pivot on the land's outer face. The flow passages where the bores meet are not drawn (cross-block-npt's way).
No vendor file was opened (pneu-r112)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "cross-6way-block-npt", "1.0", "connector"
TITLE = "generic six-way block cross, six female NPT 1/4 ports, steel bar"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic fitting with 6 connections (ETIM 10.0 EC010367), a six-way block cross machined from bar; "
            "NPT series from toolkit/pneu.py D1, female ports bored at E1 + h from pneu.NPT (calculated from ASME B1.20.1's "
            "formulas); the block's sizes are design choices")
ORIGIN = ("where the run, branch and side-branch axes meet (the block's centre): port-a toward -x and port-b toward +x on the run, "
          "port-c toward +y and port-d toward -y on the branch, port-e toward +z and port-f toward -z on the side branch")
COMMAND = "CROSS-6WAY-BLOCK-NPT"
PARAMS = dict(thread="NPT1/4")

SECTION = {"NPT1/8": 22.0, "NPT1/4": 28.0, "NPT3/8": 28.0}   # design choices: cross-block-npt's section across the branch (y)
RUN = {"NPT1/8": 34.0, "NPT1/4": 46.0, "NPT3/8": 48.0}       # design choices: cross-block-npt's length along the run (x)
LAND = {"NPT1/8": 14.0, "NPT1/4": 18.0, "NPT3/8": 21.0}      # design choices: cross-block-npt's square land round each bore
LAND_T = 0.2                                                 # each land 0.2 proud of its face (GEO-050), valve-ball-32's fields
WALL = 3.0                                                   # design choice: at least 3 mm of steel between bores and round each
MAT = "M-ZINC"                                               # class values: steel, zinc-plated (the surface a design choice)


def bore(thread="NPT1/4"):
    """(diameter, depth) of a female port in mm from pneu.NPT: E1 + h, the male's major diameter at the hand-tight plane, and
    L2 + 2, a run-out past the male's effective thread (tank 2.0)"""
    t = pneu.NPT[thread]["table"]
    return (t["E1"] + t["h"]) * 25.4, pneu.NPT[thread]["length"] + 2.0


def top(thread="NPT1/4"):
    """the top and bottom faces' distance from the ports' plane: the lowest whole mm that keeps WALL between a side bore's floor and
    the run and branch bores, (L2 + 2) + bore / 2 + WALL rounded up (23 for NPT 1/4; 17 for 1/8, 24 for 3/8): cross-side-block-npt's
    top(), the same both ways"""
    d, l = bore(thread)
    return float(math.ceil(l + d / 2 + WALL))


for _t in SECTION:
    assert _t in pneu.THREADS
    _d, _l = bore(_t); _a, _r, _z = SECTION[_t], RUN[_t], top(_t)
    assert _l >= pneu.NPT[_t]["engagement"]                  # deeper than a male's make-up (L1 + L3)
    assert _a - _d >= 2 * WALL                               # steel round each bore across the section
    assert _r / 2 - _l - _d / 2 >= WALL                      # the run bores' floors stay clear of the branch and side bores
    assert _a - 2 * _l >= WALL                               # the two opposed branch bores' floors keep steel between them
    assert _z - _l - _d / 2 >= WALL                          # each side bore's floor stays clear of the run and branch bores
    assert 2 * _z - 2 * _l >= WALL                           # the two opposed side bores' floors keep steel between them
    assert _z >= _a / 2                                      # the top and bottom no nearer the plane than the section's half
    assert _d + 2.0 < LAND[_t] < _a                          # the land rings its bore, inside the face
    assert _a >= 8.0                                         # every envelope edge >= 8 (the AutoCAD fillet pre-flight)


def length(thread="NPT1/4"):
    """overall length along the run, land face to land face (46.4 for NPT 1/4)"""
    return RUN[thread] + 2 * LAND_T


def height(thread="NPT1/4"):
    """overall height, the bottom land's face to the top land's face (46.4 for NPT 1/4)"""
    return 2 * top(thread) + 2 * LAND_T


def _port(P, body, name, d, thread):
    """a female NPT port on the face whose outward normal is d (a unit vector in x, y or z): the plain bore into the body, its land
    (the node) with the bore through it, and the pivot on the land's outer face, its axis out of the block"""
    dx, dy, dz = d; bd, bl = bore(thread); h = LAND[thread] / 2
    c = RUN[thread] / 2 if dx else SECTION[thread] / 2 if dy else top(thread)
    P.hole("M-GASKET", (dx * (c + 1.0), dy * (c + 1.0), dz * (c + 1.0)), (dx * (c - bl), dy * (c - bl), dz * (c - bl)), bd / 2, body)
    if dx:
        x0 = c if dx > 0 else -c - LAND_T
        f = P.box(f"node:{name}|{MAT}", x0, -h, -h, LAND_T, 2 * h, 2 * h)
    elif dy:
        y0 = c if dy > 0 else -c - LAND_T
        f = P.box(f"node:{name}|{MAT}", -h, y0, -h, 2 * h, LAND_T, 2 * h)
    else:
        z0 = c if dz > 0 else -c - LAND_T
        f = P.box(f"node:{name}|{MAT}", -h, -h, z0, 2 * h, 2 * h, LAND_T)
    e = c + LAND_T
    P.hole("M-GASKET", (dx * (e + 1.0), dy * (e + 1.0), dz * (e + 1.0)), (dx * (c - 1.0), dy * (c - 1.0), dz * (c - 1.0)), bd / 2, f)
    P.pivot(name, "port", (dx * e, dy * e, dz * e), axis=(dx, dy, dz), range=(0, 0), unit=thread, gender="female")


def build(thread="NPT1/4"):
    if thread not in SECTION: raise ValueError(f"thread {thread}: one of {', '.join(SECTION)} (pneu.THREADS, D1)")
    P = Prims(); a, r, t = SECTION[thread], RUN[thread], top(thread)
    body = P.box(MAT, -r / 2, -a / 2, -t, r, a, 2 * t)                 # the bar, the run along x, reaching t above and below
    _port(P, body, "port-a", (-1, 0, 0), thread)                        # run end a, -x (the class's connection 1)
    _port(P, body, "port-b", (1, 0, 0), thread)                         # run end b, +x (connection 2), opposite a
    _port(P, body, "port-c", (0, 1, 0), thread)                         # branch c, +y (connection 3), at 90° to the run
    _port(P, body, "port-d", (0, -1, 0), thread)                        # branch d, -y (connection 4), opposite c
    _port(P, body, "port-e", (0, 0, 1), thread)                         # side branch e, +z (connection 5), square to both
    _port(P, body, "port-f", (0, 0, -1), thread)                        # side branch f, -z (connection 6), opposite e
    e, f, g = r / 2 + LAND_T, a / 2 + LAND_T, t + LAND_T
    P.collider("env", -e, -f, -g, 2 * e, 2 * f, 2 * g)
    return P


PREVIEWS = [dict(name="three-quarter", az=250, el=25), dict(name="top port-e", az=250, el=60),
            dict(name="thread NPT 1-8", az=250, el=25, params=dict(thread="NPT1/8")),
            dict(name="thread NPT 3-8", az=250, el=25, params=dict(thread="NPT3/8"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
