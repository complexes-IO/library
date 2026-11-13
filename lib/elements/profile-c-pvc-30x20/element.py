#!/usr/bin/env python3
"""profile-c-pvc-30x20: generic plastic C-profile, our own vendor-neutral design of the ETIM 10.0 class EC010682 (C-profile, plastic),
built unattended (OPERATING.md 12, generic elements; the EG019710 Profiles classes in generic.py's order: EC012022 Angle profile,
aluminium is profile-angle-alu-40x40x3; the stainless angle and the two bulb flats are rolled sections their standards shape,
lib/needs-em/mech.md). An extruded rigid PVC C-section 30 wide and 20 high, bottom and legs 3, whose top edges turn inward as lips
3 thick and leave a 14 slit along the run: a cover strip, a cable or sliding-door channel, a carrier a strip or a panel edge slides
into. Plain stock, cut to length (the `length` parameter; a parameter stays out of the id, OPERATING.md 6); no holes (a host drills
its own). The class values (spec.md, "Class values") are design inputs; the class has no load or temperature feature, so none is
claimed, and nothing moves. Every size is a design choice. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "profile-c-pvc-30x20", "1.0", "rail"
TITLE = "C-profile, plastic, generic, rigid PVC 30 x 20, bottom and legs 3, inturned lips 3 thick, slit 14, grey, plain, cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic C-profile, plastic (ETIM 10.0 EC010682), an extruded rigid PVC C-section 30 x 20, bottom and legs "
            "3, inturned lips with a 14 slit, grey, plain stock; class values are design inputs (spec.md); every size a design choice; "
            "no load, temperature or fire claim; no vendor file opened")
ORIGIN = ("run start x = 0, the section's centre line y = 0, the bottom's outer face z = 0 (the mounting face); the run along +x, the "
          "slit up at z 20")
COMMAND = "CPROFPVC"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius, set per primitive below (the rail class's 1.0 reads 3 mm walls badly, mech-r69 / r106)

W, H = 30.0, 20.0                            # outside width (y), outside height (z): design choices
TB, TL = 3.0, 3.0                            # bottom thickness, leg thickness (the class's two thickness features): design choices
TLIP = 3.0                                   # the lips' thickness: design choice (as the walls)
SLIT = 14.0                                  # the slit between the lips (the class's "Slit width"): design choice
LIP = (W - SLIT) / 2.0                       # 8: each lip from the outer face inward (5 past the leg's inner face)
MAT = "M-GREY-PVC"                           # rigid PVC, grey (lib/materials.csv pvc; render layer M-GREY-PVC)

assert TB <= 3.0 and TL <= 3.0 and TLIP <= 3.0                               # the walls' edges "short", skipped by the gate
assert LIP >= 8.0 and H - TB - TLIP >= 8.0 and W - 2 * TL >= 8.0             # the end face's other edges clear the 3 to 7 mm free-corner trap
assert LIP > TL                                                              # the lips reach past the legs: a C, not a U
AREA = W * TB + 2 * TL * (H - TB) + 2 * (LIP - TL) * TLIP                    # bottom, two legs over it, two lips past the legs: no overlap
assert abs(AREA - 222.0) < 1e-9                                              # by hand: 30 x 20 − 24 x 14 (cavity) − 14 x 3 (slit) = 222 mm²


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 100.0, "length 100 or more"
    body = P.box(MAT, 0, -W / 2, 0, L, W, H)                                                 # the section: one box ...
    P.cutbox(MAT, -1.0, -(W / 2 - TL), TB, L + 2.0, W - 2 * TL, H - TB - TLIP, body)        # ... less the cavity (y ±12, z 3 to 17) ...
    P.cutbox(MAT, -1.0, -SLIT / 2, H - TLIP - 1.0, L + 2.0, SLIT, TLIP + 2.0, body)         # ... and the slit through the lips (y ±7)
    P.collider("bottom", 0, -W / 2, 0, L, W, TB)
    for s, nm in ((-1, "left"), (1, "right")):
        P.collider(f"leg-{nm}", 0, min(s * W / 2, s * (W / 2 - TL)), TB, L, TL, H - TB)
        P.collider(f"lip-{nm}", 0, min(s * (W / 2 - TL), s * SLIT / 2), H - TLIP, L, LIP - TL, TLIP)
    for i in range(len(P)): P.radii[i] = FILLET_R                                            # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 0, 10), height=60)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
