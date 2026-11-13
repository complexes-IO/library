#!/usr/bin/env python3
"""hold-down: a hydraulic sheet hold-down for a shear: a single-acting plunger cylinder, flange-mounted on the top of the shear's
hold-down beam, whose plunger and foot pad press the sheet onto the table before the blade cuts; a spring inside lifts the plunger
back when the oil is let out. Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC012253
"Hydraulic cylinder" (the class hyd-cylinder-da-40 uses; 11 features on file); lib/inventory.csv row `hold-down` (own_design generic,
"hydraulic sheet hold-down (shear)"; shear-hydraulic, shear-sheet). The row names no class; EC012253 is the class
lib/standards/etim/classes.csv gives for a hydraulic linear actuator, and a hold-down is one, single acting (class value 11 "no").
No vendor file was opened. It is not built as an ISO 6020-2 tie-rod cylinder (no tie rods, none of that standard's mounting
styles): its form is our own, a plunger in a round body under a square flange, so its sizes are design choices. The flange's
four holes are M8 clearance, medium (ISO 273, lib/standards/holes.csv); the screws (screw-iso4017, not built) are the host's
to place later. The oil port `port-cap` on the flange's top is a plain spot face, unit "hyd-port" (the lane's placeholder, as
hyd-cylinder-da-40's), its thread open (class B, spec.md Open figures, not drawn). The plunger with its foot pad (`plunger`, translate
-z, 0 to the stroke) is the moving part; the return spring and the seals inside are not modelled."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "hold-down", "1.1", "actuator"
TITLE = "hydraulic sheet hold-down, generic, single acting plunger, Ø32, stroke 25, 160 bar, flange mount"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic hydraulic cylinder (ETIM 10.0 EC012253), a single-acting spring-return plunger cylinder used as "
            "a shear's sheet hold-down (inventory own_design generic); class values in spec.md (bore 32, stroke 25, 160 bar); flange "
            "holes M8 clearance (ISO 273 medium, lib/standards/holes.csv); port thread not on file (class B, not drawn); flange, body, "
            "plunger and foot pad are design choices; no vendor file opened")
ORIGIN = "the mounting face: the flange's underside centre on the plunger's axis (z = 0); the plunger down (-z), the port up (+z)"
COMMAND = "HOLD-DOWN"
PARAMS = dict()

BORE, STROKE = 32.0, 25.0                  # class values "Bore" (the plunger's diameter: a plunger cylinder's working area) and "Stroke length"
P_MAX_BAR = 160.0                          # class value "Max. operating pressure" (ratings.csv p_max, generic design); hpu-7.5kw's 160 bar
FLANGE, FLANGE_T = 80.0, 15.0              # design choices: the square mounting flange, 80 x 80, 15 thick, on the beam's top face
HOLE_D, HOLE_C = 9.0, 30.0                 # M8 clearance, medium (ISO 273 H13: 9.0 to 9.22; holes.csv), on a 60 x 60 square (design choice)
BODY_D, BODY_L = 56.0, 95.0                # design choices: the round body under the flange, inside the beam's bore (the host's)
PLUNGER_OUT = 15.0                         # design choice: the plunger's length out of the body at rest (retracted)
PLUNGER_IN = 75.0                          # design choice: the plunger's length inside the body at rest (its guide; the spring above it)
CLEAR = 0.5                                # design choice: radial clearance of the plunger in its bore (the guide, seals not modelled)
PAD_D, PAD_T = 50.0, 12.0                  # design choices: the foot pad (polyurethane) under the plunger, face to face
SPOT_D, SPOT_T = 24.0, 1.0                 # design choice: the port's spot face, Ø24, 1 proud of the flange's top face
IN = 0.5                                   # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_BODY, MAT_PLUNGER, MAT_PAD, MAT_SPOT = "M-CAST-BLUE", "M-SILVER", "M-ORANGE-PA", "M-STEEL-7035"

Z_BODY = -BODY_L                           # -95: the body's foot, where the plunger leaves it
Z_PL = (Z_BODY - PLUNGER_OUT, Z_BODY + PLUNGER_IN)   # -110 to -20 at rest: the plunger's lower end and inner (upper) end
Z_FLOOR = Z_PL[1] + 2.0                    # -18: the plunger bore's floor, 2 above the plunger's inner end at rest
Z_PAD = Z_PL[0] - PAD_T                    # -122: the pad's face, the element's lowest point at rest
assert BORE < BODY_D - 2 * 6.0             # at least 6 of wall round the plunger bore (design choice; the oil chamber is not modelled)
assert BODY_D < FLANGE and PAD_D < BODY_D and BORE < PAD_D
assert math.hypot(HOLE_C, HOLE_C) - HOLE_D / 2 > BODY_D / 2 + 3.0     # the holes clear the body below the flange (screw heads above)
assert FLANGE / 2 - HOLE_C - HOLE_D / 2 >= 5.0                         # at least 5 of flange between each hole and its edges
assert SPOT_D / 2 < math.hypot(HOLE_C, HOLE_C) - HOLE_D / 2 - 10.0      # the spot face clears the screw heads' circle
assert PLUNGER_IN - STROKE >= 1.5 * BORE                               # at full stroke the plunger keeps 1.5 x Ø (48) guided in the body
assert Z_FLOOR < 0.0                       # the bore stays blind inside the body, under the flange


def area():
    """the plunger's working area in mm² (a plunger cylinder: the plunger's full section)"""
    return math.pi * BORE ** 2 / 4.0


def push_kn():
    """theoretical push at P_MAX_BAR in kN: p x area (1 bar = 0.1 N/mm²); no spring, no friction"""
    return P_MAX_BAR * 0.1 * area() / 1000.0


def retracted_height(): return FLANGE_T + SPOT_T - Z_PAD    # class value "Overall height retracted": the port's face to the pad's face


def build():
    P = Prims(); h = FLANGE / 2; rb = BORE / 2 + CLEAR
    flange = P.box(MAT_BODY, -h, -h, 0.0, FLANGE, FLANGE, FLANGE_T)                                     # mounting flange
    body = P.cyl(MAT_BODY, (0, 0, Z_BODY), (0, 0, IN), BODY_D / 2)                                      # body, 0.5 into the flange
    for x in (-HOLE_C, HOLE_C):
        for y in (-HOLE_C, HOLE_C):
            P.hole(MAT_BODY, (x, y, -1.0), (x, y, FLANGE_T + 1.0), HOLE_D / 2, flange)                 # M8 clearance, through
    P.hole(MAT_BODY, (0, 0, Z_BODY - 1.0), (0, 0, Z_FLOOR), rb, body)                                  # the plunger's bore, blind
    P.cyl(f"node:plunger|{MAT_PLUNGER}", (0, 0, Z_PL[1]), (0, 0, Z_PL[0]), BORE / 2)                     # plunger
    P.cyl(f"node:plunger|{MAT_PAD}", (0, 0, Z_PL[0]), (0, 0, Z_PAD), PAD_D / 2)                         # foot pad, face to face
    P.pivot("plunger", "translate", (0, 0, Z_PAD), axis=(0, 0, -1), range=(0, STROKE), unit="mm")       # presses down by the stroke
    zt = FLANGE_T + SPOT_T
    P.cyl(f"node:port-cap|{MAT_SPOT}", (0, 0, FLANGE_T - IN), (0, 0, zt), SPOT_D / 2)                    # oil port: spot face
    P.pivot("port-cap", "port", (0, 0, zt), axis=(0, 0, 1), range=(0, 0), unit="hyd-port", gender="female", role="work")
    P.collider("body", -h, -h, Z_BODY, FLANGE, FLANGE, zt - Z_BODY)
    P.collider("plunger", -PAD_D / 2, -PAD_D / 2, Z_PAD, PAD_D, PAD_D, Z_BODY - Z_PAD)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="pad", az=300, el=-30), dict(name="flange", az=160, el=55)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
