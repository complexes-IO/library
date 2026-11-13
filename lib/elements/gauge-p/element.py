#!/usr/bin/env python3
"""gauge-p: a dial pressure gauge, bottom (lower) connection, for the bench's FRL and every gauge port of the pneumatic line.
Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC011170 "Bourdon tube pressure gauge",
synonym "Pressure gauge"; lib/inventory.csv row `gauge-p` (own_design generic, "pressure gauge, NPT 1/4 lower mount", pneu-1 D3).
No vendor file was opened. Its stem ends in a male NPT 1/4 stub (`port-1`, role gauge) drawn as fitting-pushin 2.0 draws its
stub: a plain cylinder at the external thread's major diameter at the hand-tight plane, E1 + h, length L2, both from pneu.NPT
(values calculated from ASME B1.20.1's formulas, EM 2026-11-07), so it meets every female NPT 1/4 gauge port the library cuts at
E1 + h (tank 2.0's bore rule). The span is 0-160 psig, chosen by the library's own gauge rule (PNE-009, toolkit/v_pneu.py): at
P_SUPPLY 100 psig it reads 62.5 % of span, under the 75 % PNE-009 asks, so the gauge passes on any bench line. The case, bezel,
window, dial, hex and neck are design choices. The pointer (`pointer`, rotate about the dial's axis, 0 to 270 degrees) is the
one moving part: the twin turns it to the pressure it reads. The Bourdon tube and movement inside are not modelled."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "gauge-p", "1.0", "device"
TITLE = "generic dial pressure gauge, 0-160 psig, 63 mm case, NPT 1/4 male lower mount"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Bourdon tube pressure gauge (ETIM 10.0 EC011170, synonym pressure gauge), a dial gauge with "
            "a lower NPT 1/4 male stem (inventory own_design generic); NPT stub from pneu.NPT (calculated from ASME B1.20.1's "
            "formulas, D1); span 0-160 psig by PNE-009 at P_SUPPLY (pneu.py D3); case, bezel, window, dial, hex and pointer are "
            "design choices")
ORIGIN = "joint plane: the hex's seat face z = 0 on the stem's axis (x = y = 0); the host's gauge port toward -z, the dial up"
COMMAND = "GAUGE-P"
PARAMS = dict()

PORT = "NPT1/4"                       # pneu.THREADS (D1): the bench's FRL and gauge port size (pneu.py D3; inventory row gauge-p)
SPAN_PSIG = 160.0                     # design choice by PNE-009: P_SUPPLY / span = 62.5 % <= pneu.GAUGE_FRACTION (75 %)
HEX_AF, HEX_L = 15.0, 9.0             # design choices: the stem's wrench flats and their length along z
HEX_D = 1.12                          # corners turned to 1.12 x AF (as fitting-pushin)
NECK_D = 12.0                         # design choice: the socket neck between the hex and the case
CASE_D, CASE_Y = 63.0, (-8.0, 13.0)   # design choices: the case (2.5 in nominal dial class), its depth along y (dial toward -y)
CASE_Z = 47.5                         # the dial's centre height above the seat face (neck 9 to 16 visible below the case)
BEZEL_D, BEZEL_Y = 64.0, (-14.0, -7.0)    # design choice: the front ring, 0.5 proud of the case, 1.0 into it
OPEN_D = 57.0                         # design choice: the bezel's window opening (features.csv role)
WINDOW_D, WINDOW_Y = 58.0, (-13.5, -12.5) # design choice: the clear window, held 0.5 into the ring all round
DIAL_D, DIAL_Y = 57.6, (-9.0, -7.5)       # design choice: the white dial plate, 0.5 into the case, its face at y = -9
HUB_D, HUB_Y = 5.0, (-10.8, -9.0)         # design choice: the pointer's hub, seated face to face on the dial (it turns)
NEEDLE = dict(tail=4.0, reach=24.0, w=1.6, y=(-10.3, -9.4))   # design choice: the pointer, clear of the dial and the window
SWEEP = 270.0                         # degrees from 0 to full span, clockwise seen from the front (design choice)
IN = 0.5                              # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_STEM, MAT_CASE, MAT_DIAL, MAT_WINDOW, MAT_POINTER = "M-BRASS", "M-SILVER", "M-WHITE-PA", "M-CASE-CLEAR", "M-BLACK-PA"

assert PORT in pneu.THREADS
_T = pneu.NPT[PORT]["table"]
assert HEX_AF > (_T["E2"] + _T["h"]) * 25.4                     # the flats clear the thread's largest major diameter (E2 + h)
assert NECK_D < HEX_AF and NECK_D < CASE_Y[1] - CASE_Y[0]        # the neck inside the hex's flats and the case's depth
assert pneu.psig(SPAN_PSIG) * pneu.GAUGE_FRACTION >= pneu.P_SUPPLY   # PNE-009 at P_SUPPLY passes (75 % of span or less)
assert NEEDLE["reach"] < OPEN_D / 2.0 and NEEDLE["tail"] > HUB_D / 2.0   # the pointer sweeps inside the opening, through its hub
assert WINDOW_Y[1] < NEEDLE["y"][0] and WINDOW_Y[1] < HUB_Y[0] and NEEDLE["y"][1] < DIAL_Y[0] and HUB_Y[1] == DIAL_Y[0]
assert DIAL_D > OPEN_D and WINDOW_D > OPEN_D and BEZEL_Y[1] > CASE_Y[0]


def stub():
    """(diameter, length) of the NPT male stub in mm from pneu.NPT: E1 + h and L2 (fitting-pushin 2.0's rule)"""
    return (_T["E1"] + _T["h"]) * 25.4, pneu.NPT[PORT]["length"]


def _hex_z(P, L, z0, z1, af, d):
    """a hex prism on the z axis: a cylinder of diameter d with six flats cut at af / 2 (fitting-pushin's pattern, turned to z)"""
    c = P.cyl(L, (0, 0, z0), (0, 0, z1), d / 2.0); w = d + 4.0
    for k in range(6):
        t = math.radians(30 + 60 * k); n = (math.cos(t), math.sin(t), 0.0); tg = (-math.sin(t), math.cos(t), 0.0)
        o = (n[0] * af / 2.0 + tg[0] * w / 2.0, n[1] * af / 2.0 + tg[1] * w / 2.0, z0 - 1.0)
        P.cut(L, o, n, (0, 0, 1), (-tg[0], -tg[1], 0.0), 4.0, abs(z1 - z0) + 2.0, w, c)
    return c


def build():
    P = Prims(); sd, sl = stub(); zc = CASE_Z; R = CASE_D / 2.0
    P.cyl(f"node:port-1|{MAT_STEM}", (0, 0, -sl), (0, 0, IN), sd / 2.0)                                # NPT male stub, L2 below
    _hex_z(P, f"node:port-1|{MAT_STEM}", 0.0, HEX_L, HEX_AF, HEX_AF * HEX_D)                          # hex, seat face on z = 0
    P.cyl(MAT_STEM, (0, 0, HEX_L - IN), (0, 0, zc - R + 3 * IN), NECK_D / 2.0)                       # socket neck into the case
    P.cyl(MAT_CASE, (0, CASE_Y[0], zc), (0, CASE_Y[1], zc), R)                                         # case
    ring = P.cyl(MAT_CASE, (0, BEZEL_Y[0], zc), (0, BEZEL_Y[1], zc), BEZEL_D / 2.0)                    # bezel
    P.hole(MAT_CASE, (0, BEZEL_Y[0] - 1.0, zc), (0, BEZEL_Y[1] + 1.0, zc), OPEN_D / 2.0, ring)       # its window opening
    P.cyl(MAT_WINDOW, (0, WINDOW_Y[0], zc), (0, WINDOW_Y[1], zc), WINDOW_D / 2.0)                     # clear window in the ring
    P.cyl(MAT_DIAL, (0, DIAL_Y[0], zc), (0, DIAL_Y[1], zc), DIAL_D / 2.0)                             # dial plate
    P.cyl(f"node:pointer|{MAT_POINTER}", (0, HUB_Y[0], zc), (0, HUB_Y[1], zc), HUB_D / 2.0)          # pointer hub
    a = math.sqrt(0.5); d = (-a, 0.0, -a); ez = (a, 0.0, -a)            # at rest (0 psig) the pointer points to the lower left
    t, w = NEEDLE["tail"], NEEDLE["w"]; y0, y1 = NEEDLE["y"]
    o = (-d[0] * t - ez[0] * w / 2.0, y0, zc - d[2] * t - ez[2] * w / 2.0)
    P.obox(f"node:pointer|{MAT_POINTER}", o, d, (0, 1, 0), ez, t + NEEDLE["reach"], y1 - y0, w)     # pointer, right-handed axes
    P.pivot("port-1", "port", (0, 0, 0), axis=(0, 0, -1), range=(0, 0), unit=PORT, gender="male", role="gauge", length=round(sl, 3))
    P.pivot("pointer", "rotate", (0, HUB_Y[0], zc), axis=(0, 1, 0), range=(0, SWEEP), unit="deg")
    rb = BEZEL_D / 2.0
    P.collider("env", -rb, BEZEL_Y[0], -sl, 2 * rb, CASE_Y[1] - BEZEL_Y[0], zc + rb + sl)
    return P


PREVIEWS = [dict(name="front", az=180, el=10), dict(name="three-quarter", az=225, el=25), dict(name="stem", az=300, el=-30)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
