#!/usr/bin/env python3
"""filter-air: compressed air filter, 5 um particulate, NPT 1/4 in line. Generic (OPERATING.md 12, EM 2026-11-07): our own
vendor-neutral design of ETIM 10.0 EC004033 "Compressed air filter"; the class values it is designed to are in spec.md "## Class
values". Port names, series, units and roles come from toolkit/pneu.py (D1, D7). 2.0 (pneu-r58) cuts each port's bore as tank
2.0 does: Ø E1 + h (13.616 for NPT 1/4, the male stub's own diameter that fitting-pushin 2.0 and gauge-p draw; pneu.NPT, ASME
B1.20.1 by its formulas, EM 2026-11-07), L2 + 2 deep, blind, with its role in features.csv (HOLE-010); the thread itself is drawn
plain, so 1.0's open figure (the thread, "pneu.NPT is empty") is closed. Each port keeps its pivot (gender female, PIN-002) and its
number field. 3.0 (pneu-r67, review pneu-r58 finding 1) moves each port's pivot from the head's face to its number field's outer
face, 0.2 in front of it, so a placed male's hex meets the field face to face instead of standing 0.2 into it. Every other size
(head, bowl, element, drain) is a design choice. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "filter-air", "3.0", "device"
TITLE = "compressed air filter, generic, 5 um, NPT 1/4 in line, clear bowl, manual drain"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic compressed air filter (ETIM 10.0 EC004033); class values in spec.md; ports NPT 1/4 female "
            "(toolkit/pneu.py D1, ASME B1.20.1), numbered to ISO 11727 (pneu.NODES), bored plain at E1 + h, L2 + 2 deep (pneu.NPT); "
            "head, bowl, element and drain are design choices")
ORIGIN = "in line: port-1's face centre; the port axis is the x axis, flow along +x, the bowl toward -z, the label face toward -y"
COMMAND = "FILTER-AIR"
PARAMS = dict()

PORT = "NPT1/4"                    # design choice within pneu.THREADS (D1): class value "Thread size inner thread (inch)" 1/4
HEAD = (40.0, 40.0, 32.0)          # design choice: head along the flow (x), across (y), high (z); centred on the port axis in y and z
_T = pneu.NPT[PORT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4      # 13.616 for NPT 1/4: the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # L2 (10.205) + 2: design choice, a run-out past the male's effective thread (tank 2.0)
FIELD, FIELD_T = 18.0, 0.2         # port-number field (decal), centred on the bore, 0.2 proud of the face (GEO-050); a ring round the bore
BOWL_D, BOWL_L = 36.0, 60.0        # design choice: clear bowl under the head (class value "Diameter" 36)
BOWL_BORE, BOWL_FLOOR = 30.0, 4.0  # design choice: the bowl's cavity (3 wall) and its floor
ELEM_D, ELEM_L = 16.0, 40.0        # design choice: the filter element (sintered bronze, 5 um class value) hanging from the head
DRAIN_D, DRAIN_H = 12.0, 8.0       # design choice: manual quarter-turn drain under the bowl
DRAIN_TURN = 90.0                  # deg, closed (0) to open: design choice
LABEL = (28.0, 10.0)               # complexes.org generic field on the label face (x by z)
ARROW = (24.0, 8.0)                # flow-arrow field on the top face (x by y)
MAT, FIELDM = "M-ALU-ANOD", "M-WHITE-PA"
assert PORT in pneu.THREADS and pneu.NPT[PORT]["length"]
assert BORE_L >= pneu.NPT[PORT]["engagement"]                  # deeper than a male's make-up (L1 + L3)
assert 2 * BORE_L + 10.0 <= HEAD[0]                            # the two blind bores leave 10 of head between their floors
assert min(HEAD[1], HEAD[2]) - BORE_D >= 2 * 6.0               # at least 6 of head wall round each bore
assert FIELD > BORE_D + 2.0 and FIELD < min(HEAD[1], HEAD[2])  # the field rings the bore, inside the end face

def height(): return HEAD[2] + BOWL_L + DRAIN_H     # class value "Height": head top to drain bottom

def _port(P, body, name, x, out, role):
    """a female NPT 1/4 port on an end face: the plain bore into the head, its number field (the node) with the bore through it, and
    the pivot on the field's outer face (3.0: the joint plane a placed male's hex meets), its axis out of the body toward the
    counterpart (pneu.py port frame)"""
    P.hole("M-GASKET", (x - out, 0, 0), (x + out * BORE_L, 0, 0), BORE_D / 2, body)
    h = FIELD / 2
    f = P.box(f"node:{name}|{FIELDM}", min(x, x - out * FIELD_T), -h, -h, FIELD_T, FIELD, FIELD)
    P.hole("M-GASKET", (x - out * (FIELD_T + 1.0), 0, 0), (x + out * 1.0, 0, 0), BORE_D / 2, f)
    P.pivot(name, "port", (x - out * FIELD_T, 0, 0), axis=(-out, 0, 0), range=(0, 0), unit=PORT, gender="female", role=role)

def build():
    P = Prims(); L, W, H = HEAD; xc = L / 2
    head = P.box(MAT, 0, -W / 2, -H / 2, L, W, H)
    _port(P, head, pneu.NODES["supply"], 0.0, 1, "supply")                                    # port-1, inlet (ISO 11727: 1)
    _port(P, head, pneu.NODES["work"][0], L, -1, "work")                                      # port-2, outlet (ISO 11727: 2)
    z0 = -H / 2; z1 = z0 - BOWL_L
    bowl = P.cyl("M-CASE-CLEAR", (xc, 0, z0), (xc, 0, z1), BOWL_D / 2)                         # clear bowl, hanging from the head
    P.hole("M-GASKET", (xc, 0, z0 + 1.0), (xc, 0, z1 + BOWL_FLOOR), BOWL_BORE / 2, bowl)        # its cavity, open to the head
    P.cyl("M-BRASS", (xc, 0, z0), (xc, 0, z0 - ELEM_L), ELEM_D / 2)                            # filter element, in the cavity
    P.cyl(f"node:drain|M-BLACK-PA", (xc, 0, z1), (xc, 0, z1 - DRAIN_H), DRAIN_D / 2)          # manual drain, under the bowl
    P.pivot("drain", "rotate", (xc, 0, z1), axis=(0, 0, -1), range=(0, DRAIN_TURN))
    P.box(FIELDM, xc - LABEL[0] / 2, -W / 2 - FIELD_T, -LABEL[1] / 2, LABEL[0], FIELD_T, LABEL[1])   # complexes.org generic, label face
    P.box(FIELDM, xc - ARROW[0] / 2, -ARROW[1] / 2, H / 2, ARROW[0], ARROW[1], FIELD_T)             # flow arrow 1 -> 2, top face
    P.collider("env", -FIELD_T, -W / 2 - FIELD_T, z1 - DRAIN_H, L + 2 * FIELD_T, W + FIELD_T, H + BOWL_L + DRAIN_H + FIELD_T)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="inlet port-1", az=200, el=10),
            dict(name="from below", az=250, el=-40)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
