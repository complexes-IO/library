#!/usr/bin/env python3
"""profile-u-alu-40x20x3: generic aluminium U-profile, our own vendor-neutral design of the ETIM 10.0 class EC011894 (U-profile,
aluminium), built unattended (OPERATING.md 12, generic elements; the EG019710 Profiles classes in generic.py's order by name, after
profile-t-alu-30x30x3 and the classes skipped in mech-r140). An extruded aluminium U-channel: width 40, height 20, bottom and legs 3,
sharp corners, anodised. Plain stock, cut to length (the `length` parameter; a parameter stays out of the id, OPERATING.md 6); no
holes: a host that bolts it drills its own and declares them in its own features.csv. An extruded aluminium U-section's sizes are
fixed by no dimensional standard on file (a hot-rolled steel channel's are DIN 1026 / EN 10279's, another class and not on file), so
every size is a design choice. The class values (spec.md, "Class values") are design inputs; the class has no load feature, so none
is claimed, and nothing moves. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "profile-u-alu-40x20x3", "1.0", "rail"
TITLE = "U-profile, aluminium, generic, extruded U-channel 40 x 20, bottom and legs 3, sharp corners, anodised, plain (no holes), cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic U-profile, aluminium (ETIM 10.0 EC011894), an extruded U-channel 40 wide x 20 high, bottom and "
            "legs 3, sharp corners, anodised, plain stock; class values are design inputs (spec.md); every size a design choice; no "
            "load claim; no vendor file opened")
ORIGIN = ("run start x = 0, the channel's centre plane y = 0, the bottom's underside z = 0; the run along +x, the bottom flat (z 0 to "
          "3), the legs upright (z 3 to 20), the opening up")
COMMAND = "UPROFALU"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius, set per primitive below (as the other profiles, mech-r106 / r131)

W, H = 40.0, 20.0                            # width (y, outside), height (z, outside): design choices (class features)
TB, TL = 3.0, 3.0                            # bottom thickness (z), leg thickness (y): design choices (class features)
IW = W - 2 * TL                              # 34: the clear width between the legs
IH = H - TB                                  # 17: the legs' height above the bottom
MAT = "M-ALU-ANOD"                           # anodised aluminium (lib/materials.csv al-6063; no temper claimed)

assert TB <= 3.0 and TL <= 3.0                                               # the legs' tops: "short" edges, skipped by the gate
assert IW >= 8.0 and IH >= 8.0                                               # every other end-face edge clears the 3 to 7 mm free-corner trap (mech-r69)
AREA = W * TB + 2 * TL * IH
assert abs(AREA - 222.0) < 1e-9                                              # by hand: 40 x 3 + 2 x 3 x 17 = 222 mm²
assert abs(AREA - (W * H - IW * IH)) < 1e-9                                  # = 40 x 20 − 34 x 17


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 100.0, "length 100 or more"
    body = P.box(MAT, 0, -W / 2, 0, L, W, H)                                                 # the section: one box ...
    P.cutbox(MAT, -1.0, -IW / 2, TB, L + 2.0, IW, IH + 1.0, body)                           # ... less the channel (y ±17, z 3 up): one solid
    P.collider("bottom", 0, -W / 2, 0, L, W, TB)
    P.collider("leg-left", 0, -W / 2, TB, L, TL, IH)
    P.collider("leg-right", 0, IW / 2, TB, L, TL, IH)
    for i in range(len(P)): P.radii[i] = FILLET_R                                            # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 0, 10), height=60)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
