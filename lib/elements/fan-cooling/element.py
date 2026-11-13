#!/usr/bin/env python3
"""fan-cooling: an axial cooling fan, 60 x 60 x 25, 24 V DC, the fan a drive or a rack unit blows through its heat sink with
(lib/inventory.csv row `fan-cooling`, own_design generic, a common part: vfd-0.75kw, servo-drive and ups-rack list it in made_of).
A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC001143 (the inventory row's class;
its nine features are in lib/standards/etim/class-features.csv, its name is not in the classes.csv subset, so the inventory's type
"cooling fan, 24 V DC" names it here), built to the class values in spec.md "## Class values"; no maker's datasheet and no product
is matched.
What it meets: the host's wall or heat sink, on four M4 screws through clearance holes (ISO 273 medium, lib/standards/holes.csv) at
the corners; the frame's inlet face (y = 0) is the joint plane. The 60 mm frame and the 50 mm hole pitch are design choices (no fan
frame standard is on file), chosen so the frame fits inside vfd-0.75kw's 72 mm width.
Modelled: a square frame with a round bore (the venturi), the motor's stator boss held on four struts at the outlet face, and the
impeller (node `impeller`: a hub and five pitched blades) that turns about the fan's axis y; a terminal block on the frame's +x side
with two screw clamps (port nodes t-1 = +24 V, t-2 = 0 V); a label field on the -x side. Not modelled: the motor's windings and
electronics inside the hub, a finger guard, the leads a maker's fan would carry instead of clamps. Air flows toward +y."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "fan-cooling", "1.0", "device"
TITLE = "axial cooling fan 60 x 60 x 25, 24 V DC, impeller Ø52, screw clamps 1 + / 2 -, 4 x M4 clearance holes (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic cooling fan (ETIM 10.0 EC001143); class values in spec.md; 4 x M4 clearance holes ISO 273 "
            "medium (lib/standards/holes.csv); frame, hole pitch, impeller and terminal block sizes are design choices; the screw "
            "clamps' conductor range and torque are open (spec.md); no airflow, noise or safety claim")
ORIGIN = "the frame's inlet face y = 0 on the fan's axis (x = z = 0); air flows toward +y, the struts at the outlet face y = 25, the terminal block toward +x"
COMMAND = "FANCOOL"
PARAMS = {}

# ---- what it meets (standards on file)
M4_CLR = 4.5                         # ISO 273 medium (H13), lib/standards/holes.csv "M4 clearance medium"
# ---- frame (design choices: spec.md Dimensions)
IN = 0.5                             # each fixed part runs 0.5 into the one it sits on (one solid joint)
FRAME, DEPTH = 60.0, 25.0            # square frame x, z +-30, y 0 ... 25
BORE_R = 28.0                        # the venturi bore Ø56 through the frame (2 wall at the sides' middles)
HOLE_P = 50.0                        # 4 x M4 holes at x, z = +-25 (2.75 of wall to the frame's edges)
# ---- the impeller (node `impeller`, design choices)
HUB_R, HUB_Y = 11.0, (2.0, 19.5)     # hub Ø22, y 2 ... 19.5
BLADES, BLADE_R0, BLADE_R1 = 5, 10.0, 26.0   # 5 blades from r 10 (1 into the hub) to r 26 (impeller Ø52, 2 clear of the bore)
BLADE_L, BLADE_T, BLADE_PITCH = 14.0, 1.0, 50.0   # chord 14, 1 thick, set 50 deg from the axis
BLADE_YC = 10.5                      # the blades' mid plane
# ---- the stator boss and struts at the outlet (fixed)
BOSS_R, BOSS_Y = 10.0, (20.0, 24.0)  # stator boss Ø20, y 20 ... 24 (0.5 behind the hub)
STRUT_W = 1.2                        # four struts along +-x and +-z, 1.2 wide, y 20 ... 24, r 9.5 ... 28.5
# ---- terminals (design choices; their conductor range and torque NOT ON FILE (B): IEC 60947-1)
TB = dict(x=(FRAME / 2 - IN, 37.5), y=(4.0, 21.0), z=(-8.0, 8.0))   # terminal block on the frame's +x side
HEAD_R, HEAD_T = 2.2, 1.2            # screw heads Ø4.4 x 1.2 on the block's +x face
TERMS = (("t-1", 4.5), ("t-2", -4.5))  # node, z: 1 = +24 V, 2 = 0 V; at y 12.5
TERM_Y = 12.5
LABEL = (4.0, 21.0, -10.0, 10.0)     # label field on the frame's -x face: y0, y1, z0, z1 (decal)


def _blade_axes(k):
    """blade k's radial, chord and thickness axes (orthonormal, right-handed: ez = ex x ey)"""
    a = 2 * math.pi * k / BLADES; p = math.radians(BLADE_PITCH)
    ex = (math.cos(a), 0.0, math.sin(a))                       # radial
    t = (-math.sin(a), 0.0, math.cos(a))                       # tangential
    ey = (t[0] * math.sin(p), math.cos(p), t[2] * math.sin(p))  # the chord: 50 deg from the axis y toward the tangent
    ez = (ex[1] * ey[2] - ex[2] * ey[1], ex[2] * ey[0] - ex[0] * ey[2], ex[0] * ey[1] - ex[1] * ey[0])
    return ex, ey, ez


_p = math.radians(BLADE_PITCH)
_AX = BLADE_L * math.cos(_p) + BLADE_T * math.sin(_p)            # the blade's axial extent, 9.77
_TG = BLADE_L * math.sin(_p) + BLADE_T * math.cos(_p)            # its tangential extent, 11.37
assert HUB_Y[0] < BLADE_YC - _AX / 2 and BLADE_YC + _AX / 2 < HUB_Y[1]   # the blades inside the hub's length (y 5.6 ... 15.4)
assert math.hypot(BLADE_R1, _TG / 2) < BORE_R - 1.0              # the blade tips' corners 1.4 clear of the bore
assert _TG < 2 * math.pi * HUB_R / BLADES                        # neighbouring blades clear of each other at the hub
assert BLADE_R0 < HUB_R and BOSS_R < HUB_R and HUB_Y[1] < BOSS_Y[0]   # the blades rooted in the hub; the hub 0.5 clear of the boss
assert math.hypot(HOLE_P / 2, HOLE_P / 2) - M4_CLR / 2 > BORE_R + 4.0 and FRAME / 2 - HOLE_P / 2 - M4_CLR / 2 >= 2.5
assert TERMS[0][1] - TERMS[1][1] > 2 * HEAD_R + 4.0 and TERMS[0][1] + HEAD_R < TB["z"][1]   # heads clear of each other and inside the block


def build():
    P = Prims(); F = "M-BLACK-PA"; R = "M-BLACK-PC"
    h = FRAME / 2
    fr = P.box(F, -h, 0.0, -h, FRAME, DEPTH, FRAME)                                             # frame
    P.hole(F, (0, -1.0, 0), (0, DEPTH + 1.0, 0), BORE_R, fr)                                   # venturi bore Ø56
    for x in (-HOLE_P / 2, HOLE_P / 2):
        for z in (-HOLE_P / 2, HOLE_P / 2):
            P.hole(F, (x, -1.0, z), (x, DEPTH + 1.0, z), M4_CLR / 2, fr)                       # 4 x M4 clearance, ISO 273 medium
    b0, b1 = BOSS_Y
    P.cyl(F, (0, b0, 0), (0, b1, 0), BOSS_R)                                                   # stator boss
    r0, r1, w = BOSS_R - IN, BORE_R + IN, STRUT_W
    P.box(F, r0, b0, -w / 2, r1 - r0, b1 - b0, w)                                              # strut +x
    P.box(F, -r1, b0, -w / 2, r1 - r0, b1 - b0, w)                                             # strut -x
    P.box(F, -w / 2, b0, r0, w, b1 - b0, r1 - r0)                                              # strut +z
    P.box(F, -w / 2, b0, -r1, w, b1 - b0, r1 - r0)                                             # strut -z
    N = f"node:impeller|{R}"
    P.cyl(N, (0, HUB_Y[0], 0), (0, HUB_Y[1], 0), HUB_R)                                         # hub
    for k in range(BLADES):                                                                    # pitched blades
        ex, ey, ez = _blade_axes(k)
        o = tuple(BLADE_R0 * ex[i] - BLADE_L / 2 * ey[i] - BLADE_T / 2 * ez[i] + (BLADE_YC if i == 1 else 0.0) for i in range(3))
        P.obox(N, o, ex, ey, ez, BLADE_R1 - BLADE_R0, BLADE_L, BLADE_T)
    P.pivot("impeller", "rotate", (0, BLADE_YC, 0), axis=(0, 1, 0), range=(0, 360))
    (x0, x1), (y0, y1), (z0, z1) = TB["x"], TB["y"], TB["z"]
    P.box(F, x0, y0, z0, x1 - x0, y1 - y0, z1 - z0)                                            # terminal block
    for n, z in TERMS:                                                                         # screw heads: the port nodes
        P.cyl(f"node:{n}|M-ZINC", (x1, TERM_Y, z), (x1 + HEAD_T, TERM_Y, z), HEAD_R)
        P.pivot(n, "port", (x1 + HEAD_T, TERM_Y, z), axis=(1, 0, 0), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp
    ly0, ly1, lz0, lz1 = LABEL
    P.box("M-WHITE-PA", -h - 0.6, ly0, lz0, 0.6, ly1 - ly0, lz1 - lz0)                         # label field (decal)
    P.collider("env", -h - 0.6, 0.0, -h, x1 + HEAD_T + h + 0.6, DEPTH, FRAME)
    return P

PREVIEWS = [dict(name="inlet three-quarter", az=240, el=20),
            dict(name="outlet and struts", az=60, el=20),
            dict(name="inlet", az=270, el=0),
            dict(name="terminals", az=0, el=10, center=(35, 12, 0), height=30)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
