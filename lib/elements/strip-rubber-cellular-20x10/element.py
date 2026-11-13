#!/usr/bin/env python3
"""strip-rubber-cellular-20x10: generic cellular rubber strip, our own vendor-neutral design of the ETIM 10.0 class EC010649 (Cellular
rubber strip), built unattended (OPERATING.md 12, generic elements; the EG019710 Profiles classes in generic.py's order by name, after
profile-c-steel-40x20). A plain closed-cell EPDM sponge strip 20 wide and 10 high, black: the soft seal or buffer a machine bonds or
clamps on a door edge, a cover's flange or a panel's rim. Plain stock, cut to length (the `length` parameter; a parameter stays out of
the id, OPERATING.md 6); not self-adhesive (the host bonds or clamps it). Drawn uncompressed, as delivered. The class values (spec.md,
"Class values") are design inputs; no hardness, temperature, sealing or compression figure is claimed, and nothing moves. Every size
is a design choice. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "strip-rubber-cellular-20x10", "1.0", "rail"
TITLE = "Cellular rubber strip, generic, closed-cell EPDM sponge 20 x 10, black, not self-adhesive, plain, cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic cellular rubber strip (ETIM 10.0 EC010649), a closed-cell EPDM sponge strip 20 x 10, black, not "
            "self-adhesive, plain stock; class values are design inputs (spec.md); every size a design choice; no hardness, temperature "
            "or sealing claim; no vendor file opened")
ORIGIN = ("run start x = 0, the strip's centre line y = 0, the bearing face z = 0 (the face that lies on the host); the run along +x, "
          "the sealing face up at z 10")
COMMAND = "STRIPCR"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius, set per primitive below (as the other profiles, mech-r106 / r131)

W, H = 20.0, 10.0                            # width (y), height (z), uncompressed: design choices
MAT = "M-GASKET"                             # EPDM sponge, black (lib/materials.csv epdm; render layer M-GASKET, the library's black rubber)

assert W >= 8.0 and H >= 8.0                                                 # the end face's edges clear the gate's 3 to 7 mm free-corner trap
AREA = W * H
assert abs(AREA - 200.0) < 1e-9                                              # by hand: 20 x 10 = 200 mm²


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 100.0, "length 100 or more"
    P.box(MAT, 0, -W / 2, 0, L, W, H)                                                        # the strip: one box
    P.collider("strip", 0, -W / 2, 0, L, W, H)
    for i in range(len(P)): P.radii[i] = FILLET_R                                            # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 0, 5), height=40)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
