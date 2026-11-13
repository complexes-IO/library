#!/usr/bin/env python3
"""lubrication-central-air-6: a central lubrication unit for a machine tool's ways and ballscrews (a CNC mill, a machining centre): an oil
reservoir on a base plate, an air-operated single-acting piston pump in the pump head over the reservoir, and a progressive
distributor block in front with six metered outlets to the lubrication points. A pulse of air at `port-air` (the machine's air
line, through its own valve) drives the pump's plunger one stroke; the spring returns it; each stroke pushes a metered shot through
the distributor to every outlet in turn, and the distributor's cycle indicator pin (`indicator`) steps out once a cycle. Our own
design (OPERATING.md 12, own designs; lib/inventory.csv row `lubrication-central-air-6`, own_design yes: core watch 2026-11-11, request
pneu-11's answer item 1: no ETIM class and no lubrication standard on file, so a plain own design with no ratings of its own, built
unattended). What it meets takes its figures from the pneumatic contract on file (toolkit/pneu.py D1 NPT threads; pneu.NPT, ASME
B1.20.1 by its formulas, for every bore): `port-air` is a female NPT 1/4 port in the air cylinder's cap, bored Ø (E1 + h) × (L2 + 2)
deep as flow-control-inline 1.0's; the six outlets `port-out-1` to `port-out-6` are female NPT 1/8 ports bored the same way, where a
fitting-pushin (NPT 1/8 stub, 5/32 tube) screws in. The reservoir, plate, pump head, air cylinder, filler, distributor and pin are
design choices. Air-operated, not motor-driven: the air contract is on file and a motor's rating is not (the answer's "no ratings"),
so the unit has no electrical port; the pump's plunger, spring, the pistons inside the distributor and the oil are not modelled.
No pressure, flow, shot or cycle figure is claimed (no ratings.csv): a rated version waits for a standard in sources.csv."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "lubrication-central-air-6", "1.0", "device"
TITLE = "central lubrication unit, air-operated piston pump, oil reservoir, progressive distributor with 6 outlets, NPT 1/4 air, NPT 1/8 outlets"
TOOLKIT = "1.3"
BASELINE = ("our own design (inventory own_design yes; request pneu-11's answer item 1: no ETIM class, no standard on file, no ratings "
            "of its own); air-operated single-acting piston pump on an oil reservoir, progressive distributor with six outlets; "
            "`port-air` NPT 1/4 female and `port-out-1` to `port-out-6` NPT 1/8 female (toolkit/pneu.py D1), bored at E1 + h from "
            "pneu.NPT (calculated from ASME B1.20.1's formulas); reservoir, plate, pump head, air cylinder, filler, distributor and "
            "cycle indicator pin are design choices; no vendor file opened")
ORIGIN = ("the centre of the base plate's underside in x, the reservoir's centre in y (the mounting plane, z = 0); the outlets face "
          "-y (the front), the air port up (+z), the cycle indicator pin out of the distributor's +x end")
COMMAND = "LUBRICATION-CENTRAL"
PARAMS = dict()

AIR_PORT, OUT_PORT = "NPT1/4", "NPT1/8"         # design choices within pneu.THREADS (D1): the air inlet; the six oil outlets
OUTLETS = 6                                      # design choice: six lubrication points (a small mill's ways and screws)
PLATE = (200.0, -95.0, 65.0, 10.0)               # base plate: 200 along x (centred), y from -95 to 65, 10 thick (z 0 to 10)
RES = (120.0, 100.0, 160.0)                      # reservoir: x by y by z, clear polymer, centred on x = 0, y = 0, on the plate
HEAD_OVER, HEAD_H = 8.0, 40.0                    # pump head over the reservoir, overhanging 8 all round, 40 high
CYL_D, CYL_H = 50.0, 70.0                        # air cylinder on the head's top, centred (the single-acting air piston inside it)
FILL_XY, FILL_D, FILL_H = (48.0, 30.0), 30.0, 14.0   # filler cap on the head's top
DIST = (110.0, -88.0, -62.0, 46.0)               # distributor block: 110 along x (centred), y from -88 to -62, 46 high, on the plate
PITCH = 16.0                                     # outlet pitch along x on the distributor's front face
FIELD_AIR, FIELD_OUT, FIELD_T = 18.0, 14.0, 0.2  # port-number fields (decals), centred on each bore, 0.2 proud of the face (GEO-050)
PIN_D, PIN_L, PIN_TRAVEL = 6.0, 8.0, 4.0         # the cycle indicator pin on the distributor's +x end face, face to face; steps out 4
IN = 0.5                                         # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_PLATE, MAT_RES, MAT_HEAD, MAT_CYL, MAT_FILL, MAT_DIST, MAT_PIN, FIELDM = (
    "M-STEEL-7035", "M-CASE-CLEAR", "M-ALU-ANOD", "M-ALU-ANOD", "M-BLACK-PA", "M-GALV", "M-SILVER", "M-WHITE-PA")   # M-ALU-ANOD: a Godot material (lib/godot/qa/materials)

_TA, _TO = pneu.NPT[AIR_PORT]["table"], pneu.NPT[OUT_PORT]["table"]
BORE_AIR = (_TA["E1"] + _TA["h"]) * 25.4         # 13.616 for NPT 1/4 (pneu.NPT, ASME B1.20.1 by its formulas)
BORE_AIR_L = pneu.NPT[AIR_PORT]["length"] + 2.0  # L2 + 2 = 12.205 (tank 2.0's rule)
BORE_OUT = (_TO["E1"] + _TO["h"]) * 25.4         # 10.242 for NPT 1/8
BORE_OUT_L = pneu.NPT[OUT_PORT]["length"] + 2.0  # L2 + 2 = 8.702

Z_PLATE = PLATE[3]                               # 10: the plate's top
Z_RES = Z_PLATE - IN + RES[2]                    # 169.5: the reservoir's top
Z_HEAD = Z_RES - IN + HEAD_H                     # 209: the pump head's top
Z_CYL = Z_HEAD - IN + CYL_H                      # 278.5: the air cylinder's cap face (port-air's end face)
Z_DIST = Z_PLATE - IN + DIST[3]                  # 55.5: the distributor's top
Z_OUT = (Z_PLATE + Z_DIST) / 2.0                 # 32.75: the outlets' axis height
HX, HY = RES[0] / 2.0 + HEAD_OVER, RES[1] / 2.0 + HEAD_OVER   # the head's half sizes
DX0, DX1 = -DIST[0] / 2.0, DIST[0] / 2.0
OUT_X = [(i - (OUTLETS - 1) / 2.0) * PITCH for i in range(OUTLETS)]   # -40, -24, -8, 8, 24, 40

assert AIR_PORT in pneu.THREADS and OUT_PORT in pneu.THREADS
assert BORE_AIR_L >= pneu.NPT[AIR_PORT]["engagement"] and BORE_OUT_L >= pneu.NPT[OUT_PORT]["engagement"]   # deeper than a male's make-up
assert BORE_AIR_L + 10.0 <= CYL_H and CYL_D - BORE_AIR >= 2 * 5.0           # the air bore blind in the cap, 5 of wall round it
assert BORE_OUT_L + 5.0 <= DIST[2] - DIST[1]                                # the outlet bores blind in the block, 5 of floor
assert PITCH - BORE_OUT >= 5.0 and DIST[3] - BORE_OUT >= 2 * 5.0            # 5 of wall between and round the outlet bores
assert OUT_X[0] - FIELD_OUT / 2.0 > DX0 + 5.0 and OUT_X[-1] + FIELD_OUT / 2.0 < DX1 - 5.0   # the fields inside the front face
assert FIELD_OUT > BORE_OUT + 2.0 and FIELD_OUT < PITCH and FIELD_AIR > BORE_AIR + 2.0 and FIELD_AIR < CYL_D
assert RES[0] / 2.0 + HEAD_OVER < PLATE[0] / 2.0 and -RES[1] / 2.0 - HEAD_OVER > DIST[2]   # the head over the plate, clear of the block
assert DIST[1] > PLATE[1] and DX1 < PLATE[0] / 2.0 - 5.0 and RES[1] / 2.0 < PLATE[2]         # the block and the reservoir on the plate
assert DX1 + PIN_L + PIN_TRAVEL < PLATE[0] / 2.0                                            # the pin stays over the plate
assert CYL_D / 2.0 + 2.0 < FILL_XY[0] - FILL_D / 2.0 and FILL_XY[0] + FILL_D / 2.0 < HX and FILL_XY[1] + FILL_D / 2.0 < HY   # filler clear


def _bore(P, solid, name, p_face, axis, d, depth, field, unit, role=None):
    """a female NPT port in a face: the plain bore into the solid, its number field (the node) with the bore through it, and the
    pivot on the field's outer face, its axis out of the body toward the counterpart (pneu.py port frame; flow-control-inline 1.0)"""
    ax, ay, az = axis; x, y, z = p_face
    P.hole("M-GASKET", (x + ax * 1.0, y + ay * 1.0, z + az * 1.0), (x - ax * depth, y - ay * depth, z - az * depth), d / 2, solid)
    h = field / 2.0
    if az: f = P.box(f"node:{name}|{FIELDM}", x - h, y - h, z, field, field, FIELD_T)
    elif ay: f = P.box(f"node:{name}|{FIELDM}", x - h, min(y, y + ay * FIELD_T), z - h, field, FIELD_T, field)
    else: f = P.box(f"node:{name}|{FIELDM}", min(x, x + ax * FIELD_T), y - h, z - h, FIELD_T, field, field)
    P.hole("M-GASKET", (x + ax * (FIELD_T + 1.0), y + ay * (FIELD_T + 1.0), z + az * (FIELD_T + 1.0)), (x - ax, y - ay, z - az), d / 2, f)
    kw = dict(role=role) if role else {}
    P.pivot(name, "port", (x + ax * FIELD_T, y + ay * FIELD_T, z + az * FIELD_T), axis=axis, range=(0, 0), unit=unit, gender="female", **kw)


def build():
    P = Prims()
    px, py0, py1, pt = PLATE
    P.box(MAT_PLATE, -px / 2.0, py0, 0.0, px, py1 - py0, pt)                                                 # base plate
    P.box(MAT_RES, -RES[0] / 2.0, -RES[1] / 2.0, Z_PLATE - IN, RES[0], RES[1], RES[2])                       # reservoir, 0.5 into the plate
    P.box(MAT_HEAD, -HX, -HY, Z_RES - IN, 2 * HX, 2 * HY, HEAD_H)                                           # pump head, 0.5 into the reservoir
    cyl = P.cyl(MAT_CYL, (0, 0, Z_HEAD - IN), (0, 0, Z_CYL), CYL_D / 2.0)                                   # air cylinder, 0.5 into the head
    _bore(P, cyl, "port-air", (0, 0, Z_CYL), (0, 0, 1), BORE_AIR, BORE_AIR_L, FIELD_AIR, AIR_PORT, role="work")   # the air inlet, in the cap
    P.cyl(MAT_FILL, (FILL_XY[0], FILL_XY[1], Z_HEAD - IN), (FILL_XY[0], FILL_XY[1], Z_HEAD + FILL_H), FILL_D / 2.0)   # filler cap
    dist = P.box(MAT_DIST, DX0, DIST[1], Z_PLATE - IN, DIST[0], DIST[2] - DIST[1], DIST[3])                 # distributor block, 0.5 into the plate
    for i, x in enumerate(OUT_X):                                                                           # six metered outlets, front face
        _bore(P, dist, f"port-out-{i + 1}", (x, DIST[1], Z_OUT), (0, -1, 0), BORE_OUT, BORE_OUT_L, FIELD_OUT, OUT_PORT)
    yc = (DIST[1] + DIST[2]) / 2.0
    P.cyl(f"node:indicator|{MAT_PIN}", (DX1, yc, Z_OUT), (DX1 + PIN_L, yc, Z_OUT), PIN_D / 2.0)             # cycle indicator pin, face to face
    P.pivot("indicator", "translate", (DX1, yc, Z_OUT), axis=(1, 0, 0), range=(0, PIN_TRAVEL), unit="mm")
    P.collider("body", -px / 2.0, py0, 0.0, px, py1 - py0, Z_CYL + FIELD_T)
    P.collider("indicator", DX1, yc - PIN_D / 2.0, Z_OUT - PIN_D / 2.0, PIN_L, PIN_D, PIN_D)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="outlets", az=270, el=15), dict(name="top air port", az=225, el=65)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
