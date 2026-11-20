#!/usr/bin/env python3
"""tt-rtd: a temperature transmitter with a Pt100 resistance thermometer in its probe, measuring range 0 to 200 °C, output 4-20 mA on a
two-wire loop powered at 24 V DC (terminals 1 = loop +, 2 = loop -): the process temperature reading of the heat-exchanger loop, the
cure ovens, the process skids and the test benches (lib/inventory.csv row `tt-rtd`, 8 systems), an AI 4-20 mA into the PLC's analogue
input as pt 1.0's. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC002919
"Temperature transformer" (synonym "Temperature transmitter"), built to the class values in spec.md "## Class values"; no maker's
datasheet and no product is matched (lib/inventory.csv row `tt-rtd`, own_design generic).
What it meets: a host's female NPT 1/4 port that bores through into the medium, as gauge-t 1.2 meets it: the hex's seat face is the
joint plane, a male NPT 1/4 stub below it (`port-1`, role gauge) drawn as gauge-t draws its stub, a plain cylinder at E1 + h, length
L2, both from pneu.NPT (calculated from ASME B1.20.1's formulas, EM 2026-11-07), and below the stub the probe's sheath that carries the
Pt100 element into the medium. The cable entry is M20 x 1.5 tapped, its minor diameter derived (derive.thread, ISO 68-1 / ISO 965-1),
as pt 1.0's and pressure-switch 1.0's.
Not placed in this version (OPERATING.md 12, quality at the source): the receptacle-m12 the inventory row lists as its part (not past
station 6), so this is the cable-entry form with screw clamps, as pt 1.0; the installer's cable gland; the Pt100 element and the
transmitter's electronics inside.
Modelled from the probe up: the sheath, the NPT stub and the hex (the port node), an extension neck that keeps the head off the
process, then pt 1.0's terminal head as a frame (a bottom plate, two side walls, the +x one thick enough to carry the cable entry, a
back wall, a top plate) round a terminal compartment closed by a front cover; two terminal screw heads on the back wall (the port
nodes t-1, t-2). Nothing moves: the twin reads the loop's states (behaviour.csv)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "tt-rtd", "1.0", "device"
TITLE = "temperature transmitter with Pt100 probe, 0-200 C, 4-20 mA two-wire loop at 24 V DC, NPT 1/4 male, M20 x 1.5 entry (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Temperature transformer (ETIM 10.0 EC002919, synonym temperature transmitter); class values in "
            "spec.md; the stem meets a host's female NPT 1/4 port as gauge-t 1.2 (pneu.NPT, calculated from ASME B1.20.1's formulas); "
            "cable entry M20 x 1.5 derived (ISO 68-1 / ISO 965-1); probe, neck and head sizes are design choices; the terminals' "
            "conductor range and torque and the loop's lift-off voltage are open (spec.md)")
ORIGIN = "joint plane: the hex's seat face z = 0 on the stem's axis (x = y = 0); the host's port and the probe toward -z, the terminal head up, its front cover toward -y"
COMMAND = "TTRTD"
PARAMS = {}

# ---- what it meets (elements and standards on file)
PORT = "NPT1/4"                      # pneu.THREADS (D1); a host's gauge port, as gauge-t 1.2 and gauge-p
ENTRY_D = 18.3762                    # M20 x 1.5 internal thread's minor diameter D1, derived: derive.thread(20.0, 1.5) (ISO 68-1, ISO 965-1)
# ---- probe and stem (design choices: spec.md Dimensions)
INSERT_L, SHEATH_D = 100.0, 6.0      # insertion length below the seat face; the probe's sheath Ø (the Pt100 element at its tip, not modelled)
HEX_AF, HEX_L, HEX_D = 15.0, 9.0, 1.12   # wrench flats, length, corners 1.12 x AF: gauge-t 1.2's
IN = 0.5                             # each fixed part runs 0.5 into the one it sits on (one solid joint)
NECK_D = 12.0                        # extension neck between the hex and the head (keeps the head off the process)
# ---- terminal head: pt 1.0's, raised on the neck (design choices: spec.md Dimensions)
HEAD = dict(x=20.0, y=18.0, z=(40.0, 76.0))  # terminal head x ±20, y ±18, z 40 ... 76
PLATE = 6.0                          # bottom plate z 40 ... 46, top plate z 70 ... 76
WALL, WALL_E, BACK, COVER = 4.0, 8.0, 4.0, 3.0   # -x wall 4, +x wall 8 (carries the entry), back wall y 14 ... 18, front cover y -18 ... -15
ENTRY = (0.0, 58.0)                  # (y, z) of the entry's axis, along x through the +x wall into the compartment
# ---- terminals (design choices; their conductor range and torque NOT ON FILE (B): IEC 60947-1)
HEAD_R, HEAD_T = 2.2, 1.2            # terminal screw heads Ø4.4 x 1.2 on the back wall's front face (y 14)
TERMS = (("t-1", -7.0, 58.0), ("t-2", 3.0, 58.0))   # node, x, z: loop + and loop -
LABEL = (-12.0, 12.0, 50.0, 66.0)    # label field on the cover: x0, x1, z0, z1 (decal)

assert PORT in pneu.THREADS
_T = pneu.NPT[PORT]["table"]
assert HEX_AF > (_T["E2"] + _T["h"]) * 25.4                           # the flats clear the thread's largest major diameter (E2 + h)
assert SHEATH_D < (_T["E1"] + _T["h"]) * 25.4 and INSERT_L > pneu.NPT[PORT]["length"] + 10.0   # the sheath leaves the stub below it
assert NECK_D < HEX_AF and NECK_D < 2 * HEAD["y"]                     # neck inside the flats, under the head
assert ENTRY_D / 2 < min(ENTRY[1] - HEAD["z"][0] - PLATE, HEAD["z"][1] - PLATE - ENTRY[1])   # the entry inside the +x wall's height
assert all(-HEAD["x"] + WALL + HEAD_R < x < HEAD["x"] - WALL_E - HEAD_R for _, x, _ in TERMS)  # heads inside the compartment
assert TERMS[1][1] - TERMS[0][1] > 2 * HEAD_R + 4.0                   # the two heads clear of each other (a screwdriver between)


def stub():
    """(diameter, length) of the NPT male stub in mm from pneu.NPT: E1 + h and L2 (gauge-t 1.2's rule)"""
    return (_T["E1"] + _T["h"]) * 25.4, pneu.NPT[PORT]["length"]


def _hex_z(P, L, z0, z1, af, d):
    """a hex prism on the z axis: a cylinder of diameter d with six flats cut at af / 2 (gauge-t 1.2's and pt 1.0's pattern)"""
    c = P.cyl(L, (0, 0, z0), (0, 0, z1), d / 2.0); w = d + 4.0
    for k in range(6):
        t = math.radians(30 + 60 * k); n = (math.cos(t), math.sin(t), 0.0); tg = (-math.sin(t), math.cos(t), 0.0)
        o = (n[0] * af / 2.0 + tg[0] * w / 2.0, n[1] * af / 2.0 + tg[1] * w / 2.0, z0 - 1.0)
        P.cut(L, o, n, (0, 0, 1), (-tg[0], -tg[1], 0.0), 4.0, abs(z1 - z0) + 2.0, w, c)
    return c


def build():
    P = Prims(); S = "M-SILVER"; G = "M-GREY-PA"; sd, sl = stub()
    P.cyl(f"node:port-1|{S}", (0, 0, -sl), (0, 0, IN), sd / 2.0)                                # NPT male stub, L2 below the seat face
    _hex_z(P, f"node:port-1|{S}", 0.0, HEX_L, HEX_AF, HEX_AF * HEX_D)                           # hex, seat face on z = 0
    P.cyl(S, (0, 0, -INSERT_L), (0, 0, -sl + IN), SHEATH_D / 2.0)                              # probe sheath below the stub
    hx, hy = HEAD["x"], HEAD["y"]; z0, z1 = HEAD["z"]; zi0, zi1 = z0 + PLATE, z1 - PLATE; ch = zi1 - zi0
    P.cyl(S, (0, 0, HEX_L - IN), (0, 0, z0 + IN), NECK_D / 2.0)                                # extension neck, 0.5 into the head
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
    P.pivot("port-1", "port", (0, 0, 0), axis=(0, 0, -1), range=(0, 0), unit=PORT, gender="male", role="gauge", length=round(sl, 3))
    P.collider("env", -hx, -hy - 0.6, -INSERT_L, 2 * hx, 2 * hy + 0.6, z1 + INSERT_L)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear and cable entry", az=60, el=20),
            dict(name="front", az=270, el=0),
            dict(name="stem and hex", az=230, el=-30, center=(0, 0, 0), height=40),
            dict(name="front cover and label", az=270, el=0, center=(0, -15, 58), height=40)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
