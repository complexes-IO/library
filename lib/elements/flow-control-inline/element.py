#!/usr/bin/env python3
"""flow-control-inline: a pneumatic one-way flow control valve (a throttle with a bypass check), in line, NPT 1/4, for setting a cylinder's
speed: air from `port-1` to `port-2` passes the adjustable throttle; air from `port-2` to `port-1` lifts the check and passes free.
Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC011463 "Regulating valve" (synonyms "Manual
throttle", "Throttle"; 45 features on file), hyd-flow-control's class; lib/inventory.csv row `flow-control-inline`, own_design generic,
made_of fitting-pushin x2 (a fitting placed in each port, in an assembly, as check-valve's). No vendor file was opened. Port names,
series and units come from toolkit/pneu.py (D1, D7); each port is bored as valve-needle 2.0's, Ø (E1 + h) × (L2 + 2) deep from
pneu.NPT (ASME B1.20.1 by its formulas), with its pivot on its number field's outer face. The body, bonnet, lock nut and knob are
design choices. The adjusting knob (`knob`, rotate about +z, five turns) is the one moving part; the throttle needle, the check and
its spring inside are not modelled. The inventory row's banjo form is not built: this is the in-line form."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "flow-control-inline", "1.0", "device"
TITLE = "pneumatic one-way flow control valve, generic, in line, NPT 1/4, throttle with bypass check, 10 bar, knob set, lock nut"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic regulating valve (ETIM 10.0 EC011463), a pneumatic in-line one-way flow control (throttle with "
            "a bypass check); class values in spec.md (10 bar, manual, lockable); ports NPT 1/4 female (toolkit/pneu.py D1), bored "
            "at E1 + h from pneu.NPT (calculated from ASME B1.20.1's formulas), numbered to ISO 11727 (pneu.NODES); body, bonnet, "
            "lock nut and knob are design choices; no vendor file opened")
ORIGIN = ("in line: port-1's end face centre on the port axis (port-1's pivot 0.2 out, on its number field); the port axis is the x "
          "axis, the throttled way along +x, the knob toward +z, the label face toward -y")
COMMAND = "FLOW-CONTROL"
PARAMS = dict()

PORT = "NPT1/4"                    # design choice within pneu.THREADS (D1): class values "Connection 1" and "Connection 2"
P_MAX_BAR = 10.0                   # class value 16 "Max. operating pressure" (ratings.csv p_max, generic design)
BODY = (44.0, 24.0, 24.0)          # design choice: body along the port axis (x), across (y), high (z); centred on the axis in y and z
FIELD, FIELD_T = 18.0, 0.2         # port-number field (decal), centred on the bore, 0.2 proud of the face (GEO-050)
_T = pneu.NPT[PORT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4      # 13.616 for NPT 1/4: the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # L2 (10.205) + 2: design choice, a run-out past the male's effective thread (tank 2.0)
BONNET_D, BONNET_H = 16.0, 10.0    # design choice: the bonnet carrying the throttle's spindle, on the body's top face at mid-length
NUT_D, NUT_T = 20.0, 5.0           # design choice: the lock nut on the bonnet's top (class value 19, lockable)
KNOB_D, KNOB_H = 18.0, 14.0        # design choice: the adjusting knob, seated face to face on the lock nut
TURNS = 5                          # design choice: the knob's travel from the throttle shut to fully open
LABEL = (28.0, 10.0)               # complexes.org generic field and the throttled way's arrow, on the label face (x by z)
IN = 0.5                           # the bonnet runs 0.5 into the body, the lock nut 0.5 into the bonnet (one solid joint each)
MAT, MAT_NUT, MAT_KNOB, FIELDM = "M-BRASS", "M-SILVER", "M-BLACK-PA", "M-WHITE-PA"

X_C = BODY[0] / 2.0                # 22: the spindle's axis over the body's centre
Z_TOP = BODY[2] / 2.0              # 12: the body's top face
Z_NUT = Z_TOP + BONNET_H           # 22: the bonnet's top = the lock nut's seat
Z_KNOB = Z_NUT + NUT_T             # 27: the lock nut's top = the knob's seat
assert PORT in pneu.THREADS
assert BORE_L >= pneu.NPT[PORT]["engagement"]                  # deeper than a male's make-up (L1 + L3)
assert 2 * BORE_L + 10.0 <= BODY[0]                            # the two blind bores leave at least 10 of body between their floors
assert min(BODY[1], BODY[2]) - BORE_D >= 2 * 5.0               # at least 5 of body wall round each bore
assert FIELD > BORE_D + 2.0 and FIELD < min(BODY[1], BODY[2])  # the field rings the bore, inside the end face
assert P_MAX_BAR * 100.0 >= pneu.P_SUPPLY                      # PNE-003 (kPa): 1000 kPa above the bench drop's 689.5
assert BONNET_D < NUT_D < BODY[1]                              # the nut wider than the bonnet, inside the body's top face
assert KNOB_D <= NUT_D                                         # the knob seats on the nut's top face, not over its edge
assert LABEL[0] < BODY[0] and LABEL[1] < BODY[2]               # the label field inside the label face


def knob_height(): return Z_KNOB + KNOB_H - Z_TOP              # class value 40 "Height operating element": body top to knob top


def _port(P, body, name, x, out):
    """a female NPT 1/4 port on an end face: the plain bore into the body, its number field (the node) with the bore through it, and
    the pivot on the field's outer face, its axis out of the body toward the counterpart (pneu.py port frame; valve-needle 2.0)"""
    P.hole("M-GASKET", (x - out, 0, 0), (x + out * BORE_L, 0, 0), BORE_D / 2, body)
    h = FIELD / 2
    f = P.box(f"node:{name}|{FIELDM}", min(x, x - out * FIELD_T), -h, -h, FIELD_T, FIELD, FIELD)
    P.hole("M-GASKET", (x - out * (FIELD_T + 1.0), 0, 0), (x + out * 1.0, 0, 0), BORE_D / 2, f)
    P.pivot(name, "port", (x - out * FIELD_T, 0, 0), axis=(-out, 0, 0), range=(0, 0), unit=PORT, gender="female", role="work")


def build():
    P = Prims(); L, W, H = BODY
    body = P.box(MAT, 0, -W / 2, -H / 2, L, W, H)                                                    # body block
    _port(P, body, pneu.NODES["supply"], 0.0, 1)                                                     # port-1 (ISO 11727: 1)
    _port(P, body, pneu.NODES["work"][0], L, -1)                                                     # port-2 (ISO 11727: 2)
    P.cyl(MAT, (X_C, 0, Z_TOP - IN), (X_C, 0, Z_NUT), BONNET_D / 2)                                  # bonnet, 0.5 into the body
    P.cyl(MAT_NUT, (X_C, 0, Z_NUT - IN), (X_C, 0, Z_KNOB), NUT_D / 2)                                # lock nut, 0.5 into the bonnet
    P.cyl(f"node:knob|{MAT_KNOB}", (X_C, 0, Z_KNOB), (X_C, 0, Z_KNOB + KNOB_H), KNOB_D / 2)          # adjusting knob, face to face
    P.pivot("knob", "rotate", (X_C, 0, Z_KNOB), axis=(0, 0, 1), range=(0, 360 * TURNS), unit="deg")  # counter-clockwise opens
    P.box(FIELDM, X_C - LABEL[0] / 2, -W / 2 - FIELD_T, -LABEL[1] / 2, LABEL[0], FIELD_T, LABEL[1])  # complexes.org generic, arrow 1 -> 2
    P.collider("body", -FIELD_T, -W / 2 - FIELD_T, -H / 2, L + 2 * FIELD_T, W + FIELD_T, Z_KNOB + H / 2)
    P.collider("knob", X_C - KNOB_D / 2, -KNOB_D / 2, Z_KNOB, KNOB_D, KNOB_D, KNOB_H)
    return P


PREVIEWS = [dict(name="three-quarter", az=250, el=20), dict(name="port-1", az=200, el=10), dict(name="top knob", az=250, el=65)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
