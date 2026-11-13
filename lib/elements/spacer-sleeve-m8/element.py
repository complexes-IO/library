#!/usr/bin/env python3
"""spacer-sleeve-m8: generic spacer sleeve for an M8 screw, our own vendor-neutral design of the ETIM 10.0 class EC002334 (Spacer
sleeve; the class's synonyms name the bush, the distance bush and the spacer bush), built unattended (OPERATING.md 12, generic
elements; the first class of group EG021006 Accessories/components for fasteners and anchoring systems, in lib/toolkit/generic.py's
order, whose shape no dimensional standard fixes and whose use carries no rated load; mech-r145, the 03:31 run's work, recovered). A plain round steel sleeve that an
M8 screw passes through, set between two parts to hold them a fixed distance apart: Ø14 outside, a through bore Ø9.0 (ISO 273 medium
clearance for M8, lib/standards/holes.csv), cut to length by the `length` parameter (default 20; a parameter stays out of the id,
OPERATING.md 6). The class is tier 2: its features are not in lib/standards/etim/class-features.csv, so its class values are written
under plain names as design values (the core's answers mech-8 and mech-9: right until the features come). Every size but the bore is a
design choice. No load, torque or temperature claim. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "spacer-sleeve-m8", "1.1", "connector-part"
TITLE = "spacer sleeve, generic, steel zinc plated, round D14 with an M8 clearance bore D9.0 (ISO 273 medium), cut to length (default 20)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic spacer sleeve (ETIM 10.0 EC002334), steel, zinc plated, round D14 with a through bore D9.0 for an "
            "M8 screw (ISO 273 medium clearance), length a parameter, default 20; class values are design inputs under plain names "
            "(spec.md; the class's features not on file); every other size a design choice; no load, torque or temperature claim; no "
            "vendor file opened")
ORIGIN = ("one end face (its seat on the lower clamped part) z = 0 on the sleeve's axis; the axis along +z; the other end face at "
          "z = length (default 20)")
COMMAND = "SPACERSL"
PARAMS = dict(length=20.0)

OD = 14.0                                    # outside diameter: design choice (a wall 2.5 round the bore)
BORE = 9.0                                   # M8 clearance medium, ISO 273 H13 (lib/standards/holes.csv: 9.0 to 9.22)
WALL = (OD - BORE) / 2.0                     # 2.5
MAT = "M-ZINC"                               # steel, zinc plated (render layer M-ZINC, not a printed layer)
L_MIN, L_MAX = 3.0, 200.0                    # the lengths this design takes: design choice

assert abs(WALL - 2.5) < 1e-9                # each end face a ring Ø9.0 to Ø14 for the clamped parts (and a washer) to bear on;
                                             # the screw's head and nut sizes are the screw standards', not on file, and not claimed


def build(length=20.0):
    L = float(length)
    assert L_MIN <= L <= L_MAX, f"length {L} outside {L_MIN} to {L_MAX}"
    P = Prims()
    sleeve = P.cyl(MAT, (0, 0, 0), (0, 0, L), OD / 2.0)                                         # the sleeve, Ø14 x length
    P.hole(MAT, (0, 0, -1.0), (0, 0, L + 1.0), BORE / 2.0, sleeve)                              # the through bore Ø9.0
    P.collider("sleeve", -OD / 2.0, -OD / 2.0, 0, OD, OD, L)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
