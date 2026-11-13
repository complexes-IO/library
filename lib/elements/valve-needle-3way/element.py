#!/usr/bin/env python3
"""valve-needle-3way: three-way needle valve, in line, NPT 1/4, a hand knob with a rising, rotating needle spindle throttling port-1
to port-2, and a third port, port-g, a gauge port on the body's side between the seat and port-2 (it reads the throttled pressure).
Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC010214 "Three-way needle valve" (synonym
"Needle valve block"); the class values it is designed to are in spec.md "## Class values". valve-needle 2.0's body, bores, fields,
bonnet, spindle and knob, the body lengthened to carry the third port. Port names, series, units and roles come from toolkit/pneu.py
(D1, D7, ROLES; pneu.NODES has no gauge number, so `port-g` as frl's). Each port is bored Ø (E1 + h) × (L2 + 2) deep from pneu.NPT
(values calculated from ASME B1.20.1's formulas, EM 2026-11-07), so a placed male stub (fitting-pushin 2.0, gauge-p) fits; each
port's pivot stands on its number field's outer face. Every other size is a design choice. No vendor file was opened (pneu-r96)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "valve-needle-3way", "1.0", "device"
TITLE = "three-way needle valve, generic, in line, NPT 1/4, gauge port, hand knob, rising spindle"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic three-way needle valve (ETIM 10.0 EC010214); class values in spec.md; ports NPT 1/4 female "
            "(toolkit/pneu.py D1), bored at E1 + h from pneu.NPT (calculated from ASME B1.20.1's formulas), port-1 and port-2 numbered "
            "to ISO 11727 (pneu.NODES), port-g the gauge port (pneu.ROLES gauge); body, bonnet and knob are design choices")
ORIGIN = ("in line: port-1's end face centre on the port axis (port-1's pivot 0.2 out, on its number field); the port axis is the x "
          "axis, flow along +x, the knob toward +z, the gauge port toward +y, the label face toward -y")
COMMAND = "VALVE-NEEDLE-3WAY"
PARAMS = dict()

PORT = "NPT1/4"                    # design choice within pneu.THREADS (D1): class values "Connection 1", "Connection 2", "Connection 3"
P_MAX_BAR = 10.0                   # class value 14 "Max. operating pressure at 20 °C" (ratings.csv p_max, generic design)
BODY = (64.0, 24.0, 24.0)          # design choice: body along the flow (x), across (y), high (z); centred on the port axis in y and z
FIELD, FIELD_T = 18.0, 0.2         # port-number field (decal), centred on the bore, 0.2 proud of the face (GEO-050); valve-needle 2.0's
SEAT_X = 20.0                      # design choice: the seat, bonnet, spindle and knob over x = 20 (valve-needle 2.0's mid-length)
GAUGE_X = 40.0                     # design choice: port-g's axis, downstream of the seat, on the +y face
WALL = 3.0                         # design choice: the least brass between two bores, a bore and a face, a field and a face edge
_T = pneu.NPT[PORT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4      # 13.616 for NPT 1/4: the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # L2 (10.205) + 2: design choice, a run-out past the male's effective thread (tank 2.0)
assert BORE_L >= pneu.NPT[PORT]["engagement"]                       # deeper than a male's make-up (L1 + L3)
assert min(BODY[1], BODY[2]) - BORE_D >= 2 * 5.0                    # at least 5 of body wall round each end bore
assert BORE_L <= BODY[1] / 2 + BORE_D / 2 - WALL and BORE_L < BODY[1] - WALL   # port-g blind, short of the −y face
assert GAUGE_X - BORE_D / 2 - BORE_L >= WALL                        # port-g's side clear of port-1's floor
assert BODY[0] - BORE_L - (GAUGE_X + BORE_D / 2) >= WALL            # port-g's side clear of port-2's floor
assert SEAT_X + 8.0 <= GAUGE_X - FIELD / 2                          # the bonnet (Ø16) ends before port-g's field begins, in x
assert FIELD > BORE_D + 2.0 and FIELD < min(BODY[1], BODY[2])       # each field rings its bore, inside its face
assert P_MAX_BAR * 100.0 >= pneu.P_SUPPLY                           # PNE-003 (kPa): 1000 kPa above the bench drop's 689.5
BONNET_D, BONNET_H = 16.0, 12.0    # design choice: bonnet on the body's top face over the seat
SPINDLE_D, SPINDLE_H = 6.0, 6.0    # design choice: the visible spindle between the bonnet and the knob (turns and rises with it)
KNOB_D, KNOB_H = 20.0, 16.0        # design choice: class values 26 "Length of handle/diameter of hand wheel" 20, 25 "Handle/hand wheel height" 16
TURNS, LEAD = 5, 0.5               # design choice: closed (0) to fully open in 5 turns; the spindle rises 0.5 per turn
LABEL = (28.0, 10.0)               # complexes.org generic field and flow arrow, on the label face (x by z)
MAT, FIELDM = "M-BRASS", "M-WHITE-PA"
assert PORT in pneu.THREADS and "gauge" in pneu.ROLES

def height(): return BODY[2] + BONNET_H + SPINDLE_H + KNOB_H      # body underside to knob top, closed: 58

def _end_port(P, body, name, x, out, role):
    """a female NPT 1/4 port on an end face: the plain bore into the body, its number field (the node) with the bore through it, and
    the pivot on the field's outer face, its axis out of the body toward the counterpart (pneu.py port frame; valve-needle 2.0)"""
    P.hole("M-GASKET", (x - out, 0, 0), (x + out * BORE_L, 0, 0), BORE_D / 2, body)
    h = FIELD / 2
    f = P.box(f"node:{name}|{FIELDM}", min(x, x - out * FIELD_T), -h, -h, FIELD_T, FIELD, FIELD)
    P.hole("M-GASKET", (x - out * (FIELD_T + 1.0), 0, 0), (x + out * 1.0, 0, 0), BORE_D / 2, f)
    P.pivot(name, "port", (x - out * FIELD_T, 0, 0), axis=(-out, 0, 0), range=(0, 0), unit=PORT, gender="female", role=role)

def _gauge_port(P, body, name, x, y):
    """port-g: the same bore, field and pivot on the +y side face at x, axis +y"""
    P.hole("M-GASKET", (x, y + 1.0, 0), (x, y - BORE_L, 0), BORE_D / 2, body)
    h = FIELD / 2
    f = P.box(f"node:{name}|{FIELDM}", x - h, y, -h, FIELD, FIELD_T, FIELD)
    P.hole("M-GASKET", (x, y + FIELD_T + 1.0, 0), (x, y - 1.0, 0), BORE_D / 2, f)
    P.pivot(name, "port", (x, y + FIELD_T, 0), axis=(0, 1, 0), range=(0, 0), unit=PORT, gender="female", role="gauge")

def build():
    P = Prims(); L, W, H = BODY
    body = P.box(MAT, 0, -W / 2, -H / 2, L, W, H)
    _end_port(P, body, pneu.NODES["supply"], 0.0, 1, "supply")                                # port-1, inlet (ISO 11727: 1)
    _end_port(P, body, pneu.NODES["work"][0], L, -1, "work")                                  # port-2, outlet (ISO 11727: 2)
    _gauge_port(P, body, "port-g", GAUGE_X, W / 2)                                            # port-g, gauge (frl's name; no ISO 11727 number)
    z0 = H / 2; z1 = z0 + BONNET_H; z2 = z1 + SPINDLE_H; xc = SEAT_X
    P.cyl(MAT, (xc, 0, z0), (xc, 0, z1), BONNET_D / 2)                                         # bonnet
    P.cyl(f"node:knob|{MAT}", (xc, 0, z1), (xc, 0, z2), SPINDLE_D / 2)                         # spindle, turns with the knob
    P.cyl(f"node:knob|M-BLACK-PA", (xc, 0, z2), (xc, 0, z2 + KNOB_H), KNOB_D / 2)               # hand knob
    P.pivot("knob", "rotate", (xc, 0, z1), axis=(0, 0, 1), range=(0, 360 * TURNS), unit="deg", lead=LEAD)   # counter-clockwise opens
    P.box(FIELDM, L / 2 - LABEL[0] / 2, -W / 2 - FIELD_T, -LABEL[1] / 2, LABEL[0], FIELD_T, LABEL[1])   # complexes.org generic, arrow 1 -> 2
    P.collider("env", -FIELD_T, -W / 2 - FIELD_T, -H / 2, L + 2 * FIELD_T, W + 2 * FIELD_T, height())
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="gauge port-g", az=70, el=15),
            dict(name="top knob", az=250, el=65)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
