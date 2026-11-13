#!/usr/bin/env python3
"""profile-u-pvc-25x25: generic plastic U-profile, our own vendor-neutral design of the ETIM 10.0 class EC010683 (U-profile, plastic),
built unattended (OPERATING.md 12, generic elements; the EG019710 Profiles classes in generic.py's order by name, beside
profile-u-alu-40x20x3, mech-r141). An extruded rigid PVC U-section: width 25, height 25, bottom and legs 2.5, sharp corners, grey: a
cover, edge or socket profile a panel edge, a strip or a cable sits in. Plain stock, cut to length (the `length` parameter; a parameter
stays out of the id, OPERATING.md 6); no holes (a host drills its own). The class values (spec.md, "Class values") are design inputs;
the class has no load, temperature or fire feature, so none is claimed, and nothing moves. A plastic U-section's sizes are fixed by no
dimensional standard: every size is a design choice. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "profile-u-pvc-25x25", "1.0", "rail"
TITLE = "U-profile, plastic, generic, rigid PVC U-section 25 x 25, bottom and legs 2.5, sharp corners, grey, plain (no holes), cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic U-profile, plastic (ETIM 10.0 EC010683), an extruded rigid PVC U-section 25 wide x 25 high, "
            "bottom and legs 2.5, sharp corners, grey, plain stock; class values are design inputs (spec.md); every size a design "
            "choice; no load, temperature or fire claim; no vendor file opened")
ORIGIN = ("run start x = 0, the section's centre plane y = 0, the bottom's outer face z = 0 (the mounting face); the run along +x, "
          "the opening up at z 25")
COMMAND = "UPROFPVC"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius, set per primitive below (the rail class's 1.0 reads thin walls badly, mech-r69 / r106)

W, H = 25.0, 25.0                            # width (y, outside), height (z, outside): design choices (class features)
TB, TL = 2.5, 2.5                            # bottom thickness, leg thickness (the class's two thickness features): design choices
IW = W - 2 * TL                              # 20: the clear width between the legs
IH = H - TB                                  # 22.5: the legs' height above the bottom
MAT = "M-GREY-PVC"                           # rigid PVC, grey (lib/materials.csv pvc; render layer M-GREY-PVC)

assert TB <= 3.0 and TL <= 3.0                                               # the legs' tops: "short" edges, skipped by the gate
assert IW >= 8.0 and IH >= 8.0                                               # every other end-face edge clears the 3 to 7 mm free-corner trap (mech-r69)
AREA = W * TB + 2 * TL * IH
assert abs(AREA - 175.0) < 1e-9                                              # by hand: 25 x 2.5 + 2 x 2.5 x 22.5 = 175 mm²
assert abs(AREA - (W * H - IW * IH)) < 1e-9                                  # = 25 x 25 − 20 x 22.5


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 100.0, "length 100 or more"
    body = P.box(MAT, 0, -W / 2, 0, L, W, H)                                                 # the section: one box ...
    P.cutbox(MAT, -1.0, -IW / 2, TB, L + 2.0, IW, IH + 1.0, body)                           # ... less the channel (y ±10, z 2.5 up): one solid
    P.collider("bottom", 0, -W / 2, 0, L, W, TB)
    P.collider("leg-left", 0, -W / 2, TB, L, TL, IH)
    P.collider("leg-right", 0, IW / 2, TB, L, TL, IH)
    for i in range(len(P)): P.radii[i] = FILLET_R                                            # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 0, 12.5), height=60)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
