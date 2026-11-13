#!/usr/bin/env python3
"""slide-profile-flat-belt: generic flat belt slide profile, our own vendor-neutral design of the ETIM 10.0 class EC010730 (Flat belt
slide profile), built unattended (OPERATING.md 12, generic elements; `python lib/build.py inventory mech` lists the class as the next
mech class once no inventory row builds unattended). A flat belt's carrying run slides along it instead of on rollers: a plastic slide
profile 66 wide and 12 high with a tread 50 wide sunk 2 between two guide lips 8 wide, so a flat belt up to 50 wide slides on the tread
and the lips keep it on the run; under it a galvanized steel mounting flat 100 x 3 with M6 clearance holes (ISO 273 medium) beside the
profile, for the screws into the conveyor's frame. Cut to length (the `length` parameter; a parameter stays out of the id, OPERATING.md
6). slide-profile-round-belt's sibling (EC010729): the same flat, holes and construction. The class values (spec.md, "Class values")
are design inputs; the class has no load, speed or friction feature, so none is claimed and nothing moves in the model (the belt is the
host's). Every size is a design choice. No vendor file was opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "slide-profile-flat-belt", "1.1", "rail"
TITLE = "flat belt slide profile, generic, 66 x 12 with a tread 50 between two guide lips, on a 100 x 3 mounting flat, cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic flat belt slide profile (ETIM 10.0 EC010730), a PE-UHMW slide profile with a tread 50 wide between "
            "two guide lips on a galvanized steel mounting flat with M6 holes at ISO 273 medium clearance; class values are design "
            "inputs (spec.md); every size a design choice; no load, speed or friction claim; no vendor file opened")
ORIGIN = ("run start x = 0, the profile's centre line y = 0, the mounting flat's underside z = 0 (the mounting face, on the frame); "
          "the run along +x, the tread up at z 13, the lips' tops at z 15")
COMMAND = "SLIDEPROFFB"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                                   # the gate's radius, set per primitive below (the rail class's 1.0 reads 10 mm edges short, mech-r69 / r106)

TREAD = 50.0                                     # the tread's width: a flat belt up to 50 wide slides on it: design choice (class value Tread width)
LIP_W, LIP_H = 8.0, 2.0                          # the guide lips each side, 8 wide, standing 2 over the tread: design choice
PW, PH = TREAD + 2 * LIP_W, 12.0                 # the slide profile, 66 wide (y), 12 high (z): design choices (class values Width, Height)
FW, FT = 100.0, 3.0                              # the mounting flat, 100 wide, 3 thick: design choice (3.0: the gate's "short" edge, skipped)
HOLE_D = 6.6                                     # M6 clearance medium H13 (ISO 273, lib/standards/holes.csv)
HOLE_Y = 41.0                                    # the holes' rows, y +-41: design: an M6 head up to Ø10.5 clears the profile's side (33) by
                                                 # 2.75 and the flat's edge (50) by 3.75 (a design allowance; screw-head standards not on file)
END = 50.0                                       # the end holes 50 in from each end; between them at most HOLE_PITCH apart
HOLE_PITCH = 450.0
MAT_P = "M-WHITE-PA"                             # the slide profile, appearance only (white): PE-UHMW (spec.md; no PE layer in godot/qa/materials)
MAT_F = "M-GALV"                                 # the mounting flat, galvanized steel

assert PH - LIP_H >= 8.0                                                   # 10 of profile under the tread
assert LIP_W >= 8.0                                                        # each lip's top end edge 8 or longer (the fillet trap: 3 to 7)
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
    P.cutbox(MAT_P, -1.0, -TREAD / 2, FT + PH - LIP_H, L + 2.0, TREAD, LIP_H + 1.0, prof)   # the tread, sunk 2 between the lips, open both ends
    for x in hole_xs(L):
        for s in (-1, 1):
            P.hole(MAT_F, (x, s * HOLE_Y, -1.0), (x, s * HOLE_Y, FT + 1.0), HOLE_D / 2, flat)   # M6 clearance through the flat
    P.collider("body", 0, -FW / 2, 0, L, FW, FT + PH)
    for i in range(len(P)): P.radii[i] = FILLET_R                                        # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 0, 8), height=120)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
