#!/usr/bin/env python3
"""valve-gauge-double: double pressure gauge valve, NPT 1/4 male (process) underneath, two NPT 1/4 female gauge ports (top and
right side), each shut off by its own hand knob on a rising spindle.
Generic (OPERATING.md 12, EM 2026-11-07; autopilot.md 2.b2 and lib/requests/core/pneu-idle-2026-11-12.md: the first ETIM class
`inventory pneu` lists): our own vendor-neutral design of ETIM 10.0 EC010471 "Double pressure gauge valve" (synonyms "Double
pressure gauge tap", "Dual gauge valve"); the class values it is designed to are in spec.md "## Class values". The two gauge
outlets let a working gauge and a test gauge (or two gauges of different spans) read one tapping, each changed with the line live.
No tension socket and no inspection flange (class values 5 and 6: no), so nothing in its shape waits on a dimensional standard.
Port series, units and roles come from toolkit/pneu.py (D1, ROLES, NODES: ISO 11727's 1 for the inlet, 2 and 4 for the outlets).
Ports drawn as valve-gauge 3.0 draws them: the male stub plain at E1 + h (the external thread's major diameter at the hand-tight
plane), length L2; each female a blind bore of the same diameter, L2 + 2 deep (tank 2.0's rule), with its pivot on the number
field's outer face (filter-air 3.0's rule). The thread form and taper are not drawn. Every other size is a design choice. No vendor
file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "valve-gauge-double", "1.1", "device"
TITLE = ("double pressure gauge valve, generic, NPT 1/4 male process to two NPT 1/4 female gauge ports, two hand knobs, rising "
         "spindles")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic double pressure gauge valve (ETIM 10.0 EC010471); class values in spec.md; process NPT 1/4 male "
            "underneath, gauge ports NPT 1/4 female on top and on the right side (toolkit/pneu.py D1), stub and bores at E1 + h from "
            "pneu.NPT (calculated from ASME B1.20.1's formulas); body, bore depths and knobs are design choices")
ORIGIN = ("in line, upright: the process connection's shoulder centre on the body's underside; the stub toward -z, gauge port 2 on "
          "top (+z), gauge port 4 on the right side (+x), both knobs toward -y")
COMMAND = "VALVE-GAUGE-DOUBLE"
PARAMS = dict()

PORT = "NPT1/4"                    # design choice within pneu.THREADS (D1): class value "Connection size"
WAF, H = 22.0, 70.0                # design choice: square body, 22 across its flats, 70 high (class value "Height")
_T = pneu.NPT[PORT]["table"]
STUB_D = (_T["E1"] + _T["h"]) * 25.4      # 13.616: the male's major diameter at the hand-tight plane (pneu.NPT; gauge-p's stub rule)
STUB_L = pneu.NPT[PORT]["length"]         # 10.205: L2, the male's effective thread (pneu.NPT)
BORE_D = STUB_D                           # each female bore at the same diameter, so a male stub and the bore touch (tank 2.0's rule)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # 12.205: L2 + 2, the 2 a run-out past the male's effective thread (design choice, tank 2.0)
FIELD, FIELD_T = 18.0, 0.2         # port-number fields (decals), centred on each bore, 0.2 proud of the face (GEO-050)
Z4 = 22.0                          # design choice: port-4's axis height on the right side face (+x)
ZK4, ZK2 = 20.0, 50.0              # design choice: the knobs' axis heights on the front face (-y): knob-4 low, knob-2 high
BONNET_D, BONNET_H = 14.0, 6.0     # design choice: bonnets on the front face
SPINDLE_D, SPINDLE_H = 6.0, 6.0    # design choice: the visible spindles between the bonnets and the knobs (turn and rise with them)
KNOB_D, KNOB_H = 24.0, 12.0        # design choice: class value "Length of handle/diameter of hand wheel" 24
TURNS, LEAD = 4, 0.5               # design choice: closed (0) to fully open in 4 turns; each spindle rises 0.5 per turn
LABEL, ZL = (16.0, 10.0), 35.0     # complexes.org generic field on the left side face (-x), y by z, centred at z = 35
WALL = 3.0                         # design choice: at least 3 mm of brass round each bore (gas-regulator 2.0's figure)
MAT, FIELDM = "M-BRASS", "M-WHITE-PA"
assert PORT in pneu.THREADS
assert WAF > (_T["E2"] + _T["h"]) * 25.4                        # the body's flats clear the thread's largest major diameter (E2 + h)
assert BORE_L >= pneu.NPT[PORT]["engagement"] and BORE_L < WAF  # deeper than the make-up L1 + L3; port-4's bore stays blind in the body
assert WAF - BORE_D >= 2 * WALL and FIELD > BORE_D              # 4.19 of wall round each bore; the fields ring them
assert WAF / 2 - BORE_L > -WAF / 2 + WALL                       # port-4's floor (x = -1.205) leaves the left wall whole
assert Z4 - FIELD / 2 >= 0 and Z4 - BORE_D / 2 >= WALL           # port-4's field on the side face; brass under its bore
assert Z4 + BORE_D / 2 + WALL < H - BORE_L                      # port-4's bore stays under port-2's floor (z = 57.795)
assert ZK2 - ZK4 > KNOB_D and ZK2 + KNOB_D / 2 <= H and ZK4 - KNOB_D / 2 >= 0   # the knobs clear each other, within the body's height
assert 0 <= ZL - LABEL[1] / 2 and ZL + LABEL[1] / 2 <= H         # the label field (left face) stays on the body

def height(): return H                               # class value "Height": the body, underside (the shoulder) to the top face
def construction_length(): return STUB_L + H         # the stub's end to port-2's face (spec.md)

def build():
    P = Prims(); h = WAF / 2
    body = P.box(MAT, -h, -h, 0.0, WAF, WAF, H)
    P.cyl(f"node:port-1|{MAT}", (0, 0, 0), (0, 0, -STUB_L), STUB_D / 2)                        # process connection: the male stub
    P.pivot("port-1", "port", (0, 0, 0), axis=(0, 0, -1), range=(0, 0), unit=PORT, gender="male", role="supply",
            length=round(STUB_L, 3))
    P.hole("M-GASKET", (0, 0, H + 1.0), (0, 0, H - BORE_L), BORE_D / 2, body)                  # gauge port 2: the top bore
    f2 = P.box(f"node:port-2|{FIELDM}", -FIELD / 2, -FIELD / 2, H, FIELD, FIELD, FIELD_T)      # its number field, the bore through it
    P.hole("M-GASKET", (0, 0, H + FIELD_T + 1.0), (0, 0, H - 1.0), BORE_D / 2, f2)
    P.pivot("port-2", "port", (0, 0, H + FIELD_T), axis=(0, 0, 1), range=(0, 0), unit=PORT, gender="female", role="gauge")
    P.hole("M-GASKET", (h + 1.0, 0, Z4), (h - BORE_L, 0, Z4), BORE_D / 2, body)                # gauge port 4: the right side bore
    f4 = P.box(f"node:port-4|{FIELDM}", h, -FIELD / 2, Z4 - FIELD / 2, FIELD_T, FIELD, FIELD)  # its number field, the bore through it
    P.hole("M-GASKET", (h + FIELD_T + 1.0, 0, Z4), (h - 1.0, 0, Z4), BORE_D / 2, f4)
    P.pivot("port-4", "port", (h + FIELD_T, 0, Z4), axis=(1, 0, 0), range=(0, 0), unit=PORT, gender="female", role="gauge")
    y1 = -h - BONNET_H; y2 = y1 - SPINDLE_H
    for knob, zk in (("knob-2", ZK2), ("knob-4", ZK4)):
        P.cyl(MAT, (0, -h, zk), (0, y1, zk), BONNET_D / 2)                                      # bonnet
        P.cyl(f"node:{knob}|{MAT}", (0, y1, zk), (0, y2, zk), SPINDLE_D / 2)                    # spindle, turns with the knob
        P.cyl(f"node:{knob}|M-BLACK-PA", (0, y2, zk), (0, y2 - KNOB_H, zk), KNOB_D / 2)         # hand knob
        P.pivot(knob, "rotate", (0, y1, zk), axis=(0, -1, 0), range=(0, 360 * TURNS), unit="deg", lead=LEAD)   # counter-clockwise opens
    P.box(FIELDM, -h - FIELD_T, -LABEL[0] / 2, ZL - LABEL[1] / 2, FIELD_T, LABEL[0], LABEL[1])  # complexes.org generic, left side face
    yf = y2 - KNOB_H; xk = max(h + FIELD_T, KNOB_D / 2)                                       # the knobs stand foremost and widest
    P.collider("env", -xk, yf, -STUB_L, 2 * xk, h - yf, H + STUB_L + FIELD_T)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="right side, port 4", az=330, el=15),
            dict(name="from below, process stub", az=230, el=-40)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
