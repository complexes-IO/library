#!/usr/bin/env python3
"""strip-rubber-bumper-40x22: generic rubber bumping section, our own vendor-neutral design of the ETIM 10.0 class EC010644 (Rubber
bumping section), built unattended (OPERATING.md 12, generic elements; the EG019710 Profiles classes in generic.py's order by name,
beside strip-rubber-rect-30x10, mech-r138). A solid black EPDM buffer strip: a rectangular base 40 wide and 12 high with a half-round
crown Ø20 on its centre line, 22 high overall. The bump strip a machine bonds or clamps along a frame, a cart's or a guard's edge,
where a trolley, a door or a hand may strike it. No fastening holes (the host bonds or clamps it). Plain stock, cut to length (the
`length` parameter; a parameter stays out of the id, OPERATING.md 6). The class values (spec.md, "Class values") are design inputs; no
hardness, impact energy, temperature or fire figure is claimed, and nothing moves (the crown's squeeze is not modelled). Every size is
a design choice. No vendor file was opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "strip-rubber-bumper-40x22", "1.1", "rail"
TITLE = "Rubber bumping section, generic, solid EPDM, base 40 x 12 with a half-round crown D20, height 22, no fastening holes, black, plain, cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic rubber bumping section (ETIM 10.0 EC010644), solid EPDM, a rectangular base 40 wide x 12 high with "
            "a half-round crown D20 on its centre line, 22 high overall, no fastening holes, black, plain stock; class values are design "
            "inputs (spec.md); every size a design choice; no hardness, impact, temperature or fire claim; no vendor file opened")
ORIGIN = ("run start x = 0, the strip's centre plane y = 0, the base's underside z = 0 (the face that lies on the host); the run along "
          "+x, the crown's axis along x at z 12, its top at z 22")
COMMAND = "RUBBERBUMP"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius, set per primitive below (as the other profiles, mech-r106 / r131)

W, TB = 40.0, 12.0                           # base width (y), base height (z): design choices (class features Width)
R = 10.0                                     # the crown's radius (Ø20): a design choice
ZC = TB                                      # 12: the crown's axis on the base's upper face, so its lower half lies inside the base
H = ZC + R                                   # 22: total height (class feature Height)
MAT = "M-GASKET"                             # EPDM, solid, black (lib/materials.csv epdm; render layer M-GASKET, the library's black rubber)

assert ZC - R > 0.0                                                          # the crown's underside (z 2) lies inside the base: no tangent with z 0
assert (W / 2.0 - R) >= 8.0                                                  # 10: the base's flat each side of the crown, clear of the 3 to 7 trap
assert TB >= 8.0 and W >= 8.0                                                # the base's end-face edges (12, 40) clear the 3 to 7 mm trap (mech-r69)
assert abs(H - 22.0) < 1e-9
AREA = W * TB + math.pi * R * R / 2.0                                        # the section: the base + the crown's upper half
assert abs(AREA - 637.08) < 0.01                                             # by hand: 40 x 12 + π 10² / 2 = 480 + 157.08 = 637.08 mm²


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 100.0, "length 100 or more"
    P.box(MAT, 0, -W / 2, 0, L, W, TB)                                                       # the base
    P.cyl(MAT, (0, 0, ZC), (L, 0, ZC), R)                                                     # the crown, Ø20, its lower half inside the base
    P.collider("base", 0, -W / 2, 0, L, W, TB)
    P.collider("crown", 0, -R, TB, L, 2 * R, R)
    for i in range(len(P)): P.radii[i] = FILLET_R                                            # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 0, 11), height=55)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
