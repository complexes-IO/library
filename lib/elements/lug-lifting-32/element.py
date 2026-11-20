#!/usr/bin/env python3
"""lug-lifting-32: generic lifting lug, weld-on (a pad eye), our own vendor-neutral design of the ETIM 10.0 class EC012274 (Lifting lug;
synonyms Lashing eye, Lifting eye), built unattended (OPERATING.md 12, generic elements; group EG010320 Lifting equipment, after
clamp-girder-200, lib/rounds/mech/r172.md). One painted steel plate 120 x 20 x 120 stands on its foot, which is welded to a host's flat
steel surface; its two top corners are cut off at an angle, leaving a top 60 wide; a Ø32 eye through the plate (axis y) takes a shackle's
pin or a hook. The weld, its size and the host are not drawn. The class's other forms (an eye bolt or eye nut, whose shape DIN 580 / DIN 582
fix) are not this element and are not built: no dimensional standard is on file for them. The class's features are not on file
(lib/standards/etim/class-features.csv has no EC012274 rows): spec.md gives the design values under plain names, as clamp-girder-200
does. Every size is a design choice; no standard is claimed. No working load limit, proof load or safety claim. No element is placed or
read. No vendor file opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "lug-lifting-32", "1.0", "plate"
TITLE = ("lifting lug (pad eye), generic, weld-on, painted steel plate 120 x 20 x 120 with its top corners cut to a top 60 wide, "
         "eye Ø32 at 80 over its foot")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic lifting lug (ETIM 10.0 EC012274), the weld-on form: one painted steel plate 120 wide, 20 thick, "
            "120 high, its two top corners cut off from 60 up the sides to a top 60 wide, a Ø32 eye along y with its centre 80 over the "
            "foot; welded to a host's flat steel surface (the weld not drawn, its size not stated); class features not on file, design "
            "values under plain names (spec.md); every size a design choice; no load capacity, proof load or safety claim; no vendor "
            "file opened")
ORIGIN = ("the foot's middle on the host's surface: x = 0 the plate's middle across its width, y = 0 the plate's mid-thickness, z = 0 "
          "the foot's underside (the host's surface the lug is welded to), z up; the plate's faces y = ±10, the eye's axis along y")
COMMAND = "LUGLF32"
PARAMS = dict()

W = 120.0                                       # design: the plate 120 wide along x (x -60 to 60)
T = 20.0                                        # design: the plate 20 thick along y (y -10 to 10)
H = 120.0                                       # design: the plate 120 high (z 0 to 120)
ZC = 60.0                                       # design: the corner cuts start 60 up the sides
TOP = 60.0                                      # design: the top left 60 wide (x -30 to 30)
RE, ZE = 16.0, 80.0                             # design: the eye Ø32 along y, its centre at x 0, z 80
MAT = "M-YELLOW"                                # painted steel, the yellow of clamp-girder-200 and beam-runway (no marking claim)

DX, DZ = W / 2 - TOP / 2, H - ZC                # 30, 60: each corner cut's run across and rise
L_CUT = math.hypot(DX, DZ)                      # 67.08: the cut face's length in the x-z plane
UX, UZ = DX / L_CUT, DZ / L_CUT                 # the cut line's direction (inward and up) and its outward normal (UZ, UX)
# the eye's wall: to the top, to each cut face (the eye centre's distance from the cut line less the eye's radius), to the sides
WALL_TOP = H - ZE - RE                                                      # 24
WALL_CUT = (W / 2 - 0.0) * UZ + (ZC - ZE) * UX - RE                          # 28.7
WALL_SIDE = W / 2 - RE                                                      # 44
assert WALL_TOP >= 20 and WALL_CUT >= 20 and WALL_SIDE >= 20                # at least the plate's thickness of wall round the eye
assert ZE - RE >= 3 * RE                                                     # 64 of plate between the foot's weld and the eye
assert TOP >= 2 * RE + 20                                                    # the top wider than the eye by 10 each side
# Volume by hand: the plate 120 x 20 x 120 less two corner triangles 30 x 60 / 2 x 20 less the eye Ø32 x 20.
VOL = W * T * H - 2 * (DX * DZ / 2) * T - math.pi * RE ** 2 * T
assert abs(VOL - 235915.0) < 0.1


def build():
    P = Prims()
    p = P.box(MAT, -W / 2, -T / 2, 0.0, W, T, H)                                                      # the plate
    m = 20.0                                                                                         # the cuts start 20 below the corner's start
    # +x corner: ex up the cut line toward the middle, ey -y, ez = ex x ey the outward normal (+x, +z)
    o = (W / 2 + m * UX, T / 2 + 1.0, ZC - m * UZ)
    P.cut(MAT, o, (-UX, 0, UZ), (0, -1, 0), (UZ, 0, UX), L_CUT + 2 * m, T + 2.0, 60.0, p)
    # -x corner: ex up the cut line toward the middle, ey +y, ez the outward normal (-x, +z)
    o = (-W / 2 - m * UX, -T / 2 - 1.0, ZC - m * UZ)
    P.cut(MAT, o, (UX, 0, UZ), (0, 1, 0), (-UZ, 0, UX), L_CUT + 2 * m, T + 2.0, 60.0, p)
    P.hole(MAT, (0.0, -T / 2 - 1.0, ZE), (0.0, T / 2 + 1.0, ZE), RE, p)                             # the eye
    P.collider("plate", -W / 2, -T / 2, 0.0, W, T, H)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="front", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
