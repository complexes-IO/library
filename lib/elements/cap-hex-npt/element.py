#!/usr/bin/env python3
"""cap-hex-npt: hex cap, one female NPT port bored blind into a length of hex bar, closing a male NPT end of the same size (a
nipple's free end, a pipe's or a stub's end a circuit leaves open: "every port connected or plugged", request pneu-1).
Generic (OPERATING.md 12, EM 2026-11-07; autopilot.md 2.b2: the next ETIM class in pneu's order that builds): our own
vendor-neutral design of ETIM 10.0 EC003023 "Fitting with 1 connection" (synonyms "Cap", "Cap with hexagonal", "Blind plug"); the
class values it is designed to are in spec.md "## Class values". plug-hex-npt 1.0's female sibling: plug-hex-npt closes a female
port, this cap closes a male end. Series and units come from toolkit/pneu.py (request pneu-1: D1 NPT threads). The port is
tee-block-npt 1.0's: a blind bore at the male's major diameter at the hand-tight plane, E1 + h, L2 + 2 deep (tank 2.0's rule), from
pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07), through a land 0.2 proud of the open face (the port node),
the pivot on the land's outer face (filter-air 3.0's rule). Turned from hex bar, not ASME B16.11's round forged cap: the hex-bar form
is the reason it is generic and its sizes are design choices (1.1, review cap-hex-npt-1.0.md finding 2; spec.md says why). No vendor
file was opened (pneu-r106)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "cap-hex-npt", "1.1", "connector"
TITLE = "generic hex cap, female NPT 1/4"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic fitting with 1 connection (ETIM 10.0 EC003023), a hex cap turned from hex bar; NPT series "
            "from toolkit/pneu.py D1, the female port bored at E1 + h from pneu.NPT (calculated from ASME B1.20.1's formulas); the "
            "hex, its length and the land are design choices")
ORIGIN = ("joint plane: port-a's land face (the cap's open -y face) y = 0 on the thread's axis (x = z = 0); the male it closes "
          "comes from -y, the cap's closed end toward +y")
COMMAND = "CAP-HEX-NPT"
PARAMS = dict(thread="NPT1/4")

HEX_AF = {"NPT1/8": 17.0, "NPT1/4": 21.0, "NPT3/8": 24.0}   # design choices: the hex bar's flats (>= 3 mm of steel round the bore; 21 one over)
LAND_D = {"NPT1/8": 15.0, "NPT1/4": 19.0, "NPT3/8": 22.0}   # design choices: the round land round the bore (the port node), AF - 2
HEX_D = 1.06                                                # corners turned to 1.06 x AF (a sharp hex is 1.155 x AF): the catalogue's
                                                            # envelope is this turned diameter on x and z, rounded to the mm, and the
                                                            # flats lie on x, so it must stay within the Godot QA's 2.0 mm of AF (asserted)
LAND_T = 0.2                                                # the land 0.2 proud of the open face (GEO-050), tee-block-npt's
FLOOR = 4.0                                                 # design choice: the steel past the bore's floor, the cap's closed end
WALL = 3.0                                                  # design choice: at least 3 mm of steel round the bore (tee-block-npt's)
MAT = "M-ZINC"                                              # steel, zinc-plated (a design choice for its look)


def bore(thread="NPT1/4"):
    """(diameter, depth) of the female port in mm from pneu.NPT: E1 + h, the male's major diameter at the hand-tight plane, and
    L2 + 2, a run-out past the male's effective thread (tank 2.0)"""
    t = pneu.NPT[thread]["table"]
    return (t["E1"] + t["h"]) * 25.4, pneu.NPT[thread]["length"] + 2.0


def hex_length(thread="NPT1/4"):
    """the hex body's length along y: the bore's depth + FLOOR (16.205 for NPT 1/4)"""
    return bore(thread)[1] + FLOOR


def length(thread="NPT1/4"):
    """overall length, land face to closed end: LAND_T + bore depth + FLOOR (16.405 for NPT 1/4)"""
    return LAND_T + hex_length(thread)


for _t in HEX_AF:
    assert _t in pneu.THREADS
    _d, _l = bore(_t)
    assert _l >= pneu.NPT[_t]["engagement"]                  # deeper than a male's make-up (L1 + L3)
    assert HEX_AF[_t] - _d >= 2 * WALL                       # steel round the bore across the flats
    assert _d + 2.0 < LAND_D[_t] < HEX_AF[_t]                # the land rings its bore, inside the flats
    assert hex_length(_t) >= 8.0 and HEX_AF[_t] >= 8.0       # every envelope edge >= 8 (the AutoCAD fillet pre-flight)
    assert round(HEX_AF[_t] * HEX_D) - HEX_AF[_t] <= 1.5     # the catalogue's rounded envelope vs the flats on x (Godot QA: 2.0 mm)

def _hex(P, L, y0, y1, af, d, turn=0.0):
    """a hex prism on the y axis: a cylinder of diameter d with six flats cut at af / 2 (plug-hex-npt's and nipple-hex-npt's pattern);
    with turn 0 two flats face ±x and two corners ±z"""
    c = P.cyl(L, (0, y0, 0), (0, y1, 0), d / 2.0); lo = min(y0, y1); w = d + 4.0
    for k in range(6):
        t = math.radians(30 + turn + 60 * k); n = (math.sin(t), 0.0, math.cos(t)); tg = (math.cos(t), 0.0, -math.sin(t))
        o = (n[0] * af / 2.0 + tg[0] * w / 2.0, lo - 1.0, n[2] * af / 2.0 + tg[2] * w / 2.0)
        P.cut(L, o, n, (0, 1, 0), (-tg[0], 0.0, -tg[2]), 4.0, abs(y1 - y0) + 2.0, w, c)
    return c


def build(thread="NPT1/4"):
    if thread not in HEX_AF: raise ValueError(f"thread {thread}: one of {', '.join(HEX_AF)} (pneu.THREADS, D1)")
    P = Prims(); af = HEX_AF[thread]; bd, bl = bore(thread); hl = hex_length(thread)
    body = _hex(P, MAT, LAND_T, LAND_T + hl, af, af * HEX_D)                                     # hex body, its open face on y = 0.2
    P.hole("M-GASKET", (0, LAND_T - 1.0, 0), (0, LAND_T + bl, 0), bd / 2.0, body)                 # the blind bore, L2 + 2 deep
    f = P.cyl(f"node:port-a|{MAT}", (0, 0, 0), (0, LAND_T, 0), LAND_D[thread] / 2.0)               # the land (the port node)
    P.hole("M-GASKET", (0, -1.0, 0), (0, LAND_T + 1.0, 0), bd / 2.0, f)                            # the bore through the land
    P.pivot("port-a", "port", (0, 0, 0), axis=(0, -1, 0), range=(0, 0), unit=thread, gender="female")
    r = af * HEX_D / 2.0
    P.collider("env", -r, 0, -r, 2 * r, LAND_T + hl, 2 * r)
    return P


PREVIEWS = [dict(name="three-quarter open end", az=250, el=25), dict(name="closed end", az=70, el=25),
            dict(name="thread NPT 1/8", az=250, el=25, params=dict(thread="NPT1/8")),
            dict(name="thread NPT 3/8", az=250, el=25, params=dict(thread="NPT3/8"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
