#!/usr/bin/env python3
"""profile-t-alu-30x30x3: generic aluminium T-profile, our own vendor-neutral design of the ETIM 10.0 class EC011891 (T-profile,
aluminium), built unattended (OPERATING.md 12, generic elements; the EG019710 Profiles classes in generic.py's order by name, after
strip-rubber-trapezium-30x15 and the classes skipped in mech-r140). An extruded aluminium equal T-section: base (flange) 30 wide and 3
thick, post (web) 3 thick, total height 30, sharp corners, anodised. Plain stock, cut to length (the `length` parameter; a parameter
stays out of the id, OPERATING.md 6); no holes: a host that bolts it drills its own and declares them in its own features.csv. An
extruded aluminium T-section's sizes are fixed by no dimensional standard on file (a rolled steel T's are EN 10055's, another class
and not on file), so every size is a design choice. The class values (spec.md, "Class values") are design inputs; the class has no
load feature, so none is claimed, and nothing moves. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "profile-t-alu-30x30x3", "1.0", "rail"
TITLE = "T-profile, aluminium, generic, extruded equal T 30 x 30, base and post 3, sharp corners, anodised, plain (no holes), cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic T-profile, aluminium (ETIM 10.0 EC011891), an extruded equal T-section, base 30 wide x 3 thick, "
            "post 3 thick, total height 30, sharp corners, anodised, plain stock; class values are design inputs (spec.md); every size "
            "a design choice; no load claim; no vendor file opened")
ORIGIN = ("run start x = 0, the post's centre plane y = 0, the base's underside z = 0; the run along +x, the base flat (z 0 to 3), "
          "the post upright (z 3 to 30)")
COMMAND = "TPROFALU"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius, set per primitive below (as the other profiles, mech-r106 / r131)

BW, TB = 30.0, 3.0                           # base width (y), base thickness (z): design choices (class features)
H, TP = 30.0, 3.0                            # total height (z), post thickness (y): design choices (class features)
OUT = (BW - TP) / 2.0                        # 13.5: the base's outstand each side of the post
POST = H - TB                                # 27: the post's height above the base
MAT = "M-ALU-ANOD"                           # anodised aluminium (lib/materials.csv al-6063; no temper claimed)

assert TB <= 3.0 and TP <= 3.0                                               # base ends and post top: "short" edges, skipped by the gate
assert OUT >= 8.0 and POST >= 8.0                                            # every other end-face edge clears the 3 to 7 mm free-corner trap (mech-r69)
AREA = BW * TB + POST * TP
assert abs(AREA - 171.0) < 1e-9                                              # by hand: 30 x 3 + 27 x 3 = 171 mm²
assert abs(AREA - (BW * H - 2 * OUT * POST)) < 1e-9                          # = 30 x 30 − 2 x 13.5 x 27


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 100.0, "length 100 or more"
    body = P.box(MAT, 0, -BW / 2, 0, L, BW, H)                                               # the section: one box ...
    P.cutbox(MAT, -1.0, -BW / 2 - 1.0, TB, L + 2.0, OUT + 1.0, POST + 1.0, body)             # ... less the space on −y over the base ...
    P.cutbox(MAT, -1.0, TP / 2, TB, L + 2.0, OUT + 1.0, POST + 1.0, body)                    # ... and on +y: one solid
    P.collider("base", 0, -BW / 2, 0, L, BW, TB)
    P.collider("post", 0, -TP / 2, TB, L, TP, POST)
    for i in range(len(P)): P.radii[i] = FILLET_R                                            # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 0, 15), height=50)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
