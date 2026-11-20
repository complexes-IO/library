#!/usr/bin/env python3
"""flow-meter: a liquid flow meter, in line, two female NPT 3/8 ports, volume flow 1 to 20 l/min, with a transmitter in its head:
output 4-20 mA on a two-wire loop powered at 24 V DC (terminals 1 = loop +, 2 = loop -), an AI 4-20 mA into the PLC's analogue
input as pt 1.1's and tt-rtd 1.0's: the flow reading of the calibration bench, the heat-exchanger loop, the process skid and the
test benches (lib/inventory.csv row `flow-meter`, 6 systems). A generic element (OPERATING.md 12, EM 2026-11-07): our own
vendor-neutral design of the ETIM 10.0 class EC010586 "Liquid flow meter", built to the class values in spec.md "## Class values";
no maker's datasheet and no product is matched (lib/inventory.csv row `flow-meter`, own_design generic).
What it meets: a male NPT 3/8 stub in each end face, as flow-control-inline 1.0 and valve-needle 2.0 meet theirs: each port a plain
bore at E1 + h, L2 + 2 deep, from pneu.NPT (calculated from ASME B1.20.1's formulas, EM 2026-11-07), its pivot on its number field's
outer face. The cable entry is M20 x 1.5 tapped, its minor diameter derived (derive.thread, ISO 68-1 / ISO 965-1), as pt 1.1's.
Not placed in this version (OPERATING.md 12, quality at the source): no part (the inventory row lists none); the installer's cable
gland; the measuring element in the flow and the transmitter's electronics inside. The passage between the two bores is not drawn.
Modelled from the line up: the body block on the port axis with its two bored end faces and their number fields (the port nodes),
a flow-arrow field on its front face, a neck on its top face, then tt-rtd 1.0's terminal head as a frame (a bottom plate, two side
walls, the +x one thick enough to carry the cable entry, a back wall, a top plate) round a terminal compartment closed by a front
cover; two terminal screw heads on the back wall (the port nodes t-1, t-2). Nothing moves: the twin reads the loop's states
(behaviour.csv)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "flow-meter", "1.0", "device"
TITLE = "liquid flow meter, in line, NPT 3/8 female x 2, 1-20 l/min, 10 bar, 4-20 mA two-wire loop at 24 V DC, M20 x 1.5 entry (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Liquid flow meter (ETIM 10.0 EC010586); class values in spec.md; ports NPT 3/8 female "
            "(toolkit/pneu.py D1), bored at E1 + h from pneu.NPT (calculated from ASME B1.20.1's formulas); cable entry M20 x 1.5 "
            "derived (ISO 68-1 / ISO 965-1); body, neck and head sizes are design choices; the terminals' conductor range and "
            "torque and the loop's lift-off voltage are open (spec.md)")
ORIGIN = ("in line: port-1's end face centre on the port axis (port-1's pivot 0.2 out, on its number field); the port axis is the x "
          "axis, the flow along +x from port-1 to port-2, the terminal head toward +z, its front cover toward -y")
COMMAND = "FLOWMETER"
PARAMS = {}

# ---- what it meets (elements and standards on file)
PORT = "NPT3/8"                      # design choice within pneu.THREADS (D1): class values "Connection 1" and "Connection 2"
ENTRY_D = 18.3762                    # M20 x 1.5 internal thread's minor diameter D1, derived: derive.thread(20.0, 1.5) (ISO 68-1, ISO 965-1)
P_MAX_KPA = 1000.0                   # class value 14 "Max. operating pressure at 20 °C" (ratings.csv p_max, generic design)
_T = pneu.NPT[PORT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4      # 17.055 for NPT 3/8: the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # L2 (10.358) + 2: design choice, a run-out past the male's effective thread (flow-control-inline 1.0)
# ---- body (design choices: spec.md Dimensions)
BODY = (70.0, 32.0, 32.0)            # along the port axis (x), across (y), high (z); centred on the axis in y and z
FIELD, FIELD_T = 22.0, 0.2           # port-number field (decal), centred on the bore, 0.2 proud of the end face
ARROW = (30.0, 10.0)                 # flow-arrow field on the body's front face (x by z), 0.2 proud
IN = 0.5                             # the neck runs 0.5 into the body and into the head (one solid joint each)
NECK_D = 12.0                        # neck between the body's top face and the head
X_C = BODY[0] / 2.0                  # 35: the neck's and the head's axis over the body's centre
Z_TOP = BODY[2] / 2.0                # 16: the body's top face
# ---- terminal head: tt-rtd 1.0's (pt 1.1's raised on a neck), about x = X_C (design choices: spec.md Dimensions)
HEAD = dict(x=20.0, y=18.0, z=(40.0, 76.0))  # terminal head x X_C ±20, y ±18, z 40 ... 76
PLATE = 6.0                          # bottom plate z 40 ... 46, top plate z 70 ... 76
WALL, WALL_E, BACK, COVER = 4.0, 8.0, 4.0, 3.0   # -x wall 4, +x wall 8 (carries the entry), back wall y 14 ... 18, front cover y -18 ... -15
ENTRY = (0.0, 58.0)                  # (y, z) of the entry's axis, along x through the +x wall into the compartment
# ---- terminals (design choices; their conductor range and torque NOT ON FILE (B): IEC 60947-1)
HEAD_R, HEAD_T = 2.2, 1.2            # terminal screw heads Ø4.4 x 1.2 on the back wall's front face (y 14)
TERMS = (("t-1", -7.0, 58.0), ("t-2", 3.0, 58.0))   # node, x from X_C, z: loop + and loop -
LABEL = (-12.0, 12.0, 50.0, 66.0)    # label field on the cover: x0, x1 from X_C, z0, z1 (decal)
MAT, MAT_NECK, MAT_HEAD, FIELDM = "M-BRASS", "M-SILVER", "M-GREY-PA", "M-WHITE-PA"

assert PORT in pneu.THREADS
assert BORE_L >= pneu.NPT[PORT]["engagement"]                         # deeper than a male's make-up (L1 + L3)
assert 2 * BORE_L + 10.0 <= BODY[0]                                   # the two blind bores leave at least 10 of body between their floors
assert min(BODY[1], BODY[2]) - BORE_D >= 2 * 5.0                      # at least 5 of body wall round each bore
assert FIELD > BORE_D + 2.0 and FIELD < min(BODY[1], BODY[2])         # the field rings the bore, inside the end face
assert P_MAX_KPA >= pneu.P_SUPPLY                                     # PNE-003 (kPa): 1000 above a bench drop's 689.5, should a bench place it in air
assert NECK_D < BODY[1] and NECK_D < 2 * HEAD["y"]                    # the neck inside the body's top face, under the head
assert HEAD["z"][0] - Z_TOP >= 20.0                                   # the head stands clear of the body (a wrench on the line's fittings)
assert HEAD["x"] < X_C                                                # the head inside the body's length
assert ARROW[0] < BODY[0] and ARROW[1] < BODY[2]                      # the arrow field inside the front face
assert ENTRY_D / 2 < min(ENTRY[1] - HEAD["z"][0] - PLATE, HEAD["z"][1] - PLATE - ENTRY[1])   # the entry inside the +x wall's height
assert all(-HEAD["x"] + WALL + HEAD_R < x < HEAD["x"] - WALL_E - HEAD_R for _, x, _ in TERMS)  # heads inside the compartment
assert TERMS[1][1] - TERMS[0][1] > 2 * HEAD_R + 4.0                   # the two heads clear of each other (a screwdriver between)


def _port(P, body, name, x, out):
    """a female NPT 3/8 port on an end face: the plain bore into the body, its number field (the node) with the bore through it, and
    the pivot on the field's outer face, its axis out of the body toward the counterpart (pneu.py port frame; flow-control-inline 1.0)"""
    P.hole("M-GASKET", (x - out, 0, 0), (x + out * BORE_L, 0, 0), BORE_D / 2, body)
    h = FIELD / 2
    f = P.box(f"node:{name}|{FIELDM}", min(x, x - out * FIELD_T), -h, -h, FIELD_T, FIELD, FIELD)
    P.hole("M-GASKET", (x - out * (FIELD_T + 1.0), 0, 0), (x + out * 1.0, 0, 0), BORE_D / 2, f)
    P.pivot(name, "port", (x - out * FIELD_T, 0, 0), axis=(-out, 0, 0), range=(0, 0), unit=PORT, gender="female", role="work")


def build():
    P = Prims(); L, W, H = BODY; G = MAT_HEAD
    body = P.box(MAT, 0, -W / 2, -H / 2, L, W, H)                                              # body block on the port axis
    _port(P, body, "port-1", 0.0, 1)                                                           # inlet
    _port(P, body, "port-2", L, -1)                                                            # outlet
    P.box(FIELDM, X_C - ARROW[0] / 2, -W / 2 - FIELD_T, -ARROW[1] / 2, ARROW[0], FIELD_T, ARROW[1])   # flow arrow 1 -> 2 (decal)
    hx, hy = HEAD["x"], HEAD["y"]; z0, z1 = HEAD["z"]; zi0, zi1 = z0 + PLATE, z1 - PLATE; ch = zi1 - zi0
    P.cyl(MAT_NECK, (X_C, 0, Z_TOP - IN), (X_C, 0, z0 + IN), NECK_D / 2.0)                     # neck, 0.5 into the body and the head
    yc = -hy + COVER                                                                           # the compartment's front (cover's back face)
    P.box(G, X_C - hx, -hy, z0, 2 * hx, 2 * hy, PLATE)                                         # bottom plate
    P.box(G, X_C - hx, yc, zi0, WALL, hy - yc, ch)                                             # -x side wall
    ew = P.box(G, X_C + hx - WALL_E, yc, zi0, WALL_E, hy - yc, ch)                             # +x side wall, carries the entry
    ey, ez = ENTRY
    P.hole("M-GASKET", (X_C + hx - WALL_E - 0.5, ey, ez), (X_C + hx + 0.5, ey, ez), ENTRY_D / 2, ew)   # M20 x 1.5 cable entry (minor Ø, derived)
    yb = hy - BACK
    P.box(G, X_C - hx + WALL, yb, zi0, 2 * hx - WALL - WALL_E, BACK, ch)                       # back wall (terminals on its front face)
    P.box(G, X_C - hx, -hy, zi0, 2 * hx, COVER, ch)                                            # front cover over the compartment
    P.box(G, X_C - hx, -hy, zi1, 2 * hx, 2 * hy, PLATE)                                        # top plate
    for n, x, z in TERMS:                                                                      # terminal screw heads: the port nodes
        P.cyl(f"node:{n}|M-ZINC", (X_C + x, yb, z), (X_C + x, yb - HEAD_T, z), HEAD_R)
        P.pivot(n, "port", (X_C + x, yb - HEAD_T, z), axis=(0, -1, 0), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp
    x0, x1, lz0, lz1 = LABEL
    P.box(FIELDM, X_C + x0, -hy - 0.6, lz0, x1 - x0, 0.6, lz1 - lz0)                           # label field on the cover (decal)
    P.collider("env", -FIELD_T, -hy - 0.6, -H / 2, L + 2 * FIELD_T, 2 * hy + 0.6, z1 + H / 2)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear and cable entry", az=60, el=20),
            dict(name="front", az=270, el=0),
            dict(name="port-1", az=190, el=10, center=(0, 0, 0), height=50),
            dict(name="front cover and label", az=270, el=0, center=(35, -15, 58), height=40)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
