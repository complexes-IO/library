#!/usr/bin/env python3
"""manifold-pneu: valve manifold sub-base for n 18 mm valve stations (ISO 15407-1 size class), panel mounted. Our own design
(OPERATING.md 12: manifolds; lib/inventory.csv own_design yes). Ports, names, series and roles come from toolkit/pneu.py (request pneu-1,
D1, D6, D7). The body's sizes, the station pitch and the port places are design choices. Two things it meets are NOT ON FILE, and this
version leaves them out rather than guess them: the NPT port bores (ASME B1.20.1 table: pneu.NPT is empty) and the ISO 15407-1 18 mm
valve interface face (pneu.ISO15407_18 is empty). Each port is a pivot on its axis, shown by a port-number field centred on it; the
bores and the valve face's holes come in 2.0, when those rows are on file."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "manifold-pneu", "1.1", "device"
TITLE = ("valve manifold sub-base, 4 stations sized for 18 mm valves (valve face NOT ON FILE until 2.0), NPT ports (1 supply, "
         "3 / 5 exhaust, 2 / 4 per station)")
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, inventory own_design yes): block, pitch and port places are design choices; ports NPT "
            "(toolkit/pneu.py D1), numbered to ISO 11727 (pneu.NODES); NPT bores and the ISO 15407-1 18 mm face NOT ON FILE")
ORIGIN = "panel mount: back face on the panel y = 0, left end x = 0, bottom face z = 0; stations along +x, valve face toward -y"
COMMAND = "MANIFOLD-PNEU"
PARAMS = dict(stations=4)

END, PITCH = 20.0, 25.0          # design choices: end zone (fixing hole, end ports); station pitch, wider than the 18 mm size class
D, H = 36.0, 50.0                # design choices: depth panel to valve face (y), height (z)
FIX_D = 5.5                      # M5 clearance, medium (ISO 273 H13: 5.5 to 5.68; lib/standards/holes.csv); the screw is placed later
FIX_Z = 25.0                     # fixing holes through y at mid-height, END / 2 from each end
PORT_Z = (38.0, 12.0)            # end ports' heights: clear of the fixing hole's line at FIX_Z
WORK_Y = {"port-2": -27.0, "port-4": -9.0}    # work ports on the bottom face: 2 toward the valve face, 4 toward the panel
MARK, MARK_T = 6.0, 0.2          # port-number field (decal) centred on each port's axis, 0.2 proud of the face (GEO-050)
LOGO = (16.0, 8.0)               # 1.1, design choice: the complexes.org field on the top face's left end zone (x by y)
# 1.1 (review manifold-pneu-1.0 finding 1): the station numbers and complexes.org go on the top face (z = H), which no valve covers;
# the valve face (-y) is where the valves sit, so marks there would be hidden in service
SUPPLY, EXHAUST, WORK = "NPT1/4", "NPT1/4", "NPT1/8"   # design choices from pneu.THREADS; 1/8 matches pneu.ISO15552[32]'s port
MAT, FIELD = "M-ALU-ANOD", "M-WHITE-PA"
assert {SUPPLY, EXHAUST, WORK} <= set(pneu.THREADS)

def length(stations): return 2 * END + stations * PITCH

def _port(P, name, centre, axis, unit, role):
    """a female NPT port: the pivot on its axis at the face (pneu.py port frame) and its number field around it"""
    c = tuple(float(v) for v in centre); a = tuple(float(v) for v in axis); h = MARK / 2
    lo = [c[i] - h if a[i] == 0 else min(c[i], c[i] + a[i] * MARK_T) for i in range(3)]
    sz = [MARK if a[i] == 0 else MARK_T for i in range(3)]
    P.box(f"node:{name}|{FIELD}", *lo, *sz)
    P.pivot(name, "port", c, axis=a, range=(0, 0), unit=unit, gender="female", role=role)

def build(stations=4):
    n = int(stations); assert 1 <= n <= 10, "stations: 1 to 10"
    P = Prims(); L = length(n)
    body = P.box(MAT, 0, -D, 0, L, D, H)
    for x in (END / 2, L - END / 2):                                                            # panel fixing holes, through y
        P.hole("M-GASKET", (x, 1.0, FIX_Z), (x, -D - 1.0, FIX_Z), FIX_D / 2, body)
    _port(P, pneu.NODES["supply"], (0, -D / 2, PORT_Z[0]), (-1, 0, 0), SUPPLY, "supply")          # port-1, left end
    _port(P, "port-3", (L, -D / 2, PORT_Z[0]), (1, 0, 0), EXHAUST, "exhaust")                    # port-3 and port-5, right end
    _port(P, "port-5", (L, -D / 2, PORT_Z[1]), (1, 0, 0), EXHAUST, "exhaust")
    for k in range(1, n + 1):                                                                   # st<k>-port-2 / -4, bottom face
        x = END + (k - 0.5) * PITCH
        for w in pneu.NODES["work"]:
            _port(P, pneu.NODES["station"].replace("<k>", str(k)) + w, (x, WORK_Y[w], 0), (0, 0, -1), WORK, "work")
        P.box(FIELD, x - MARK / 2, -D / 2 - MARK / 2, H, MARK, MARK, MARK_T)                   # station-number field, top face
    P.box(FIELD, END / 2 - LOGO[0] / 2, -D / 2 - LOGO[1] / 2, H, LOGO[0], LOGO[1], MARK_T)       # complexes.org field, top face
    P.collider("env", -MARK_T, -D, -MARK_T, L + 2 * MARK_T, D, H + 2 * MARK_T)                   # 1.1: the top-face fields
    return P

PREVIEWS = [dict(name="front three-quarter, 4 stations", az=250, el=20), dict(name="bottom work ports", az=250, el=-35),
            dict(name="top face marks", az=250, el=70),
            dict(name="2 stations", az=250, el=20, params=dict(stations=2))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
