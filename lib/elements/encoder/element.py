#!/usr/bin/env python3
"""encoder: incremental rotary encoder, optical, 1024 pulses per revolution, push-pull (HTL) outputs A, B and the zero pulse N fed
24 V DC, construction size 58 (housing Ø58), solid shaft Ø10, three M4 tapped mounting holes in the front face, an axial M12
connector seat at the back. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0
class EC001486 "Rotary encoder", built to the class values in spec.md "## Class values"; no maker's datasheet (the folder's earlier
stub is reference only and was not used; its record is kept verbatim as the end block of references/source.txt).
What it meets comes from the standards on file: the three mounting holes are M4 x 0.7 tapped, their minor diameter derived
(derive.thread, ISO 68-1 / ISO 965-1). Every other size, the housing, spigot and shaft included, is a design choice, said so in
spec.md; the shaft's and the spigot's fit tolerances are a standard's table not on file (spec.md Dimensions).
Not placed in this version (OPERATING.md 12, quality at the source: a host places only common parts past station 6): receptacle-m12
(built, not yet past station 6), coupling-shaft and screw-iso4762 x3 of the inventory's made_of (not built). So the connection is a
connector seat on the back (port node port-x1, gender none: no contact is modelled until receptacle-m12 is placed on it, a later
version), the holes are bare tapped holes for the installer's M4 screws, and the shaft is plain for the installer's coupling.
Modelled from the outside in: the housing (front face = the mounting face, with the three tapped holes), the spigot on the front
face, the shaft (node `shaft`, rotates), a boss and the connector seat on the back face, a label field; the code disc, the optics
and the bearings inside are not modelled."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "encoder", "1.1", "device"
TITLE = "rotary encoder, incremental, optical, 1024 ppr, push-pull HTL A B N, 24 V DC, size 58, solid shaft 10, axial M12 seat (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Rotary encoder (ETIM 10.0 EC001486); class values in spec.md; mounting holes M4 x 0.7 tapped, "
            "minor diameter derived (ISO 68-1 / ISO 965-1); housing, spigot, shaft and every other size are design choices; "
            "receptacle-m12 not past station 6, so the connection is a connector seat with its port node (spec.md)")
ORIGIN = "the housing's front (mounting) face y = 0, shaft axis x = 0, z = 0, shaft toward -y, housing toward +y"
COMMAND = "ENCODER"
PARAMS = {}

# ---- housing, spigot, shaft (design choices: spec.md Dimensions)
BODY_D, BODY_L = 58.0, 42.0          # housing Ø58 (construction size 58, Class values 7), y 0 ... 42
SPIGOT_D, SPIGOT_L = 36.0, 3.0       # spigot (centring collar) Ø36, 3 proud of the mounting face (y -3 ... 0)
SHAFT_D, SHAFT_E = 10.0, 20.0        # solid shaft Ø10 (Class values 14), 20 out from the mounting face (y -3 ... -20 beyond the spigot)
# ---- what it meets (standards on file)
TAP_D = 3.2422                       # M4 x 0.7 internal thread's minor diameter D1, derived: derive.thread(4.0, 0.7) (ISO 68-1, ISO 965-1)
TAP_DEPTH = 6.0                      # tapped depth into the housing from the mounting face (design choice)
PCD = 48.0                           # three holes on a Ø48 pitch circle, at 90, 210 and 330 deg (one on top, +z) (design choice)
# ---- connector boss and seat on the back face (design choices; receptacle-m12 is placed on the seat at a later version)
BOSS_D, BOSS_L = 20.0, 6.0           # boss Ø20, y 42 ... 48
SEAT_D, SEAT_L = 16.0, 4.0           # seat Ø16, y 48 ... 52: the face the receptacle sits on
# ---- label field on the back face, below the boss (decal; design choice)
LABEL = (-12.0, 12.0, -24.0, -13.0)  # x0, x1, z0, z1

def build():
    P = Prims(); A = "M-ALU-ANOD"; K = "M-BLACK-PA"
    r = BODY_D / 2
    body = P.cyl(A, (0, 0, 0), (0, BODY_L, 0), r)                                           # housing; its front face is the mounting face
    for deg in (90.0, 210.0, 330.0):                                                         # three M4 tapped holes (minor Ø, derived)
        a = math.radians(deg); x = PCD / 2 * math.cos(a); z = PCD / 2 * math.sin(a)
        P.hole("M-GASKET", (x, -0.5, z), (x, TAP_DEPTH, z), TAP_D / 2, body)
    P.cyl(A, (0, -SPIGOT_L, 0), (0, 0, 0), SPIGOT_D / 2)                                    # spigot on the mounting face
    P.cyl("node:shaft|M-ZINC", (0, -SPIGOT_L, 0), (0, -SHAFT_E, 0), SHAFT_D / 2)            # solid shaft, seated on the spigot's face
    P.pivot("shaft", "rotate", (0, -SPIGOT_L, 0), axis=(0, -1, 0), range=(0, 360))
    y0 = BODY_L
    P.cyl(K, (0, y0, 0), (0, y0 + BOSS_L, 0), BOSS_D / 2)                                    # connector boss on the back face
    y1 = y0 + BOSS_L; y2 = y1 + SEAT_L
    P.cyl(f"node:port-x1|{K}", (0, y1, 0), (0, y2, 0), SEAT_D / 2)                           # connector seat (receptacle-m12 later)
    P.pivot("port-x1", "port", (0, y2, 0), axis=(0, 1, 0), range=(0, 0), unit="m12-a", gender="none")   # PIN-002: no contact modelled yet
    x0, x1, z0, z1 = LABEL
    P.box("M-WHITE-PA", x0, y0, z0, x1 - x0, 0.6, z1 - z0)                                  # label field (decal)
    P.collider("env", -r, -SHAFT_E, -r, BODY_D, SHAFT_E + y2, BODY_D)
    return P

PREVIEWS = [dict(name="shaft end three-quarter", az=250, el=20),
            dict(name="back, connector seat and label", az=60, el=20),
            dict(name="mounting face and holes", az=270, el=0, center=(0, 0, 0), height=70),
            dict(name="side", az=0, el=0)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
