#!/usr/bin/env python3
"""fitting-pushin: straight push-in fitting, one inch tube OD to one male NPT thread. Generic (OPERATING.md 12, EM 2026-11-07):
our own vendor-neutral design of ETIM 10.0 EC003024 "Fitting with 2 connections"; lib/inventory.csv own_design generic. Series,
units and the port frame come from toolkit/pneu.py (request pneu-1: D1 NPT threads, D2 inch tube and ISO 14743 push-in fittings).
The hex, body and release-sleeve sizes are design choices. 2.0 adds the NPT male stub below the seat face from pneu.NPT (values
calculated from ASME B1.20.1's formulas, EM 2026-11-07): length L2 (the effective thread), drawn as a plain cylinder at the
external thread's major diameter at the hand-tight plane, E1 + h (the library draws threads as plain cylinders: gland-m20,
shock-buffer); the 1:16 taper and the thread form are not drawn. The push-in bore and insertion depth stay out (pneu.PUSHIN is
empty, never guessed). Each joint is a pivot on its axis: `port-thread` on the hex's seat face, `port-tube` on the release
sleeve's face."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "fitting-pushin", "2.0", "connector"
TITLE = "generic push-in fitting, straight, tube 1/4 in to NPT 1/8 male (push-in bore NOT ON FILE)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic fitting with 2 connections (ETIM 10.0 EC003024), a straight push-in fitting (inventory "
            "own_design generic); tube OD and NPT series from toolkit/pneu.py D1, D2; NPT stub from pneu.NPT (calculated from "
            "ASME B1.20.1's formulas); hex, body and sleeve are design choices; push-in bore NOT ON FILE")
ORIGIN = "joint plane: the hex's seat face y = 0 on the thread's axis (x = z = 0); the host port toward -y, the tube end toward +y"
COMMAND = "FITTING-PUSHIN"
PARAMS = dict(tube="1/4", thread="NPT1/8")

HEX_AF = {"NPT1/8": 14.0, "NPT1/4": 17.0, "NPT3/8": 21.0}   # design choices: wrench flats per thread size (not a standard's figure)
HEX_L = 7.0                                                # design choice: hex length along y
HEX_D = 1.12                                               # corners turned to 1.12 x AF (a sharp hex is 1.155 x AF), design choice
BODY_D = {"5/32": 10.0, "1/4": 12.0, "3/8": 16.0}          # design choices: the push-in body's diameter per tube OD
BODY_L = 14.0                                              # design choice: body length above the hex
SLEEVE_DD, SLEEVE_L, SLEEVE_IN = 1.0, 3.0, 0.5             # release sleeve: 1.0 under the body's diameter, 3.0 long, 0.5 into the body
MAT_HEX, MAT_BODY, MAT_SLEEVE = "M-SILVER", "M-BLACK-PA", "M-GREY-PA"
STUB_IN = 0.5                                              # the stub runs 0.5 into the hex (one solid joint)


def stub(thread):
    """(diameter, length) of the NPT male stub in mm from pneu.NPT: the major diameter at the hand-tight plane, E1 + h, and L2"""
    t = pneu.NPT[thread]["table"]
    return (t["E1"] + t["h"]) * 25.4, pneu.NPT[thread]["length"]


for _t in HEX_AF:
    assert _t in pneu.THREADS
    _tb = pneu.NPT[_t]["table"]
    assert HEX_AF[_t] > (_tb["E2"] + _tb["h"]) * 25.4      # each hex's flats clear its thread's largest major diameter (E2 + h)
for _o in BODY_D: assert _o in pneu.TUBES_IN and BODY_D[_o] > pneu.TUBES_IN[_o]


def length(): return HEX_L + BODY_L + SLEEVE_L - SLEEVE_IN


def _hex(P, L, y0, y1, af, d, turn=0.0):
    """a hex prism on the y axis: a cylinder of diameter d with six flats cut at af / 2 (gland-m20's pattern)"""
    c = P.cyl(L, (0, y0, 0), (0, y1, 0), d / 2.0); lo = min(y0, y1); w = d + 4.0
    for k in range(6):
        t = math.radians(30 + turn + 60 * k); n = (math.sin(t), 0.0, math.cos(t)); tg = (math.cos(t), 0.0, -math.sin(t))
        o = (n[0] * af / 2.0 + tg[0] * w / 2.0, lo - 1.0, n[2] * af / 2.0 + tg[2] * w / 2.0)
        P.cut(L, o, n, (0, 1, 0), (-tg[0], 0.0, -tg[2]), 4.0, abs(y1 - y0) + 2.0, w, c)
    return c


def build(tube="1/4", thread="NPT1/8"):
    if tube not in BODY_D: raise ValueError(f"tube {tube}: one of {', '.join(BODY_D)} (pneu.TUBES_IN, D2)")
    if thread not in HEX_AF: raise ValueError(f"thread {thread}: one of {', '.join(HEX_AF)} (pneu.THREADS, D1)")
    P = Prims(); af = HEX_AF[thread]; bd = BODY_D[tube]
    y_body, y_top = HEX_L, HEX_L + BODY_L
    y_end = y_top + SLEEVE_L - SLEEVE_IN
    sd, sl = stub(thread)
    _hex(P, f"node:port-thread|{MAT_HEX}", 0.0, HEX_L, af, af * HEX_D)                         # hex, seat face on y = 0
    P.cyl(f"node:port-thread|{MAT_HEX}", (0, -sl, 0), (0, STUB_IN, 0), sd / 2.0)                 # NPT male stub, L2 below the seat face
    P.cyl(MAT_BODY, (0, y_body - 0.5, 0), (0, y_top, 0), bd / 2.0)                             # push-in body, 0.5 into the hex
    P.cyl(f"node:port-tube|{MAT_SLEEVE}", (0, y_top - SLEEVE_IN, 0), (0, y_end, 0), (bd - SLEEVE_DD) / 2.0)   # release sleeve
    P.pivot("port-thread", "port", (0, 0, 0), axis=(0, -1, 0), range=(0, 0), unit=thread, gender="male", length=round(sl, 3))
    P.pivot("port-tube", "port", (0, y_end, 0), axis=(0, 1, 0), range=(0, 0), unit=f"tube-{tube}", gender="female")
    r = max(af * HEX_D, bd) / 2.0
    P.collider("env", -r, -sl, -r, 2 * r, y_end + sl, 2 * r)
    return P


PREVIEWS = [dict(name="three-quarter, tube 1/4 to NPT 1/8", az=250, el=25), dict(name="seat face", az=250, el=-40),
            dict(name="tube 3/8 to NPT 1/4", az=250, el=25, params=dict(tube="3/8", thread="NPT1/4")),
            dict(name="tube 5/32 to NPT 1/8", az=250, el=25, params=dict(tube="5/32", thread="NPT1/8"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
