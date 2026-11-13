#!/usr/bin/env python3
"""strip-rubber-bulb-30x18: generic rubber bulb section, our own vendor-neutral design of the ETIM 10.0 class EC010639 (Rubber bulb
section), built unattended (OPERATING.md 12, generic elements; the EG019710 Profiles classes in generic.py's order by name, after
strip-rubber-angle-25x20, mech-r137). A solid black EPDM base strip 30 wide and 3 thick with a hollow round bead on its centre line:
bead Ø16 outside, wall 3 (a Ø10 hollow core), 18 high overall. The door or cover seal a machine lays along a frame, the bead pressed
by the closing door. Plain stock, cut to length (the `length` parameter; a parameter stays out of the id, OPERATING.md 6). The class
values (spec.md, "Class values") are design inputs; no hardness, sealing force, compression, temperature or fire figure is claimed,
and nothing moves (the bead's squeeze is not modelled). Every size is a design choice. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "strip-rubber-bulb-30x18", "1.0", "rail"
TITLE = "Rubber bulb section, generic, solid EPDM, base 30 x 3, hollow round centric bead D16 wall 3, height 18, black, plain, cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic rubber bulb section (ETIM 10.0 EC010639), solid EPDM, base 30 wide x 3 thick, a round hollow "
            "centric bead D16 with a 3 wall, 18 high overall, black, plain stock; class values are design inputs (spec.md); every size "
            "a design choice; no hardness, sealing, compression, temperature or fire claim; no vendor file opened")
ORIGIN = ("run start x = 0, the bead's centre plane y = 0, the base's underside z = 0; the run along +x, the base flat (z 0 to 3), "
          "the bead's axis along x at z 10")
COMMAND = "RUBBERBULB"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius, set per primitive below (as the other profiles, mech-r106 / r131)

BW, TB = 30.0, 3.0                           # base width (y), base thickness (z): design choices (class features)
BD, WALL = 16.0, 3.0                         # bead outside diameter, bead wall thickness: design choices (class features)
R, RI = BD / 2.0, BD / 2.0 - WALL            # 8, 5: the bead's outer and core radii (the core Ø10)
SINK = 1.0                                   # the bead sits 1 into the base, so the two solids join along a band, not a tangent line
ZC = TB + R - SINK                           # 10: the bead's axis height
H = ZC + R                                   # 18: total height, the base's underside to the bead's crown
BEAD_H = H - TB                              # 15: bead height above the base's upper face
MAT = "M-GASKET"                             # EPDM, solid, black (lib/materials.csv epdm; render layer M-GASKET, the library's black rubber)

assert TB <= 3.0 and WALL <= 3.0                                             # base ends: "short" edges; the bead's wall ring no wider than the profiles'
assert ZC - RI >= TB + 2.0                                                   # the core stays 2 or more above the base's upper face: wall under it 3 (z 2 to 5)
assert ZC - R < TB and ZC - R > 0.0                                          # the bead's underside lies inside the base: joined, not floating
assert (BW / 2.0 - R) >= 7.0                                                 # 7: the base's flat each side of the bead, for a host's clip or bond
assert abs(H - 18.0) < 1e-9 and abs(BEAD_H - 15.0) < 1e-9


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 100.0, "length 100 or more"
    P.box(MAT, 0, -BW / 2, 0, L, BW, TB)                                                     # the base strip
    bead = P.cyl(MAT, (0, 0, ZC), (L, 0, ZC), R)                                              # the bead, Ø16, 1 into the base
    P.hole(MAT, (-1.0, 0, ZC), (L + 1.0, 0, ZC), RI, bead)                                   # its hollow core Ø10, through (features.csv kind own)
    P.collider("base", 0, -BW / 2, 0, L, BW, TB)
    P.collider("bead", 0, -R, TB, L, BD, H - TB)
    for i in range(len(P)): P.radii[i] = FILLET_R                                            # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 0, 9), height=40)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
