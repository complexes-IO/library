#!/usr/bin/env python3
"""pressure-washer-skid: a stationary cold-water pressure washer for a parts-cleaning cell (the industrial cleaner of
lib/machines-factory.txt): a skid plate on four rubber feet carrying a horizontal three-phase motor close-coupled to a triplex
plunger pump; the pump's manifold head takes the water in at `port-in` and delivers it at `port-out` to the cell's high-pressure
hose and lance; the unloader valve on the head (its knob fixed in 1.x) returns the flow to the inlet side when the lance is shut.
Our own design (OPERATING.md 12, own designs; lib/inventory.csv row `pressure-washer-skid`, own_design yes: core watch 2026-11-11,
request pneu-11's answer item 1: no ETIM class and no standard on file, so a plain own design with no ratings of its own, built
unattended). What it meets takes its figures from the pneumatic contract's threads on file (toolkit/pneu.py D1 NPT; pneu.NPT, ASME
B1.20.1 by its formulas, for the bores): `port-in` and `port-out` are female NPT 3/8 ports bored Ø (E1 + h) × (L2 + 2) deep as
hyd-cooler 1.0's water ports and flow-control-inline 1.0's, with the pivot on each port's field; the hose and gun threads of the trade are
not on file, so the outlet is a plain NPT 3/8 port and an adapter is the hose's. The motor is drawn as the unit's own body (no IEC
frame figure is used, no motor element placed) and has no electrical port in 1.0: a motor rating is what the answer rules out until
a standard is on file (no ratings.csv), and an unrated `pwr` would make ELR read a current it has no figure for; the terminal box
is drawn, the entry is a later rated version's. Plate, feet, motor, pump, head, unloader and ports are design choices; the pump's
crank, plungers, valves and the water are not modelled. No pressure, flow or power figure is claimed."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "pressure-washer-skid", "1.0", "device"
TITLE = "pressure washer, stationary cold water, motor and triplex plunger pump on a skid, unloader, NPT 3/8 inlet and outlet"
TOOLKIT = "1.3"
BASELINE = ("our own design (inventory own_design yes; request pneu-11's answer item 1: no ETIM class, no standard on file, no ratings "
            "of its own); skid plate on rubber feet, horizontal motor close-coupled to a triplex plunger pump, manifold head with an "
            "unloader valve; `port-in` and `port-out` NPT 3/8 female (toolkit/pneu.py D1), bored at E1 + h from pneu.NPT (calculated "
            "from ASME B1.20.1's formulas); plate, feet, motor, pump, head and unloader are design choices; no motor element placed "
            "and no electrical port in 1.0; no vendor file opened")
ORIGIN = ("the centre of the skid plate in x and y on the feet's underside (the floor, z = 0); the motor toward -x, the pump head "
          "and `port-out` toward +x, `port-in` on the head's front (-y) face, the unloader up (+z)")
COMMAND = "PRESSURE-WASHER"
PARAMS = dict()

PORT = "NPT3/8"                                  # design choice within pneu.THREADS (D1): the inlet and the outlet
PLATE = (560.0, 300.0, 8.0)                      # skid plate: x by y by thickness, centred
FOOT_D, FOOT_H, FOOT_IN = 30.0, 20.0, 30.0       # four rubber feet under the plate, 30 in from its corners
MFOOT = (-230.0, -10.0, -60.0, 60.0, 32.0)       # the motor's foot block on the plate: x0, x1, y0, y1, height
MOTOR_D, MOTOR_X = 160.0, (-240.0, 20.0)         # motor body: Ø160, along x from -240 to 20, its axis at Z_AX
COWL_D, COWL_L = 150.0, 40.0                     # fan cowl on the motor's -x end
TBOX = (-160.0, -90.0, -30.0, 30.0, 50.0)        # terminal box on the motor's top: x0, x1, y0, y1, height (no entry in 1.0)
FLANGE_D, FLANGE_L = 130.0, 24.0                 # the pump's bell flange on the motor's +x end (the close coupling)
PUMP = (120.0, 110.0, 110.0)                     # the pump's crankcase: along x, y, z, centred on the axis, after the flange
HEAD = (50.0, 130.0, 120.0)                      # the manifold head on the crankcase's +x end: along x, y, z, centred on the axis
UNL_D, UNL_H, KNOB_D, KNOB_H = 32.0, 40.0, 36.0, 16.0   # unloader valve cartridge up from the head's top and its knob (fixed)
FIELD, FIELD_T = 22.0, 0.2                       # port fields (decals), centred on each bore, 0.2 proud of the face (GEO-050)
IN = 0.5                                         # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_PLATE, MAT_FOOT, MAT_MOTOR, MAT_FLANGE, MAT_PUMP, MAT_HEAD, MAT_UNL, MAT_KNOB, FIELDM = (
    "M-STEEL-7035", "M-BLACK-PA", "M-CAST-BLUE", "M-ALU-ANOD", "M-ALU-ANOD", "M-BRASS", "M-SILVER", "M-BLACK-PA", "M-WHITE-PA")   # M-ALU-ANOD: a Godot material

_T = pneu.NPT[PORT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4             # 17.055 for NPT 3/8 (pneu.NPT, ASME B1.20.1 by its formulas)
BORE_L = pneu.NPT[PORT]["length"] + 2.0          # L2 + 2 = 12.358 (tank 2.0's rule)

Z_PLATE0 = FOOT_H - IN                           # 19.5: the plate's underside (0.5 into the feet)
Z_PLATE = Z_PLATE0 + PLATE[2]                    # 27.5: the plate's top
Z_MFOOT = Z_PLATE - IN + MFOOT[4]                # 59: the motor foot block's top
Z_AX = Z_MFOOT - IN + MOTOR_D / 2.0              # 138.5: the motor and pump axis
X_FLANGE = MOTOR_X[1] - IN + FLANGE_L            # 43.5: the flange's +x face
X_PUMP = X_FLANGE - IN + PUMP[0]                 # 163: the crankcase's +x face
X_HEAD = X_PUMP - IN + HEAD[0]                   # 212.5: the head's +x face (port-out's end face)
Z_HEAD = Z_AX + HEAD[2] / 2.0                    # 198.5: the head's top
Z_MOTOR = Z_AX + MOTOR_D / 2.0                   # 218.5: the motor's top
Y_HEAD = -HEAD[1] / 2.0                          # -65: the head's front face (port-in's end face)

assert PORT in pneu.THREADS
assert BORE_L >= pneu.NPT[PORT]["engagement"]                                   # deeper than a male's make-up (L1 + L3)
assert BORE_L + 10.0 <= HEAD[0] and BORE_L + 10.0 <= HEAD[1] / 2.0              # both bores blind in the head, 10 of floor
assert min(HEAD[1], HEAD[2]) - BORE_D >= 2 * 5.0 and FIELD > BORE_D + 2.0 and FIELD < HEAD[0]   # wall round each bore, fields inside the faces
assert MOTOR_X[0] - COWL_L + IN > -PLATE[0] / 2.0 and X_HEAD + FIELD_T < PLATE[0] / 2.0   # cowl and head over the plate
assert MFOOT[0] > MOTOR_X[0] and MFOOT[1] < MOTOR_X[1] and MFOOT[3] < MOTOR_D / 2.0 - 10.0   # the foot block under the motor
assert TBOX[0] > MOTOR_X[0] and TBOX[1] < MOTOR_X[1] and TBOX[3] < MOTOR_D / 2.0 - 20.0    # the terminal box on the motor's top
assert FLANGE_D < MOTOR_D and PUMP[1] >= FLANGE_D - 20.0 and HEAD[1] > PUMP[1] and HEAD[2] > PUMP[2]  # flange inside the motor's end, head proud of the crankcase
Z_TOP = max(Z_MOTOR - IN + TBOX[4], Z_HEAD + UNL_H + KNOB_H)                    # 268: the terminal box's top, the unit's height
assert Z_AX - PUMP[2] / 2.0 > Z_PLATE + 10.0 and Z_AX - HEAD[2] / 2.0 > Z_PLATE + 10.0    # pump and head clear of the plate
assert UNL_D < HEAD[0] and KNOB_D < HEAD[1] / 2.0 and FOOT_D / 2.0 + FOOT_IN < PLATE[1] / 2.0   # unloader on the head's top, feet under the plate


def _port(P, solid, name, p_face, axis):
    """a female NPT 3/8 port in a face: the plain bore into the solid, its field (the node) with the bore through it, and the pivot on
    the field's outer face, its axis out of the body toward the counterpart (pneu.py port frame; flow-control-inline 1.0)"""
    ax, ay, az = axis; x, y, z = p_face; h = FIELD / 2.0
    P.hole("M-GASKET", (x + ax, y + ay, z + az), (x - ax * BORE_L, y - ay * BORE_L, z - az * BORE_L), BORE_D / 2, solid)
    if ay: f = P.box(f"node:{name}|{FIELDM}", x - h, min(y, y + ay * FIELD_T), z - h, FIELD, FIELD_T, FIELD)
    else: f = P.box(f"node:{name}|{FIELDM}", min(x, x + ax * FIELD_T), y - h, z - h, FIELD_T, FIELD, FIELD)
    P.hole("M-GASKET", (x + ax * (FIELD_T + 1.0), y + ay * (FIELD_T + 1.0), z), (x - ax, y - ay, z), BORE_D / 2, f)
    P.pivot(name, "port", (x + ax * FIELD_T, y + ay * FIELD_T, z), axis=axis, range=(0, 0), unit=PORT, gender="female")


def build():
    P = Prims(); px, py, pt = PLATE
    for sx in (-1, 1):
        for sy in (-1, 1):                                                                                   # four rubber feet
            x, y = sx * (px / 2.0 - FOOT_IN), sy * (py / 2.0 - FOOT_IN)
            P.cyl(MAT_FOOT, (x, y, 0.0), (x, y, FOOT_H), FOOT_D / 2.0)
    P.box(MAT_PLATE, -px / 2.0, -py / 2.0, Z_PLATE0, px, py, pt)                                              # skid plate
    x0, x1, y0, y1, h = MFOOT
    P.box(MAT_MOTOR, x0, y0, Z_PLATE - IN, x1 - x0, y1 - y0, h)                                              # motor foot block
    P.cyl(MAT_MOTOR, (MOTOR_X[0], 0, Z_AX), (MOTOR_X[1], 0, Z_AX), MOTOR_D / 2.0)                              # motor body
    P.cyl(MAT_MOTOR, (MOTOR_X[0] - COWL_L + IN, 0, Z_AX), (MOTOR_X[0] + IN, 0, Z_AX), COWL_D / 2.0)            # fan cowl, 0.5 into the body
    x0, x1, y0, y1, h = TBOX
    P.box(MAT_MOTOR, x0, y0, Z_MOTOR - IN, x1 - x0, y1 - y0, h)                                              # terminal box, 0.5 into the body
    P.cyl(MAT_FLANGE, (MOTOR_X[1] - IN, 0, Z_AX), (X_FLANGE, 0, Z_AX), FLANGE_D / 2.0)                        # bell flange
    P.box(MAT_PUMP, X_FLANGE - IN, -PUMP[1] / 2.0, Z_AX - PUMP[2] / 2.0, PUMP[0], PUMP[1], PUMP[2])           # crankcase
    head = P.box(MAT_HEAD, X_PUMP - IN, Y_HEAD, Z_AX - HEAD[2] / 2.0, HEAD[0], HEAD[1], HEAD[2])               # manifold head
    xc = X_PUMP - IN + HEAD[0] / 2.0
    _port(P, head, "port-in", (xc, Y_HEAD, Z_AX), (0, -1, 0))                                                # water inlet, front face
    _port(P, head, "port-out", (X_HEAD, 0, Z_AX), (1, 0, 0))                                                 # high-pressure outlet, +x face
    P.cyl(MAT_UNL, (xc, 0, Z_HEAD - IN), (xc, 0, Z_HEAD + UNL_H), UNL_D / 2.0)                                # unloader cartridge
    P.cyl(MAT_KNOB, (xc, 0, Z_HEAD + UNL_H - IN), (xc, 0, Z_HEAD + UNL_H + KNOB_H), KNOB_D / 2.0)             # its knob, fixed in 1.x
    P.collider("body", -px / 2.0, -py / 2.0, 0.0, px, py, Z_TOP)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="ports", az=320, el=15)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
