#!/usr/bin/env python3
"""hyd-flow-control: a hydraulic one-way flow control valve (a throttle with a bypass check), inline, for a meter-out circuit:
oil from `port-1` to `port-2` passes the adjustable throttle; oil from `port-2` to `port-1` lifts the check and passes free. The
press-hydraulic design (lib/assemblies/press-hydraulic/design.md, hydraulic.csv line A) asks for one to slow the 0.29 m/s ram, and
the core's request (lib/requests/core/pneu-hydraulic-2026-11-09.md item 4) asks pneu for the element. Generic (OPERATING.md 12, EM
2026-11-07): our own vendor-neutral design of ETIM 10.0 EC011463 "Regulating valve" (synonyms "Manual throttle", "Throttle";
45 features on file), the class lib/standards/etim/classes.csv gives for a manually set throttle; no inventory row yet (request
pneu-8 asks the core for a gap row). No vendor file was opened. The body, bonnet, lock nut and knob are design choices. The two oil
ports are plain spot faces on the body's end faces, unit "hyd-port" (the lane's placeholder, as hold-down's and hyd-cylinder-da-40's),
their thread open (class B, spec.md Open figures, not drawn). The adjusting knob (`knob`, rotate about +z, five turns) is the one
moving part; the throttle needle, the check poppet and its spring inside are not modelled."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "hyd-flow-control", "1.2", "device"
TITLE = "hydraulic one-way flow control valve, generic, inline, throttle with bypass check, 160 bar, knob set, lock nut"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic regulating valve (ETIM 10.0 EC011463), a hydraulic inline one-way flow control (throttle with a "
            "bypass check) for a meter-out circuit; class values in spec.md (160 bar, manual, lockable); port thread not on file "
            "(class B, not drawn); body, bonnet, lock nut and knob are design choices; no vendor file opened")
ORIGIN = "port-1's face: the inlet spot face's outer face on the flow axis (x = 0); the flow axis along +x to port-2, the knob up (+z)"
COMMAND = "HYD-FLOW-CONTROL"
PARAMS = dict()

P_MAX_BAR = 160.0                          # class value "Max. operating pressure" (ratings.csv p_max, generic design); hpu-7.5kw's 160 bar
BODY_L, BODY_W, BODY_H = 70.0, 40.0, 40.0  # design choices: the steel body block, flow axis along x through its centre
SPOT_D, SPOT_T = 26.0, 1.0                 # design choice: each port's spot face, Ø26, 1 proud of its end face (as hold-down's)
BONNET_D, BONNET_L = 22.0, 12.0            # design choice: the bonnet carrying the throttle's spindle, on the body's top face
NUT_D, NUT_T = 30.0, 6.0                   # design choice: the lock nut on the bonnet's top (class value 19, lockable)
KNOB_D, KNOB_H = 28.0, 14.0                # design choice: the adjusting knob, seated face to face on the lock nut
TURNS = 5                                  # design choice: the knob's travel from the throttle shut to fully open
IN = 0.5                                   # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_BODY, MAT_SPOT, MAT_NUT, MAT_KNOB = "M-ZINC", "M-STEEL-7035", "M-SILVER", "M-BLACK-PA"

X_BODY = (SPOT_T, SPOT_T + BODY_L)         # 1 to 71: the body between the two spot faces
X_C = (X_BODY[0] + X_BODY[1]) / 2.0        # 36: the spindle's axis over the body's centre
X2 = X_BODY[1] + SPOT_T                    # 72: port-2's face
Z_TOP = BODY_H / 2.0                       # 20: the body's top face
Z_NUT = Z_TOP + BONNET_L                   # 32: the bonnet's top = the lock nut's seat
Z_KNOB = Z_NUT + NUT_T                     # 38: the lock nut's top = the knob's seat
assert SPOT_D < min(BODY_W, BODY_H) - 2 * 5.0          # each spot face keeps 5 of end face round it
assert BONNET_D < NUT_D and NUT_D < BODY_W             # the nut wider than the bonnet, inside the body's top face
assert KNOB_D <= NUT_D                                 # the knob seats on the nut's top face, not over its edge
assert X_C - BONNET_D / 2 - (X_BODY[0] + IN) == 23.5 == (X_BODY[1] - IN) - (X_C + BONNET_D / 2)   # the x gap from each spot face's inner end to the bonnet (spec.md Dimensions)


def knob_height(): return Z_KNOB + KNOB_H - Z_TOP       # class value "Height operating element": the body's top to the knob's top


def build():
    P = Prims(); w, h = BODY_W / 2, BODY_H / 2
    P.box(MAT_BODY, X_BODY[0], -w, -h, BODY_L, BODY_W, BODY_H)                                          # body block
    P.cyl(MAT_BODY, (X_C, 0, Z_TOP - IN), (X_C, 0, Z_NUT), BONNET_D / 2)                                 # bonnet, 0.5 into the body
    P.cyl(MAT_NUT, (X_C, 0, Z_NUT - IN), (X_C, 0, Z_KNOB), NUT_D / 2)                                    # lock nut, 0.5 into the bonnet
    P.cyl(f"node:knob|{MAT_KNOB}", (X_C, 0, Z_KNOB), (X_C, 0, Z_KNOB + KNOB_H), KNOB_D / 2)              # adjusting knob, face to face
    P.cyl(f"node:port-1|{MAT_SPOT}", (0, 0, 0), (X_BODY[0] + IN, 0, 0), SPOT_D / 2)                       # inlet spot face (throttled 1 to 2)
    P.cyl(f"node:port-2|{MAT_SPOT}", (X_BODY[1] - IN, 0, 0), (X2, 0, 0), SPOT_D / 2)                      # outlet spot face (free 2 to 1)
    P.pivot("port-1", "port", (0, 0, 0), axis=(-1, 0, 0), range=(0, 0), unit="hyd-port", gender="female", role="work")
    P.pivot("port-2", "port", (X2, 0, 0), axis=(1, 0, 0), range=(0, 0), unit="hyd-port", gender="female", role="work")
    P.pivot("knob", "rotate", (X_C, 0, Z_KNOB), axis=(0, 0, 1), range=(0, 360 * TURNS), unit="deg")
    P.collider("body", 0.0, -w, -h, X2, BODY_W, Z_KNOB + h)
    P.collider("knob", X_C - KNOB_D / 2, -KNOB_D / 2, Z_KNOB, KNOB_D, KNOB_D, KNOB_H)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="port-2", az=60, el=15)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
