#!/usr/bin/env python3
"""silencer: an exhaust silencer for a valve's or manifold's exhaust port, a porous sintered element on a hex and a male NPT stub.
Generic (OPERATING.md 12, EM 2026-11-07), of no ETIM class: the subset on file (lib/standards/etim/classes.csv) has no pneumatic
silencer class (EC011254 is a fan silencer), so, as request pneu-3's answer says (lib/requests/core/pneu-3-answer.md), "our own
design: generic exhaust silencer (no ETIM class; ASME B1.20.1 values)": the one standard its figures follow is the NPT thread.
lib/inventory.csv row `silencer` ("exhaust silencer, sintered, NPT 1/8 and 1/4", a common part: vacuum and manifold-pneu place it).
The stub (`port-1`, male, role silencer, pneu.ROLES) is drawn as fitting-pushin 2.0 and gauge-p draw theirs: a plain cylinder at
the external thread's major diameter at the hand-tight plane, E1 + h, length L2, both from pneu.NPT (values calculated from ASME
B1.20.1's formulas, EM 2026-11-07), so it meets every female NPT port the library cuts at E1 + h (tank 2.0's bore rule). The hex
and the sintered body are design choices. The porous element's pores and the air path are not modelled. No pressure rating is
claimed: ASME B1.20.1 states none and no class feature is on file (spec.md Open figures)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "silencer", "1.0", "connector"
TITLE = "generic exhaust silencer, sintered, NPT 1/8 or NPT 1/4 male"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic exhaust silencer (no ETIM class; ASME B1.20.1 values) (inventory own_design generic, a common "
            "part; request pneu-3's answer); NPT male stub from pneu.NPT (calculated from ASME B1.20.1's formulas, D1); hex and "
            "sintered body are design choices; no pressure rating claimed")
ORIGIN = "joint plane: the hex's seat face z = 0 on the stub's axis (x = y = 0); the host's exhaust port toward -z, the body up"
COMMAND = "SILENCER"
PARAMS = dict(thread="NPT1/4")

HEX_AF = {"NPT1/8": 14.0, "NPT1/4": 17.0}     # design choices: wrench flats per thread size (not a standard's figure)
HEX_L = {"NPT1/8": 5.0, "NPT1/4": 6.0}        # design choices: the hex's length along z
HEX_D = 1.12                                  # corners turned to 1.12 x AF (as fitting-pushin and gauge-p)
BODY_D = {"NPT1/8": 13.0, "NPT1/4": 16.0}     # design choices: the sintered body's diameter, inside the hex's flats
BODY_L = {"NPT1/8": 18.0, "NPT1/4": 24.0}     # design choices: its length above the hex
CAP_D, CAP_L = 4.0, 2.0                       # design choice: the end's chamfer step, Ø (BODY_D - 4) x 2 on the body's top
IN = 0.5                                      # each part runs 0.5 into the one below it (one solid joint)
MAT_HEX, MAT_BODY = "M-BRASS", "M-BRASS"      # brass hex, sintered bronze body

for _t in HEX_AF:
    assert _t in pneu.THREADS
    _T = pneu.NPT[_t]["table"]
    assert HEX_AF[_t] > (_T["E2"] + _T["h"]) * 25.4      # the flats clear the thread's largest major diameter (E2 + h)
    assert BODY_D[_t] <= HEX_AF[_t]                       # the body stands inside the hex's flats
    assert BODY_D[_t] > (_T["E1"] + _T["h"]) * 25.4       # and wider than the stub (a wrench on the hex, the body clear of the port)


def stub(thread="NPT1/4"):
    """(diameter, length) of the NPT male stub in mm from pneu.NPT: E1 + h and L2 (fitting-pushin 2.0's rule)"""
    t = pneu.NPT[thread]["table"]
    return (t["E1"] + t["h"]) * 25.4, pneu.NPT[thread]["length"]


def height(thread="NPT1/4"):
    """the silencer's length above the seat face (hex, body and chamfer step)"""
    return HEX_L[thread] + BODY_L[thread] + CAP_L - 2 * IN


def _hex_z(P, L, z0, z1, af, d):
    """a hex prism on the z axis: a cylinder of diameter d with six flats cut at af / 2 (gauge-p's pattern)"""
    c = P.cyl(L, (0, 0, z0), (0, 0, z1), d / 2.0); w = d + 4.0
    for k in range(6):
        t = math.radians(30 + 60 * k); n = (math.cos(t), math.sin(t), 0.0); tg = (-math.sin(t), math.cos(t), 0.0)
        o = (n[0] * af / 2.0 + tg[0] * w / 2.0, n[1] * af / 2.0 + tg[1] * w / 2.0, z0 - 1.0)
        P.cut(L, o, n, (0, 0, 1), (-tg[0], -tg[1], 0.0), 4.0, abs(z1 - z0) + 2.0, w, c)
    return c


def build(thread="NPT1/4"):
    if thread not in HEX_AF: raise ValueError(f"thread {thread}: one of {', '.join(HEX_AF)} (pneu.THREADS, D1; inventory row silencer)")
    P = Prims(); sd, sl = stub(thread); af, hl = HEX_AF[thread], HEX_L[thread]
    zb = hl + BODY_L[thread] - IN
    P.cyl(f"node:port-1|{MAT_HEX}", (0, 0, -sl), (0, 0, IN), sd / 2.0)                              # NPT male stub, L2 below
    _hex_z(P, f"node:port-1|{MAT_HEX}", 0.0, hl, af, af * HEX_D)                                    # hex, seat face on z = 0
    P.cyl(MAT_BODY, (0, 0, hl - IN), (0, 0, zb), BODY_D[thread] / 2.0)                              # sintered body
    P.cyl(MAT_BODY, (0, 0, zb - IN), (0, 0, zb - IN + CAP_L), (BODY_D[thread] - CAP_D) / 2.0)       # chamfer step on its top
    P.pivot("port-1", "port", (0, 0, 0), axis=(0, 0, -1), range=(0, 0), unit=thread, gender="male", role="silencer",
            length=round(sl, 3))
    r = af * HEX_D / 2.0
    P.collider("env", -r, -r, -sl, 2 * r, 2 * r, height(thread) + sl)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="stub", az=300, el=-30),
            dict(name="NPT 1/8", az=225, el=25, params=dict(thread="NPT1/8"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
