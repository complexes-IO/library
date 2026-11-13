#!/usr/bin/env python3
"""profile-rect-pvc-30x20: generic plastic rectangular profile, our own vendor-neutral design of the ETIM 10.0 class EC010686
(Rectangular profile, plastic), built unattended (OPERATING.md 12, generic elements; the EG019710 Profiles classes in generic.py's
order by name, beside profile-angle-pvc-30x30x3 this round). An extruded rigid PVC rectangular hollow section 30 wide and 20 high:
two upright posts (the side walls) and two flat beams (the top and bottom walls), each 2.5 thick, sharp corners, grey, open at both
ends: a light spacer, sleeve or cover tube. ETIM's "post" and "beam" are read as the upright and the flat members, as
profile-h-pvc-8x20 and profile-i-pvc-30x20 read them (spec.md, "Class values"). Plain stock, cut to length (the `length` parameter;
a parameter stays out of the id, OPERATING.md 6); no holes. Every size is a design choice (no dimensional standard shapes a plastic
rectangular section). The class values are design inputs; the class has no load or temperature feature, so none is claimed, and
nothing moves. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "profile-rect-pvc-30x20", "1.0", "rail"
TITLE = "rectangular profile, plastic, generic, rigid PVC hollow section 30 wide x 20 high, posts and beams 2.5, sharp corners, grey, cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic rectangular profile, plastic (ETIM 10.0 EC010686), an extruded rigid PVC rectangular hollow "
            "section 30 wide x 20 high, posts (side walls) and beams (top and bottom walls) 2.5, grey, plain stock; class values are "
            "design inputs (spec.md); every size a design choice; no load, temperature or fire claim; no vendor file opened")
ORIGIN = ("run start x = 0, the section's centre plane y = 0, the bottom beam's underside z = 0; the run along +x, the posts upright "
          "(y −15 to −12.5 and 12.5 to 15), the beams flat (z 0 to 2.5 and 17.5 to 20)")
COMMAND = "RECTPVC"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius, set per primitive below (as the other thin-walled profiles, mech-r106 / r131)

W, H = 30.0, 20.0                            # outside width (y), outside height (z): design choices
TP, TB = 2.5, 2.5                            # post (side wall) thickness, beam (top / bottom wall) thickness (the class's two thickness features)
BORE_W, BORE_H = W - 2 * TP, H - 2 * TB      # 25 x 15: the clear bore
MAT = "M-GREY-PVC"                           # rigid PVC, grey (lib/materials.csv pvc; render layer M-GREY-PVC)

assert TP <= 3.0 and TB <= 3.0                                               # wall-thickness edges: "short", skipped by the gate
assert BORE_W >= 8.0 and BORE_H >= 8.0 and W >= 8.0 and H >= 8.0             # every other end-face edge clears the 3 to 7 mm free-corner trap (mech-r69)
AREA = W * H - BORE_W * BORE_H
assert abs(AREA - 225.0) < 1e-9                                              # by hand: 30 x 20 − 25 x 15 = 225 mm²
assert abs(AREA - (2 * W * TB + 2 * BORE_H * TP)) < 1e-9                     # = 2 x 30 x 2.5 + 2 x 15 x 2.5


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 100.0, "length 100 or more"
    body = P.box(MAT, 0, -W / 2, 0, L, W, H)                                                 # the section: one box ...
    P.cutbox(MAT, -1.0, -BORE_W / 2, TB, L + 2.0, BORE_W, BORE_H, body)                      # ... less its bore, open at both ends: one solid
    P.collider("beam-bottom", 0, -W / 2, 0, L, W, TB)
    P.collider("beam-top", 0, -W / 2, H - TB, L, W, TB)
    P.collider("post-left", 0, -W / 2, TB, L, TP, BORE_H)
    P.collider("post-right", 0, W / 2 - TP, TB, L, TP, BORE_H)
    for i in range(len(P)): P.radii[i] = FILLET_R                                            # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 0, 10), height=40)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
