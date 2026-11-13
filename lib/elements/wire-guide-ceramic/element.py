#!/usr/bin/env python3
"""wire-guide-ceramic: generic ceramic wire guide (a flanged eyelet of hard ceramic that a running wire, thread or fine cable passes
through, so the wire wears the ceramic and not the machine's frame), our own vendor-neutral design of the ETIM 10.0 class EC010725
(Ceramic wire guide), built unattended (OPERATING.md 12, generic elements). A flange 24 across and 4 thick seats on the host's
plate; a shank 14 across goes 8 into the host's hole; the bore is 8 through, 12 long. The class values (spec.md, "Class values")
are design inputs; the class has no load, speed or wear feature, so none is claimed and nothing moves in the model. Every size is a
design choice. No vendor file was opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "wire-guide-ceramic", "1.0", "device"
TITLE = "ceramic wire guide, generic, flanged eyelet, bore 8, length 12, flange 24 x 4, shank 14 x 8"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic ceramic wire guide (ETIM 10.0 EC010725), a flanged eyelet of alumina ceramic; class values "
            "are design inputs (spec.md); the host's hole a design figure with a bond gap; every size a design choice; no load, "
            "speed or wear claim; no vendor file opened")
ORIGIN = ("the seating face (the flange's underside, z = 0, where it seats on the host's plate) on the bore's axis; the bore along z, "
          "the flange above (z 0 to 4), the shank below in the host's hole (z -8 to 0)")
COMMAND = "WIREGUIDECER"
PARAMS = dict()

BORE_D = 8.0                                     # class value: inner diameter 8
LENGTH = 12.0                                    # class value: length 12 (the flange's top face to the shank's end)
FL_D, FL_T = 24.0, 4.0                           # the flange, 24 across, 4 thick: design choice
SH_D = 14.0                                      # the shank, 14 across: design choice (3 of ceramic around the bore)
SH_L = LENGTH - FL_T                             # 8: the shank below the seating face
IN = 0.5                                         # the shank runs 0.5 into the flange (one solid joint)
GAP = 0.1                                        # radial bond gap in the host's hole: design choice (What it meets)
HOST_D = SH_D + 2 * GAP                          # 14.2: the host's hole
MAT = "M-WHITE-PA"                               # appearance only: white (alumina ceramic, spec.md; no ceramic layer in godot/qa/materials)

assert (SH_D - BORE_D) / 2 >= 3.0                # 3 of ceramic wall around the bore in the shank
assert (FL_D - HOST_D) / 2 >= 4.0                # the flange overlaps the host's hole 4.9 all round
assert FL_T >= 3.0 and SH_L >= 2 * FL_T          # a flange stiff enough to seat, a shank twice its thickness


def build():
    P = Prims()
    fl = P.cyl(MAT, (0, 0, 0.0), (0, 0, FL_T), FL_D / 2)                    # flange, seating face at z 0
    sh = P.cyl(MAT, (0, 0, -SH_L), (0, 0, IN), SH_D / 2)                     # shank in the host's hole, 0.5 into the flange
    P.hole(MAT, (0, 0, -1.0), (0, 0, FL_T + 1.0), BORE_D / 2, fl)             # the bore through the flange
    P.hole(MAT, (0, 0, -SH_L - 1.0), (0, 0, IN + 1.0), BORE_D / 2, sh)        # the same bore through the shank (one hole cuts one solid)
    P.collider("body", -FL_D / 2, -FL_D / 2, -SH_L, FL_D, FL_D, LENGTH)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
