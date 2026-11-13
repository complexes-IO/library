#!/usr/bin/env python3
"""damper: a rectangular multi-blade air damper, our own design (OPERATING.md 12, own designs; inventory row own_design "yes": "our own
design (core watch 2026-11-12, request mech-13): no air damper class on file (EC003372 Flap valve is a fluid valve); no airflow or
leakage rating claimed"; 2 systems, hvac-trainer and ventilation-industrial). It sits on fan-exhaust's discharge flange and sets how
much air the fan pushes up the exhaust duct: a short galvanized casing the size of the fan's discharge duct (200 x 230 outside, 10
walls), a bottom flange drilled to the fan's flange pattern (read from fan-exhaust with library.load, so the two cannot drift apart)
and a top flange drilled the same for the exhaust duct, and inside three flat blades, each on its own axle across the casing, each
its own node (blade-1 .. blade-3) turning 0 to 90 degrees about its axle: at 0 the blades lie flat across the airway (closed, as
built), at 90 they stand on edge along the flow (open). Each blade's sweep stays clear of its neighbours (closed or open) and of the
casing's walls, so no blade meets anything over its whole turn whatever the others do (MOT-010 sweeps each node with the rest
still). The axles run through clearance bores in the casing's x walls and stand 20 out of the +x wall for the linkage and the
actuator, which are placed in a later version (OPERATING.md 12: no linkage or actuator element is on file). Every size other than
the flange pattern is a design choice. No airflow, pressure, leakage or torque claim. No vendor file was opened, and no size is taken
from the catalogue record that came with the folder (references/source.txt: another maker's round motorized damper)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "damper", "1.0", "machine"
TITLE = "rectangular air damper, own design, for fan-exhaust 1.0's discharge: 200 x 230 casing, flanges with 4 x M8 at its pattern, three blades turning 0 to 90 degrees"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; the casing's section and both flanges' size and "
            "4 x M8 hole pattern from fan-exhaust 1.0's discharge duct and flange (library.load), holes ISO 273 medium; every other "
            "size a design choice; the linkage and actuator placed in a later version; no airflow, pressure, leakage or torque claim; "
            "no vendor file opened")
ORIGIN = ("the bottom flange's underside (z = 0) at the airway's centre: x across the blades' axles' direction (the axles run along x), "
          "y across the blades, z up along the flow; placed on fan-exhaust, this origin goes to (0, -125, 875) in the fan's frame")
COMMAND = "DAMPER"
PARAMS = dict()

FE = library.load("fan-exhaust")                  # fan-exhaust 1.0: the fan whose discharge flange this damper sits on (one home for its figures)
YC = (FE.DUCT_Y0 + FE.DUCT_Y1) / 2                # -125: the discharge duct's centre line in the fan's frame (this element's y = 0)
OX = FE.DUCT_X                                    # 100: the casing's outside half-width along x (the fan's duct, 200)
OY = (FE.DUCT_Y1 - FE.DUCT_Y0) / 2                # 115: the casing's outside half-width along y (the fan's duct, 230)
WALL = FE.DUCT_W                                  # 10: the casing's walls, as the fan's duct
IX, IY = OX - WALL, OY - WALL                     # 90, 105: the airway 180 x 210, the fan's duct bore
FLX = FE.FL_X                                     # 130: the flanges' half-width along x (260)
FLY = (FE.FL_Y1 - FE.FL_Y0) / 2                   # 145: the flanges' half-width along y (290)
FL_T = FE.FL_T                                    # 15: the flanges' thickness
HOLE_X = FE.FL_HOLE_X                             # 115: the flange holes at x +-115
HOLE_Y = tuple(y - YC for y in FE.FL_HOLE_Y)      # (-130, 130): the flange holes along y, in this frame
M8_CLR = 9.0                                      # M8 clearance, ISO 273 medium H13 (lib/standards/holes.csv)
H = 150.0                                         # overall height: flange 15, casing 120, flange 15 (design choice: room for the blades' sweep)
N_BLADES = 3                                      # three blades across the 210 (design choice)
PITCH = 2 * IY / N_BLADES                         # 70: the axles' pitch along y, the outer ones 35 from the walls
BLADE_C, BLADE_T = 64.0, 2.0                      # each blade 64 wide (across y when closed) and 2 thick (design choice: 6 between neighbours closed)
BLADE_X = IX - 2.0                                # 88: the blades run x +-88, 2 clear of the x walls' inner faces
ZB = H / 2                                        # 75: the axles' height, the casing's middle
R_AXLE, R_BORE = 5.0, 6.0                         # axles Ø10 in Ø12 bores through the x walls (design choice: 1 radial clearance, no bearing drawn)
AXLE_X0, AXLE_X1 = -(OX + 0.5), OX + 20.0         # the axles from 0.5 proud of the -x wall to 20 out of the +x wall (the linkage's stub)
SWING = 90.0                                      # closed (0) to open (90), degrees
BLADE_Y = [-IY + PITCH / 2 + k * PITCH for k in range(N_BLADES)]   # -70, 0, 70: the axles' y
MAT, MAT_BLADE = "M-GALV", "M-ZINC"

SWEEP_R = math.hypot(BLADE_C / 2, BLADE_T / 2)    # 32.02: a blade's corner radius about its axle
assert abs(YC + 125.0) < 1e-9 and abs(PITCH - 70.0) < 1e-9
assert IY - (BLADE_Y[-1] + SWEEP_R) >= 2.5                        # the outer blades' sweep 2.98 clear of the y walls
assert PITCH - BLADE_C / 2 - SWEEP_R >= 5.5                       # a turning blade 5.98 clear of a closed neighbour's edge
assert PITCH - BLADE_T / 2 - SWEEP_R >= 30.0                      # and far clear of an open neighbour's face
assert ZB - SWEEP_R > FL_T and ZB + SWEEP_R < H - FL_T            # the sweep inside the casing's height (z 42.98 to 107.02)
assert R_AXLE < R_BORE and BLADE_X < IX
assert HOLE_X - M8_CLR / 2 > OX + 5.0 and FLX - HOLE_X - M8_CLR / 2 >= 10.0     # the flange holes clear the casing and keep 10 of edge
assert all(abs(y) - M8_CLR / 2 > OY + 5.0 and FLY - abs(y) - M8_CLR / 2 >= 10.0 for y in HOLE_Y)


def build():
    P = Prims()
    for z0 in (0.0, H - FL_T):                                                                  # bottom and top flange
        fl = P.box(MAT, -FLX, -FLY, z0, 2 * FLX, 2 * FLY, FL_T)
        P.cutbox(MAT, -IX, -IY, z0 - 1.0, 2 * IX, 2 * IY, FL_T + 2.0, fl)                       # the airway through it
        for x in (-HOLE_X, HOLE_X):
            for y in HOLE_Y:
                P.hole(MAT, (x, y, z0 - 1.0), (x, y, z0 + FL_T + 1.0), M8_CLR / 2, fl)          # 4 x M8, ISO 273 medium, fan-exhaust's pattern
    casing = P.box(MAT, -OX, -OY, FL_T, 2 * OX, 2 * OY, H - 2 * FL_T)                            # casing between the flanges
    P.cutbox(MAT, -IX, -IY, FL_T - 1.0, 2 * IX, 2 * IY, H - 2 * FL_T + 2.0, casing)             # its airway
    for y in BLADE_Y:
        P.hole(MAT, (-OX - 1.0, y, ZB), (OX + 1.0, y, ZB), R_BORE, casing)                     # the axle's bores through both x walls
    for k, y in enumerate(BLADE_Y, start=1):
        N = f"node:blade-{k}|{MAT_BLADE}"
        P.box(N, -BLADE_X, y - BLADE_C / 2, ZB - BLADE_T / 2, 2 * BLADE_X, BLADE_C, BLADE_T)   # the blade, flat across the airway (closed)
        P.cyl(N, (AXLE_X0, y, ZB), (AXLE_X1, y, ZB), R_AXLE)                                    # its axle
        P.pivot(f"blade-{k}", "rotate", (0.0, y, ZB), axis=(1, 0, 0), range=(0, SWING), unit="deg")
    P.collider("flange-bottom", -FLX, -FLY, 0.0, 2 * FLX, 2 * FLY, FL_T)
    P.collider("casing", -OX, -OY, FL_T, 2 * OX, 2 * OY, H - 2 * FL_T)
    P.collider("flange-top", -FLX, -FLY, H - FL_T, 2 * FLX, 2 * FLY, FL_T)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
