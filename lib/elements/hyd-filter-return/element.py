#!/usr/bin/env python3
"""hyd-filter-return: a hydraulic return-line filter, inline: a head with the two oil ports and a spin-on canister hanging under it.
Oil coming back from the directional valve's T port enters `port-in`, passes from the outside of the element in the canister to
its core and leaves through `port-out` to the tank. A bypass valve in the head opens when the element is clogged, so the return
line is never blocked; the clogging indicator on the head (`indicator`, a button that rises) shows the pressure drop across the
element before the bypass opens. lib/inventory.csv row `hyd-filter-return` (own_design generic, "hydraulic filter (return line)";
hpu-assembly-station, test-bench-hydraulic). Generic (OPERATING.md 12, EM 2026-11-07 and 2026-11-08): the ETIM subset on file has
no class for it (EC010080 "Bucket filter, single", synonym "Oil filter", is a pipeline basket strainer and has no features on
file), so it is generic by the standard whose rating quantities its Class values follow, ISO 4413 (as hpu-7.5kw and
valve-counterbalance); no vendor file was opened. The head, canister, wrench boss and indicator are design choices. The two oil
ports are plain spot faces, unit "hyd-port" (toolkit/hyd.py H1: the dash size open), their thread a figure of SAE J1926-1 table 1
(class B, spec.md Open figures, not drawn). The indicator's button is the one moving part; the element, the bypass valve and the
indicator's piston and spring inside are not modelled."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import hyd, library
from toolkit.prims import Prims

ID, VERSION, CLASS = "hyd-filter-return", "1.2", "device"
TITLE = "hydraulic return-line filter, generic, inline head with spin-on canister, 16 bar, bypass 3 bar, clogging indicator"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic hydraulic return-line filter (no ETIM class; ISO 4413 values), an inline head with a spin-on "
            "canister, a bypass valve and a visual clogging indicator; class values in spec.md (16 bar, bypass 3 bar, indicator "
            "2 bar); port thread not on file (class B, not drawn); head, canister, wrench boss and indicator are design choices; "
            "no vendor file opened")
ORIGIN = ("port-in's face: the inlet spot face's outer face on the flow axis (x = 0); the flow axis along +x to port-out, the "
          "canister down (-z), the clogging indicator up (+z)")
COMMAND = "HYD-FILTER"
PARAMS = dict()

P_MAX_BAR = 16.0                           # class value 1 "max. operating pressure" (ratings.csv p_max): design, >= the tank line's
BYPASS_BAR = 3.0                           # class value 3: the bypass valve's opening pressure drop, a design choice
INDICATOR_BAR = 2.0                        # class value 4: the indicator shows at this pressure drop, a design choice below the bypass
HEAD_L, HEAD_W, HEAD_H = 100.0, 80.0, 40.0 # design choices: the aluminium head, flow axis along x through its centre
SPOT_D, SPOT_T = 32.0, 1.0                 # design choice: each port's spot face, Ø32, 1 proud of its end face
CAN_D, CAN_L = 76.0, 130.0                 # design choice: the spin-on canister under the head (0.59 l outside; the element's space inside it is not modelled)
BOSS_D, BOSS_L = 30.0, 8.0                 # design choice: the wrench boss under the canister's end (drawn round)
IND_D, IND_L = 20.0, 10.0                  # design choice: the indicator's housing on the head's top face, over the inlet side
BTN_D, BTN_H = 10.0, 4.0                   # design choice: the indicator's button, seated face to face on its housing
BTN_RISE = 5.0                             # design choice: the button's travel, flush seat to fully shown
IND_X = 26.0                               # design choice: the indicator 25 toward the inlet from the head's centre
IN = 0.5                                   # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_HEAD, MAT_SPOT, MAT_CAN, MAT_IND, MAT_BTN = "M-ALU-ANOD", "M-SILVER", "M-STEEL-7035", "M-BLACK-PA", "M-RED-PA"

X_HEAD = (SPOT_T, SPOT_T + HEAD_L)         # 1 to 101: the head between the two spot faces
X_C = (X_HEAD[0] + X_HEAD[1]) / 2.0        # 51: the canister's axis, under the head's centre
X2 = X_HEAD[1] + SPOT_T                    # 102: port-out's face
Z_TOP = HEAD_H / 2.0                       # 20: the head's top face
Z_BOT = -HEAD_H / 2.0                      # -20: the head's underside, the canister's seat
Z_CAN = Z_BOT - CAN_L                      # -150: the canister's end
Z_BOSS = Z_CAN - BOSS_L                    # -158: the wrench boss's end, the lowest point
Z_IND = Z_TOP + IND_L                      # 30: the indicator housing's top = the button's seat
assert SPOT_D <= HEAD_H - 2 * 4.0 and SPOT_D <= HEAD_W - 2 * 4.0   # each spot face keeps 4 of end face round it
assert CAN_D <= HEAD_W - 2 * 2.0 and CAN_D <= HEAD_L - 2 * 2.0     # the canister 2 inside the head's underside all round
assert BOSS_D < CAN_D                                               # the wrench boss inside the canister's end
assert X_HEAD[0] + 5.0 <= IND_X - IND_D / 2.0 and IND_D < HEAD_W    # the indicator's housing 5 inside the head's top face
assert BTN_D < IND_D                                                # the button seats on the housing's top face, not over its edge
assert INDICATOR_BAR < BYPASS_BAR < P_MAX_BAR                       # the indicator shows before the bypass opens
assert P_MAX_BAR >= hyd.P_TANK                                      # H5: a return-line part is judged at the tank line's pressure


def build():
    P = Prims(); w, h = HEAD_W / 2, HEAD_H / 2
    P.box(MAT_HEAD, X_HEAD[0], -w, -h, HEAD_L, HEAD_W, HEAD_H)                                           # head
    P.cyl(MAT_CAN, (X_C, 0, Z_CAN), (X_C, 0, Z_BOT + IN), CAN_D / 2)                                     # canister, 0.5 into the head
    P.cyl(MAT_CAN, (X_C, 0, Z_BOSS), (X_C, 0, Z_CAN + IN), BOSS_D / 2)                                   # wrench boss, 0.5 into the canister
    P.cyl(MAT_IND, (IND_X, 0, Z_TOP - IN), (IND_X, 0, Z_IND), IND_D / 2)                                 # indicator housing, 0.5 into the head
    P.cyl(f"node:indicator|{MAT_BTN}", (IND_X, 0, Z_IND), (IND_X, 0, Z_IND + BTN_H), BTN_D / 2)          # indicator button, face to face
    P.cyl(f"node:port-in|{MAT_SPOT}", (0, 0, 0), (X_HEAD[0] + IN, 0, 0), SPOT_D / 2)                      # inlet spot face
    P.cyl(f"node:port-out|{MAT_SPOT}", (X_HEAD[1] - IN, 0, 0), (X2, 0, 0), SPOT_D / 2)                    # outlet spot face
    P.pivot("port-in", "port", (0, 0, 0), axis=(-1, 0, 0), range=(0, 0), unit="hyd-port", gender="female")
    P.pivot("port-out", "port", (X2, 0, 0), axis=(1, 0, 0), range=(0, 0), unit="hyd-port", gender="female")
    P.pivot("indicator", "translate", (IND_X, 0, Z_IND), axis=(0, 0, 1), range=(0, BTN_RISE), unit="mm")
    P.collider("body", 0.0, -w, Z_BOSS, X2, HEAD_W, Z_IND - Z_BOSS)
    P.collider("indicator", IND_X - BTN_D / 2, -BTN_D / 2, Z_IND, BTN_D, BTN_D, BTN_H)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="outlet side", az=60, el=15), dict(name="from below", az=225, el=-35)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
