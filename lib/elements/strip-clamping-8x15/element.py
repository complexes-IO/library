#!/usr/bin/env python3
"""strip-clamping-8x15: generic clamping strip section, our own vendor-neutral design of the ETIM 10.0 class EC010640 (Clamping strip
section), built unattended (OPERATING.md 12, generic elements; the EG019710 Profiles classes in generic.py's order by name, after
strip-rubber-cellular-20x10; the mounting-rail and flooring classes between them by name are building-trade parts, lib/needs-em/mech.md).
A solid black EPDM U-section 8 wide and 15 high, a slot 12 deep: 1.6 wide over its grip (z 2 to 12) under a 2.0 wide, 2 deep lead-in
at the mouth: the edge protection strip a machine pushes on a sheet edge (a guard's opening, a cut-out, a panel's rim) so the raw
edge is covered. It grips by its own interference: the grip slot is narrower than the thinnest sheet it takes (2.0 spreads each wall
0.2, 2.5 spreads each 0.45); no steel reinforcement and no sponge seal. Plain stock, cut to length (the `length` parameter; a
parameter stays out of the id, OPERATING.md 6). The class values (spec.md, "Class values") are design inputs; no holding force,
hardness or temperature figure is claimed, and nothing moves. Every size is a design choice. No vendor file was opened.
2.0 (review mech-r133 finding 1): 1.0 drew the slot 2.0 over its whole depth, so a 2.0 sheet met it with no interference."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "strip-clamping-8x15", "2.0", "rail"
TITLE = ("Clamping strip section, generic, solid EPDM U-section 8 x 15, slot 12 deep (grip 1.6, lead-in 2.0 x 2), for sheet 2.0 to 2.5, "
         "black, plain, cut to length")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic clamping strip section (ETIM 10.0 EC010640), a solid EPDM U-section 8 x 15, slot 12 deep, 1.6 "
            "wide over its grip under a 2.0 x 2 lead-in, for a sheet edge 2.0 to 2.5 by interference, black, no reinforcement, no "
            "sponge seal, plain stock; class values are design inputs (spec.md); every size a design choice; no holding force, "
            "hardness or temperature claim; no vendor file opened")
ORIGIN = ("run start x = 0, the slot's centre plane y = 0, the slot's mouth z = 0 (the sheet enters from below); the run along +x, "
          "the sheet edge seats at the slot's bottom z 12, the crown's outer face at z 15")
COMMAND = "STRIPCLMP"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius, set per primitive below (as the other profiles, mech-r106 / r131)

W, H = 8.0, 15.0                             # outside width (y), outside height (z): design choices
SHEET_MIN, SHEET_MAX = 2.0, 2.5              # Min. / Max. clamping range: the sheets it is drawn for (design choice; no force claimed)
SLOT = 1.6                                   # the grip slot's width, 0.4 under the thinnest sheet: 2.0 spreads each wall 0.2 (design choice)
MOUTH, MOUTH_D = 2.0, 2.0                    # the lead-in at the mouth, 2.0 wide (= SHEET_MIN) and 2 deep, so the sheet enters square
DEPTH = 12.0                                 # the slot's depth from the mouth, how far the sheet edge goes in: design choice
TW = (W - MOUTH) / 2.0                       # 3: each wall (leg) at the mouth, the end face's leg edges
TG = (W - SLOT) / 2.0                        # 3.2: each wall over the grip (its end-face edges are cut edges, skipped)
TC = H - DEPTH                               # 3: the crown over the sheet edge
MAT = "M-GASKET"                             # EPDM, solid, black (lib/materials.csv epdm; render layer M-GASKET, the library's black rubber)

assert TW <= 3.0 and TC <= 3.0 and SLOT <= 3.0 and MOUTH <= 3.0              # leg ends, crown, slot bottom, lead-in: "short" edges, skipped
assert W >= 8.0 and H >= 8.0 and DEPTH - MOUTH_D >= 8.0                      # every other end-face edge clears the 3 to 7 mm free-corner trap
assert SLOT < SHEET_MIN <= MOUTH < SHEET_MAX                                 # the thinnest sheet enters the lead-in and is gripped below it
assert (SHEET_MAX - SLOT) / 2.0 < TG / 4.0                                   # the spread at the largest sheet (0.45) is a small part of a wall
AREA = W * H - MOUTH * MOUTH_D - SLOT * (DEPTH - MOUTH_D)
assert abs(AREA - 100.0) < 1e-9                                              # by hand: 8 x 15 − 2.0 x 2 − 1.6 x 10 = 100 mm²


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 100.0, "length 100 or more"
    body = P.box(MAT, 0, -W / 2, 0, L, W, H)                                                 # the section: one box ...
    P.cutbox(MAT, -1.0, -MOUTH / 2, -1.0, L + 2.0, MOUTH, MOUTH_D + 1.0, body)                # ... less the lead-in (y ±1, z 0 to 2) ...
    P.cutbox(MAT, -1.0, -SLOT / 2, MOUTH_D - 0.5, L + 2.0, SLOT, DEPTH - MOUTH_D + 0.5, body)  # ... and the grip slot (y ±0.8, z 2 to 12)
    for s, nm in ((-1, "left"), (1, "right")):
        P.collider(f"leg-{nm}", 0, min(s * W / 2, s * MOUTH / 2), 0, L, TW, H)               # legs |y| 1 to 4: the slot's air stays free
    P.collider("crown", 0, -MOUTH / 2, DEPTH, L, MOUTH, TC)
    for i in range(len(P)): P.radii[i] = FILLET_R                                            # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 0, 7.5), height=40)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
