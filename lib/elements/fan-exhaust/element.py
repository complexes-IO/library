#!/usr/bin/env python3
"""fan-exhaust: exhaust (extraction) fan, centrifugal, our own vendor-neutral design of the ETIM 10.0 class EC010994 (Centrifugal
fan), built unattended (OPERATING.md 12, generic elements; lib/inventory.csv row "fan-exhaust", own_design generic, 8 systems:
booth-paint, booth-powder, booth-spray-paint, dust-collection-system, fume-extraction-system, hvac-trainer, powder-coating-system,
ventilation-industrial; request mech-13's answer: generic of EC010994, built under plain names as conveyor-wheel because the class's
56 features are not on file). The fan that draws air out of a booth, a dust collector or a fume hood: a steel housing (the scroll
drawn as a drum, its spiral not drawn: appearance, class C) on a base plate, the inlet on its -y face with a round collar for the
duct, the discharge a rectangular duct straight up from the top with a flange for the exhaust duct, and inside an open
radial-bladed impeller on its own shaft, node `impeller`, turning about the horizontal y axis. The shaft runs back through the
housing's back wall and a bearing stand (the bearings not drawn: internal, class C) to a free end where a coupling (coupling-shaft,
not built) meets the motor; the motor (motor-iec71-370w, on file but not past station 6) is placed later on a seat drilled to its
foot pattern and set to its shaft height, both read from that element (library.load). The class values (spec.md "Class values")
are design inputs; the flow's power at the duty point is computed, below the seated motor's output. Every size below is a design
choice. No vendor file was opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "fan-exhaust", "1.1", "machine"
TITLE = "exhaust fan, centrifugal, generic, impeller Ø480, inlet Ø250, discharge 200 x 230 up, motor seat for motor-iec71-370w, 4 x M12 anchor holes"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic centrifugal fan (ETIM 10.0 EC010994), an exhaust fan with the motor placed later; class values "
            "are design inputs under plain names until the class's features are on file (spec.md); anchor holes M12 and flange holes "
            "M8 in ISO 273 medium clearance; the motor seat's M6 tapped holes at their derived minor diameter (ISO 68-1, ISO 965-1) on "
            "motor-iec71-370w's foot pattern and shaft height; the scroll drawn as a drum; every size a design choice; no flow, "
            "pressure, noise or safety claim beyond the class values; no vendor file opened")
ORIGIN = ("the floor plane (z = 0, the base plate's underside) on the shaft's axis line: x = 0 through the shaft's axis, y = 0 at the "
          "housing's back face; the shaft runs along y at z 420, the inlet opens toward -y, the motor stands at +y, the discharge points up")
COMMAND = "FANEXHAUST"
PARAMS = dict()

MOTOR = library.load("motor-iec71-370w")    # the motor this design seats (placed later): its shaft height, foot pattern and drive-end shield
MOTOR_SHAFT_L = 30.0                        # its shaft Ø14 x 30 past the drive-end shield (motor-iec71-370w element.py, from its drawing p. 1)

ZC = 420.0                                  # the shaft's axis height over the floor (design choice: the drum's underside 120 up, room for the support)
BASE_X, BASE_Y0, BASE_Y1, BASE_T = 350.0, -360.0, 540.0, 15.0   # base plate x +-350, y -360..540, 15 thick (design choice)
R_DRUM, Y_FRONT, Y_BACK = 300.0, -250.0, 0.0                    # the housing drum Ø600 x 250 wide (design choice: the scroll's envelope)
R_CAV, WALL = 280.0, 15.0                   # the cavity Ø560 inside it, the back wall 15 thick
PLATE_T, R_INLET = 15.0, 125.0              # the inlet plate on the -y face, 15 thick, the inlet Ø250 (design choice: the duct's size)
COLLAR_R, COLLAR_L = 135.0, 60.0            # the inlet collar Ø270 x 60 (10 wall) the inlet duct slides over (design choice)
SUP_X, SUP_IN = 150.0, 5.0                  # the drum's support block x +-150, y -240..-10, its top 5 into the drum's underside
DUCT_X, DUCT_Y0, DUCT_Y1, DUCT_W = 100.0, -240.0, -10.0, 10.0  # the discharge duct 200 x 230 outside, 10 walls (design choice)
DUCT_Z0, DUCT_Z1 = 701.0, 860.0             # its foot 1 above the cavity's top (z 700), inside the drum's shell; its top 860
FL_X, FL_Y0, FL_Y1, FL_T = 130.0, -270.0, 20.0, 15.0           # the discharge flange 260 x 290 x 15 (design choice)
FL_HOLE_X, FL_HOLE_Y = 115.0, (-255.0, 5.0)                     # 4 x M8 flange holes, 15 in from the flange's edges
M8_CLR, M12_CLR = 9.0, 13.5                 # ISO 273 medium (H13): lib/standards/holes.csv
ANCHOR_X, ANCHOR_Y = 310.0, (-320.0, 500.0)  # 4 x M12 anchor holes, 40 in from the base plate's edges
R_IMP, IMP_T, R_HUB = 240.0, 10.0, 50.0     # impeller back disc Ø480 x 10, hub Ø100 (design choice)
IMP_Y = -55.0                               # the back disc y -55..-45, its -y face toward the inlet carrying the blades; the hub y -50..-25
BLADES, BLADE_R0, BLADE_T, BLADE_L = 8, 100.0, 3.0, 145.0       # 8 straight radial blades, r 100..235, 3 thick, y -55..-200 (design choice)
BLADE_R1 = 235.0
R_SHAFT, SHAFT_END = 12.0, 200.0            # the fan's shaft Ø24 from the hub to its free end at y 200 (design choice)
R_WALL_BORE, R_STAND_BORE = 20.0, 13.0      # the shaft's clearance through the back wall and the bearing stand (bearings not drawn)
STAND_X, STAND_Y0, STAND_Y1, STAND_TOP = 60.0, 40.0, 120.0, 460.0  # the bearing stand 120 x 80, up to 40 over the axis (design choice)
COUPLING_GAP = 40.0                         # between the fan's shaft end and the motor's: the coupling's room (coupling-shaft, placed later)
SEAT_X, SEAT_Y0, SEAT_Y1 = 100.0, 300.0, 500.0                  # the motor seat 200 x 200 (design choice), its top at the motor's shaft height
TAP6_D1, TAP6_DEPTH = 4.9175, 12.0          # 4 x M6 tapped holes at D1 (6H min), 12 deep: derived: derive.thread(6.0, 1.0); K = 7 feet take M6
MAT, MAT_IMP = "M-STEEL-7035", "M-SILVER"

Y_MOTOR_SHAFT_END = SHAFT_END + COUPLING_GAP                    # 240: the motor's shaft end
Y_MOTOR = Y_MOTOR_SHAFT_END - MOTOR.Y_DE + MOTOR_SHAFT_L        # 350: the motor's front foot-hole row (its origin's y)
SEAT_TOP = ZC - MOTOR.SH                                        # 349: the motor's foot plane, its shaft then on this axis
MOTOR_HOLES = [(sx * MOTOR.HX / 2, Y_MOTOR + dy) for sx in (-1, 1) for dy in (0.0, MOTOR.HY)]   # (+-56, 350 / 440)

FLOW_M3H, PRESSURE_PA = 1200.0, 600.0       # the duty point: volume flow and pressure increase (class values, design inputs)
MOTOR_KW = 0.37                             # the seated motor's rated output (motor-iec71-370w's title)


def air_power_w():
    """the flow's power at the duty point, q_v x delta p: 1200 m3/h = 0.333 m3/s at 600 Pa = 200 W"""
    return FLOW_M3H / 3600.0 * PRESSURE_PA


assert abs(air_power_w() - 200.0) < 1e-6 and air_power_w() < MOTOR_KW * 1000.0          # the duty point's power sits below the motor's output
assert BLADE_R1 < R_CAV - 40.0 and R_IMP <= R_CAV - 40.0                                  # 45 / 40 clear of the drum's cavity
assert IMP_Y - BLADE_L > Y_FRONT + 40.0                                                   # the blades' front edges (y -200) 50 clear of the inlet plate
assert (Y_BACK - WALL) - (IMP_Y + 30.0) >= 10.0                                           # the hub's back face (y -25) 10 clear of the back wall (y -15)
assert R_INLET < BLADE_R1 and R_INLET > BLADE_R0                                          # the inlet looks onto the blades' inner part
assert ZC + math.sqrt(R_DRUM ** 2 - DUCT_X ** 2) > DUCT_Z0 > ZC + R_CAV                   # the duct's foot sits in the drum's shell, not the cavity
assert FL_HOLE_X - M8_CLR / 2 > DUCT_X + 5.0 and FL_X - FL_HOLE_X - M8_CLR / 2 >= 10.0     # the flange holes clear the duct and keep 10 of edge
assert SEAT_TOP > BASE_T + 100.0 and abs(SEAT_TOP - 349.0) < 1e-9 and abs(Y_MOTOR - 350.0) < 1e-9
assert all(abs(x) + TAP6_D1 / 2 < SEAT_X - 20.0 and SEAT_Y0 + 20 < y < SEAT_Y1 - 20 for x, y in MOTOR_HOLES)
assert R_SHAFT < R_STAND_BORE < R_WALL_BORE and STAND_Y1 < SHAFT_END < SEAT_Y0


def build():
    P = Prims()
    P.box(MAT, -BASE_X, BASE_Y0, 0.0, 2 * BASE_X, BASE_Y1 - BASE_Y0, BASE_T)                                   # base plate
    base = 0
    for x in (-ANCHOR_X, ANCHOR_X):
        for y in ANCHOR_Y:
            P.hole(MAT, (x, y, -1.0), (x, y, BASE_T + 1.0), M12_CLR / 2, base)                                  # 4 x M12 anchor holes, ISO 273 medium
    z_drum0 = ZC - R_DRUM
    P.box(MAT, -SUP_X, Y_FRONT + 10.0, BASE_T, 2 * SUP_X, (Y_BACK - 10.0) - (Y_FRONT + 10.0), z_drum0 + SUP_IN - BASE_T)   # drum support
    drum = P.cyl(MAT, (0, Y_FRONT, ZC), (0, Y_BACK, ZC), R_DRUM)                                               # housing drum
    P.hole(MAT, (0, Y_FRONT - 1.0, ZC), (0, Y_BACK - WALL, ZC), R_CAV, drum)                                   # its cavity, open toward -y
    P.hole(MAT, (0, Y_BACK - WALL - 1.0, ZC), (0, Y_BACK + 1.0, ZC), R_WALL_BORE, drum)                        # the shaft's way through the back wall
    plate = P.cyl(MAT, (0, Y_FRONT - PLATE_T, ZC), (0, Y_FRONT, ZC), R_DRUM)                                   # inlet plate on the drum's rim
    P.hole(MAT, (0, Y_FRONT - PLATE_T - 1.0, ZC), (0, Y_FRONT + 1.0, ZC), R_INLET, plate)                      # the inlet Ø250
    y_c1 = Y_FRONT - PLATE_T
    collar = P.cyl(MAT, (0, y_c1 - COLLAR_L, ZC), (0, y_c1, ZC), COLLAR_R)                                      # inlet collar
    P.hole(MAT, (0, y_c1 - COLLAR_L - 1.0, ZC), (0, y_c1 + 1.0, ZC), R_INLET, collar)
    duct = P.box(MAT, -DUCT_X, DUCT_Y0, DUCT_Z0, 2 * DUCT_X, DUCT_Y1 - DUCT_Y0, DUCT_Z1 - DUCT_Z0)               # discharge duct
    P.cutbox(MAT, -DUCT_X + DUCT_W, DUCT_Y0 + DUCT_W, DUCT_Z0 - 1.0, 2 * (DUCT_X - DUCT_W), DUCT_Y1 - DUCT_Y0 - 2 * DUCT_W, DUCT_Z1 - DUCT_Z0 + 2.0, duct)
    fl = P.box(MAT, -FL_X, FL_Y0, DUCT_Z1, 2 * FL_X, FL_Y1 - FL_Y0, FL_T)                                       # discharge flange
    P.cutbox(MAT, -DUCT_X + DUCT_W, DUCT_Y0 + DUCT_W, DUCT_Z1 - 1.0, 2 * (DUCT_X - DUCT_W), DUCT_Y1 - DUCT_Y0 - 2 * DUCT_W, FL_T + 2.0, fl)
    for x in (-FL_HOLE_X, FL_HOLE_X):
        for y in FL_HOLE_Y:
            P.hole(MAT, (x, y, DUCT_Z1 - 1.0), (x, y, DUCT_Z1 + FL_T + 1.0), M8_CLR / 2, fl)                    # 4 x M8 flange holes, ISO 273 medium
    stand = P.box(MAT, -STAND_X, STAND_Y0, BASE_T, 2 * STAND_X, STAND_Y1 - STAND_Y0, STAND_TOP - BASE_T)        # bearing stand
    P.hole(MAT, (0, STAND_Y0 - 1.0, ZC), (0, STAND_Y1 + 1.0, ZC), R_STAND_BORE, stand)
    seat = P.box(MAT, -SEAT_X, SEAT_Y0, BASE_T, 2 * SEAT_X, SEAT_Y1 - SEAT_Y0, SEAT_TOP - BASE_T)               # motor seat
    for x, y in MOTOR_HOLES:
        P.hole(MAT, (x, y, SEAT_TOP + 1.0), (x, y, SEAT_TOP - TAP6_DEPTH), TAP6_D1 / 2, seat)                   # 4 x M6 tapped, the motor's feet
    N = f"node:impeller|{MAT_IMP}"                                                                              # the impeller on its shaft
    P.cyl(N, (0, IMP_Y, ZC), (0, IMP_Y + IMP_T, ZC), R_IMP)                                                     # back disc
    P.cyl(N, (0, IMP_Y + 5.0, ZC), (0, IMP_Y + 30.0, ZC), R_HUB)                                                # hub, toward the back wall
    P.cyl(N, (0, IMP_Y + 15.0, ZC), (0, SHAFT_END, ZC), R_SHAFT)                                                # shaft to its free end
    for k in range(BLADES):                                                                                    # blades on the back disc's front face
        a = 2 * math.pi * k / BLADES; ex = (math.cos(a), 0.0, math.sin(a)); ez = (math.sin(a), 0.0, -math.cos(a))   # ez = ex x ey (ey = -y)
        o = (BLADE_R0 * ex[0] - BLADE_T / 2 * ez[0], IMP_Y, ZC + BLADE_R0 * ex[2] - BLADE_T / 2 * ez[2])     # blade y -55..-200, centred on its radial line (1.1)
        P.obox(N, o, ex, (0.0, -1.0, 0.0), ez, BLADE_R1 - BLADE_R0, BLADE_L, BLADE_T)
    P.pivot("impeller", "rotate", (0, IMP_Y, ZC), axis=(0, 1, 0), range=(0, 360))
    P.collider("base-plate", -BASE_X, BASE_Y0, 0.0, 2 * BASE_X, BASE_Y1 - BASE_Y0, BASE_T)
    P.collider("housing", -R_DRUM, Y_FRONT - PLATE_T, z_drum0, 2 * R_DRUM, Y_BACK - Y_FRONT + PLATE_T, 2 * R_DRUM)
    P.collider("inlet", -COLLAR_R, y_c1 - COLLAR_L, ZC - COLLAR_R, 2 * COLLAR_R, COLLAR_L, 2 * COLLAR_R)
    P.collider("discharge", -FL_X, FL_Y0, DUCT_Z0, 2 * FL_X, FL_Y1 - FL_Y0, DUCT_Z1 + FL_T - DUCT_Z0)
    P.collider("support", -SUP_X, Y_FRONT + 10.0, BASE_T, 2 * SUP_X, Y_BACK - Y_FRONT - 20.0, z_drum0 - BASE_T)
    P.collider("bearing-stand", -STAND_X, STAND_Y0, BASE_T, 2 * STAND_X, STAND_Y1 - STAND_Y0, STAND_TOP - BASE_T)
    P.collider("motor-seat", -SEAT_X, SEAT_Y0, BASE_T, 2 * SEAT_X, SEAT_Y1 - SEAT_Y0, SEAT_TOP - BASE_T)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="inlet", az=270, el=10), dict(name="drive", az=60, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
