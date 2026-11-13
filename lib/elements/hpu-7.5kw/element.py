#!/usr/bin/env python3
"""hpu-7.5kw: hydraulic power unit, press class: a 100 l steel reservoir on two skids, a vertical motor-pump group on its lid (the
motor on a bell housing, the pump hung inside the reservoir), a valve block with the pressure relief valve, a return filter and a
filler-breather on the lid, a sight gauge on the front. It feeds a press's cylinder (hyd-cylinder-da-40) from `port-p` and takes the
oil back by `port-t`; `port-g` takes a pressure gauge (hyd-gauge, a later element). Generic (OPERATING.md 12, EM 2026-11-07): our own
vendor-neutral design of a product class ETIM 10.0 has no class for on file (lib/standards/etim/classes.csv holds no hydraulic power
unit class; hpu-0.37kw's row names EC001185, which is not in it), so "no ETIM class; ISO 4413 values": the power unit's rating
quantities (pressure, flow, reservoir, drive) as ISO 4413 has a hydraulic system state them. ISO 4413 is not in
lib/standards/sources.csv: no figure or clause is taken from it, the values are design inputs (spec.md Class values). lib/inventory.csv
row `hpu-7.5kw` (own_design generic, pin 2, "press-hydraulic first", EM 2026-11-08). One element, as compressor-air is: the motor,
pump, filter and valve inside it are not the inventory's motor, hyd-pump, hyd-filter-return or hyd-valve elements placed (its row has no
made_of; hpu-0.37kw is the assembly of those). The ports' thread is not on file (no hydraulic port standard in sources.csv): each port
is a plain spot face with its pivot, unit "hyd-port" as hyd-cylinder-da-40's, which the PNE checks (compressed air) don't read. No bore is
cut. The pump, suction line, oil and the motor's windings are not modelled; the supply cable is the assembly's."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "hpu-7.5kw", "1.3", "device"
TITLE = "hydraulic power unit, generic, press class, 160 bar, 22 l/min, 100 l reservoir, 7.5 kW 460 V 3-phase 60 Hz"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic hydraulic power unit, press class (no ETIM class; ISO 4413 values) (inventory own_design generic); "
            "class values in spec.md (160 bar, 22 l/min, 100 l, 7.5 kW 460 V 3-phase 60 Hz); the ports' thread not on file (class B, "
            "spot faces, no bore); reservoir, skids, lid, motor-pump group, valve block, filter, breather and sight gauge are design "
            "choices; no vendor file opened")
ORIGIN = ("the centre of the skids' underside (the floor contact plane, z = 0); length along x, width along y, z up; the motor-pump "
          "group toward -x, the valve block and the ports toward +x, the sight gauge on the front (-y)")
COMMAND = "HPU-LARGE"
PARAMS = dict()

# class values (spec.md Class values: design inputs)
P_MAX_BAR = 160.0        # max. working pressure, the relief valve's setting (ratings.csv p_max); the press class of hyd-cylinder-da-40 1.0
FLOW_LPM = 22.0          # pump delivery at the motor's rated speed, l/min
RES_L = 100.0            # reservoir, usable oil volume, l
MOTOR_KW, ETA = 7.5, 0.8 # drive motor's rated output (ratings.csv power) and the pump-and-coupling efficiency the drive is sized with
# design choices (spec.md Dimensions)
L, W, Z0, Z1 = 700.0, 450.0, 60.0, 460.0       # reservoir: x, y, from z 60 (the skids' top) to 460
SKID_W, SKID_IN = 60.0, 10.0                   # two skids under the reservoir's long sides, 60 wide, 60 high, set 10 in from
                                               # its sides and ends (no face flush with the reservoir's: GEO-050)
LID_OVER, LID_T = 10.0, 12.0                   # the lid overhangs the reservoir 10 all round, 12 thick
MX = -170.0                                    # the motor-pump group's axis (x, y = 0)
BELL_D, BELL_H = 250.0, 150.0                  # bell housing on the lid (the pump below it, inside the reservoir)
FLANGE_D, FLANGE_T = 300.0, 18.0               # the motor's flange on the bell housing
MOTOR_D, MOTOR_H = 260.0, 350.0                # motor body (the envelope drawn is our own; no IEC frame figure is used)
COWL_D, COWL_H = 240.0, 80.0                   # fan cowl on the motor's top
TBOX = (-240.0, -100.0, 100.0, 220.0, 760.0, 880.0)   # motor terminal box (x0, x1, y0, y1, z0, z1), on the motor's +y side
ENTRY_D, ENTRY_L, ENTRY_Z = 24.0, 12.0, 800.0  # `pwr`: the cable entry boss on the terminal box's +y face (motor-iec71-370w's pattern)
PWR_UNIT = "480V-3P+E"                         # the library's 480 V three-phase + PE power unit (lib/standards/cables.csv cable-pwr-480)
BLOCK = (120.0, 290.0, -70.0, 70.0, 110.0)     # valve block on the lid (x0, x1, y0, y1, height)
RV_X, RV_D, RV_H = 165.0, 36.0, 70.0           # pressure relief valve cartridge, up from the block's top
KNOB_D, KNOB_H = 50.0, 20.0                    # its adjusting knob (fixed: no moving node)
SPOT_D, SPOT_T = 24.0, 1.0                     # each port's spot face, Ø24, 1 proud (hyd-cylinder-da-40's)
PORT_Y = 35.0                                  # port-p at y = -35, port-t at y = +35 on the block's +x face
G_X = 250.0                                    # port-g on the block's top
FILT_XY, FILT_D, FILT_H = (230.0, 150.0), 90.0, 128.0   # return filter on the lid
BRTH_XY, BRTH_D, BRTH_H = (40.0, -150.0), 60.0, 50.0     # filler-breather on the lid
GAUGE_X, GAUGE_W, GAUGE_T, GAUGE_Z = 250.0, 36.0, 6.0, (200.0, 400.0)   # oil level and temperature sight gauge on the front
WIN_W, WIN_T = 20.0, 2.0                       # its clear window, 1 proud of the frame
IN = 0.5                                       # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_TANK, MAT_DARK, MAT_MOTOR, MAT_BLOCK, MAT_SPOT, MAT_CART, MAT_WIN = (
    "M-STEEL-7035", "M-BLACK-PA", "M-CAST-BLUE", "M-GALV", "M-STEEL-7035", "M-ZINC", "M-CASE-CLEAR")

Z_LID = Z1 + LID_T - IN                        # 471.5: the lid's top face
Z_BLOCK = Z_LID + BLOCK[4] - IN                # 581: the valve block's top face
Z_BELL = Z_LID + BELL_H - IN                   # the bell housing's top
Z_MOTOR0 = Z_BELL + FLANGE_T - IN              # the flange's top, the motor body's foot
Z_MOTOR1 = Z_MOTOR0 + MOTOR_H - IN             # the motor body's top
Z_TOP = Z_MOTOR1 + COWL_H - IN                 # the fan cowl's top: the unit's height
Z_PORT = Z_LID + BLOCK[4] / 2.0                # the ports' height on the block's +x face


def hydraulic_kw(): return P_MAX_BAR * FLOW_LPM / 600.0          # p (bar) x Q (l/min) / 600 = kW at the outlet


def reservoir_gross_l(): return L * W * (Z1 - Z0) / 1.0e6        # the reservoir's inside volume to its lid, l (walls not modelled)


assert hydraulic_kw() / ETA <= MOTOR_KW                           # the motor drives the pump at full pressure and flow
assert reservoir_gross_l() >= RES_L / 0.85                        # the usable volume fills at most 85 % of the reservoir (air space)
assert RES_L >= 3.0 * FLOW_LPM                                    # at least three minutes of the pump's delivery
assert abs(MX) + max(BELL_D, FLANGE_D, MOTOR_D) / 2.0 <= L / 2.0 + LID_OVER     # the motor group stands on the lid
assert MX + FLANGE_D / 2.0 < BRTH_XY[0] - BRTH_D / 2.0 and BRTH_XY[0] + BRTH_D / 2.0 < BLOCK[0]   # breather between motor and block
assert TBOX[0] > MX - MOTOR_D / 2.0 and TBOX[1] < MX + MOTOR_D / 2.0 and TBOX[2] < MOTOR_D / 2.0 - 20.0   # terminal box on the motor
assert FILT_XY[1] - FILT_D / 2.0 > BLOCK[3] + 20.0 and FILT_XY[1] + FILT_D / 2.0 < W / 2.0     # filter clear of the block, on the lid
assert G_X - SPOT_D / 2.0 > RV_X + KNOB_D / 2.0 + 20.0 and G_X + SPOT_D / 2.0 < BLOCK[1]       # port-g clear of the relief knob
assert 2 * PORT_Y >= SPOT_D + 40.0 and PORT_Y + SPOT_D / 2.0 < BLOCK[3]                          # room for a wrench, on the face
assert BLOCK[1] < L / 2.0 + LID_OVER                                                            # the block inside the lid
assert TBOX[4] + ENTRY_D / 2.0 < ENTRY_Z < TBOX[5] - ENTRY_D / 2.0 and TBOX[3] + ENTRY_L < W / 2.0 + LID_OVER   # entry on the box, in the envelope


def build():
    P = Prims(); l, w = L / 2.0, W / 2.0
    for y0 in (-w + SKID_IN, w - SKID_IN - SKID_W):
        P.box(MAT_DARK, -l + SKID_IN, y0, 0.0, L - 2 * SKID_IN, SKID_W, Z0 + IN)                     # skids
    P.box(MAT_TANK, -l, -w, Z0, L, W, Z1 - Z0)                                                      # reservoir
    P.box(MAT_TANK, -l - LID_OVER, -w - LID_OVER, Z1 - IN, L + 2 * LID_OVER, W + 2 * LID_OVER, LID_T)   # lid
    P.cyl(MAT_BLOCK, (MX, 0, Z_LID - IN), (MX, 0, Z_BELL), BELL_D / 2.0)                              # bell housing
    P.cyl(MAT_MOTOR, (MX, 0, Z_BELL - IN), (MX, 0, Z_MOTOR0), FLANGE_D / 2.0)                         # motor flange
    P.cyl(MAT_MOTOR, (MX, 0, Z_MOTOR0 - IN), (MX, 0, Z_MOTOR1), MOTOR_D / 2.0)                        # motor body
    P.cyl(MAT_MOTOR, (MX, 0, Z_MOTOR1 - IN), (MX, 0, Z_TOP), COWL_D / 2.0)                            # fan cowl
    x0, x1, y0, y1, z0, z1 = TBOX
    P.box(MAT_MOTOR, x0, y0, z0, x1 - x0, y1 - y0, z1 - z0)                                          # terminal box
    xe = (x0 + x1) / 2.0
    P.cyl(f"node:pwr|{MAT_CART}", (xe, y1 - IN, ENTRY_Z), (xe, y1 + ENTRY_L, ENTRY_Z), ENTRY_D / 2.0)  # cable entry boss
    P.pivot("pwr", "port", (xe, y1 + ENTRY_L, ENTRY_Z), axis=(0, 1, 0), range=(0, 0), unit=PWR_UNIT, gender="none")   # to screw terminals
    bx0, bx1, by0, by1, bh = BLOCK
    P.box(MAT_BLOCK, bx0, by0, Z_LID - IN, bx1 - bx0, by1 - by0, bh)                                 # valve block
    P.cyl(MAT_CART, (RV_X, 0, Z_BLOCK - IN), (RV_X, 0, Z_BLOCK + RV_H), RV_D / 2.0)                   # relief valve cartridge
    P.cyl(MAT_DARK, (RV_X, 0, Z_BLOCK + RV_H - IN), (RV_X, 0, Z_BLOCK + RV_H + KNOB_H), KNOB_D / 2.0) # its adjusting knob
    P.cyl(f"node:port-g|{MAT_SPOT}", (G_X, 0, Z_BLOCK - IN), (G_X, 0, Z_BLOCK + SPOT_T), SPOT_D / 2.0)   # gauge port: spot face
    P.pivot("port-g", "port", (G_X, 0, Z_BLOCK + SPOT_T), axis=(0, 0, 1), range=(0, 0), unit="hyd-port", gender="female", role="gauge")
    for node, y, role in (("port-p", -PORT_Y, "supply"), ("port-t", PORT_Y, None)):                  # pressure and return ports
        P.cyl(f"node:{node}|{MAT_SPOT}", (bx1 - IN, y, Z_PORT), (bx1 + SPOT_T, y, Z_PORT), SPOT_D / 2.0)
        kw = dict(role=role) if role else {}
        P.pivot(node, "port", (bx1 + SPOT_T, y, Z_PORT), axis=(1, 0, 0), range=(0, 0), unit="hyd-port", gender="female", **kw)
    P.cyl(MAT_DARK, (FILT_XY[0], FILT_XY[1], Z_LID - IN), (FILT_XY[0], FILT_XY[1], Z_LID + FILT_H), FILT_D / 2.0)   # return filter
    P.cyl(MAT_DARK, (BRTH_XY[0], BRTH_XY[1], Z_LID - IN), (BRTH_XY[0], BRTH_XY[1], Z_LID + BRTH_H), BRTH_D / 2.0)   # filler-breather
    g0 = GAUGE_X - GAUGE_W / 2.0
    P.box(MAT_DARK, g0, -w - GAUGE_T, GAUGE_Z[0], GAUGE_W, GAUGE_T + IN, GAUGE_Z[1] - GAUGE_Z[0])                  # sight gauge frame
    P.box(MAT_WIN, GAUGE_X - WIN_W / 2.0, -w - GAUGE_T - 1.0, GAUGE_Z[0] + 8.0, WIN_W, WIN_T, GAUGE_Z[1] - GAUGE_Z[0] - 16.0)
    P.collider("body", -l - LID_OVER, -w - LID_OVER, 0.0, L + 2 * LID_OVER, W + 2 * LID_OVER, Z_TOP)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="ports", az=40, el=30)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
