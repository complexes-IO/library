#!/usr/bin/env python3
"""profile-h-pvc-8x20: generic plastic H-profile, our own vendor-neutral design of the ETIM 10.0 class EC010685 (H-profile, plastic),
built unattended (OPERATING.md 12, generic elements; the EG019710 Profiles classes in generic.py's order by name, after
strip-clamping-8x15). An extruded rigid PVC H-section 8 wide and 20 high: two posts 2.5 thick joined at mid-height by a beam 2.5
thick, leaving a slot 3.0 wide and 8.75 deep above and below: the joining strip that holds two 3 mm panels edge to edge in one plane
(a guard's infill, a cover, a partition). Plain stock, cut to length (the `length` parameter; a parameter stays out of the id,
OPERATING.md 6); no holes. The class values (spec.md, "Class values") are design inputs; the class has no load or temperature
feature, so none is claimed, and nothing moves. Every size is a design choice. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "profile-h-pvc-8x20", "1.0", "rail"
TITLE = "H-profile, plastic, generic, rigid PVC 8 x 20, posts and beam 2.5, two slots 3.0 x 8.75 for 3 mm panels, grey, plain, cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic H-profile, plastic (ETIM 10.0 EC010685), an extruded rigid PVC H-section 8 x 20, posts and beam "
            "2.5, two slots 3.0 wide for 3 mm panels, grey, plain stock; class values are design inputs (spec.md); every size a design "
            "choice; no load, temperature or fire claim; no vendor file opened")
ORIGIN = ("run start x = 0, the slots' centre plane y = 0, the posts' lower ends z = 0; the run along +x, the beam at mid-height "
          "(z 8.75 to 11.25), the panels' plane y = 0, one panel entering from above and one from below")
COMMAND = "HPROFPVC"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius, set per primitive below (as the other profiles, mech-r106 / r131)

W, H = 8.0, 20.0                             # outside width (y), outside height (z): design choices
TP, TB = 2.5, 2.5                            # post thickness, beam thickness (the class's two thickness features): design choices
SLOT = W - 2 * TP                            # 3.0: each slot's width = the panel it takes
DEPTH = (H - TB) / 2.0                       # 8.75: each slot's depth, how far a panel edge goes in
MAT = "M-GREY-PVC"                           # rigid PVC, grey (lib/materials.csv pvc; render layer M-GREY-PVC)

assert TP <= 3.0 and TB <= 3.0 and SLOT <= 3.0                               # posts, beam and slot bottoms: "short" edges, skipped by the gate
assert W >= 8.0 and H >= 8.0 and DEPTH >= 8.0                                # every other end-face edge clears the 3 to 7 mm free-corner trap
assert abs(SLOT - 3.0) < 1e-9                                                # takes a 3.0 panel
AREA = 2 * TP * H + SLOT * TB
assert abs(AREA - 107.5) < 1e-9                                              # by hand: 8 x 20 − 2 x (3 x 8.75) = 107.5 mm²
assert abs(AREA - (W * H - 2 * SLOT * DEPTH)) < 1e-9


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 100.0, "length 100 or more"
    body = P.box(MAT, 0, -W / 2, 0, L, W, H)                                                 # the section: one box ...
    P.cutbox(MAT, -1.0, -SLOT / 2, -1.0, L + 2.0, SLOT, DEPTH + 1.0, body)                    # ... less the lower slot (z 0 to 8.75) ...
    P.cutbox(MAT, -1.0, -SLOT / 2, DEPTH + TB, L + 2.0, SLOT, DEPTH + 1.0, body)              # ... and the upper slot (z 11.25 to 20)
    for s, nm in ((-1, "left"), (1, "right")):
        P.collider(f"post-{nm}", 0, min(s * W / 2, s * SLOT / 2), 0, L, TP, H)
    P.collider("beam", 0, -SLOT / 2, DEPTH, L, SLOT, TB)
    for i in range(len(P)): P.radii[i] = FILLET_R                                            # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 0, 10), height=40)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
