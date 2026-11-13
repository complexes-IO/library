#!/usr/bin/env python3
"""hyd-pump: an external gear pump for a hydraulic power unit: a drive gear on the shaft and a driven gear below it turn in the body,
drawing oil in at the suction port on one side and delivering it out of the pressure port on the other. It is flange mounted: its
two-bolt flange and pilot go on a bell housing (the motor bracket) and its shaft takes the coupling to the motor. lib/inventory.csv
row `hyd-pump` (own_design generic, "hydraulic pump (gear or piston)"; 1 system, hpu-assembly-station, whose line in
lib/machines-factory.txt places it with hyd-tank, motor-iec, hyd-valve-d03, hyd-filter-return, hyd-cooler, accumulator and hyd-gauge).
Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC012031 "Gear pump" (group EG020079 Pumps, tier 2,
synonym "Hydraulic gear pump"), the class lib/standards/etim/classes.csv gives for it; the row names no class. Its features are not in
class-features.csv (tier 2, on no inventory row: the case of request pneu-4, lib/requests/core/pneu-4-answer.md), so spec.md's Class
values gives the design values under plain names, as pump-hand-hyd 1.0's. No vendor file was opened.
The mounting flange's interface (pilot, bolt pattern) and the shaft end are a standard's (ISO 3019-1 / SAE J744), not on file: drawn
as design choices with the fit open (class B, spec.md Open figures); the flange's two holes are M10 clearance, medium (ISO 273,
lib/standards/holes.csv), the screws the host's. The two oil ports are plain spot faces on the body's sides, unit "hyd-port" (the lane's
placeholder, as hpu-7.5kw's, hold-down's and pump-hand-hyd's), their threads open (class B, not drawn). One moving part: the shaft
(`shaft`, rotate about +x, its own axis: positive is clockwise seen on the shaft end, the pump's turning direction). The gears, bearings and seals inside are not modelled."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "hyd-pump", "1.0", "device"
TITLE = "hydraulic gear pump, generic, external gear, two-bolt flange mounted, side ports"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic gear pump (ETIM 10.0 EC012031), an external gear pump for a hydraulic power unit (inventory "
            "own_design generic); design values in spec.md; flange holes M10 clearance (ISO 273 medium, lib/standards/holes.csv); the "
            "flange and shaft interface, the port threads and the max. pressure not on file (classes B, B and A, spec.md Open figures); "
            "flange, pilot, shaft, body and cover are design choices; no vendor file opened")
ORIGIN = ("the mounting face: the flange's front face (x = 0), y = 0 and z = 0 on the shaft's axis; the shaft and pilot toward -x, "
          "the body toward +x, the suction port on +y, the pressure port on -y")
COMMAND = "HYD-PUMP"
PARAMS = dict()

FL_T, FL_W, FL_H = 10.0, 116.0, 50.0                  # design choices: the two-bolt flange, 10 thick, 116 wide (y), 50 high (z)
HOLE_D, HOLE_Y = 11.0, 45.0                           # M10 clearance, medium (ISO 273 H13: 11.0 to 11.27; holes.csv); 90 apart (design)
PILOT_D, PILOT_L = 50.0, 6.0                          # design choice: the pilot (spigot) on the mounting face, Ø50 x 6
SHAFT_D, SHAFT_L = 16.0, 30.0                         # design choice: the drive shaft, Ø16, 30 out of the pilot, plain (no key drawn)
BODY_X, BODY_Y, BODY_Z = (10.0, 74.0), 35.0, (-50.0, 30.0)   # design choices: the gear body, x 10 to 74, y ±35, z -50 to 30
GEAR_PITCH = 24.0                                     # design choice: the driven gear's axis 24 below the drive gear's (not modelled)
COVER_X, COVER_IN = 86.0, 2.0                         # design choice: the rear cover to x = 86, 2 in from the body's sides
PORT_X = (BODY_X[0] + BODY_X[1]) / 2                  # 42: both ports mid-body, at the gears' mesh
PORT_Z = -GEAR_PITCH / 2                              # -12: the mesh, between the two gears' axes
SPOT_S, SPOT_P, SPOT_T = 40.0, 32.0, 1.0              # design choices: spot faces, suction Ø40 (the larger port) and pressure Ø32, 1 proud
IN = 0.5                                              # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_BODY, MAT_SHAFT, MAT_SPOT = "M-ALU-ANOD", "M-ZINC", "M-STEEL-7035"

assert FL_W / 2 > BODY_Y and FL_H / 2 < BODY_Z[1] and -FL_H / 2 > BODY_Z[0]   # the flange wider than the body, inside its height: no flush face
assert HOLE_Y - HOLE_D / 2 - BODY_Y >= 4.0            # 4.5 between a hole's edge and the body's side (a nut's room behind the flange)
assert FL_W / 2 - HOLE_Y - HOLE_D / 2 >= 5.0 and FL_H / 2 - HOLE_D / 2 >= 15.0   # plate past each hole
assert HOLE_Y - HOLE_D / 2 > PILOT_D / 2 + 10.0       # the holes clear the pilot
assert SHAFT_D < PILOT_D - 20.0
for d in (SPOT_S, SPOT_P):                            # each spot face inside its side face, clear of the flange and the cover
    assert PORT_X - d / 2 >= BODY_X[0] + 5.0 and PORT_X + d / 2 <= BODY_X[1] - 5.0
    assert PORT_Z - d / 2 >= BODY_Z[0] + 5.0 and PORT_Z + d / 2 <= BODY_Z[1] - 5.0


def build():
    P = Prims(); hw = FL_W / 2; hh = FL_H / 2
    fl = P.box(MAT_BODY, 0.0, -hw, -hh, FL_T + IN, FL_W, FL_H)                                       # flange, 0.5 into the body
    for y in (-HOLE_Y, HOLE_Y):
        P.hole(MAT_BODY, (-1.0, y, 0.0), (FL_T + IN + 1.0, y, 0.0), HOLE_D / 2, fl)                 # M10 clearance, through
    P.cyl(MAT_BODY, (IN, 0, 0), (-PILOT_L, 0, 0), PILOT_D / 2)                                       # pilot, 0.5 into the flange
    P.cyl(f"node:shaft|{MAT_SHAFT}", (-PILOT_L, 0, 0), (-PILOT_L - SHAFT_L, 0, 0), SHAFT_D / 2)       # shaft, face to face on the pilot
    P.pivot("shaft", "rotate", (-PILOT_L, 0, 0), axis=(1, 0, 0), range=(0, 360), unit="deg")      # + = clockwise seen on the shaft end
    P.box(MAT_BODY, BODY_X[0], -BODY_Y, BODY_Z[0], BODY_X[1] - BODY_X[0], 2 * BODY_Y, BODY_Z[1] - BODY_Z[0])   # gear body
    cy, z0, z1 = BODY_Y - COVER_IN, BODY_Z[0] + COVER_IN, BODY_Z[1] - COVER_IN
    P.box(MAT_BODY, BODY_X[1] - IN, -cy, z0, COVER_X - BODY_X[1] + IN, 2 * cy, z1 - z0)            # rear cover, 0.5 into the body
    for node, s, d, role in (("port-s", 1, SPOT_S, None), ("port-p", -1, SPOT_P, "supply")):         # suction (+y), pressure (-y)
        y0, y1 = s * (BODY_Y - IN), s * (BODY_Y + SPOT_T)
        P.cyl(f"node:{node}|{MAT_SPOT}", (PORT_X, y0, PORT_Z), (PORT_X, y1, PORT_Z), d / 2)
        kw = dict(role=role) if role else {}
        P.pivot(node, "port", (PORT_X, y1, PORT_Z), axis=(0, s, 0), range=(0, 0), unit="hyd-port", gender="female", **kw)
    x0 = -PILOT_L - SHAFT_L
    P.collider("env", x0, -hw, BODY_Z[0], COVER_X - x0, FL_W, BODY_Z[1] - BODY_Z[0])
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="suction side", az=60, el=15), dict(name="pressure side", az=300, el=15)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
