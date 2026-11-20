#!/usr/bin/env python3
"""traverse-crane-2000: generic crane hook traverse (a lifting beam), 2000 long, our own vendor-neutral design of the ETIM 10.0 class
EC004250 (Crane hook traverse; synonyms Crane traverse, Cross traverse, C-hook, ...), built unattended (OPERATING.md 12, generic
elements; group EG010320 Lifting equipment, after lug-lifting-32, lib/rounds/mech/r173.md). A painted steel box beam 2000 long, 100
wide and 200 high (wall 8, both ends closed by plates 10 thick) hangs from a crane's hook by one lug welded on its top at the middle and
carries the load from two lugs welded under it, 1600 apart. The three lugs are placed lug-lifting-32 1.0 elements, never redrawn: the
top one stands on the beam's top face, the two under it are the same part turned 180 degrees about y so they hang from its underside.
The welds are not drawn. The class's features are not on file (lib/standards/etim/class-features.csv has no EC004250 rows): spec.md
gives the design values under plain names, as lug-lifting-32 does. Every size is a design choice; no standard is claimed. No working
load limit, proof load or safety claim (lib/needs-em/mech.md 256). No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "traverse-crane-2000", "1.0", "furniture"
TITLE = ("crane hook traverse (lifting beam), generic, 2000 long, painted steel box beam 100 x 200 with a placed lifting lug on top "
         "for the hook and two placed lifting lugs under it 1600 apart for the load")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic crane hook traverse (ETIM 10.0 EC004250), a lifting beam: one painted steel box beam 2000 long, "
            "100 wide, 200 high, wall 8, closed at both ends by plates 10 thick; one placed lug-lifting-32 1.0 on its top face at the "
            "middle for the crane's hook, two placed lug-lifting-32 1.0 under it at x +-800 (turned 180 degrees about y) for the load's "
            "slings; the lug's figures read from that element (library.load); welds not drawn; class features not on file, design "
            "values under plain names (spec.md); every size a design choice; no load capacity, proof load or safety claim; no vendor "
            "file opened")
ORIGIN = ("the middle of the beam's underside: x = 0 the beam's middle along its length (x -1000 to 1000), y = 0 its mid-width "
          "(y -50 to 50), z = 0 its underside (z 0 to 200), z up; the hook's lug's eye centre at (0, 0, 280), the load lugs' eye "
          "centres at (+-800, 0, -80)")
COMMAND = "TRVCR2K"
PARAMS = dict()

LUG_V = "1.0"                                   # the lug's version, pinned
LG = library.load("lug-lifting-32", LUG_V)      # the lug (one home for each of its figures)
L = 2000.0                                      # design: the beam 2000 long over its end plates (x -1000 to 1000)
B = 100.0                                       # design: the beam 100 wide (y -50 to 50)
D = 200.0                                       # design: the beam 200 high (z 0 to 200)
T = 8.0                                         # design: the box section's wall
TE = 10.0                                       # design: the end plates 10 thick, the box's full section
XL = 800.0                                      # design: the load lugs at x +-800, 1600 apart
MAT = "M-YELLOW"                                # painted steel, the lug's layer (clamp-girder-200, beam-runway)

XT = L / 2 - TE                                 # 990: the tube's ends, where the end plates start
Z_HOOK = D + LG.ZE                              # 280: the hook's eye centre over the beam's underside
Z_LOAD = -LG.ZE                                 # -80: the load eyes' centres under it
assert abs(LG.W - 120.0) < 1e-9 and abs(LG.T - 20.0) < 1e-9 and abs(LG.H - 120.0) < 1e-9 and abs(LG.ZE - 80.0) < 1e-9   # as read
assert LG.T <= B - 2 * T                        # each lug's foot (20 thick) lies on the box's 100 face, over its inner hollow 84
assert LG.W / 2 <= XT                           # the hook lug's foot (x -60 to 60) on the top face
assert XL + LG.W / 2 <= XT - LG.W / 2           # the load lugs' feet (x 740 to 860) on the underside, 130 short of the end plates
assert abs(Z_HOOK - 280.0) < 1e-9 and abs(Z_LOAD + 80.0) < 1e-9 and abs(2 * XL - 1600.0) < 1e-9
# Volume by hand: the box section 100 x 200 - 84 x 184 = 4544 mm^2 over 1980; two end plates 10 x 100 x 200; three lugs (the lug's VOL).
SEC = B * D - (B - 2 * T) * (D - 2 * T)
VOL_BEAM = SEC * 2 * XT + 2 * TE * B * D
VOL = VOL_BEAM + 3 * LG.VOL
assert abs(SEC - 4544.0) < 1e-9 and abs(VOL_BEAM - 9397120.0) < 1e-6 and abs(VOL - 10104865.0) < 0.5


def _lug(P, tag, x, z, roll):
    """place one lug-lifting-32 1.0 and name its collider under its tag, axis-aligned (a 180-degree turn keeps it a box)"""
    n0 = len(P)
    library.place(P, dict(element="lug-lifting-32", version=LUG_V, tag=tag, parent="", x=x, y=0.0, z=z, yaw=0.0, roll=roll, params={}))
    for i in range(n0, len(P)):
        Lr, k, q = P[i]
        if not Lr.startswith("collider:"): continue
        if k == "obox":                                                          # the turned collider: back to a box, same corners
            o, ex, ey, ez, l, w, h = q
            pts = [[o[j] + ex[j] * l * a + ey[j] * w * b + ez[j] * h * c for j in range(3)] for a in (0, 1) for b in (0, 1) for c in (0, 1)]
            lo = [round(min(p[j] for p in pts), 6) for j in range(3)]; hi = [round(max(p[j] for p in pts), 6) for j in range(3)]
            q = (lo[0], lo[1], lo[2], hi[0] - lo[0], hi[1] - lo[1], hi[2] - lo[2]); k = "box"
        P[i] = (f"collider:{tag}-{Lr[9:]}", k, q)


def build():
    P = Prims()
    b = P.box(MAT, -XT, -B / 2, 0.0, 2 * XT, B, D)                                               # the box beam
    P.cutbox(MAT, -XT - 1.0, -B / 2 + T, T, 2 * XT + 2.0, B - 2 * T, D - 2 * T, b)              # its hollow, through
    P.box(MAT, -L / 2, -B / 2, 0.0, TE, B, D)                                                    # the -x end plate
    P.box(MAT, XT, -B / 2, 0.0, TE, B, D)                                                        # the +x end plate
    P.collider("beam", -L / 2, -B / 2, 0.0, L, B, D)
    _lug(P, "lug-hook", 0.0, D, 0.0)                                                             # on the top face, for the hook
    _lug(P, "lug-load-l", -XL, 0.0, 180.0)                                                       # under the beam, for the slings
    _lug(P, "lug-load-r", XL, 0.0, 180.0)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="front", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
