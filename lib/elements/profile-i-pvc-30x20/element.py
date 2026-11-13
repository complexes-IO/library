#!/usr/bin/env python3
"""profile-i-pvc-30x20: generic plastic I-profile, our own vendor-neutral design of the ETIM 10.0 class EC010684 (I-profile,
plastic), built unattended (OPERATING.md 12, generic elements; the EG019710 Profiles classes in generic.py's order by name, beside
profile-i-alu-40x30 this round). An extruded rigid PVC I-section 30 high and 20 wide: an upright post (the web) 2.5 thick between two
flat beams (the flanges) 2.5 thick, sharp corners, white: a light stiffener or spacer strip. ETIM's "post" and "beam" are read as
the upright and the flat members, as profile-h-pvc-8x20 reads them (spec.md, "Class values"). Plain stock, cut to length (the
`length` parameter; a parameter stays out of the id, OPERATING.md 6); no holes. Every size is a design choice (no dimensional
standard shapes a plastic I-section). The class values are design inputs; the class has no load or temperature feature, so none is
claimed, and nothing moves. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "profile-i-pvc-30x20", "1.0", "rail"
TITLE = "I-profile, plastic, generic, rigid PVC 30 high x 20 wide, post (web) and beams (flanges) 2.5, sharp corners, white, plain, cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic I-profile, plastic (ETIM 10.0 EC010684), an extruded rigid PVC I-section 30 high x 20 wide, post "
            "(web) and beams (flanges) 2.5, white, plain stock; class values are design inputs (spec.md); every size a design choice; "
            "no load, temperature or fire claim; no vendor file opened")
ORIGIN = ("run start x = 0, the post's centre plane y = 0, the lower beam's underside z = 0; the run along +x, the post upright "
          "(z 2.5 to 27.5), the beams flat (z 0 to 2.5 and 27.5 to 30)")
COMMAND = "IPROFPVC"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius, set per primitive below (as the other profiles, mech-r106 / r131)

H, W = 30.0, 20.0                            # outside height (z), beam width (y): design choices
TB, TP = 2.5, 2.5                            # beam (flange) thickness, post (web) thickness (the class's two thickness features)
OUT = (W - TP) / 2.0                         # 8.75: each beam's outstand past the post
WEB = H - 2 * TB                             # 25: the post's clear height between the beams
MAT = "M-WHITE-PVC"                          # rigid PVC, white (lib/materials.csv pvc; render layer M-WHITE-PVC)

assert TB <= 3.0 and TP <= 3.0                                               # beam ends and post edges: "short", skipped by the gate
assert OUT >= 8.0 and WEB >= 8.0                                             # every other end-face edge clears the 3 to 7 mm free-corner trap (mech-r69)
AREA = 2 * W * TB + WEB * TP
assert abs(AREA - 162.5) < 1e-9                                              # by hand: 2 x 20 x 2.5 + 25 x 2.5 = 162.5 mm²
assert abs(AREA - (W * H - 2 * OUT * WEB)) < 1e-9                            # = 20 x 30 − 2 x 8.75 x 25


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 100.0, "length 100 or more"
    body = P.box(MAT, 0, -W / 2, 0, L, W, H)                                                 # the section: one box ...
    P.cutbox(MAT, -1.0, -W / 2 - 1.0, TB, L + 2.0, OUT + 1.0, WEB, body)                     # ... less the recess on −y ...
    P.cutbox(MAT, -1.0, TP / 2, TB, L + 2.0, OUT + 1.0, WEB, body)                           # ... and the recess on +y: one solid
    P.collider("beam-bottom", 0, -W / 2, 0, L, W, TB)
    P.collider("beam-top", 0, -W / 2, H - TB, L, W, TB)
    P.collider("post", 0, -TP / 2, TB, L, TP, WEB)
    for i in range(len(P)): P.radii[i] = FILLET_R                                            # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 0, 15), height=50)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
