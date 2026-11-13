#!/usr/bin/env python3
"""pt: a pressure transmitter for hydraulic oil, measuring range 0 to 250 bar, output 4-20 mA on a two-wire loop powered at 24 V DC
(terminals 1 = loop +, 2 = loop -): the press-hydraulic machine's pressure reading (lib/assemblies/press-hydraulic/controls.csv row
pressure, an AI 4-20 mA into the PLC for the HMI's reading and the over-pressure alarm; hydraulic.csv: it tees off the P line at the
HPU's gauge port, beside the gauge and the pressure switch). A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral
design of the ETIM 10.0 class EC011478 "Pressure transmitter", built to the class values in spec.md "## Class values"; no maker's
datasheet and no product is matched (lib/inventory.csv row `pt`, own_design generic, pin 11).
What it meets: the host's gauge port, as hyd-gauge 1.1 and pressure-switch 1.0 meet it: the stem's hex seat face is the joint plane and
the port node `port-p` (unit "hyd-port", male, role gauge), the hex's corners inside the Ø24 spot face of hpu-7.5kw's and
hyd-cylinder-da-40's ports. No hydraulic port standard is on file (ISO 6149, SAE J1926), so the stem's thread and length are an open
class B figure and no stub is drawn below the seat face (a major adds it once the standard is on file). The cable entry is M20 x 1.5
tapped, its minor diameter derived (derive.thread, ISO 68-1 / ISO 965-1), as pressure-switch 1.0's and limit-switch 1.0's.
Not placed in this version (OPERATING.md 12, quality at the source): the receptacle-m12 the inventory row lists as its part (not past
station 6), so this is the cable-entry form with screw clamps, as pressure-switch 1.0; the installer's cable gland; the sensing cell
and its electronics inside.
Modelled from the stem up: the hex (the port node), a neck, the round sensor body, then the terminal head as a frame (a bottom plate,
two side walls, the +x one thick enough to carry the cable entry, a back wall, a top plate) round a terminal compartment closed by a
front cover; two terminal screw heads on the back wall (the port nodes t-1, t-2). Nothing moves: the twin reads the loop's states
(behaviour.csv)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "pt", "1.0", "device"
TITLE = "pressure transmitter for hydraulic oil, 0-250 bar, 4-20 mA two-wire loop at 24 V DC, M20 x 1.5 entry (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Pressure transmitter (ETIM 10.0 EC011478); class values in spec.md; the stem meets a host's gauge "
            "port as hyd-gauge 1.1 and pressure-switch 1.0 (hyd-port, its thread open: no hydraulic port standard on file); cable entry "
            "M20 x 1.5 derived (ISO 68-1 / ISO 965-1); body and head sizes are design choices; the terminals' conductor range and torque "
            "and the loop's lift-off voltage are open (spec.md)")
ORIGIN = "joint plane: the hex's seat face z = 0 on the stem's axis (x = y = 0); the host's port toward -z, the terminal head up, its front cover toward -y"
COMMAND = "PTRANS"
PARAMS = {}

# ---- what it meets (elements and standards on file)
HOST_SPOT_D = 24.0                   # hpu-7.5kw's and hyd-cylinder-da-40's port spot face (their element.py SPOT_D): the seat face lands on it
HEX_AF, HEX_L, HEX_D = 15.0, 9.0, 1.12   # design choices, hyd-gauge 1.1's and pressure-switch 1.0's: wrench flats, length, corners 1.12 x AF
ENTRY_D = 18.3762                    # M20 x 1.5 internal thread's minor diameter D1, derived: derive.thread(20.0, 1.5) (ISO 68-1, ISO 965-1)
# ---- body (design choices: spec.md Dimensions)
IN = 0.5                             # each fixed part runs 0.5 into the one it sits on (one solid joint)
NECK_D = 12.0                        # neck between the hex and the sensor body
BODY_D, BODY_Z = 27.0, (13.0, 60.0)  # round sensor body (sensing cell and electronics inside, not modelled)
HEAD = dict(x=20.0, y=18.0, z=(60.0, 96.0))  # terminal head x ±20, y ±18, z 60 ... 96
PLATE = 6.0                          # bottom plate z 60 ... 66, top plate z 90 ... 96
WALL, WALL_E, BACK, COVER = 4.0, 8.0, 4.0, 3.0   # -x wall 4, +x wall 8 (carries the entry), back wall y 14 ... 18, front cover y -18 ... -15
ENTRY = (0.0, 78.0)                  # (y, z) of the entry's axis, along x through the +x wall into the compartment
# ---- terminals (design choices; their conductor range and torque NOT ON FILE (B): IEC 60947-1)
HEAD_R, HEAD_T = 2.2, 1.2            # terminal screw heads Ø4.4 x 1.2 on the back wall's front face (y 14)
TERMS = (("t-1", -7.0, 78.0), ("t-2", 3.0, 78.0))   # node, x, z: loop + and loop -
LABEL = (-12.0, 12.0, 70.0, 86.0)    # label field on the cover: x0, x1, z0, z1 (decal)

assert HEX_AF * HEX_D < HOST_SPOT_D                                   # the hex's corners sit inside a host's spot face
assert NECK_D < HEX_AF and NECK_D < BODY_D and BODY_D < 2 * HEAD["y"] # neck inside the flats, body under the head
assert ENTRY_D / 2 < min(ENTRY[1] - HEAD["z"][0] - PLATE, HEAD["z"][1] - PLATE - ENTRY[1])   # the entry inside the +x wall's height
assert all(-HEAD["x"] + WALL + HEAD_R < x < HEAD["x"] - WALL_E - HEAD_R for _, x, _ in TERMS)  # heads inside the compartment
assert TERMS[1][1] - TERMS[0][1] > 2 * HEAD_R + 4.0                   # the two heads clear of each other (a screwdriver between)


def _hex_z(P, L, z0, z1, af, d):
    """a hex prism on the z axis: a cylinder of diameter d with six flats cut at af / 2 (hyd-gauge 1.1's and pressure-switch 1.0's pattern)"""
    c = P.cyl(L, (0, 0, z0), (0, 0, z1), d / 2.0); w = d + 4.0
    for k in range(6):
        t = math.radians(30 + 60 * k); n = (math.cos(t), math.sin(t), 0.0); tg = (-math.sin(t), math.cos(t), 0.0)
        o = (n[0] * af / 2.0 + tg[0] * w / 2.0, n[1] * af / 2.0 + tg[1] * w / 2.0, z0 - 1.0)
        P.cut(L, o, n, (0, 0, 1), (-tg[0], -tg[1], 0.0), 4.0, abs(z1 - z0) + 2.0, w, c)
    return c


def build():
    P = Prims(); S = "M-SILVER"; G = "M-GREY-PA"
    _hex_z(P, "node:port-p|M-ZINC", 0.0, HEX_L, HEX_AF, HEX_AF * HEX_D)                         # hex, seat face on z = 0
    b0, b1 = BODY_Z
    P.cyl(S, (0, 0, HEX_L - IN), (0, 0, b0 + IN), NECK_D / 2.0)                                # neck
    P.cyl(S, (0, 0, b0), (0, 0, b1 + IN), BODY_D / 2.0)                                       # sensor body, 0.5 into the head
    hx, hy = HEAD["x"], HEAD["y"]; z0, z1 = HEAD["z"]; zi0, zi1 = z0 + PLATE, z1 - PLATE; ch = zi1 - zi0
    yc = -hy + COVER                                                                           # the compartment's front (cover's back face)
    P.box(G, -hx, -hy, z0, 2 * hx, 2 * hy, PLATE)                                              # bottom plate
    P.box(G, -hx, yc, zi0, WALL, hy - yc, ch)                                                  # -x side wall
    ew = P.box(G, hx - WALL_E, yc, zi0, WALL_E, hy - yc, ch)                                   # +x side wall, carries the entry
    ey, ez = ENTRY
    P.hole("M-GASKET", (hx - WALL_E - 0.5, ey, ez), (hx + 0.5, ey, ez), ENTRY_D / 2, ew)        # M20 x 1.5 cable entry (minor Ø, derived)
    yb = hy - BACK
    P.box(G, -hx + WALL, yb, zi0, 2 * hx - WALL - WALL_E, BACK, ch)                            # back wall (terminals on its front face)
    P.box(G, -hx, -hy, zi0, 2 * hx, COVER, ch)                                                 # front cover over the compartment
    P.box(G, -hx, -hy, zi1, 2 * hx, 2 * hy, PLATE)                                             # top plate
    for n, x, z in TERMS:                                                                      # terminal screw heads: the port nodes
        P.cyl(f"node:{n}|M-ZINC", (x, yb, z), (x, yb - HEAD_T, z), HEAD_R)
        P.pivot(n, "port", (x, yb - HEAD_T, z), axis=(0, -1, 0), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp
    x0, x1, lz0, lz1 = LABEL
    P.box("M-WHITE-PA", x0, -hy - 0.6, lz0, x1 - x0, 0.6, lz1 - lz0)                           # label field on the cover (decal)
    P.pivot("port-p", "port", (0, 0, 0), axis=(0, 0, -1), range=(0, 0), unit="hyd-port", gender="male", role="gauge")
    P.collider("env", -hx, -hy - 0.6, 0.0, 2 * hx, 2 * hy + 0.6, z1)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear and cable entry", az=60, el=20),
            dict(name="front", az=270, el=0),
            dict(name="stem and hex", az=230, el=-40, center=(0, 0, 10), height=40),
            dict(name="front cover and label", az=270, el=0, center=(0, -15, 78), height=40)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
