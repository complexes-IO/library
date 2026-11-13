#!/usr/bin/env python3
"""valve-sol-52-sr: four-way (5/2) solenoid valve, single solenoid, spring return, pilot operated, 24 V DC, body ported NPT 1/4, panel
mounted. Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC010304 "Four-way solenoid valve";
the class values it is designed to are in spec.md "## Class values". Port names, series, roles and the coil's voltage and connector
come from toolkit/pneu.py (D1, D6, D7). Body ported, so no sub-base interface is involved (the ISO 15407-1 face of D6 is not on
file and this valve takes none). Each port is a bore with its port pivot (gender female, PIN-002) and its number field. The
coil's M12 receptacle (receptacle-m12, male A, pneu.py D6) is placed in a later version, once it has passed station 6
(OPERATING.md 12, foundation first). Every other size is a design choice. No vendor file was opened.
2.0 (pneu-r76, review valve-sol-4way-1.0.md findings 1 and 2, the cloud elements' bores and ratings): each port is bored as tank
2.0's and valve-sol-32nc-sr 2.0's, Ø (E1 + h) × (L2 + 2) deep from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM
2026-11-07), so a placed male stub (fitting-pushin 2.0) fits; each port's pivot stands on its number field's outer face (filter-air
3.0's fix), so a male's hex seats on the field; ratings.csv carries p_max, p_min and coil_v. The thread is no longer an open figure."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "valve-sol-52-sr", "2.1", "device"
TITLE = "four-way solenoid valve 5/2, generic, single solenoid, spring return, 24 V DC, body ported NPT 1/4"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic four-way solenoid valve (ETIM 10.0 EC010304); class values in spec.md; 5/2 body ported, ports NPT "
            "1/4 female (toolkit/pneu.py D1), bored at E1 + h from pneu.NPT (calculated from ASME B1.20.1's formulas), numbered to "
            "ISO 11727 (D7), coil 24 V DC (D6); sizes are design choices")
ORIGIN = ("surface mount: back face on the panel y = 0, the left mounting hole's centre x = 0, z = 0; body toward -y, ports on the "
          "front face (-y; each port's pivot 0.2 out, on its number field), spool along +x, the solenoid at the left end")
COMMAND = "VALVE-SOL-4WAY"
PARAMS = dict()

PORT = "NPT1/4"                    # design choice within pneu.THREADS (D1): every port the same size
P_MAX_BAR, P_MIN_BAR = 10.0, 2.0   # class values 10 "Max. pressure difference for DC model", 11 "Min. pressure difference" (ratings.csv)
X0, L, D, H = -6.0, 80.0, 30.0, 44.0   # design choice: body from x = -6, 80 long (x), 30 deep (y), 44 high (z), centred on z = 0
FIX_D, FIX_X = 4.5, (0.0, 68.0)    # M4 clearance, medium (ISO 273 H13: 4.5 to 4.68; lib/standards/holes.csv), through y at z = 0
_T = pneu.NPT[PORT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4      # 13.616 for NPT 1/4: the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # L2 (10.205) + 2: design choice, a run-out past the male's effective thread (tank 2.0)
FIELD, FIELD_T = 18.0, 0.2         # port-number field (decal), centred on the bore, 0.2 proud of the face (GEO-050); 2.0: 16 -> 18
PORTS = {"port-5": (14.0, -10.0, "exhaust"), "port-1": (34.0, -10.0, "supply"), "port-3": (54.0, -10.0, "exhaust"),   # lower row
         "port-4": (24.0, 10.0, "work"), "port-2": (44.0, 10.0, "work")}                                           # upper row
PILOT = (12.0, 28.0, 42.0)         # design choice: pilot head between the body and the coil (x by y by z), 1 inside the body's faces
COIL = (30.0, 26.0, 36.0)          # design choice: encapsulated coil (x by y by z); its left end face takes receptacle-m12 later
CAP = 6.0                          # design choice: spring-return end cap on the right end, the pilot head's section
OVR_D, OVR_P = 6.0, 1.5            # design choice: locking manual override (turn), on the pilot head's front face, 1.5 proud
OVR_TURN = 90.0                    # deg, off (0) to locked on: design choice
LED_D, LED_P = 3.0, 0.6            # design choice: the coil's LED lens on its front face
LABEL = (60.0, 14.0)               # complexes.org generic field on the body's top face (x by y)
MAT, BLK, COILM, FIELDM = "M-ALU-ANOD", "M-BLACK-PA", "M-BLACK-PA", "M-WHITE-PA"
assert PORT in pneu.THREADS and set(PORTS) == {pneu.NODES["supply"], *pneu.NODES["work"], *pneu.NODES["exhaust"]}
assert BORE_L >= pneu.NPT[PORT]["engagement"] and BORE_L + 10.0 <= D       # deeper than a male's make-up; 10 of body behind each
assert all(H / 2 - abs(z) - BORE_D / 2 >= 5.0 for _, z, _ in PORTS.values())   # at least 5 of wall to the top and bottom faces
assert FIELD > BORE_D + 2.0 and all(H / 2 - abs(z) - FIELD / 2 >= 2.0 for _, z, _ in PORTS.values())   # the field rings its bore
assert all(abs(x - fx) - FIELD / 2 - FIX_D / 2 >= 2.0 for x, _, _ in PORTS.values() for fx in FIX_X)  # fields clear the fixing holes
assert P_MAX_BAR * 100.0 >= pneu.P_SUPPLY and P_MIN_BAR * 100.0 <= pneu.P_WORK_MAX   # PNE-003 / PNE-007 (kPa)

def _port(P, body, name, x, z, role):
    """a female NPT 1/4 port on the front face: the bore into the body, its number field (the node) with the bore through it, and
    the pivot on the field's outer face (2.0), its axis out of the body toward the counterpart (pneu.py port frame)"""
    P.hole("M-GASKET", (x, -D - 1.0, z), (x, -D + BORE_L, z), BORE_D / 2, body)
    h = FIELD / 2
    f = P.box(f"node:{name}|{FIELDM}", x - h, -D - FIELD_T, z - h, FIELD, FIELD_T, FIELD)
    P.hole("M-GASKET", (x, -D - FIELD_T - 1.0, z), (x, -D + 1.0, z), BORE_D / 2, f)
    P.pivot(name, "port", (x, -D - FIELD_T, z), axis=(0, -1, 0), range=(0, 0), unit=PORT, gender="female", role=role)

def build():
    P = Prims()
    body = P.box(MAT, X0, -D, -H / 2, L, D, H)
    for x in FIX_X:                                                                            # panel fixing holes, through y
        P.hole("M-GASKET", (x, 1.0, 0), (x, -D - 1.0, 0), FIX_D / 2, body)
    for name, (x, z, role) in PORTS.items(): _port(P, body, name, x, z, role)
    px0 = X0 - PILOT[0]                                                                        # pilot head, left of the body
    P.box(BLK, px0, -1.0 - PILOT[1], -PILOT[2] / 2, PILOT[0], PILOT[1], PILOT[2])
    cx0 = px0 - COIL[0]                                                                        # the coil (node coil-14), left of the pilot
    P.box(f"node:{pneu.NODES['coil']}|{COILM}", cx0, -2.0 - COIL[1], -COIL[2] / 2, COIL[0], COIL[1], COIL[2])
    P.pivot(pneu.NODES["coil"], "fixed", (cx0 + COIL[0] / 2, -2.0 - COIL[1] / 2, 0))
    P.box(BLK, X0 + L, -1.0 - PILOT[1], -PILOT[2] / 2, CAP, PILOT[1], PILOT[2])                # spring-return end cap, right end
    ox, oy = px0 + PILOT[0] / 2, -1.0 - PILOT[1]                                               # manual override 14, pilot head front
    P.cyl(f"node:{pneu.NODES['override']}|M-YELLOW-PA", (ox, oy, 0), (ox, oy - OVR_P, 0), OVR_D / 2)
    P.pivot(pneu.NODES["override"], "rotate", (ox, oy, 0), axis=(0, -1, 0), range=(0, OVR_TURN))
    lx, ly, lz = cx0 + COIL[0] - 6.0, -2.0 - COIL[1], COIL[2] / 2 - 6.0                       # LED 14, coil front, upper right
    P.cyl(f"node:{pneu.NODES['led']}|M-LENS-YELLOW", (lx, ly, lz), (lx, ly - LED_P, lz), LED_D / 2)
    P.pivot(pneu.NODES["led"], "emissive", (lx, ly, lz), axis=(0, -1, 0), range=(0, 1))
    P.box(FIELDM, X0 + (L - LABEL[0]) / 2, -D / 2 - LABEL[1] / 2, H / 2, LABEL[0], LABEL[1], FIELD_T)   # complexes.org generic, top
    y0 = min(-D - FIELD_T, oy - OVR_P)                                                         # the override stands foremost
    P.collider("env", cx0, y0, -H / 2, X0 + L + CAP - cx0, -y0, H + FIELD_T)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="front ports", az=270, el=8),
            dict(name="top and coil end", az=210, el=55)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
