#!/usr/bin/env python3
"""strip-rubber-angle-25x20: generic rubber angle profile, our own vendor-neutral design of the ETIM 10.0 class EC010647 (Rubber angle
profile), built unattended (OPERATING.md 12, generic elements; the EG019710 Profiles classes in generic.py's order by name, after
strip-rubber-u-20x15, mech-r136). A solid black EPDM angle: a foot 25 wide and 3 thick, an upright 20 high and 3 thick, joined at the
heel. The soft edge or corner guard a machine lays over a panel's or a frame's outer edge. Plain stock, cut to length (the `length`
parameter; a parameter stays out of the id, OPERATING.md 6). The class values (spec.md, "Class values") are design inputs; no
hardness, sealing, temperature or fire figure is claimed, and nothing moves. Every size is a design choice. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "strip-rubber-angle-25x20", "1.0", "rail"
TITLE = "Rubber angle profile, generic, solid EPDM, width 25, height 20, base and post 3, black, plain, cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic rubber angle profile (ETIM 10.0 EC010647), solid EPDM, width 25 x height 20, base 3 thick, "
            "post 3 thick, black, plain stock; class values are design inputs (spec.md); every size a design choice; no hardness, "
            "sealing, temperature or fire claim; no vendor file opened")
ORIGIN = ("run start x = 0, the angle's outer corner line y = 0, z = 0 (the heel); the run along +x, the base along +y (its underside "
          "z 0), the post along +z (its outer face y 0)")
COMMAND = "RUBBERANG"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius, set per primitive below (as the other profiles, mech-r106 / r131)

W, H = 25.0, 20.0                            # width (y, the base leg), height (z, the post leg): design choices (class features)
TB, TP = 3.0, 3.0                            # base thickness (z), post thickness (y): design choices (class features)
MAT = "M-GASKET"                             # EPDM, solid, black (lib/materials.csv epdm; render layer M-GASKET, the library's black rubber)

assert TB <= 3.0 and TP <= 3.0                                               # the leg ends: "short" edges, skipped by the gate
assert W - TP >= 8.0 and H - TB >= 8.0                                       # inner faces 22 and 17: clear of the 3 to 7 mm free-corner trap (mech-r69)
AREA = W * TB + (H - TB) * TP                                                # the section: two rectangles, no overlap
assert abs(AREA - 126.0) < 1e-9                                              # by hand: 25 x 3 + 17 x 3 = 126 mm²
assert abs(AREA - (W * H - (W - TP) * (H - TB))) < 1e-9                      # = 25 x 20 − 22 x 17


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 100.0, "length 100 or more"
    body = P.box(MAT, 0, 0, 0, L, W, H)                                                      # the angle: one box ...
    P.cutbox(MAT, -1.0, TP, TB, L + 2.0, W - TP + 1.0, H - TB + 1.0, body)                   # ... less its inside: one solid
    P.collider("base", 0, 0, 0, L, W, TB)
    P.collider("post", 0, 0, TB, L, TP, H - TB)
    for i in range(len(P)): P.radii[i] = FILLET_R                                            # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 12.5, 10), height=50)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
