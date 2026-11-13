#!/usr/bin/env python3
"""valve-ball-42: four-way ball valve, a manual 4/2 reversing valve: four NPT 1/4 female ports round a square brass body, a double-L
ball under a quarter-turn lever. Position a (the lever at 0) joins 1 to 2 and 4 to 3; position b (90) joins 1 to 4 and 2 to 3, so a
double-acting cylinder on 2 and 4 is driven one way or the other by hand, its exhaust leaving through 3.
Generic (OPERATING.md 12, EM 2026-11-07; autopilot.md 2.b2: the next ETIM class `inventory pneu` lists after EC010471): our own
vendor-neutral design of ETIM 10.0 EC010102 "Four-way ball valve"; the class values it is designed to are in spec.md "## Class
values". Threaded connections, no coupling and no flange (class values 6, 9, 12, 15 and 18), so nothing in its shape waits on a
dimensional standard. It is not the inventory's valve-ball row (a 2-way ball valve with an ISO 5211 actuator flange, waiting on that
standard). Port series, units and roles come from toolkit/pneu.py (D1, ROLES, NODES: ISO 11727's 1 supply, 2 and 4 work, 3 exhaust).
Ports drawn as valve-gauge-double 1.0 draws its female ports: a blind bore Ø E1 + h, L2 + 2 deep (tank 2.0's rule), each through its
number field, the pivot on the field's outer face (filter-air 3.0's rule). The ball, its seats and passages are not modelled. Every
other size is a design choice. No vendor file was opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "valve-ball-42", "1.0", "device"
TITLE = "four-way ball valve, generic, manual 4/2 reversing, four NPT 1/4 female ports, quarter-turn lever"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic four-way ball valve (ETIM 10.0 EC010102); class values in spec.md; a manual 4/2 reversing valve "
            "(double-L ball), four ports NPT 1/4 female (toolkit/pneu.py D1), bored at E1 + h from pneu.NPT (calculated from ASME "
            "B1.20.1's formulas), numbered to ISO 11727 (pneu.NODES); body, boss and lever are design choices")
ORIGIN = ("the body's centre, on the plane of the four port axes: port-1 toward -x, port-2 +y, port-3 +x, port-4 -y; the lever on top "
          "(+z), pointing toward -y in position a (0) and toward +x in position b (90)")
COMMAND = "VALVE-BALL-42"
PARAMS = dict()

PORT = "NPT1/4"                    # design choice within pneu.THREADS (D1): class values 5, 8, 11, 14
B, H = 50.0, 30.0                  # design choice: square body B x B in plan, H high, centred on the origin
FIELD, FIELD_T = 18.0, 0.2         # port-number fields (decals), centred on each bore, 0.2 proud of the face (GEO-050)
BOSS_D, BOSS_H = 14.0, 5.0         # design choice: the stem boss on the body's top face, on the centre
STEM_D, STEM_H = 6.0, 4.0          # design choice: the stem showing between the boss and the lever (turns with it)
ARM = (60.0, 6.0, 12.0, 3.0)       # design choice: lever arm reach from the stem axis (class value 36), tail, width, thickness
NUT_D, NUT_H = 10.0, 3.0           # design choice: the nut holding the lever on the stem
TURN = 90.0                        # deg: position a (0) to position b (90), a quarter turn
LABEL, LABEL_C = (16.0, 10.0), (-14.0, 15.0)   # complexes.org generic field on the top face (x by y), centred in the -x +y quarter
WALL = 3.0                         # design choice: at least 3 mm of brass between bores and round each (valve-gauge-double's figure)
MAT, FIELDM = "M-BRASS", "M-WHITE-PA"
P_MAX_BAR = 10.0                   # class value 19 (EF020150 Max. pressure difference at 20 °C): ratings.csv p_max
assert PORT in pneu.THREADS
_T = pneu.NPT[PORT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4      # 13.616: the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # 12.205: L2 + 2, the 2 a run-out past the male's effective thread (tank 2.0)
FLOOR = B / 2 - BORE_L                    # 12.795: each bore's floor from the centre
assert BORE_L >= pneu.NPT[PORT]["engagement"]                         # deeper than a male's make-up (L1 + L3)
assert H - BORE_D >= 2 * WALL                                          # brass above and below each bore
assert FLOOR - BORE_D / 2 >= WALL                                      # neighbouring bores' floors and sides stay apart
assert (FLOOR - BORE_D / 2) * math.sqrt(2) >= WALL                     # 8.47 of brass across the corner between two neighbours
assert FIELD > BORE_D + 2.0 and FIELD < H                              # the field rings the bore, inside the side face
_lx0, _ly0 = LABEL_C[0] - LABEL[0] / 2, LABEL_C[1] - LABEL[1] / 2
assert _lx0 >= -B / 2 and _ly0 + LABEL[1] <= B / 2                    # the label field stays on the top face
assert math.hypot(_lx0 + LABEL[0], _ly0) > BOSS_D / 2                 # and clear of the boss
assert P_MAX_BAR * 100.0 >= pneu.P_SUPPLY                             # PNE-003 (kPa): 1000 kPa above the bench drop's 689.5

def height(): return H + BOSS_H + STEM_H + ARM[3] + NUT_H             # body underside to the nut's top: 45
def handle_height(): return H / 2 + BOSS_H + STEM_H + ARM[3] + NUT_H  # class value 35: the port axes' plane to the nut's top: 30

def _port(P, body, name, d, role):
    """a female NPT 1/4 port on the side face whose outward normal is d (a unit vector in x or y): the plain bore into the body, its
    number field (the node) with the bore through it, and the pivot on the field's outer face, its axis out of the body"""
    dx, dy = d; c = B / 2
    P.hole("M-GASKET", (dx * (c + 1.0), dy * (c + 1.0), 0), (dx * (c - BORE_L), dy * (c - BORE_L), 0), BORE_D / 2, body)
    h = FIELD / 2
    if dx:
        x0 = c if dx > 0 else -c - FIELD_T
        f = P.box(f"node:{name}|{FIELDM}", x0, -h, -h, FIELD_T, FIELD, FIELD)
    else:
        y0 = c if dy > 0 else -c - FIELD_T
        f = P.box(f"node:{name}|{FIELDM}", -h, y0, -h, FIELD, FIELD_T, FIELD)
    e = c + FIELD_T
    P.hole("M-GASKET", (dx * (e + 1.0), dy * (e + 1.0), 0), (dx * (c - 1.0), dy * (c - 1.0), 0), BORE_D / 2, f)
    P.pivot(name, "port", (dx * e, dy * e, 0), axis=(dx, dy, 0), range=(0, 0), unit=PORT, gender="female", role=role)

def build():
    P = Prims()
    body = P.box(MAT, -B / 2, -B / 2, -H / 2, B, B, H)
    _port(P, body, pneu.NODES["supply"], (-1, 0), "supply")            # port-1, supply (ISO 11727: 1)
    _port(P, body, pneu.NODES["work"][0], (0, 1), "work")              # port-2, work (ISO 11727: 2)
    _port(P, body, pneu.NODES["exhaust"][0], (1, 0), "exhaust")        # port-3, exhaust (ISO 11727: 3)
    _port(P, body, pneu.NODES["work"][1], (0, -1), "work")             # port-4, work (ISO 11727: 4)
    z0 = H / 2; z1 = z0 + BOSS_H; z2 = z1 + STEM_H; z3 = z2 + ARM[3]
    P.cyl(MAT, (0, 0, z0), (0, 0, z1), BOSS_D / 2)                                              # stem boss
    P.cyl(f"node:lever|{MAT}", (0, 0, z1), (0, 0, z2), STEM_D / 2)                              # stem, turns with the lever
    reach, tail, w, t = ARM
    P.box("node:lever|M-BLACK-PA", -w / 2, -reach, z2, w, reach + tail, t)                      # lever arm, toward -y in position a
    P.cyl("node:lever|M-ZINC", (0, 0, z3), (0, 0, z3 + NUT_H), NUT_D / 2)                       # lever nut
    P.pivot("lever", "rotate", (0, 0, z1), axis=(0, 0, 1), range=(0, TURN), unit="deg")        # +90 about +z: -y to +x, a to b
    P.box(FIELDM, _lx0, _ly0, z0, LABEL[0], LABEL[1], FIELD_T)                                   # complexes.org generic, the 4/2 symbol
    e = B / 2 + FIELD_T
    P.collider("env", -e, -reach, -H / 2, 2 * e, reach + e, height())
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="supply port-1", az=180, el=10),
            dict(name="top lever", az=250, el=65)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
