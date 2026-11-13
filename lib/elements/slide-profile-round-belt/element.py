#!/usr/bin/env python3
"""slide-profile-round-belt: generic circular belt slide profile, our own vendor-neutral design of the ETIM 10.0 class EC010729
(Circular belt slide profile), built unattended (OPERATING.md 12, generic elements; `python lib/build.py inventory mech` lists the
class as the next mech class once no inventory row builds unattended). A round belt's carrying run slides along it instead of on
rollers: a plastic slide profile 30 wide and 15 high with a 90-degree V-groove along its top (11.3 wide, 5.66 deep), so a Ø8
round belt rests on both flanks with its centre in the top face and stands 4 above the profile to carry the goods; under it a galvanized steel mounting flat 62 x 3 with
M6 clearance holes (ISO 273 medium) beside the profile, for the screws into the conveyor's frame. Cut to length (the `length`
parameter; a parameter stays out of the id, OPERATING.md 6). The class values (spec.md, "Class values") are design inputs; the class
has no load, speed or friction feature, so none is claimed and nothing moves in the model (the belt is the host's). Every size is a
design choice. No vendor file was opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "slide-profile-round-belt", "1.1", "rail"
TITLE = "circular belt slide profile, generic, 30 x 15 with a 90-degree V-groove for a round belt 8, on a 62 x 3 mounting flat, cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic circular belt slide profile (ETIM 10.0 EC010729), a PE-UHMW slide profile with a 90-degree V-groove "
            "for a round belt 8 on a galvanized steel mounting flat with M6 holes at ISO 273 medium clearance; class values are design "
            "inputs (spec.md); every size a design choice; no load, speed or friction claim; no vendor file opened")
ORIGIN = ("run start x = 0, the profile's centre line y = 0, the mounting flat's underside z = 0 (the mounting face, on the frame); "
          "the run along +x, the groove up, the belt's axis in the profile's top face at z 18")
COMMAND = "SLIDEPROFRB"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                                   # the gate's radius, set per primitive below: the profile's top end edges are 9.3
                                                 # between the corner and the groove (r 1.0, the rail class's default, reads 10 mm edges short, mech-r69)

BELT_D = 8.0                                     # the round belt the groove is made for: design choice (the class value "belt", spec.md)
V_DEPTH = BELT_D / 2 * math.sqrt(2.0)            # a 90-degree V-groove whose flanks touch the belt with its centre in the top face:
V_TOP = 2 * V_DEPTH                              # apex 5.657 under the top face, 11.314 wide there; the belt stands 4 above the profile
PW, PH = 30.0, 15.0                             # the slide profile, 30 wide (y), 15 high (z): design choices (class values Width, Height)
FW, FT = 62.0, 3.0                               # the mounting flat, 62 wide, 3 thick: design choice (3.0: the gate's "short" edge, skipped);
                                                 # 62 so each hole's edge distance 31 - 22.5 - 3.3 = 5.2 >= 1.5 t = 4.5 (DFM-010)
HOLE_D = 6.6                                     # M6 clearance medium H13 (ISO 273, lib/standards/holes.csv)
HOLE_Y = 22.5                                    # the holes' rows, y +-22.5: design: an M6 head up to Ø10.5 clears the profile's side (15)
                                                 # by 2.25 and the flat's edge (31) by 3.25 (screw-head standards not on file: a design allowance)
END = 50.0                                       # the end holes 50 in from each end; between them at most HOLE_PITCH apart
HOLE_PITCH = 450.0
MAT_P = "M-WHITE-PA"                             # the slide profile, appearance only (white): PE-UHMW (spec.md; no PE layer in godot/qa/materials)
MAT_F = "M-GALV"                                 # the mounting flat, galvanized steel

assert PH - V_DEPTH >= 8.0                                                 # 8 or more of profile under the groove's apex
assert (PW - V_TOP) / 2 >= 8.0                                         # each top end-edge segment 8 or longer (the fillet trap: 3 to 7)
assert HOLE_Y - 5.25 > PW / 2 + 2.0 and FW / 2 - HOLE_Y - 5.25 >= 2.0       # the screw head clears the profile and the flat's edge
assert FW / 2 - HOLE_Y - HOLE_D / 2 >= 1.5 * FT                            # DFM-010: hole edge distance 1.5 t or more
assert FT <= 3.0                                                         # the flat's end and side edges "short", skipped by the gate


def hole_xs(L):
    """the holes' x positions: END in from each end, evenly between at most HOLE_PITCH apart"""
    n = int(math.ceil((L - 2 * END) / HOLE_PITCH)) + 1
    return [END + k * (L - 2 * END) / (n - 1) for k in range(n)]


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 200.0, "length 200 or more"
    flat = P.box(MAT_F, 0, -FW / 2, 0, L, FW, FT)                                        # the mounting flat, on the frame
    prof = P.box(MAT_P, 0, -PW / 2, FT, L, PW, PH)                                       # the slide profile, seated on the flat
    a = 1.0 / math.sqrt(2.0); S = 12.0                                                   # S: past the top face along each flank (8.0 reaches it)
    P.cut(MAT_P, (-1.0, 0, FT + PH - V_DEPTH), (1, 0, 0), (0, a, a), (0, -a, a),        # the 90-degree V-groove along the top, open both ends:
          L + 2.0, S, S, prof)                                                            # corner on the apex line, ey / ez along the two flanks
    for x in hole_xs(L):
        for s in (-1, 1):
            P.hole(MAT_F, (x, s * HOLE_Y, -1.0), (x, s * HOLE_Y, FT + 1.0), HOLE_D / 2, flat)   # M6 clearance through the flat
    P.collider("body", 0, -FW / 2, 0, L, FW, FT + PH)
    for i in range(len(P)): P.radii[i] = FILLET_R                                        # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 0, 10), height=80)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
