#!/usr/bin/env python3
"""gland-m20: M20 x 1.5 nylon cable gland with locknut, cord 6.1-13. Brief: references/measure.md (largest diameter 29.72, hexes
27 / 25 AF, 38.1 overall = 27.7 body + 10.2 thread). 1.2 (review gland-m20-1.1): the body stands 27.7 proud of the plate face and the
thread runs 10.2 from it (was 38.1 + 12.2, the thread counted twice); the hexes are solids (a cylinder with six flats cut, as
nut-m12), so the STEP and DWG carry them: body and dome nut 27 AF with the corners turned to the drawing's largest diameter 29.72,
the locknut 25 AF (the AF assignment: spec.md, Assumption (B)). 1.3 (PIN-002): the `self` port declares gender none (a gland, as
OPERATING.md 6 names it); the part is unchanged."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "gland-m20", "1.3", "connector"
TITLE = "M20 x 1.5 nylon cable gland with locknut, 6-13 mm cord"
TOOLKIT = "1.3"
BASELINE = "reference gland, 2-D drawing p. 1 and STEP read-back (references/measure.md)"
ORIGIN = "cut-out centre class: knockout centre on the plate's outer face y = 0, dome toward -y, locknut toward +y inside"
COMMAND = "GLND"
CUTOUT = 20.5                   # lib/standards/holes.csv:27, M20 x 1.5 entry 20.2 to 20.7 (manufacturer practice); 20.5 a choice in it
PARAMS = dict(plate_t=2.0)

D_MAX = 29.72                   # largest diameter, drawing p. 1 (1.17 in)
BODY_L = 27.7                   # body length above the seat face, drawing p. 1 (1.09 in)
THREAD_L = 10.2                 # thread length from the seat face, drawing p. 1 (0.4 in)
THREAD_D = 20.0                 # M20 x 1.5: the designation's nominal diameter (drawing p. 1)
AF_BODY, AF_LOCK = 27.0, 25.0   # drawing p. 1 gives 25 and 27; which part takes which: STEP read-back (spec.md, Assumption (B))
LOCK_L = 6.0                    # locknut thickness, STEP read-back (measure.md)
SEAL_D = 13.0                   # the seal's bore at the largest cord, 13 (product page)
TURN_BODY, TURN_LOCK = 15.0, 0.0   # each hex's turn about the axis (free: no figure sets it; the locknut turns on its own). The body at
                                # 15 deg: a turned corner 15 deg off x and z, so the cut glb measures 29.3 both ways, within 2 mm of the
                                # catalogue's uncut 29.72 (Godot QA; at 0 a flat faces x, 27.0 against the catalogue's 30: the catalogue
                                # does not apply cuts, reported to the core in mech-r8). The locknut at 0: its 25 AF faces x, where the
                                # AutoCAD gate's brief check finds it

def _hex(P, L, y0, y1, af, d, turn=0.0):
    """a hex prism on the y axis: a cylinder of diameter d with six flats cut at af / 2 (corners turned where d < af / cos 30)"""
    c = P.cyl(L, (0, y0, 0), (0, y1, 0), d / 2.0); lo = min(y0, y1)
    for k in range(6):
        t = math.radians(30 + turn + 60 * k); n = (math.sin(t), 0.0, math.cos(t)); tg = (math.cos(t), 0.0, -math.sin(t))
        o = (n[0] * af / 2.0 + tg[0] * 12.0, lo - 1.0, n[2] * af / 2.0 + tg[2] * 12.0)
        P.cut(L, o, n, (0, 1, 0), (-tg[0], 0.0, -tg[2]), 4.0, abs(y1 - y0) + 2.0, 24.0, c)
    return c

def build(plate_t=2.0):
    if not 0 < plate_t <= THREAD_L - LOCK_L: raise ValueError(f"plate_t {plate_t}: the locknut ({LOCK_L}) must fit on the {THREAD_L} thread")
    P = Prims(); M = "M-GREY-PA"
    _hex(P, M, 0.0, -BODY_L, AF_BODY, D_MAX, TURN_BODY)                                               # body hex and dome nut, one profile
    P.cyl("node:self|M-GASKET", (0, -BODY_L - 0.2, 0), (0, -BODY_L + 0.6, 0), SEAL_D / 2.0)          # seal insert 0.2 proud of the dome end (GEO-050)
    P.pivot("self", "port", (0, -BODY_L, 0), axis=(0, -1, 0), range=(0, 0), unit="cable", gender="none")   # PIN-002: a gland (OPERATING.md 6)
    P.cyl(M, (0, 0, 0), (0, THREAD_L, 0), THREAD_D / 2.0)                                             # thread spigot through the plate
    _hex(P, M, plate_t, plate_t + LOCK_L, AF_LOCK, D_MAX, TURN_LOCK)                                 # locknut inside (sharp: 28.87 across corners)
    P.collider("env", -D_MAX / 2, -BODY_L, -D_MAX / 2, D_MAX, BODY_L + THREAD_L, D_MAX)
    return P

PREVIEWS = [dict(name="three-quarter", az=250, el=25), dict(name="inside locknut", az=60, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
