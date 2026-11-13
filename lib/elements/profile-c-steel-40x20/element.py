#!/usr/bin/env python3
"""profile-c-steel-40x20: generic steel C-profile, our own vendor-neutral design of the ETIM 10.0 class EC003165 (C-profile, steel),
built unattended (OPERATING.md 12, generic elements; the EG019710 Profiles classes in generic.py's order by name, after
profile-angle-alu-40x40x3 and profile-c-pvc-30x20, mech-r131). A cold-formed, galvanised mild-steel lipped channel 40 wide and 20 high
from 2.0 sheet: bottom and legs 2, the legs' top edges bent inward as lips 2 thick that leave a 20 slit along the run. A light
mounting channel, a cover or a guide a strip, a panel edge or a cable runs in. Plain stock, cut to length (the `length` parameter;
a parameter stays out of the id, OPERATING.md 6); no holes (a host drills its own). The class values (spec.md, "Class values") are
design inputs; the class has no load feature, so none is claimed, and nothing moves. Every size is a design choice. No vendor file
was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "profile-c-steel-40x20", "1.0", "rail"
TITLE = "C-profile, steel, generic, cold-formed galvanised 40 x 20 from 2.0 sheet, inturned lips, slit 20, plain, cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic C-profile, steel (ETIM 10.0 EC003165), a cold-formed galvanised mild-steel lipped channel 40 x 20 "
            "from 2.0 sheet, inturned lips with a 20 slit, plain stock; class values are design inputs (spec.md); every size a design "
            "choice; no load claim; no vendor file opened")
ORIGIN = ("run start x = 0, the section's centre line y = 0, the bottom's outer face z = 0 (the mounting face); the run along +x, the "
          "slit up at z 20")
COMMAND = "CPROFSTL"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius, set per primitive below (the rail class's 1.0 reads thin walls badly, mech-r69 / r106)

W, H = 40.0, 20.0                            # outside width (y), outside height (z): design choices
T = 2.0                                      # the sheet: bottom, legs and lips alike (cold-formed from one strip): design choice
TB, TL, TLIP = T, T, T                       # the class's bottom and leg thickness, and the lips'
SLIT = 20.0                                  # the slit between the lips (the class's "Slit width"): design choice
LIP = (W - SLIT) / 2.0                       # 10: each lip from the outer face inward (8 past the leg's inner face)
MAT = "M-GALV"                               # galvanised mild steel (lib/materials.csv steel-mild; render layer M-GALV)

assert T <= 3.0                                                              # every wall's end edges "short", skipped by the gate
assert LIP >= 8.0 and LIP - TL >= 8.0 and H - TB - TLIP >= 8.0 and W - 2 * TL >= 8.0   # the end face's other edges clear the 3 to 7 mm trap
assert LIP > TL                                                              # the lips reach past the legs: a C, not a U
AREA = W * TB + 2 * TL * (H - TB) + 2 * (LIP - TL) * TLIP                    # bottom, two legs over it, two lips past the legs: no overlap
assert abs(AREA - 184.0) < 1e-9                                              # by hand: 40 x 20 − 36 x 16 (cavity) − 20 x 2 (slit) = 184 mm²


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 100.0, "length 100 or more"
    body = P.box(MAT, 0, -W / 2, 0, L, W, H)                                                 # the section: one box ...
    P.cutbox(MAT, -1.0, -(W / 2 - TL), TB, L + 2.0, W - 2 * TL, H - TB - TLIP, body)        # ... less the cavity (y ±18, z 2 to 18) ...
    P.cutbox(MAT, -1.0, -SLIT / 2, H - TLIP - 1.0, L + 2.0, SLIT, TLIP + 2.0, body)         # ... and the slit through the lips (y ±10)
    P.collider("bottom", 0, -W / 2, 0, L, W, TB)
    for s, nm in ((-1, "left"), (1, "right")):
        P.collider(f"leg-{nm}", 0, min(s * W / 2, s * (W / 2 - TL)), TB, L, TL, H - TB)
        P.collider(f"lip-{nm}", 0, min(s * (W / 2 - TL), s * SLIT / 2), H - TLIP, L, LIP - TL, TLIP)
    for i in range(len(P)): P.radii[i] = FILLET_R                                            # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 0, 10), height=60)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
