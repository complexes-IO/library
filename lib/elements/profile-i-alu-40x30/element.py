#!/usr/bin/env python3
"""profile-i-alu-40x30: generic aluminium I-profile, our own vendor-neutral design of the ETIM 10.0 class EC012316 (I-profile,
aluminium), built unattended (OPERATING.md 12, generic elements; the EG019710 Profiles classes in generic.py's order by name, after
profile-h-pvc-8x20 and the building-trade classes skipped in mech-r133). An extruded aluminium I-section 40 high and 30 wide: two
flanges 3 thick joined by a web 3 thick, sharp corners, anodised. Plain stock, cut to length (the `length` parameter; a parameter
stays out of the id, OPERATING.md 6); no holes: a host that bolts it drills its own and declares them in its own features.csv. An
extruded aluminium I-section's sizes are fixed by no dimensional standard on file (a rolled steel I-beam's are EN 10365's, another
class), so every size is a design choice. The class values (spec.md, "Class values") are design inputs; the class has no load
feature, so none is claimed, and nothing moves. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "profile-i-alu-40x30", "1.0", "rail"
TITLE = "I-profile, aluminium, generic, extruded 40 high x 30 wide, flanges and web 3, sharp corners, anodised, plain (no holes), cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic I-profile, aluminium (ETIM 10.0 EC012316), an extruded I-section 40 high x 30 wide, flanges and "
            "web 3, sharp corners, anodised, plain stock; class values are design inputs (spec.md); every size a design choice; no load "
            "claim; no vendor file opened")
ORIGIN = ("run start x = 0, the web's centre plane y = 0, the lower flange's underside z = 0; the run along +x, the web upright "
          "(z 3 to 37), the flanges flat (z 0 to 3 and 37 to 40)")
COMMAND = "IPROFALU"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius, set per primitive below (as the other profiles, mech-r106 / r131)

H, W = 40.0, 30.0                            # outside height (z), flange width (y): design choices
TF, TW = 3.0, 3.0                            # flange thickness, web thickness (the class's two thickness features): design choices
OUT = (W - TW) / 2.0                         # 13.5: each flange's outstand past the web
WEB = H - 2 * TF                             # 34: the web's clear height between the flanges
MAT = "M-ALU-ANOD"                           # anodised aluminium (lib/materials.csv al-6063; no temper claimed)

assert TF <= 3.0 and TW <= 3.0                                               # flange ends and web edges: "short", skipped by the gate
assert OUT >= 8.0 and WEB >= 8.0                                             # every other end-face edge clears the 3 to 7 mm free-corner trap (mech-r69)
AREA = 2 * W * TF + WEB * TW
assert abs(AREA - 282.0) < 1e-9                                              # by hand: 2 x 30 x 3 + 34 x 3 = 282 mm²
assert abs(AREA - (W * H - 2 * OUT * WEB)) < 1e-9                            # = 30 x 40 − 2 x 13.5 x 34


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 100.0, "length 100 or more"
    body = P.box(MAT, 0, -W / 2, 0, L, W, H)                                                 # the section: one box ...
    P.cutbox(MAT, -1.0, -W / 2 - 1.0, TF, L + 2.0, OUT + 1.0, WEB, body)                     # ... less the recess on −y ...
    P.cutbox(MAT, -1.0, TW / 2, TF, L + 2.0, OUT + 1.0, WEB, body)                           # ... and the recess on +y: one solid
    P.collider("flange-bottom", 0, -W / 2, 0, L, W, TF)
    P.collider("flange-top", 0, -W / 2, H - TF, L, W, TF)
    P.collider("web", 0, -TW / 2, TF, L, TW, WEB)
    for i in range(len(P)): P.radii[i] = FILLET_R                                            # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 0, 20), height=70)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
