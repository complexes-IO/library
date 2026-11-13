#!/usr/bin/env python3
"""valve-needle: needle valve, in line, NPT 1/4, hand knob with a rising, rotating needle spindle. Generic (OPERATING.md 12, EM
2026-11-07): our own vendor-neutral design of ETIM 10.0 EC010238 "Needle valve"; the class values it is designed to are in spec.md
"## Class values". Port names, series, units and roles come from toolkit/pneu.py (D1, D7). 2.0 (pneu-r74, review
valve-needle-1.0.md findings 1 and 2): each port is bored as tank 2.0's and valve-air-shutoff 2.0's, Ø (E1 + h) × (L2 + 2) deep from
pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07), so a placed male stub (fitting-pushin 2.0, gauge-p) fits;
each port's pivot stands on its number field's outer face (filter-air 3.0's fix), so a male's hex seats on the field; ratings.csv
carries p_max. Every other size (body, bonnet, spindle, knob, lead, field) is a design choice. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "valve-needle", "2.0", "device"
TITLE = "needle valve, generic, in line, NPT 1/4, hand knob, rising spindle"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic needle valve (ETIM 10.0 EC010238); class values in spec.md; ports NPT 1/4 female (toolkit/pneu.py "
            "D1), bored at E1 + h from pneu.NPT (calculated from ASME B1.20.1's formulas), numbered to ISO 11727 (pneu.NODES); body, "
            "bonnet and knob are design choices")
ORIGIN = ("in line: port-1's end face centre on the port axis (port-1's pivot 0.2 out, on its number field); the port axis is the x "
          "axis, flow along +x, the knob toward +z, the label face toward -y")
COMMAND = "VALVE-NEEDLE"
PARAMS = dict()

PORT = "NPT1/4"                    # design choice within pneu.THREADS (D1): class values "Connection 1" and "Connection 2"
P_MAX_BAR = 10.0                   # class value 10 "Max. pressure difference at 20 °C" (ratings.csv p_max, generic design)
BODY = (40.0, 24.0, 24.0)          # design choice: body along the flow (x), across (y), high (z); centred on the port axis in y and z
FIELD, FIELD_T = 18.0, 0.2         # port-number field (decal), centred on the bore, 0.2 proud of the face (GEO-050); 2.0: 16 -> 18
_T = pneu.NPT[PORT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4      # 13.616 for NPT 1/4: the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # L2 (10.205) + 2: design choice, a run-out past the male's effective thread (tank 2.0)
assert BORE_L >= pneu.NPT[PORT]["engagement"]                  # deeper than a male's make-up (L1 + L3)
assert 2 * BORE_L + 10.0 <= BODY[0]                            # the two blind bores leave at least 10 of body between their floors
assert min(BODY[1], BODY[2]) - BORE_D >= 2 * 5.0               # at least 5 of body wall round each bore
assert FIELD > BORE_D + 2.0 and FIELD < min(BODY[1], BODY[2])  # the field rings the bore, inside the end face
assert P_MAX_BAR * 100.0 >= pneu.P_SUPPLY                      # PNE-003 (kPa): 1000 kPa above the bench drop's 689.5
BONNET_D, BONNET_H = 16.0, 12.0    # design choice: bonnet on the body's top face, at mid-length
SPINDLE_D, SPINDLE_H = 6.0, 6.0    # design choice: the visible spindle between the bonnet and the knob (turns and rises with it)
KNOB_D, KNOB_H = 20.0, 16.0        # design choice: class values "Length of handle/diameter of hand wheel" 20, "Handle/hand wheel height" 16
TURNS, LEAD = 5, 0.5               # design choice: closed (0) to fully open in 5 turns; the spindle rises 0.5 per turn
LABEL = (28.0, 10.0)               # complexes.org generic field and flow arrow, on the label face (x by z)
MAT, FIELDM = "M-BRASS", "M-WHITE-PA"
assert PORT in pneu.THREADS

def height(): return BODY[2] + BONNET_H + SPINDLE_H + KNOB_H      # body underside to knob top, closed

def _port(P, body, name, x, out, role):
    """a female NPT 1/4 port on an end face: the plain bore into the body, its number field (the node) with the bore through it, and
    the pivot on the field's outer face (2.0), its axis out of the body toward the counterpart (pneu.py port frame)"""
    P.hole("M-GASKET", (x - out, 0, 0), (x + out * BORE_L, 0, 0), BORE_D / 2, body)
    h = FIELD / 2
    f = P.box(f"node:{name}|{FIELDM}", min(x, x - out * FIELD_T), -h, -h, FIELD_T, FIELD, FIELD)
    P.hole("M-GASKET", (x - out * (FIELD_T + 1.0), 0, 0), (x + out * 1.0, 0, 0), BORE_D / 2, f)
    P.pivot(name, "port", (x - out * FIELD_T, 0, 0), axis=(-out, 0, 0), range=(0, 0), unit=PORT, gender="female", role=role)

def build():
    P = Prims(); L, W, H = BODY; xc = L / 2
    body = P.box(MAT, 0, -W / 2, -H / 2, L, W, H)
    _port(P, body, pneu.NODES["supply"], 0.0, 1, "supply")                                    # port-1, inlet (ISO 11727: 1)
    _port(P, body, pneu.NODES["work"][0], L, -1, "work")                                      # port-2, outlet (ISO 11727: 2)
    z0 = H / 2; z1 = z0 + BONNET_H; z2 = z1 + SPINDLE_H
    P.cyl(MAT, (xc, 0, z0), (xc, 0, z1), BONNET_D / 2)                                         # bonnet
    P.cyl(f"node:knob|{MAT}", (xc, 0, z1), (xc, 0, z2), SPINDLE_D / 2)                         # spindle, turns with the knob
    P.cyl(f"node:knob|M-BLACK-PA", (xc, 0, z2), (xc, 0, z2 + KNOB_H), KNOB_D / 2)               # hand knob
    P.pivot("knob", "rotate", (xc, 0, z1), axis=(0, 0, 1), range=(0, 360 * TURNS), unit="deg", lead=LEAD)   # counter-clockwise opens
    P.box(FIELDM, xc - LABEL[0] / 2, -W / 2 - FIELD_T, -LABEL[1] / 2, LABEL[0], FIELD_T, LABEL[1])   # complexes.org generic, arrow 1 -> 2
    P.collider("env", -FIELD_T, -W / 2 - FIELD_T, -H / 2, L + 2 * FIELD_T, W + FIELD_T, height())
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="inlet port-1", az=200, el=10),
            dict(name="top knob", az=250, el=65)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
