#!/usr/bin/env python3
"""strip-rubber-corner-30x30: generic rubber corner guard section, our own vendor-neutral design of the ETIM 10.0 class EC010648
(Rubber corner guard section), built unattended (OPERATING.md 12, generic elements; the EG019710 Profiles classes in generic.py's
order by name, beside strip-rubber-cord-10, mech-r139). A solid black EPDM angle that covers a host's square outside edge: two legs 3
thick lying on the host's two faces, 30 wide each from the host's corner line (mounting widths 1 and 2), and a round bead Ø16 along
the outer corner that takes the blow. Not self-adhesive, no hollow core, no fastening holes (the host bonds or clamps it). Plain stock,
cut to length (the `length` parameter; a parameter stays out of the id, OPERATING.md 6). The class values (spec.md, "Class values")
are design inputs; no hardness, impact energy, temperature or fire figure is claimed, and nothing moves. Every size is a design
choice. No vendor file was opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "strip-rubber-corner-30x30", "1.0", "rail"
TITLE = "Rubber corner guard section, generic, solid EPDM, legs 30 x 30 x 3 with a corner bead D16, not self-adhesive, black, plain, cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic rubber corner guard section (ETIM 10.0 EC010648), solid EPDM, two legs 3 thick with mounting widths "
            "30 and 30 from the host's corner line, a round bead D16 along the outer corner, not self-adhesive, no hollow core, black, plain "
            "stock; class values are design inputs (spec.md); every size a design choice; no hardness, impact, temperature or fire claim; "
            "no vendor file opened")
ORIGIN = ("run start x = 0, the host's corner line along +x at y = 0, z = 0; the host fills y < 0, z < 0; leg 1 lies on the host's top "
          "face (z 0 to 3, y -30 to 3), leg 2 on its side face (y 0 to 3, z -30 to 3)")
COMMAND = "RUBBERCORNER"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius, set per primitive below (as the other profiles, mech-r106 / r131)

MW1, MW2 = 30.0, 30.0                        # mounting widths 1 (leg on the top face, -y) and 2 (leg on the side face, -z): design choices
T = 3.0                                      # the legs' wall: a design choice, at the gate's 3.0 short-edge limit (mech-r126)
RB = 8.0                                     # the bead's radius (Ø16, class feature Diameter): a design choice
C = 6.0                                      # the bead's axis at y = z = 6 on the corner's diagonal: a design choice
MAT = "M-GASKET"                             # EPDM, solid, black (lib/materials.csv epdm; render layer M-GASKET, the library's black rubber)

assert C * math.sqrt(2.0) > RB                                               # 8.49 > 8: the bead never reaches the host's corner (0, 0)
assert C - math.sqrt(RB * RB - C * C) > 0.0                                  # 0.71: where the bead crosses y = 0 (or z = 0) it lies above the host, z (or y) > 0
assert C - RB < 0.0 and C - RB > -T                                          # -2: the bead's underside (y 6, z -2) lies beside leg 2's outer face and runs into it; the same for leg 1
assert C + RB > T                                                            # 14: the bead stands 11 proud of the legs' outer faces
assert MW1 >= 8.0 and MW2 >= 8.0                                             # the legs' long edges clear the 3 to 7 mm trap (mech-r69)


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 100.0, "length 100 or more"
    a = P.box(MAT, 0, -MW1, -MW2, L, MW1 + T, MW2 + T)                                       # the angle's envelope, y -30 to 3, z -30 to 3
    P.cutbox(MAT, -1, -MW1 - 1, -MW2 - 1, L + 2, MW1 + 1, MW2 + 1, a)                         # the host's quadrant, y < 0 and z < 0: leaves the L
    P.cyl(MAT, (0, C, C), (L, C, C), RB)                                                      # the bead, Ø16, along the outer corner
    P.collider("leg-1", 0, -MW1, 0, L, MW1, T)
    P.collider("leg-2", 0, 0, -MW2, L, T, MW2)
    P.collider("bead", 0, C - RB, C - RB, L, 2 * RB, 2 * RB)
    for i in range(len(P)): P.radii[i] = FILLET_R                                            # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 0, -8), height=55)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
