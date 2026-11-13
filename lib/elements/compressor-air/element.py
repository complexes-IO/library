#!/usr/bin/env python3
"""compressor-air: air compressor, a small trainer and workshop unit: one oil-free piston pump driven directly by a single-phase
motor on a 24 l horizontal receiver, with a pressure switch (automatic start and stop), a non-return valve, a spring safety valve,
a lever outlet valve with an NPT 1/4 port and a manual condensate drain. Generic (OPERATING.md 12, EM 2026-11-07): our own
vendor-neutral design of ETIM 10.0 EC002860 "Air compressor"; the class values it is designed to are in spec.md "## Class values"
(the electrical ones are class values, not a certification). The outlet port's name, series, unit and role come from
toolkit/pneu.py (D1, D7). 2.0 (review compressor-air-1.0.md finding 1): the outlet's bore is cut as the lane's other female NPT
ports are: Ø (E1 + h) (13.616 for NPT 1/4, the male stub's own diameter that fitting-pushin 2.0 and gauge-p draw; pneu.NPT, ASME
B1.20.1 by its formulas) and L2 + 2 deep (tank 2.0's rule), so a placed male touches the bore and never overlaps the valve body;
the thread itself is drawn plain. The outlet valve's body is 26 square round the bore (6.19 of wall, asserted), the number field 18
square, and the port pivot (gender female, PIN-002) sits on the field's outer face (filter-air 3.0's fix). The ratings the checks
read are in ratings.csv (finding 2). The supply cord and its plug come in a later version (spec.md, Notes). Every other size is a
design choice. No vendor file was opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "compressor-air", "2.0", "machine"
TITLE = "air compressor, generic, oil-free piston, 0.55 kW 120 V 60 Hz, 24 l receiver, 8 bar, outlet NPT 1/4"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic air compressor (ETIM 10.0 EC002860); class values in spec.md; outlet NPT 1/4 female (toolkit/pneu.py "
            "D1, ASME B1.20.1), numbered to ISO 11727 (pneu.NODES), bored plain at E1 + h, L2 + 2 deep (pneu.NPT); receiver, pump, "
            "motor and fittings are design choices")
ORIGIN = ("floor machine: floor plane z = 0; x = 0 at the receiver's left end, y = 0 on its front-most line; the receiver along +x, "
          "the body toward +y, the outlet facing -y")
COMMAND = "COMPRESSOR-AIR"
PARAMS = dict()

PORT = "NPT1/4"                    # design choice within pneu.THREADS (D1): class value "Connection size outlet"
TANK_D, TANK_X = 260.0, (15.0, 495.0)   # design choice: receiver shell Ø260 x 480; with a 2.5 wall it holds 24 l (class value)
TANK_WALL = 2.5                    # design choice: the shell's wall, for the capacity only (the receiver is modelled solid)
YC, ZT = TANK_D / 2, 170.0         # receiver axis: y = 130, z = 170 (its underside 40 above the floor)
DOME_D, DOME_L = 200.0, 15.0       # design choice: the dished ends, shown as a short Ø200 step at each end
FOOT_X, FOOT = (70.0, 400.0), (40.0, 10.0, 250.0, 15.0, 45.0)   # design choice: two foot brackets (x, width, y0, y1, z0, z1)
PAD_D, PAD_H, PAD_Y = 30.0, 15.0, (30.0, 230.0)   # design choice: rubber feet under the brackets
PLATE = (150.0, 410.0, 50.0, 210.0, 296.0, 306.0) # design choice: saddle plate on the receiver's top (x0, x1, y0, y1, z0, z1)
MOTOR_D, MOTOR_X, MOTOR_Z = 130.0, (170.0, 330.0), 381.0   # design choice: the motor's frame, its shaft along +x
MFEET = (190.0, 310.0, 85.0, 175.0, 306.0, 322.0)  # design choice: the motor's feet on the plate
FAN_D, FAN_X = 126.0, (140.0, 170.0)               # design choice: fan cover, the motor's left end
CRANK = (330.0, 410.0, 90.0, 170.0, 306.0, 430.0)  # design choice: crankcase, direct on the motor's shaft end
PX = 375.0                                          # the pump cylinder's axis, x (y = YC): its fins clear the motor's end (x 330)
BARREL_D, BARREL_Z = 70.0, (430.0, 490.0)          # design choice: the cylinder (bore 50, stroke 34: not modelled inside)
FIN_D, FIN_T, FIN_Z = 86.0, 3.0, (440.0, 452.0, 464.0, 476.0)   # design choice: cooling fins
HEAD = (337.0, 413.0, 92.0, 168.0, 490.0, 512.0)   # design choice: cylinder head, centred on the cylinder
INTAKE_D, INTAKE_H = 50.0, 28.0                    # design choice: intake filter on the head
PIPE_R, PIPE_X, PIPE_Z = 4.0, 430.0, 501.0         # design choice: delivery pipe, head to the non-return valve (Ø8 copper)
CHECKV = (418.0, 442.0, 118.0, 142.0, 296.0, 330.0)   # design choice: non-return valve on the receiver's top
MANI = (452.0, 492.0, 110.0, 150.0, 296.0, 330.0)     # design choice: outlet manifold on the receiver's top
SWITCH = (442.0, 502.0, 128.0, 192.0, 330.0, 400.0)   # design choice: pressure switch housing on the manifold
KNOB_D, KNOB_L, KNOB_XZ = 24.0, 12.0, (472.0, 368.0)  # design choice: the switch's rotary knob, off (0) to auto (90)
GRIP_R, GRIP_L, GRIP_YZ = 7.0, 12.0, (175.0, 350.0)   # design choice: cord grip on the switch's right face
OUTV = (459.0, 485.0, 78.0, 110.0, 300.0, 326.0)      # design choice: outlet valve body on the manifold's front face, 26 square (2.0)
_T = pneu.NPT[PORT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4      # 13.616 for NPT 1/4: the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # L2 (10.205) + 2: design choice, a run-out past the male's effective thread (tank 2.0)
FIELD, FIELD_T = 18.0, 0.2         # port-number field (decal), centred on the bore, 0.2 proud of the face (GEO-050); a ring round the bore
STEM_D, STEM_H = 6.0, 5.0          # design choice: the outlet valve's stem
ARM = (45.0, 6.0, 10.0, 3.0)       # design choice: outlet lever arm: reach, tail, width, thickness
NUT_D, NUT_H = 8.0, 3.0            # design choice: the lever's nut
SAFETY = (16.0, 20.0, 12.0, 6.0)   # design choice: safety valve body Ø16 x 20 and its cap Ø12 x 6, on the manifold's right face
DRAIN_X, BOSS, DRAIN = 255.0, (14.0, 12.0), (18.0, 8.0)   # design choice: drain boss Ø14 under the receiver, drain knob Ø18 x 8
TURN = 90.0                        # deg: the knob, the outlet lever and the drain each turn a quarter turn
LABEL = (200.0, 320.0, 150.0, 190.0, 3.2)          # complexes.org generic plate on the receiver's front (x0, x1, z0, z1, depth)
PUMP_BORE, PUMP_STROKE, SPEED = 50.0, 34.0, 1720.0  # design choices behind the class value "Piston displacement per minute"
BLUE, GREY, ALU, FIELDM = "M-BLUE", "M-STEEL-7035", "M-ALU-7035", "M-WHITE-PA"
assert PORT in pneu.THREADS and pneu.NPT[PORT]["length"]
assert BORE_L >= pneu.NPT[PORT]["engagement"]                                   # deeper than a male's make-up (L1 + L3)
assert min(OUTV[1] - OUTV[0], OUTV[5] - OUTV[4]) - BORE_D >= 2 * 6.0            # at least 6 of valve body round the bore (6.19)
assert OUTV[3] - OUTV[2] - BORE_L >= 15.0                                       # the bore blind: 19.8 of body behind its floor
assert FIELD > BORE_D + 2.0 and FIELD < min(OUTV[1] - OUTV[0], OUTV[5] - OUTV[4])   # the field rings the bore, inside the front face
assert MANI[0] <= OUTV[0] and OUTV[1] <= MANI[1] and MANI[4] <= OUTV[4] and OUTV[5] <= MANI[5]   # the body inside the manifold's front face
assert OUTV[5] + STEM_H + ARM[3] + NUT_H <= KNOB_XZ[1] - KNOB_D / 2 - 10.0      # the lever's nut 19 under the switch knob's lowest line
assert OUTV[4] - (ZT + math.sqrt((TANK_D / 2) ** 2 - (OUTV[3] - YC) ** 2)) >= 1.0   # the body 1.5 above the receiver's shell at its back edge

def capacity_l():
    """class value "Tank capacity": the shell's inside, Ø(260 - 2 x 2.5) over (480 - 2 x 2.5), in litres (the dished ends not counted)"""
    d, l = TANK_D - 2 * TANK_WALL, TANK_X[1] - TANK_X[0] - 2 * TANK_WALL
    return math.pi / 4 * d * d * l / 1e6

def displacement_l_min():
    """class value "Piston displacement per minute": swept volume x speed, in litres"""
    return math.pi / 4 * PUMP_BORE ** 2 * PUMP_STROKE * SPEED / 1e6

def _box(P, L, b): return P.box(L, b[0], b[2], b[4], b[1] - b[0], b[3] - b[2], b[5] - b[4])

def build():
    P = Prims()
    tank = P.cyl(BLUE, (TANK_X[0], YC, ZT), (TANK_X[1], YC, ZT), TANK_D / 2)                     # receiver shell
    P.cyl(BLUE, (TANK_X[0] - DOME_L, YC, ZT), (TANK_X[0], YC, ZT), DOME_D / 2)                   # dished ends
    P.cyl(BLUE, (TANK_X[1], YC, ZT), (TANK_X[1] + DOME_L, YC, ZT), DOME_D / 2)
    w, y0, y1, z0, z1 = FOOT
    for x in FOOT_X:                                                                            # foot brackets and rubber feet
        P.box(BLUE, x, y0, z0, w, y1 - y0, z1 - z0)
        for y in PAD_Y: P.cyl("M-GASKET", (x + w / 2, y, 0), (x + w / 2, y, PAD_H), PAD_D / 2)
    _box(P, BLUE, PLATE)                                                                        # saddle plate
    P.cyl(f"node:motor|{GREY}", (MOTOR_X[0], YC, MOTOR_Z), (MOTOR_X[1], YC, MOTOR_Z), MOTOR_D / 2)   # motor frame (node: the twin runs it)
    _box(P, f"node:motor|{GREY}", MFEET)
    P.cyl("node:motor|M-BLACK-PA", (FAN_X[0], YC, MOTOR_Z), (FAN_X[1], YC, MOTOR_Z), FAN_D / 2)
    P.pivot("motor", "fixed", (sum(MOTOR_X) / 2, YC, MOTOR_Z))
    _box(P, ALU, CRANK)                                                                         # the pump: crankcase, cylinder, fins, head
    P.cyl(ALU, (PX, YC, BARREL_Z[0]), (PX, YC, BARREL_Z[1]), BARREL_D / 2)
    for z in FIN_Z: P.cyl(ALU, (PX, YC, z), (PX, YC, z + FIN_T), FIN_D / 2)
    _box(P, ALU, HEAD)
    P.cyl("M-BLACK-PA", (PX, YC, HEAD[5]), (PX, YC, HEAD[5] + INTAKE_H), INTAKE_D / 2)          # intake filter
    P.cyl("M-CU", (HEAD[1], YC, PIPE_Z), (PIPE_X + PIPE_R, YC, PIPE_Z), PIPE_R)                 # delivery pipe, head to the non-return valve
    P.cyl("M-CU", (PIPE_X, YC, PIPE_Z + PIPE_R), (PIPE_X, YC, CHECKV[5]), PIPE_R)
    _box(P, "M-BRASS", CHECKV)                                                                  # non-return valve
    mani = _box(P, "M-BRASS", MANI)                                                             # outlet manifold
    _box(P, "M-GREY-PA", SWITCH)                                                                # pressure switch, automatic start / stop
    kx, kz = KNOB_XZ
    P.cyl("node:switch|M-RED-PA", (kx, SWITCH[2], kz), (kx, SWITCH[2] - KNOB_L, kz), KNOB_D / 2)
    P.pivot("switch", "rotate", (kx, SWITCH[2], kz), axis=(0, -1, 0), range=(0, TURN), unit="deg")   # 0 off, 90 auto
    gy, gz = GRIP_YZ
    P.cyl("M-BLACK-PA", (SWITCH[1], gy, gz), (SWITCH[1] + GRIP_L, gy, gz), GRIP_R)             # cord grip (the cord: a later version)
    body = _box(P, "M-BRASS", OUTV)                                                             # outlet valve and its port
    vx, vz = (OUTV[0] + OUTV[1]) / 2, (OUTV[4] + OUTV[5]) / 2; vy = OUTV[2]
    P.hole("M-GASKET", (vx, vy - 1.0, vz), (vx, vy + BORE_L, vz), BORE_D / 2, body)
    h = FIELD / 2; name = pneu.NODES["work"][0]
    f = P.box(f"node:{name}|{FIELDM}", vx - h, vy - FIELD_T, vz - h, FIELD, FIELD_T, FIELD)
    P.hole("M-GASKET", (vx, vy - FIELD_T - 1.0, vz), (vx, vy + 1.0, vz), BORE_D / 2, f)
    P.pivot(name, "port", (vx, vy - FIELD_T, vz), axis=(0, -1, 0), range=(0, 0), unit=PORT, gender="female", role="work")   # on the field's outer face
    sx, sy = vx, (OUTV[2] + OUTV[3]) / 2; s0 = OUTV[5]; s1 = s0 + STEM_H; s2 = s1 + ARM[3]
    P.cyl("node:lever|M-BRASS", (sx, sy, s0), (sx, sy, s1), STEM_D / 2)                         # stem, turns with the lever
    reach, tail, aw, at = ARM
    P.box("node:lever|M-RED-PA", sx - tail, sy - aw / 2, s1, reach + tail, aw, at)             # lever along +x: across the flow, closed
    P.cyl("node:lever|M-ZINC", (sx, sy, s2), (sx, sy, s2 + NUT_H), NUT_D / 2)
    P.pivot("lever", "rotate", (sx, sy, s0), axis=(0, 0, -1), range=(0, TURN), unit="deg")     # +90 about -z: +x to -y, along the flow: open
    sd, sl, cd, cl = SAFETY; sz = (MANI[4] + MANI[5]) / 2 - 4.0
    P.cyl("M-BRASS", (MANI[1], YC, sz), (MANI[1] + sl, YC, sz), sd / 2)                         # spring safety valve
    P.cyl("M-BRASS", (MANI[1] + sl, YC, sz), (MANI[1] + sl + cl, YC, sz), cd / 2)
    zb = ZT - TANK_D / 2
    P.cyl("M-BRASS", (DRAIN_X, YC, zb + 4.0), (DRAIN_X, YC, zb - BOSS[1] + 4.0), BOSS[0] / 2)   # drain boss under the receiver
    zd = zb - BOSS[1] + 4.0
    P.cyl("node:drain|M-RED-PA", (DRAIN_X, YC, zd), (DRAIN_X, YC, zd - DRAIN[1]), DRAIN[0] / 2)  # condensate drain, quarter turn
    P.pivot("drain", "rotate", (DRAIN_X, YC, zd), axis=(0, 0, -1), range=(0, TURN), unit="deg")
    lx0, lx1, lz0, lz1, ld = LABEL
    P.box(FIELDM, lx0, -FIELD_T, lz0, lx1 - lx0, ld, lz1 - lz0)                                # complexes.org generic plate, 0.2 proud
    xmax = max(MANI[1] + sl + cl, sx + reach)
    P.collider("env", 0.0, -FIELD_T, 0.0, xmax, TANK_D + FIELD_T, HEAD[5] + INTAKE_H)
    return P

def envelope():
    """class values Width, Height, Depth (cm): the built extents, the outlet lever closed"""
    from toolkit.prims import extents
    lo, hi = extents(build())
    return tuple(round((hi[i] - lo[i]) / 10.0, 1) for i in range(3))

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="outlet end", az=300, el=25),
            dict(name="back three-quarter", az=60, el=30)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
