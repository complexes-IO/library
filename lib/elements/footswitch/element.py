#!/usr/bin/env python3
"""footswitch: guarded foot switch, single pedal, one N.C. and one N.O. contact (11-12, 23-24), momentary, AC-15 3 A at 230 V, a
plastic housing 100 x 200 x 130 with a protective hood over the pedal and an M20 x 1.5 cable entry in its heel. A generic element
(OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC001258 "Foot switch", built to the class values
in spec.md "## Class values"; no maker's datasheet and no product matched (no folder or stub existed before this element). Not a
safety-function device (Class values 12): no forced opening is claimed, and the hood guards the pedal against an unintended press, it
is no safeguard of the machine.
What it meets comes from the standards on file: the cable entry is M20 x 1.5 tapped, its minor diameter derived (derive.thread,
ISO 68-1 / ISO 965-1). Every other size is a design choice, said so in spec.md.
Not placed in this version (OPERATING.md 12, quality at the source): the installer's cable gland in the entry, the pedal's return
spring and the contact block inside the heel.
Modelled from the outside in: a base plate; two side walls and a top plate (the hood), open at the toe end for the foot; in the heel,
a terminal compartment (back wall with the cable entry, front wall, cover) with four terminal screw heads on the front wall's back
face (the port nodes t-11, t-12, t-23, t-24); the pedal (node `pedal`: the plate and its hinge pin), which turns 5 deg toe down
about the hinge pin seated between the side walls."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "footswitch", "1.0", "device"
TITLE = "foot switch, guarded, single pedal, 1 N.C. + 1 N.O. (11-12, 23-24), momentary, AC-15 3 A 230 V, housing 100 x 200 x 130, M20 x 1.5 entry (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Foot switch (ETIM 10.0 EC001258); class values in spec.md; cable entry M20 x 1.5 derived "
            "(ISO 68-1 / ISO 965-1); housing, hood and pedal sizes are design choices; the terminals' conductor range and torque "
            "are open (spec.md)")
ORIGIN = "the heel's back face y = 0, x = 0 the centreline, z = 0 the base's bottom face (the floor), the toe end and the hood's opening toward -y"
COMMAND = "FOOTSW"
PARAMS = {}

# ---- housing and hood (design choices: spec.md Dimensions)
W, L, H = 100.0, 200.0, 130.0        # overall: x ±50, y -200 ... 0, z 0 ... 130
BASE_T = 12.0                        # base plate z 0 ... 12, full footprint
SIDE = 8.0                           # side walls x ±42 ... ±50, y -200 ... 0, z 12 ... 122
TOP_T = 8.0                          # top plate z 122 ... 130, full footprint (the hood's roof)
# ---- heel compartment (design choices): between the side walls, x ±42
HEEL = (-50.0, 0.0, 70.0)            # y front, y back, z top of the compartment's walls
WALL_T = 8.0                         # back wall y -8 ... 0, front wall y -50 ... -42, cover z 62 ... 70 (y -42 ... -8)
# ---- what it meets (standards on file)
ENTRY_D = 18.3762                    # M20 x 1.5 internal thread's minor diameter D1, derived: derive.thread(20.0, 1.5) (ISO 68-1, ISO 965-1)
ENTRY_Z = 37.0                       # the entry's axis: along y through the back wall at x 0, z 37
# ---- terminals (design choices; their conductor range and torque NOT ON FILE (B): IEC 60947-1)
HEAD_R, HEAD_T = 2.2, 1.2            # terminal screw heads Ø4.4 x 1.2 on the front wall's back face (y -42), toward +y
TERMS = (("t-11", -10.0, 50.0), ("t-12", -10.0, 30.0), ("t-23", 10.0, 50.0), ("t-24", 10.0, 30.0))   # node, x, z
LABEL = (-30.0, 30.0, -150.0, -90.0) # label field on the top plate: x0, x1, y0, y1 (decal)
# ---- pedal (design choices)
PEDAL = (41.0, -190.0, -52.0, 30.0, 8.0)   # half width (x ±41), y from ... to, z bottom, thickness (z 30 ... 38)
HINGE = (-56.0, 34.0, 4.0)           # hinge pin axis y, z and radius; the pin spans x ±42, seated on the side walls' inner faces
TRAVEL = 5.0                         # the pedal turns 5 deg toe down when pressed (the toe's underside to z 18.3, above the base's 12)

def build():
    P = Prims(); Y = "M-YELLOW-PA"; K = "M-BLACK-PA"
    w = W / 2; wi = w - SIDE
    P.box(Y, -w, -L, 0.0, W, L, BASE_T)                                                    # base plate
    for sx in (-1, 1):                                                                     # hood side walls, full length
        P.box(Y, wi if sx > 0 else -w, -L, BASE_T, SIDE, L, H - TOP_T - BASE_T)
    P.box(Y, -w, -L, H - TOP_T, W, L, TOP_T)                                               # hood top plate
    yf, yb, zt = HEEL
    back = P.box(Y, -wi, yb - WALL_T, BASE_T, 2 * wi, WALL_T, zt - BASE_T)                 # heel back wall (cable entry)
    P.hole("M-GASKET", (0.0, yb + 0.5, ENTRY_Z), (0.0, yb - WALL_T - 0.5, ENTRY_Z), ENTRY_D / 2, back)   # M20 x 1.5 entry (minor Ø, derived)
    P.box(Y, -wi, yf, BASE_T, 2 * wi, WALL_T, zt - BASE_T)                                 # heel front wall (terminals on its back face)
    P.box(Y, -wi, yf + WALL_T, zt - WALL_T, 2 * wi, (yb - WALL_T) - (yf + WALL_T), WALL_T) # compartment cover
    yi = yf + WALL_T                                                                       # the front wall's back face (y -42)
    for n, x, z in TERMS:                                                                  # terminal screw heads: the port nodes
        P.cyl(f"node:{n}|M-ZINC", (x, yi, z), (x, yi + HEAD_T, z), HEAD_R)
        P.pivot(n, "port", (x, yi + HEAD_T, z), axis=(0, 1, 0), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp
    x0, x1, y0, y1 = LABEL
    P.box("M-WHITE-PA", x0, y0, H, x1 - x0, y1 - y0, 0.6)                                  # label field on the hood's top (decal)
    pw, p0, p1, pz, pt = PEDAL
    hy, hz, hr = HINGE
    P.box(f"node:pedal|{K}", -pw, p0, pz, 2 * pw, p1 - p0, pt)                             # pedal plate (the node's first box: poses.py)
    P.cyl("node:pedal|M-SILVER", (-wi, hy, hz), (wi, hy, hz), hr)                          # hinge pin between the side walls
    P.pivot("pedal", "rotate", (0.0, hy, hz), axis=(1, 0, 0), range=(0, TRAVEL))
    P.collider("env", -w, -L, 0.0, W, L, H + 0.6)
    return P

PREVIEWS = [dict(name="front three-quarter, the hood's opening", az=250, el=20),
            dict(name="rear and cable entry", az=60, el=20),
            dict(name="front, pedal at rest", az=270, el=0),
            dict(name="side, the pedal under the hood", az=0, el=0),
            dict(name="top and label", az=270, el=80, center=(0, -120, 130), height=90)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
