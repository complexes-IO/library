#!/usr/bin/env python3
"""gear-reducer: worm gear reducer, foot mounted, our own design (OPERATING.md 12, own designs; lib/inventory.csv row "gear-reducer",
own_design yes, 8 systems: bender-section, mechanisms-bench, positioner-welding, roll-plate, rotary-index-table, rotator-welding,
saw-band-auto, saw-circular-metal; request mech-13's answer: no gearbox class on file, the ratio a design figure and a parameter,
output torque, efficiency and service factor not claimed, the input meets motor-iec71-370w). A single-stage worm reducer in a
closed housing on its own base plate: the input (worm) shaft along y, at the motor's shaft height over the same floor so a coupling
(coupling-shaft, not built) joins the two shafts on one axis; the output (wheel) shaft along x, the centre distance above it. The
worm and the wheel inside the housing are not drawn (internal, class C): the housing is drawn by its outside with the two shafts'
bores. Both shafts are nodes (`input`, `output`), each turning about its own axis; the output turns 1 / ratio of the input's turn.
The motor on file (motor-iec71-370w) is a B3 foot motor with no flange, so the input meets its shaft through the coupling, not a
flange: the input shaft is drawn at the motor shaft's Ø14 x 30 and its axis at the motor's shaft height, both read from that
element (library.load / its drawing p. 1 figures). The keys and keyways of both shafts are not drawn: a parallel key's section and
keyway depths are tabulated by DIN 6885-1, not on file (spec.md What it meets). Every other size is a design choice. No vendor
file was opened; the folder's catalogue record (another maker's product) is not used."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "gear-reducer", "1.0", "machine"
TITLE = "worm gear reducer, foot mounted, input shaft Ø14 x 30 at motor-iec71-370w's shaft height, output shaft Ø20 x 40, centre distance 40, 4 x M8 foot holes"
TOOLKIT = "1.3"
BASELINE = ("our own design: worm gear reducer (no gearbox class on file, request mech-13's answer), the input shaft and its axis "
            "height read from motor-iec71-370w so a coupling joins them on one axis; foot holes M8 in ISO 273 medium clearance; the "
            "ratio a design figure and a parameter; the worm, the wheel, the bearings and seals not drawn; the shafts' keys and "
            "keyways not drawn (DIN 6885-1 not on file); every size a design choice; no torque, efficiency, speed or service "
            "factor claimed; no vendor file opened")
ORIGIN = ("the floor plane (z = 0, the base plate's underside); x = 0 the plane through the input shaft's axis, y = 0 the plane "
          "through the output shaft's axis; the input shaft runs along y at z 71 and comes out toward -y, the output shaft runs "
          "along x at z 111 and comes out toward +x")
COMMAND = "GEARREDUCER"
PARAMS = dict(ratio=20.0)

MOTOR = library.load("motor-iec71-370w")    # the motor this design meets (placed by the assembly): its shaft height
MOTOR_SHAFT_R, MOTOR_SHAFT_L = 7.0, 30.0    # its shaft Ø14 x 30 past the drive-end shield (motor-iec71-370w element.py, from its drawing p. 1)

ZI = MOTOR.SH                               # 71: the input axis over the floor = the motor's shaft height, so both stand on one plane
A = 40.0                                    # centre distance between the worm (input) and the wheel (output) axes (design choice)
ZO = ZI + A                                 # 111: the output axis, the worm under the wheel (design choice)
RATIO_MIN, RATIO_MAX = 5.0, 100.0           # the range of a single worm stage this housing is drawn for (design choice)

BASE_X, BASE_Y, BASE_T = 75.0, 65.0, 16.0   # base plate x +-75, y +-65, 16 thick (design choice)
HOLE_X, HOLE_Y = 60.0, 50.0                 # 4 x M8 foot holes at 120 x 100, 15 in from the plate's edges
M8_CLR = 9.0                                # ISO 273 medium (H13): lib/standards/holes.csv
BODY_X, BODY_Y, BODY_TOP = 45.0, 50.0, 160.0  # housing body x +-45, y +-50, from the base plate to z 160 (design choice)
IN_BOSS_R, IN_BOSS_L, IN_CAP_L = 28.0, 12.0, 8.0   # input bearing boss Ø56 x 12 on the -y face, cover Ø56 x 8 on the +y face
OUT_BOSS_R, OUT_BOSS_L = 32.0, 12.0         # output bearing bosses Ø64 x 12 on both x faces
IN_BORE_R, IN_BORE_DEPTH = 8.0, 30.0        # the input shaft's bore Ø16 through the boss and 30 into the body (bearings not drawn)
OUT_BORE_R = 11.0                           # the output shaft's bore Ø22 through both bosses and the body
OUT_R, OUT_L = 10.0, 40.0                   # output shaft Ø20, 40 past the +x boss's face (design choice)
IN_INNER, OUT_INNER = 5.0, 2.0              # the input shaft's inner end 5 short of its bore's end; the output's 2 inside the -x boss's face
MAT, MAT_SHAFT = "M-CAST-BLUE", "M-SILVER"

Y_IN_FACE = -BODY_Y - IN_BOSS_L             # -62: the input boss's face
X_OUT_FACE = BODY_X + OUT_BOSS_L            # 57: the output bosses' faces (+-)

assert abs(ZI - 71.0) < 1e-9 and abs(ZO - 111.0) < 1e-9
assert ZI - IN_BOSS_R > BASE_T + 10.0                                           # the input boss stands 27 clear of the base plate
assert ZO + OUT_BOSS_R < BODY_TOP and ZO - OUT_BOSS_R > BASE_T + 10.0           # the output bosses inside the body's height
assert ZI + IN_BORE_R < ZO - OUT_BORE_R - 10.0                                  # the two bores 21 apart: the worm and the wheel are inside
assert MOTOR_SHAFT_R < IN_BORE_R and OUT_R < OUT_BORE_R                          # both shafts touch nothing (1 radial clearance)
assert HOLE_X - M8_CLR / 2 > BODY_X + 10.0 and BASE_X - HOLE_X - M8_CLR / 2 >= 10.0   # the foot holes clear the body by 10.5, 10.5 of edge
assert BASE_Y - HOLE_Y - M8_CLR / 2 >= 10.0


def build(ratio=20.0):
    r = float(ratio)
    assert RATIO_MIN <= r <= RATIO_MAX, f"ratio {r}: a single worm stage in this housing takes {RATIO_MIN:g} to {RATIO_MAX:g} (design choice)"
    P = Prims()
    base = P.box(MAT, -BASE_X, -BASE_Y, 0.0, 2 * BASE_X, 2 * BASE_Y, BASE_T)                                      # base plate (the feet)
    for x in (-HOLE_X, HOLE_X):
        for y in (-HOLE_Y, HOLE_Y):
            P.hole(MAT, (x, y, -1.0), (x, y, BASE_T + 1.0), M8_CLR / 2, base)                                    # 4 x M8 foot holes, ISO 273 medium
    body = P.box(MAT, -BODY_X, -BODY_Y, BASE_T, 2 * BODY_X, 2 * BODY_Y, BODY_TOP - BASE_T)                       # housing body
    P.hole(MAT, (0, -BODY_Y - 1.0, ZI), (0, -BODY_Y + IN_BORE_DEPTH, ZI), IN_BORE_R, body)                      # input bore into the body
    P.hole(MAT, (-BODY_X - 1.0, 0, ZO), (BODY_X + 1.0, 0, ZO), OUT_BORE_R, body)                               # output bore through the body
    ib = P.cyl(MAT, (0, Y_IN_FACE, ZI), (0, -BODY_Y, ZI), IN_BOSS_R)                                            # input bearing boss
    P.hole(MAT, (0, Y_IN_FACE - 1.0, ZI), (0, -BODY_Y + 1.0, ZI), IN_BORE_R, ib)
    P.cyl(MAT, (0, BODY_Y, ZI), (0, BODY_Y + IN_CAP_L, ZI), IN_BOSS_R)                                          # input end cover (closed)
    for s in (-1, 1):                                                                                          # output bearing bosses
        ob = P.cyl(MAT, (s * BODY_X, 0, ZO), (s * X_OUT_FACE, 0, ZO), OUT_BOSS_R)
        P.hole(MAT, (s * (BODY_X - 1.0), 0, ZO), (s * (X_OUT_FACE + 1.0), 0, ZO), OUT_BORE_R, ob)
    P.cyl(f"node:input|{MAT_SHAFT}", (0, -BODY_Y + IN_BORE_DEPTH - IN_INNER, ZI), (0, Y_IN_FACE - MOTOR_SHAFT_L, ZI), MOTOR_SHAFT_R)  # input shaft Ø14
    P.pivot("input", "rotate", (0, Y_IN_FACE, ZI), axis=(0, -1, 0), range=(0, 360))
    P.cyl(f"node:output|{MAT_SHAFT}", (-(X_OUT_FACE - OUT_INNER), 0, ZO), (X_OUT_FACE + OUT_L, 0, ZO), OUT_R)  # output shaft Ø20
    P.pivot("output", "rotate", (X_OUT_FACE, 0, ZO), axis=(1, 0, 0), range=(0, 360))
    P.collider("base-plate", -BASE_X, -BASE_Y, 0.0, 2 * BASE_X, 2 * BASE_Y, BASE_T)
    P.collider("housing", -X_OUT_FACE, Y_IN_FACE, BASE_T, 2 * X_OUT_FACE, 2 * BODY_Y + IN_CAP_L + IN_BOSS_L, BODY_TOP - BASE_T)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="input", az=270, el=10), dict(name="output", az=0, el=15)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
