#!/usr/bin/env python3
"""valve-gauge: pressure gauge valve, straight, NPT 1/4 male (process) to NPT 1/4 female (gauge), hand knob with a rising spindle.
Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC010262 "Pressure gauge valve"; the class
values it is designed to are in spec.md "## Class values". Not to DIN 16270 or 16271 (neither is on file), no test connection and no
tension socket, so nothing in its shape waits on a dimensional standard. Port series, units and roles come from toolkit/pneu.py (D1,
ROLES). 2.0 (pneu-r57) takes both ports' figures from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07), as
gauge-p and gas-regulator 2.0 do: the male process stub is drawn plain at E1 + h (the external thread's major diameter at the
hand-tight plane), length L2; the female gauge port is a blind bore of the same diameter, L2 + 2 deep (tank 2.0's rule), so a male
NPT 1/4 stub (gauge-p's) meets it face to face. The thread form and taper are not drawn. Every other size is a design choice. No
vendor file was opened. 3.0 (pneu-r71; review valve-gauge-2.0.md finding 1, pneu-r58 finding 1, filter-air 3.0's fix): port-2's
pivot stands on its number field's outer face (z = H + FIELD_T), not on the body's top under the field, so a placed male's seat
meets the field face to face instead of sitting 0.2 into it."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "valve-gauge", "3.0", "device"
TITLE = "pressure gauge valve, generic, straight, NPT 1/4 male to NPT 1/4 female, hand knob, rising spindle"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic pressure gauge valve (ETIM 10.0 EC010262); class values in spec.md; straight, process NPT 1/4 male, "
            "gauge NPT 1/4 female (toolkit/pneu.py D1), stub and bore at E1 + h from pneu.NPT (calculated from ASME B1.20.1's "
            "formulas); body, bore depth and knob are design choices")
ORIGIN = ("in line, upright: the process connection's shoulder centre on the body's underside; the stub toward -z, the gauge port on "
          "top (+z), the knob toward -y")
COMMAND = "VALVE-GAUGE"
PARAMS = dict()

PORT = "NPT1/4"                    # design choice within pneu.THREADS (D1): class values "Connection size 1" and "Connection size 2"
WAF, H = 22.0, 40.0                # design choice: square body, 22 across its flats (class value "Wrench width"), 40 high (class value "Height")
_T = pneu.NPT[PORT]["table"]
STUB_D = (_T["E1"] + _T["h"]) * 25.4      # 13.616: the male's major diameter at the hand-tight plane (pneu.NPT; gauge-p's stub rule)
STUB_L = pneu.NPT[PORT]["length"]         # 10.205: L2, the male's effective thread (pneu.NPT)
BORE_D = STUB_D                           # the female bore at the same diameter, so a male stub and this bore touch (tank 2.0's rule)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # 12.205: L2 + 2, the 2 a run-out past the male's effective thread (design choice, tank 2.0)
FIELD, FIELD_T = 18.0, 0.2         # port-number field (decal), centred on the bore, 0.2 proud of the face (GEO-050)
ZK = 18.0                          # design choice: the knob's axis height on the front face
BONNET_D, BONNET_H = 14.0, 6.0     # design choice: bonnet on the front face
SPINDLE_D, SPINDLE_H = 6.0, 6.0    # design choice: the visible spindle between the bonnet and the knob (turns and rises with it)
KNOB_D, KNOB_H = 24.0, 12.0        # design choice: class value "Length of handle/diameter of hand wheel" 24
TURNS, LEAD = 4, 0.5               # design choice: closed (0) to fully open in 4 turns; the spindle rises 0.5 per turn
LABEL = (16.0, 10.0)               # complexes.org generic field on the right side face (y by z)
WALL = 3.0                         # design choice: at least 3 mm of brass round the bore (gas-regulator 2.0's figure)
MAT, FIELDM = "M-BRASS", "M-WHITE-PA"
assert PORT in pneu.THREADS
assert WAF > (_T["E2"] + _T["h"]) * 25.4                        # the body's flats clear the thread's largest major diameter (E2 + h)
assert BORE_L >= pneu.NPT[PORT]["engagement"] and BORE_L < H    # deeper than the make-up L1 + L3, blind inside the body
assert WAF - BORE_D >= 2 * WALL and FIELD > BORE_D              # 4.19 of wall round the bore; the field rings it
assert ZK + BONNET_D / 2 < H - BORE_L                           # the bonnet's top (z = 25) stays under the bore's floor (z = 27.795)

def height(): return H                               # class value "Height": the body, underside (the shoulder) to the top face
def construction_length(): return STUB_L + H         # class value "Construction length": the stub's end to the gauge port's face

def build():
    P = Prims(); h = WAF / 2
    body = P.box(MAT, -h, -h, 0.0, WAF, WAF, H)
    P.cyl(f"node:port-1|{MAT}", (0, 0, 0), (0, 0, -STUB_L), STUB_D / 2)                        # process connection: the male stub
    P.pivot("port-1", "port", (0, 0, 0), axis=(0, 0, -1), range=(0, 0), unit=PORT, gender="male", role="supply",
            length=round(STUB_L, 3))
    P.hole("M-GASKET", (0, 0, H + 1.0), (0, 0, H - BORE_L), BORE_D / 2, body)                  # gauge connection: the female bore
    f = P.box(f"node:port-2|{FIELDM}", -FIELD / 2, -FIELD / 2, H, FIELD, FIELD, FIELD_T)       # its number field, the bore through it
    P.hole("M-GASKET", (0, 0, H + FIELD_T + 1.0), (0, 0, H - 1.0), BORE_D / 2, f)
    P.pivot("port-2", "port", (0, 0, H + FIELD_T), axis=(0, 0, 1), range=(0, 0), unit=PORT, gender="female", role="gauge")   # 3.0: on the field's outer face
    y1 = -h - BONNET_H; y2 = y1 - SPINDLE_H
    P.cyl(MAT, (0, -h, ZK), (0, y1, ZK), BONNET_D / 2)                                          # bonnet
    P.cyl(f"node:knob|{MAT}", (0, y1, ZK), (0, y2, ZK), SPINDLE_D / 2)                          # spindle, turns with the knob
    P.cyl(f"node:knob|M-BLACK-PA", (0, y2, ZK), (0, y2 - KNOB_H, ZK), KNOB_D / 2)               # hand knob
    P.pivot("knob", "rotate", (0, y1, ZK), axis=(0, -1, 0), range=(0, 360 * TURNS), unit="deg", lead=LEAD)   # counter-clockwise opens
    P.box(FIELDM, h, -LABEL[0] / 2, ZK - LABEL[1] / 2 + 2.0, FIELD_T, LABEL[0], LABEL[1])     # complexes.org generic, right side face
    yf = y2 - KNOB_H; xk = max(h, KNOB_D / 2)                                                  # the knob stands foremost and widest
    P.collider("env", -xk, yf, -STUB_L, 2 * xk, h - yf, H + STUB_L + FIELD_T)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="right side", az=330, el=15),
            dict(name="from below, process stub", az=230, el=-40)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
