#!/usr/bin/env python3
"""strip-rubber-trapezium-30x15: generic rubber multi-faced/trapezium section, our own vendor-neutral design of the ETIM 10.0 class
EC010641 (Rubber multi-faced/trapezium section), built unattended (OPERATING.md 12, generic elements; the EG019710 Profiles classes in
generic.py's order by name, after strip-rubber-corner-30x30, mech-r139). A solid black EPDM section, symmetric: base 30 wide, top 20
wide, height 15; two upright lands 2 high at the base's sides, then the flanks slope in to the top face (six faces: a trapezium on a
low rectangular foot). No hollow core. The wedge strip, buffer or filler a machine lays in a channel or bonds on a frame. Plain stock,
cut to length (the `length` parameter; a parameter stays out of the id, OPERATING.md 6). The class values (spec.md, "Class values")
are design inputs; no hardness, sealing, compression, temperature or fire figure is claimed, and nothing moves. Every size is a design
choice. No vendor file was opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "strip-rubber-trapezium-30x15", "1.0", "rail"
TITLE = "Rubber trapezium section, generic, solid EPDM, base 30, top 20, height 15, symmetric, no hollow core, black, plain, cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic rubber multi-faced/trapezium section (ETIM 10.0 EC010641), solid EPDM, base 30 wide, top 20 wide, "
            "height 15, upright lands 2 at the base, symmetric, no hollow core, black, plain stock; class values are design inputs "
            "(spec.md); every size a design choice; no hardness, sealing, temperature or fire claim; no vendor file opened")
ORIGIN = ("run start x = 0, the section's centre plane y = 0, the base's underside z = 0 (the face that lies on the host); the run "
          "along +x, the top face at z 15")
COMMAND = "RUBBERTRAP"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius, set per primitive below (as the other profiles, mech-r106 / r131)

BW, TW, H = 30.0, 20.0, 15.0                 # base width (y), top width (y), height (z): design choices (class features)
LAND = 2.0                                   # the upright land at each side of the base, so no cut plane runs along the box's edge
MAT = "M-GASKET"                             # EPDM, solid, black (lib/materials.csv epdm; render layer M-GASKET, the library's black rubber)

DY, DZ = (BW - TW) / 2.0, H - LAND           # 5, 13: each flank's run in and rise
FLANK = math.hypot(DY, DZ)                   # 13.93: the flank's width on the end face
assert LAND <= 3.0                                                           # the lands' end edges: "short", skipped by the gate (mech-r126)
assert TW >= 8.0 and FLANK >= 8.0                                            # every other end-face edge clears the 3 to 7 mm free-corner trap (mech-r69)
AREA = BW * LAND + (BW + TW) / 2.0 * DZ
assert abs(AREA - 385.0) < 1e-9                                              # by hand: 30 x 2 + (30 + 20) / 2 x 13 = 60 + 325 = 385 mm²
FLANK_DEG = math.degrees(math.atan2(DZ, DY))                                 # 68.96: each flank's angle to the base


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 100.0, "length 100 or more"
    body = P.box(MAT, 0, -BW / 2, 0, L, BW, H)                                               # the section: one box ...
    s = (DY / FLANK, DZ / FLANK)                                                             # the flank's direction up and in (|y|, z)
    for side in (1.0, -1.0):                                                                 # ... less the two flanks' wedges: one solid
        a = (side * BW / 2, LAND)                                                            # the flank's foot, the land's top corner
        up = (0.0, -side * s[0], s[1])                                                       # along the flank, up and in
        out = (0.0, side * s[1], s[0])                                                       # the flank's outward normal
        o = (-1.0, a[0] - 3.0 * up[1], a[1] - 3.0 * up[2])                                   # start 3 below the foot, along the flank
        if side > 0: P.cut(MAT, o, (1, 0, 0), out, up, L + 2.0, 20.0, 25.0, body)            # right-handed: x × out = up
        else:        P.cut(MAT, o, (1, 0, 0), up, out, L + 2.0, 25.0, 20.0, body)            # right-handed: x × up = out on −y
    P.collider("foot", 0, -BW / 2, 0, L, BW, LAND)
    P.collider("core", 0, -TW / 2, LAND, L, TW, DZ)                                          # the flanks' wedges outside it stay collider-free
    for i in range(len(P)): P.radii[i] = FILLET_R                                            # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 0, 7.5), height=50)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
