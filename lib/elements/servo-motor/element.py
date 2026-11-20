#!/usr/bin/env python3
"""servo-motor: permanent-magnet synchronous servo motor, 1.0 kW at 3000 min-1 (3.18 N.m), three-phase 400 V 2.5 A, 8 poles,
incremental encoder, square flange 80, plain shaft 19 x 35, no brake. A generic element (OPERATING.md 12, EM 2026-11-07): our own
vendor-neutral design of a product class ETIM 10.0 has no class for, generic by the standard whose rating items its class values
follow (EM 2026-11-08: "no ETIM class; IEC 60034-1 values"; lib/inventory.csv: "flange and shaft a design choice stated as such"),
built to the class values in spec.md "## Class values"; no maker's datasheet (the folder's earlier stub is reference only and was
not used; its record is kept verbatim as the end block of references/source.txt). Sized for servo-drive 1.1 on file (1.0 kW, 3.0 A
continuous, 9.0 A peak, 8-pole up to 400 Hz, incremental encoder fed 5 V): the motor's ratings sit inside the drive's.
What it meets comes from the standards on file: the four flange holes are ISO 273 medium clearance for M6 (lib/standards/holes.csv);
every other size, the flange, spigot and shaft included, is a design choice, said so in spec.md.
Not placed in this version (OPERATING.md 12, quality at the source: a host places only common parts past station 6 and models no
holes for a part it will place later): receptacle-m23 x2 and screw-iso4762 x4 of the inventory's made_of are not built yet. So the
power and encoder connections are two connector seats on the housing (port nodes port-pwr and port-enc, gender none: no contact is
modelled until receptacle-m23 is placed on them, a later version), and the flange's holes are clearance holes for the installer's
M6 screws.
Modelled from the outside in: the square flange with its spigot and four holes, the plain shaft (node `shaft`, rotates), the
housing (its corners relieved behind the flange holes, 1.1), the encoder cover at the back, two connector bosses on top with their seats, a rating-plate field; the stator, rotor,
magnets, bearings and the encoder disc inside are not modelled."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "servo-motor", "1.2", "device"
TITLE = "servo motor 1.0 kW 3000 min-1 3.18 N.m, 3~ 400 V 2.5 A, incremental encoder, square flange 80, shaft 19 x 35 (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic servo motor, 1.0 kW (no ETIM class; IEC 60034-1 values); class values in spec.md; flange holes "
            "ISO 273 medium for M6 (lib/standards/holes.csv); flange, spigot, shaft and every other size are design choices; "
            "receptacle-m23 not built, so the connections are connector seats with their port nodes (spec.md)")
ORIGIN = "flange motor: the flange's mounting face y = 0, shaft axis x = 0, z = 0, shaft toward -y, body toward +y"
COMMAND = "SERVOMTR"
PARAMS = {}

# ---- flange, spigot, shaft (design choices: spec.md Dimensions; lib/inventory.csv "flange and shaft a design choice")
FL, FL_T = 80.0, 10.0                # square flange 80 x 80, 10 thick (y 0 ... 10)
SPIGOT_D, SPIGOT_L = 70.0, 3.0       # spigot (pilot) Ø70, 3 proud of the mounting face (y -3 ... 0)
SHAFT_D, SHAFT_E = 19.0, 35.0        # plain shaft Ø19 (no key), 35 out from the mounting face (y 0 ... -35)
PCD = 90.0                           # four holes on a Ø90 pitch circle, at 45° (x, z = ±31.82)
HOLE_D = 6.6                         # ISO 273 medium clearance for M6 (lib/standards/holes.csv; features.csv)
# ---- housing and encoder cover (design choices)
BODY, BODY_L = 76.0, 130.0           # square housing 76 x 76 (x, z ±38), y 10 ... 140
RELIEF = 24.0                        # 1.1 (review servo-motor-1.0 finding 1): the housing's four corners relieved to ±24 the full length
                                     # (a cross section: a centre box x ±38, z ±24 and two slabs x ±24, z ±24 ... ±38), so each flange hole
                                     # (axis x, z ±31.82) has 7.82 clear to the housing in x and in z behind the flange: room for an M6 head or nut
                                     # (1.2: a design allowance, a head or nut up to Ø12 across its corners; no screw standard on file)
ENC, ENC_L = 70.0, 35.0              # encoder cover 70 x 70, y 140 ... 175
# ---- connector bosses and seats on top (design choices; receptacle-m23 is placed on the seats at a later version)
BOSS, BOSS_H = 30.0, 10.0            # bosses 30 x 30, 10 high on the housing's top (z 38 ... 48)
SEAT_D, SEAT_H = 23.0, 8.0           # seats Ø23 x 8 (z 48 ... 56): the face the receptacle sits on
SEATS = (("port-pwr", "m23-power", 118.0), ("port-enc", "m23-signal", 82.0))   # node, unit, y of the boss centre
# ---- rating-plate field on the housing's +x side (decal; design choice)
PLATE = (40.0, 100.0, -20.0, 20.0)   # y0, y1, z0, z1

def build():
    P = Prims(); A = "M-ALU-ANOD"; K = "M-BLACK-PA"
    h = FL / 2; b = BODY / 2; e = ENC / 2
    fl = P.box(A, -h, 0.0, -h, FL, FL_T, FL)                                                # square flange, mounting face y = 0
    a = PCD / 2 / math.sqrt(2.0)
    for sx in (-1, 1):
        for sz in (-1, 1):                                                                  # four M6 clearance holes, ISO 273 medium
            P.hole("M-GASKET", (sx * a, -0.5, sz * a), (sx * a, FL_T + 0.5, sz * a), HOLE_D / 2, fl)
    P.cyl(A, (0, -SPIGOT_L, 0), (0, 0, 0), SPIGOT_D / 2)                                    # spigot on the mounting face
    P.cyl("node:shaft|M-ZINC", (0, -SPIGOT_L, 0), (0, -SHAFT_E, 0), SHAFT_D / 2)            # plain shaft, seated on the spigot's face
    P.pivot("shaft", "rotate", (0, -SPIGOT_L, 0), axis=(0, -1, 0), range=(0, 360))
    P.box(A, -b, FL_T, -RELIEF, BODY, BODY_L, 2 * RELIEF)                                   # housing, centre (stator inside, not modelled)
    for sz in (-1, 1):                                                                      # housing, top and bottom slabs between the reliefs
        P.box(A, -RELIEF, FL_T, RELIEF if sz > 0 else -b, 2 * RELIEF, BODY_L, b - RELIEF)
    P.box(K, -e, FL_T + BODY_L, -e, ENC, ENC_L, ENC)                                        # encoder cover at the non-drive end
    for node, unit, yc in SEATS:                                                            # connector bosses and seats on top
        P.box(A, -BOSS / 2, yc - BOSS / 2, b, BOSS, BOSS, BOSS_H)
        z0 = b + BOSS_H; z1 = z0 + SEAT_H
        P.cyl(f"node:{node}|{K}", (0, yc, z0), (0, yc, z1), SEAT_D / 2)
        P.pivot(node, "port", (0, yc, z1), axis=(0, 0, 1), range=(0, 0), unit=unit, gender="none")   # PIN-002: no contact modelled yet
    y0, y1, z0, z1 = PLATE
    P.box("M-WHITE-PA", b, y0, z0, 0.6, y1 - y0, z1 - z0)                                   # rating-plate field (decal)
    P.collider("env", -h, -SHAFT_E, -h, FL, SHAFT_E + FL_T + BODY_L + ENC_L, h + b + BOSS_H + SEAT_H)
    return P

PREVIEWS = [dict(name="drive end three-quarter", az=250, el=20),
            dict(name="non-drive end and connector seats", az=60, el=30),
            dict(name="flange face and holes", az=270, el=0, center=(0, 0, 0), height=100),
            dict(name="side and rating plate", az=0, el=10)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
