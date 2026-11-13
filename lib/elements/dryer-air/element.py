#!/usr/bin/env python3
"""dryer-air: compressed air dryer, adsorption (desiccant), point of use, NPT 1/4 in line, clear bowl, replaceable desiccant
cartridge. Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC004030 "Dryer for compressed air
system"; the class value it is designed to is in spec.md "## Class values". Port names, series, units and roles come from
toolkit/pneu.py (D1, D7). 2.0 (pneu-r78, review dryer-air-1.0.md finding 1) cuts each port's bore as tank 2.0 and filter-air 2.0
do: Ø (E1 + h) (13.616 for NPT 1/4, the male stub's own diameter that fitting-pushin 2.0 and gauge-p draw; pneu.NPT, ASME B1.20.1
by its formulas, EM 2026-11-07) × (L2 + 2) deep, blind, with its role in features.csv (HOLE-010); the thread itself is drawn plain,
so 1.0's open figure (the thread, written while pneu.NPT was empty) is closed. Each port keeps its number field (18 square now, a
ring round the wider bore) and its pivot (gender female, PIN-002), which moves to the field's outer face, 0.2 in front of the head
(filter-air 3.0's fix), so a placed male's hex meets the field face to face. Every other size (head, bowl, cartridge) is a design
choice. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "dryer-air", "2.0", "device"
TITLE = "compressed air dryer, generic, adsorption (desiccant), point of use, NPT 1/4 in line, clear bowl"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic dryer for compressed air system (ETIM 10.0 EC004030); class value in spec.md; adsorption, point of "
            "use, ports NPT 1/4 female (toolkit/pneu.py D1, ASME B1.20.1), numbered to ISO 11727 (pneu.NODES), bored plain at E1 + h, "
            "L2 + 2 deep (pneu.NPT); head, bowl and cartridge are design choices")
ORIGIN = "in line: port-1's face centre; the port axis is the x axis, flow along +x, the bowl toward -z, the label face toward -y"
COMMAND = "DRYER-AIR"
PARAMS = dict()

PORT = "NPT1/4"                    # design choice within pneu.THREADS (D1): both ports the same size
HEAD = (48.0, 48.0, 32.0)          # design choice: head along the flow (x), across (y), high (z); centred on the port axis in y and z
_T = pneu.NPT[PORT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4      # 13.616 for NPT 1/4: the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # L2 (10.205) + 2: design choice, a run-out past the male's effective thread (tank 2.0)
FIELD, FIELD_T = 18.0, 0.2         # port-number field (decal), centred on the bore, 0.2 proud of the face (GEO-050); a ring round the bore
BOWL_D, BOWL_L = 44.0, 110.0       # design choice: clear bowl under the head; the desiccant's colour is seen through it
BOWL_BORE, BOWL_FLOOR = 38.0, 4.0  # design choice: the bowl's cavity (3 wall) and its floor
CART_D, CART_L = 32.0, 96.0        # design choice: the desiccant cartridge hanging from the head (node desiccant: the twin shows its state)
LABEL = (32.0, 10.0)               # complexes.org generic field on the label face (x by z)
ARROW = (24.0, 8.0)                # flow-arrow field on the top face (x by y)
MAT, FIELDM = "M-ALU-ANOD", "M-WHITE-PA"
assert PORT in pneu.THREADS and pneu.NPT[PORT]["length"]
assert BORE_L >= pneu.NPT[PORT]["engagement"]                  # deeper than a male's make-up (L1 + L3)
assert 2 * BORE_L + 10.0 <= HEAD[0]                            # the two blind bores leave 10 of head between their floors (23.6 here)
assert min(HEAD[1], HEAD[2]) - BORE_D >= 2 * 6.0               # at least 6 of head wall round each bore (9.2 above and below)
assert FIELD > BORE_D + 2.0 and FIELD < min(HEAD[1], HEAD[2])  # the field rings the bore, inside the end face

def height(): return HEAD[2] + BOWL_L                # head top to the bowl's underside

def _port(P, body, name, x, out, role):
    """a female NPT 1/4 port on an end face: the plain bore into the head, its number field (the node) with the bore through it, and
    the pivot on the field's outer face (2.0: the joint plane a placed male's hex meets), its axis out of the body toward the
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
    P.cyl("node:desiccant|M-ORANGE-PA", (xc, 0, z0), (xc, 0, z0 - CART_L), CART_D / 2)        # desiccant cartridge, in the cavity
    P.pivot("desiccant", "fixed", (xc, 0, z0 - CART_L / 2))
    P.box(FIELDM, xc - LABEL[0] / 2, -W / 2 - FIELD_T, -LABEL[1] / 2, LABEL[0], FIELD_T, LABEL[1])   # complexes.org generic, label face
    P.box(FIELDM, xc - ARROW[0] / 2, -ARROW[1] / 2, H / 2, ARROW[0], ARROW[1], FIELD_T)             # flow arrow 1 -> 2, top face
    P.collider("env", -FIELD_T, -W / 2 - FIELD_T, z1, L + 2 * FIELD_T, W + FIELD_T, H + BOWL_L + FIELD_T)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="inlet port-1", az=200, el=10),
            dict(name="from below", az=250, el=-40)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
