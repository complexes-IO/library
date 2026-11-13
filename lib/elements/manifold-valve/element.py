#!/usr/bin/env python3
"""manifold-valve: two-valve instrument manifold (block and bleed), NPT 1/4, a calibration port, panel mounted. Generic (OPERATING.md
12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC010298 "Manifold valve"; the class values it is designed to are in
spec.md "## Class values". ETIM's class is the instrument manifold (its features: valves in the block, process side, instrument
side, calibration ports, type of shut-off valve): a block between a process line and a gauge or transmitter, here with a block
valve and a bleed valve. Threaded on both sides, so no transmitter flange interface is involved. Port series, units and roles come
from toolkit/pneu.py (D1, ROLES, the NPT table): each port is a plain bore at the male stub's diameter with its port pivot (gender
female, PIN-002) and its number field. Every other size is a design choice. No vendor file was opened.
2.0 (pneu-r77, review manifold-valve-1.0.md finding 1, the cloud elements' bores): each port is bored as tank 2.0's and valve-sol-52-sr
2.0's, Ø (E1 + h) × (L2 + 2) deep from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07), so a placed male stub
(fitting-pushin 2.0, gauge-p 1.0) fits; each port's pivot stands on its number field's outer face (filter-air 3.0's fix), so a male's
hex seats on the field; the fields go from 16 to 18. The thread is no longer an open figure. No ratings.csv: the class states no
pressure (class value 9, not stated)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "manifold-valve", "2.0", "device"
TITLE = "manifold valve, generic, two-valve block and bleed, NPT 1/4, calibration port, panel mounted"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic manifold valve (ETIM 10.0 EC010298); class values in spec.md; two-valve instrument manifold (block "
            "and bleed), process, instrument and calibration ports NPT 1/4 female (toolkit/pneu.py D1), bored at E1 + h from pneu.NPT "
            "(calculated from ASME B1.20.1's formulas); sizes are design choices")
ORIGIN = ("surface mount: back face on the panel y = 0, the lower mounting hole's centre x = 0, z = 0; body toward -y, the knobs on "
          "the front face (-y), the process port underneath (-z), the instrument port on top (+z); each port's pivot 0.2 out, on its "
          "number field")
COMMAND = "MANIFOLD-VALVE"
PARAMS = dict()

PORT = "NPT1/4"                    # design choice within pneu.THREADS (D1): class values "Connection, process side" and "..., instrument side"
X0, L = -28.0, 56.0                # design choice: body from x = -28, 56 long (x)
D = 28.0                           # design choice: body depth (y), back face on the panel at y = 0
Z0, H = -8.0, 44.0                 # design choice: body from z = -8, 44 high (z)
FIX_D, FIX_Z = 5.5, (0.0, 28.0)    # M5 clearance, medium (ISO 273 H13: 5.5 to 5.68; lib/standards/holes.csv), through y at x = 0
_T = pneu.NPT[PORT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4      # 13.616 for NPT 1/4: the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # L2 (10.205) + 2: design choice, a run-out past the male's effective thread (tank 2.0)
FIELD, FIELD_T = 18.0, 0.2         # port-number field (decal), centred on the bore, 0.2 proud of the face (GEO-050); 2.0: 16 -> 18
XB, XV, ZV = -14.0, 14.0, 14.0     # design choice: block valve (x = -14, over the process-instrument column), bleed valve (x = 14), both at z = 14
YC = -D / 2                        # the ports' and the column's mid-depth
BONNET_D, BONNET_H = 16.0, 8.0     # design choice: bonnet on the front face, each valve
SPINDLE_D, SPINDLE_H = 6.0, 6.0    # design choice: the visible spindle between the bonnet and the knob (turns and rises with it)
KNOB_D, KNOB_H = 20.0, 16.0        # design choice: hand knob, each valve (class value "Operation": hand knob)
TURNS, LEAD = 5, 0.5               # design choice: closed (0) to fully open in 5 turns; the spindle rises 0.5 per turn
LABEL = (24.0, 10.0)               # complexes.org generic field on the top face (x by y)
MAT, FIELDM = "M-BRASS", "M-WHITE-PA"
PORTS = {"port-1": ((XB, YC, Z0), (0, 0, -1), "supply"),          # process side, underneath (ISO 11727: 1, the inlet)
         "port-2": ((XB, YC, Z0 + H), (0, 0, 1), "gauge"),        # instrument side, on top (ISO 11727: 2, the outlet)
         "port-cal": ((X0 + L, YC, ZV), (1, 0, 0), "gauge")}      # calibration and vent port, right end face, behind the bleed valve
VALVES = {"knob-block": (XB, "M-BLACK-PA"), "knob-bleed": (XV, "M-RED-PA")}   # block: process to instrument; bleed: instrument to port-cal
assert PORT in pneu.THREADS and all(r in pneu.ROLES for _, _, r in PORTS.values())
assert BORE_L >= pneu.NPT[PORT]["engagement"]                                     # deeper than a male's make-up
assert abs(XB) - BORE_D / 2 - FIX_D / 2 >= 4.0                                  # port-1's bore clears the lower mounting hole (x)
assert (Z0 + H - BORE_L) - (Z0 + BORE_L) >= 15.0                                  # body left between port-1's and port-2's bores
assert X0 + L - BORE_L - XV >= 1.0                                                # port-cal's bore stops short of the bleed valve's axis
assert D / 2 - BORE_D / 2 >= 7.0 and FIELD > BORE_D + 2.0                         # wall front and back; the field rings its bore
assert abs(XB) + FIELD / 2 <= abs(X0) - 2.0 and abs(XB) - FIELD / 2 >= 2.0         # port-1 / port-2 fields on their faces, clear of x = 0
assert 14.0 - LABEL[0] / 2 > XB + FIELD / 2                                       # the top label field clear of port-2's field

def _port(P, body, name, c, n, role):
    """a female NPT 1/4 port on a face: the bore into the body, its number field (the node) with the bore through it, and the pivot
    on the field's outer face (2.0), its axis n out of the body toward the counterpart (pneu.py port frame)"""
    c, n = tuple(c), tuple(n)
    at = lambda s: tuple(c[i] + n[i] * s for i in range(3))
    P.hole("M-GASKET", at(1.0), at(-BORE_L), BORE_D / 2, body)
    lo = [c[i] - FIELD / 2 if n[i] == 0 else min(c[i], c[i] + n[i] * FIELD_T) for i in range(3)]
    sz = [FIELD if n[i] == 0 else FIELD_T for i in range(3)]
    f = P.box(f"node:{name}|{FIELDM}", *lo, *sz)
    P.hole("M-GASKET", at(FIELD_T + 1.0), at(-1.0), BORE_D / 2, f)
    P.pivot(name, "port", at(FIELD_T), axis=n, range=(0, 0), unit=PORT, gender="female", role=role)

def build():
    P = Prims()
    body = P.box(MAT, X0, -D, Z0, L, D, H)
    for z in FIX_Z:                                                                            # panel mounting holes, through y
        P.hole("M-GASKET", (0.0, 1.0, z), (0.0, -D - 1.0, z), FIX_D / 2, body)
    for name, (c, n, role) in PORTS.items(): _port(P, body, name, c, n, role)
    y1 = -D - BONNET_H; y2 = y1 - SPINDLE_H
    for name, (x, knobm) in VALVES.items():                                                    # the two needle valves, front face
        P.cyl(MAT, (x, -D, ZV), (x, y1, ZV), BONNET_D / 2)                                      # bonnet
        P.cyl(f"node:{name}|{MAT}", (x, y1, ZV), (x, y2, ZV), SPINDLE_D / 2)                    # spindle, turns with the knob
        P.cyl(f"node:{name}|{knobm}", (x, y2, ZV), (x, y2 - KNOB_H, ZV), KNOB_D / 2)            # hand knob
        P.pivot(name, "rotate", (x, y1, ZV), axis=(0, -1, 0), range=(0, 360 * TURNS), unit="deg", lead=LEAD)   # counter-clockwise opens
    P.box(FIELDM, 14.0 - LABEL[0] / 2, YC - LABEL[1] / 2, Z0 + H, LABEL[0], LABEL[1], FIELD_T)   # complexes.org generic, top face
    yf = y2 - KNOB_H                                                                           # the knobs stand foremost
    P.collider("env", X0, yf, Z0 - FIELD_T, L + FIELD_T, -yf, H + 2 * FIELD_T)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="right end, calibration port", az=320, el=15),
            dict(name="from below, process port", az=230, el=-40)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
