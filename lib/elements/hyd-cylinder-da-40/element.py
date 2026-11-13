#!/usr/bin/env python3
"""hyd-cylinder-da-40: hydraulic cylinder, double acting, tie-rod construction, bore 40, rod 22, stroke 200.
Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC012253 "Hydraulic cylinder"; lib/inventory.csv
row `hyd-cylinder-da-40` (own_design generic, pin 1: "press-hydraulic first", EM 2026-11-08), whose text says how to build it now:
"mounting and ports per ISO 6020-2 once on file; else NOT ON FILE". No vendor file was opened (the folder's metadata.json and
references/ were not used: the row's note says the vendor file is reference only). The class values (spec.md) are design inputs;
the barrel, caps, tie rods, rod and gland are design choices. Three interfaces a dimensional standard fixes are not on file and are
not drawn, each spec.md's open figure, class B: the mounting (ISO 6020-2's mounting styles), the rod-end thread, and the two ports'
thread (no hydraulic port standard is in lib/standards/sources.csv). So the caps carry no mounting holes, the rod ends plain, and each
port is a plain spot face on its cap, its pivot declared (gender female, PIN-002) with the unit "hyd-port", which is no air unit:
the PNE checks (compressed air, toolkit/pneu.py) don't read it. The rod (`rod`, translate +x, 0 to the stroke) is the moving part;
the piston, seals and cushions inside are not modelled."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "hyd-cylinder-da-40", "1.1", "actuator"
TITLE = "hydraulic cylinder, generic, double acting, tie-rod, bore 40, rod 22, stroke 200, 160 bar"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic hydraulic cylinder (ETIM 10.0 EC012253), double acting, tie-rod construction (inventory own_design "
            "generic); class values in spec.md (bore 40, stroke 200, 160 bar); mounting, rod-end thread and port thread not on file "
            "(class B, not drawn); barrel, caps, tie rods, rod and gland are design choices; no vendor file opened")
ORIGIN = "the cap end: the rear cap's back face centre on the cylinder's axis (x = 0); the axis along +x, the rod out toward +x, ports up (+z)"
COMMAND = "HYD-CYLINDER"
PARAMS = dict()

BORE, ROD_D, STROKE = 40.0, 22.0, 200.0   # class values "Bore" and "Stroke length"; the rod Ø22 a design choice (rod-to-bore 0.55)
P_MAX_BAR = 160.0                          # class value "Max. operating pressure" (ratings.csv p_max, generic design)
CAP = 60.0                                 # design choice: square end caps, 60 x 60 (y, z)
REAR_L, HEAD_L = 35.0, 40.0                # design choices: rear (cap-end) cap and head (rod-end) cap lengths along x
PISTON_L = 25.0                            # design choice: the piston's length (not modelled), what the barrel holds beside the stroke
BARREL_OD = 50.0                           # design choice: the barrel tube's OD (5 wall round the 40 bore, not modelled)
TIE_D, TIE_C = 10.0, 22.0                  # design choices: four tie rods Ø10 at y, z = ±22 (clear of the barrel by 1.1)
GLAND_D, GLAND_L = 36.0, 10.0              # design choice: the rod gland's nose on the head cap's front face
ROD_OUT = 30.0                             # design choice: rod out of the gland at rest (retracted), the rod end plain (thread not on file)
ROD_CLEAR = 0.5                            # design choice: radial clearance of the rod in its bore (the guide, seals not modelled)
SPOT_D, SPOT_T = 24.0, 1.0                 # design choice: each port's spot face, Ø24, 1 proud of its cap's top face
IN = 0.5                                   # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_BODY, MAT_ROD, MAT_TIE, MAT_SPOT = "M-CAST-BLUE", "M-SILVER", "M-ZINC", "M-STEEL-7035"

X_BARREL = (REAR_L, REAR_L + PISTON_L + STROKE)          # 35 to 260: the barrel between the caps
X_HEAD = (X_BARREL[1], X_BARREL[1] + HEAD_L)             # 260 to 300: the head cap
X_GLAND = X_HEAD[1] + GLAND_L                            # 310: the gland's front face, where the rod leaves
X_ROD = (REAR_L + PISTON_L, X_GLAND + ROD_OUT)           # 60 to 340 at rest: the rod's inner end at the piston's rod-side face
X_FLOOR = X_ROD[0] - 2.0                                 # 58: the rod bore's floor, 2 behind the rod's inner end at rest
assert math.hypot(TIE_C, TIE_C) - TIE_D / 2 > BARREL_OD / 2 and TIE_C + TIE_D / 2 < CAP / 2   # tie rods clear the barrel, inside the caps
assert BARREL_OD < CAP and GLAND_D < CAP and ROD_D < GLAND_D and BORE < BARREL_OD and ROD_D < BORE
assert X_ROD[0] + STROKE <= X_HEAD[0]                    # at full stroke the rod's inner end reaches the head cap's inner face, no further
assert SPOT_D / 2 < TIE_C - TIE_D / 2 and SPOT_D < REAR_L and SPOT_D < HEAD_L   # spot faces clear the tie rods, inside their caps


def areas():
    """(piston area, annulus area) in mm²"""
    a = math.pi * BORE ** 2 / 4.0
    return a, a - math.pi * ROD_D ** 2 / 4.0


def forces_kn():
    """theoretical (push, pull) at P_MAX_BAR in kN: p x area (1 bar = 0.1 N/mm²); no losses, no buckling check"""
    a, r = areas()
    return P_MAX_BAR * 0.1 * a / 1000.0, P_MAX_BAR * 0.1 * r / 1000.0


def retracted_length(): return X_ROD[1]                  # class value "Overall height retracted": x = 0 to the rod's end at rest


def build():
    P = Prims(); h = CAP / 2; rb = ROD_D / 2 + ROD_CLEAR
    P.box(MAT_BODY, 0.0, -h, -h, REAR_L, CAP, CAP)                                                    # rear (cap-end) cap
    barrel = P.cyl(MAT_BODY, (X_BARREL[0] - IN, 0, 0), (X_BARREL[1] + IN, 0, 0), BARREL_OD / 2)      # barrel, 0.5 into each cap
    head = P.box(MAT_BODY, X_HEAD[0], -h, -h, HEAD_L, CAP, CAP)                                      # head (rod-end) cap
    gland = P.cyl(MAT_BODY, (X_HEAD[1] - IN, 0, 0), (X_GLAND, 0, 0), GLAND_D / 2)                    # rod gland nose
    for s in (gland, head, barrel):                                                                   # the rod's bore through each
        P.hole(MAT_BODY, (X_GLAND + 1.0, 0, 0), (X_FLOOR, 0, 0), rb, s)
    for y in (-TIE_C, TIE_C):
        for z in (-TIE_C, TIE_C):
            P.cyl(MAT_TIE, (X_BARREL[0] - IN, y, z), (X_BARREL[1] + IN, y, z), TIE_D / 2)            # tie rods, cap to cap
    P.cyl(f"node:rod|{MAT_ROD}", (X_ROD[0], 0, 0), (X_ROD[1], 0, 0), ROD_D / 2)                      # piston rod, its end plain
    P.pivot("rod", "translate", (X_ROD[1], 0, 0), axis=(1, 0, 0), range=(0, STROKE), unit="mm")      # extends by the stroke
    xc, xr = REAR_L / 2, (X_HEAD[0] + X_HEAD[1]) / 2                                                   # the ports over each cap's middle
    P.cyl(f"node:port-cap|{MAT_SPOT}", (xc, 0, h - IN), (xc, 0, h + SPOT_T), SPOT_D / 2)             # cap-end port: spot face
    P.cyl(f"node:port-rod|{MAT_SPOT}", (xr, 0, h - IN), (xr, 0, h + SPOT_T), SPOT_D / 2)             # rod-end port: spot face
    P.pivot("port-cap", "port", (xc, 0, h + SPOT_T), axis=(0, 0, 1), range=(0, 0), unit="hyd-port", gender="female", role="work")
    P.pivot("port-rod", "port", (xr, 0, h + SPOT_T), axis=(0, 0, 1), range=(0, 0), unit="hyd-port", gender="female", role="work")
    P.collider("body", 0.0, -h, -h, X_GLAND, CAP, CAP + SPOT_T)
    P.collider("rod", X_GLAND, -ROD_D / 2, -ROD_D / 2, ROD_OUT, ROD_D, ROD_D)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="rod end", az=320, el=15), dict(name="ports", az=160, el=45)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
