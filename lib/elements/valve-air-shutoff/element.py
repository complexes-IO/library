#!/usr/bin/env python3
"""valve-air-shutoff: compressed air valve, a manual 2/2 shut-off: in line, NPT 1/4, quarter-turn lever. Generic (OPERATING.md 12,
EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC010590 "Compressed air valve"; the class values it is designed to are
in spec.md "## Class values". Port names, series, units and roles come from toolkit/pneu.py (D1, D7). 2.0 (review cloud-pneu
2026-11-07-r2 findings 1 and 2): each port is bored as tank 2.0's, Ø E1 + h (the male stub's own diameter, fitting-pushin 2.0 and
gauge-p) and L2 + 2 deep from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07), with its port pivot (gender
female, PIN-002) and its number field; 1.0's open thread figure closes with it, and the 10 bar class value goes in ratings.csv.
It is not lockable and has no dump: it is not the lockable 3/2 shut-off and dump valve PNE-008 asks for. Every other size (body,
boss, stem, lever) is a design choice. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "valve-air-shutoff", "2.1", "device"
TITLE = "compressed air valve, generic, manual 2/2 shut-off, in line, NPT 1/4, quarter-turn lever"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic compressed air valve (ETIM 10.0 EC010590); class values in spec.md; a manual 2/2 shut-off, ports "
            "NPT 1/4 female (toolkit/pneu.py D1), bored at E1 + h from pneu.NPT (calculated from ASME B1.20.1's formulas), numbered "
            "to ISO 11727 (pneu.NODES); body and lever are design choices")
ORIGIN = ("in line: port-1's face centre; the port axis is the x axis, flow along +x, the lever on top (+z), pointing toward -y when "
          "closed (across the flow) and along +x when open; the label face toward -y")
COMMAND = "VALVE-AIR-SHUTOFF"
PARAMS = dict()

PORT = "NPT1/4"                    # design choice within pneu.THREADS (D1): class values "Size of thread connection (inch) 1" 1/4
BODY = (44.0, 26.0, 26.0)          # design choice: body along the flow (x), across (y), high (z); centred on the port axis in y and z
FIELD, FIELD_T = 18.0, 0.2         # port-number field (decal), centred on the bore, 0.2 proud of the face (GEO-050); 2.0: 16 -> 18
BOSS_D, BOSS_H = 14.0, 5.0         # design choice: the stem boss on the body's top face, at mid-length
STEM_D, STEM_H = 6.0, 4.0          # design choice: the stem showing between the boss and the lever (turns with it)
ARM = (50.0, 6.0, 12.0, 3.0)       # design choice: lever arm, reach from the stem axis, tail behind it, width, thickness
NUT_D, NUT_H = 10.0, 3.0           # design choice: the nut holding the lever on the stem
TURN = 90.0                        # deg, closed (0, across the flow) to open (90, along the flow): a quarter turn
LABEL = (28.0, 10.0)               # complexes.org generic field and flow arrow, on the label face (x by z)
MAT, FIELDM = "M-BRASS", "M-WHITE-PA"
P_MAX_BAR = 10.0                   # class value 7 (EF023116 Max. operating pressure at 20 °C): ratings.csv p_max
assert PORT in pneu.THREADS
_T = pneu.NPT[PORT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4      # 13.616 for NPT 1/4: the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # L2 (10.205) + 2: design choice, a run-out past the male's effective thread (tank 2.0)
assert BORE_L >= pneu.NPT[PORT]["engagement"]                  # deeper than a male's make-up (L1 + L3)
assert 2 * BORE_L + 10.0 <= BODY[0]                            # the two blind bores leave at least 10 of body between their floors
assert min(BODY[1], BODY[2]) - BORE_D >= 2 * 6.0               # at least 6 of body wall round each bore
assert FIELD > BORE_D + 2.0 and FIELD < min(BODY[1], BODY[2])  # the field rings the bore, inside the end face
assert P_MAX_BAR * 100.0 >= pneu.P_SUPPLY                      # PNE-003 (kPa): 1000 kPa above the bench drop's 689.5

def height(): return BODY[2] + BOSS_H + STEM_H + ARM[3] + NUT_H      # body underside to the nut's top

def _port(P, body, name, x, out, role):
    """a female NPT 1/4 port on an end face: the plain bore into the body, its number field (the node) with the bore through it, and
    the pivot on the face, its axis out of the body toward the counterpart (pneu.py port frame)"""
    P.hole("M-GASKET", (x - out, 0, 0), (x + out * BORE_L, 0, 0), BORE_D / 2, body)
    h = FIELD / 2
    f = P.box(f"node:{name}|{FIELDM}", min(x, x - out * FIELD_T), -h, -h, FIELD_T, FIELD, FIELD)
    P.hole("M-GASKET", (x - out * (FIELD_T + 1.0), 0, 0), (x + out * 1.0, 0, 0), BORE_D / 2, f)
    P.pivot(name, "port", (x, 0, 0), axis=(-out, 0, 0), range=(0, 0), unit=PORT, gender="female", role=role)

def build():
    P = Prims(); L, W, H = BODY; xc = L / 2
    body = P.box(MAT, 0, -W / 2, -H / 2, L, W, H)
    _port(P, body, pneu.NODES["supply"], 0.0, 1, "supply")                                    # port-1, inlet (ISO 11727: 1)
    _port(P, body, pneu.NODES["work"][0], L, -1, "work")                                      # port-2, outlet (ISO 11727: 2)
    z0 = H / 2; z1 = z0 + BOSS_H; z2 = z1 + STEM_H; z3 = z2 + ARM[3]
    P.cyl(MAT, (xc, 0, z0), (xc, 0, z1), BOSS_D / 2)                                           # stem boss
    P.cyl(f"node:lever|{MAT}", (xc, 0, z1), (xc, 0, z2), STEM_D / 2)                           # stem, turns with the lever
    reach, tail, w, t = ARM
    P.box("node:lever|M-RED-PA", xc - w / 2, -reach, z2, w, reach + tail, t)                   # lever arm, coated; across the flow = closed
    P.cyl("node:lever|M-ZINC", (xc, 0, z3), (xc, 0, z3 + NUT_H), NUT_D / 2)                    # lever nut
    P.pivot("lever", "rotate", (xc, 0, z1), axis=(0, 0, 1), range=(0, TURN), unit="deg")      # +90 about +z: -y to +x, closed to open
    P.box(FIELDM, xc - LABEL[0] / 2, -W / 2 - FIELD_T, -LABEL[1] / 2, LABEL[0], FIELD_T, LABEL[1])   # complexes.org generic, arrow 1 -> 2
    P.collider("env", -FIELD_T, -reach, -H / 2, L + 2 * FIELD_T, reach + W / 2, height())
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="inlet port-1", az=200, el=10),
            dict(name="top lever", az=250, el=65)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
