#!/usr/bin/env python3
"""valve-counterbalance: a hydraulic counterbalance (load-holding) valve, inline, pilot assisted, for the line that carries a
vertical cylinder's load: oil from `port-2` (the directional valve's side) to `port-1` (the cylinder's side) lifts a check and
passes free; oil from `port-1` to `port-2` passes only when the load's pressure, helped by the pilot pressure at `port-12` (taken
from the cylinder's other line), overcomes the spring's setting, so the load cannot run ahead of the pump and stays held when the
directional valve centres. The press-hydraulic design asks for one (lib/assemblies/press-hydraulic/design.md and hydraulic.csv, EM
2026-11-09: a blocked-centre spool plus a counterbalance valve; lib/inventory.csv row `valve-counterbalance`). Generic
(OPERATING.md 12, EM 2026-11-07 and 2026-11-08): the ETIM subset on file has no class for it, so it is generic by the standard
whose rating quantities its Class values follow, ISO 4413 (as hpu-7.5kw); no vendor file was opened. The body, cartridge, lock nut
and adjusting screw are design choices. The three oil ports are plain spot faces, unit "hyd-port" (the lane's placeholder, as
hyd-flow-control's and hyd-cylinder-da-40's), their thread open (class B, spec.md Open figures, not drawn). The adjusting screw
(`screw`, rotate about +z, four turns) is the one moving part; the poppet, the pilot piston, the check and the spring inside are
not modelled."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "valve-counterbalance", "1.2", "device"
TITLE = "hydraulic counterbalance (load-holding) valve, generic, inline, pilot assisted 3:1, 160 bar, screw set, lock nut"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic hydraulic counterbalance valve (no ETIM class; ISO 4413 values), inline, pilot assisted, with a "
            "free-flow check, for the line that carries a vertical cylinder's load; class values in spec.md (160 bar, pilot ratio "
            "3:1, setting 10 to 160 bar); port thread not on file (class B, not drawn); body, cartridge, lock nut and adjusting "
            "screw are design choices; no vendor file opened")
ORIGIN = ("port-1's face: the cylinder-side spot face's outer face on the flow axis (x = 0); the flow axis along +x to port-2, the "
          "adjusting screw up (+z), the pilot port down (-z)")
COMMAND = "VALVE-COUNTERBALANCE"
PARAMS = dict()

P_MAX_BAR = 160.0                          # class value "max. operating pressure" (ratings.csv p_max, generic design); hpu-7.5kw's 160 bar
PILOT_RATIO = 3.0                          # class value: pilot area to relief seat area, a design choice
SET_BAR = (10.0, 160.0)                    # class value: the spring's setting range over the screw's travel, a design choice
BODY_L, BODY_W, BODY_H = 80.0, 40.0, 40.0  # design choices: the steel body block, flow axis along x through its centre
SPOT_D, SPOT_T = 26.0, 1.0                 # design choice: each main port's spot face, Ø26, 1 proud of its end face (hyd-flow-control's)
PILOT_D = 18.0                             # design choice: the pilot port's spot face on the underside, 1 proud (a small line, no flow)
CART_D, CART_L = 30.0, 24.0                # design choice: the cartridge (spring housing) on the body's top face
NUT_D, NUT_T = 20.0, 6.0                   # design choice: the lock nut on the cartridge's top
SCREW_D, SCREW_H = 10.0, 10.0              # design choice: the adjusting screw's head, seated face to face on the lock nut
TURNS = 4                                  # design choice: the screw's travel from the lowest setting to the highest
IN = 0.5                                   # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_BODY, MAT_SPOT, MAT_CART, MAT_SCREW = "M-ZINC", "M-STEEL-7035", "M-SILVER", "M-BLACK-PA"

X_BODY = (SPOT_T, SPOT_T + BODY_L)         # 1 to 81: the body between the two main spot faces
X_C = (X_BODY[0] + X_BODY[1]) / 2.0        # 41: the cartridge's axis and the pilot port's, over and under the body's centre
X2 = X_BODY[1] + SPOT_T                    # 82: port-2's face
Z_TOP = BODY_H / 2.0                       # 20: the body's top face
Z_BOT = -BODY_H / 2.0 - SPOT_T             # -21: the pilot spot face's outer face
Z_NUT = Z_TOP + CART_L                     # 44: the cartridge's top = the lock nut's seat
Z_SCREW = Z_NUT + NUT_T                    # 50: the lock nut's top = the screw head's seat
assert SPOT_D < min(BODY_W, BODY_H) - 2 * 5.0          # each main spot face keeps 5 of end face round it
assert PILOT_D < BODY_W - 2 * 5.0                      # the pilot spot face keeps 5 of the underside round it
assert NUT_D < CART_D < BODY_W                         # the nut inside the cartridge's top, the cartridge inside the body's top face
assert SCREW_D <= NUT_D                                # the screw head seats on the nut's top face, not over its edge
assert SET_BAR[0] < SET_BAR[1] <= P_MAX_BAR            # the setting never above the valve's own max. operating pressure


def pilot_bar(set_bar, load_bar):
    """the pilot pressure at port-12 that opens the valve against a load pressure at port-1: (setting - load) / pilot ratio
    (force balance on the poppet: the load on the seat area, the pilot on PILOT_RATIO times it, both against the spring)"""
    return max(0.0, (set_bar - load_bar) / PILOT_RATIO)


def screw_height(): return Z_SCREW + SCREW_H - Z_TOP     # the body's top face to the screw head's top


def build():
    P = Prims(); w, h = BODY_W / 2, BODY_H / 2
    P.box(MAT_BODY, X_BODY[0], -w, -h, BODY_L, BODY_W, BODY_H)                                          # body block
    P.cyl(MAT_CART, (X_C, 0, Z_TOP - IN), (X_C, 0, Z_NUT), CART_D / 2)                                   # cartridge, 0.5 into the body
    P.cyl(MAT_BODY, (X_C, 0, Z_NUT - IN), (X_C, 0, Z_SCREW), NUT_D / 2)                                  # lock nut, 0.5 into the cartridge
    P.cyl(f"node:screw|{MAT_SCREW}", (X_C, 0, Z_SCREW), (X_C, 0, Z_SCREW + SCREW_H), SCREW_D / 2)        # adjusting screw, face to face
    P.cyl(f"node:port-1|{MAT_SPOT}", (0, 0, 0), (X_BODY[0] + IN, 0, 0), SPOT_D / 2)                       # cylinder side (the held load)
    P.cyl(f"node:port-2|{MAT_SPOT}", (X_BODY[1] - IN, 0, 0), (X2, 0, 0), SPOT_D / 2)                      # directional valve side
    P.cyl(f"node:port-12|{MAT_SPOT}", (X_C, 0, -h + IN), (X_C, 0, Z_BOT), PILOT_D / 2)                    # pilot, on the underside
    P.pivot("port-1", "port", (0, 0, 0), axis=(-1, 0, 0), range=(0, 0), unit="hyd-port", gender="female", role="work")
    P.pivot("port-2", "port", (X2, 0, 0), axis=(1, 0, 0), range=(0, 0), unit="hyd-port", gender="female", role="work")
    P.pivot("port-12", "port", (X_C, 0, Z_BOT), axis=(0, 0, -1), range=(0, 0), unit="hyd-port", gender="female", role="pilot")
    P.pivot("screw", "rotate", (X_C, 0, Z_SCREW), axis=(0, 0, 1), range=(0, 360 * TURNS), unit="deg")
    P.collider("body", 0.0, -w, Z_BOT, X2, BODY_W, Z_SCREW - Z_BOT)
    P.collider("screw", X_C - SCREW_D / 2, -SCREW_D / 2, Z_SCREW, SCREW_D, SCREW_D, SCREW_H)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="port-2", az=60, el=15), dict(name="pilot from below", az=225, el=-40)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
