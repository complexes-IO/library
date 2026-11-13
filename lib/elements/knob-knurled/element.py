#!/usr/bin/env python3
"""knob-knurled: generic knurled knob with a threaded stud, our own vendor-neutral design of the ETIM 10.0 class EC011970 (Knurled
knob), built unattended (OPERATING.md 12, generic elements). A moulded polyamide knob: a knurled grip Ø32 over 30 straight knurl
ridges, a plain collar Ø20 under it whose underside seats on the work, and a moulded-in M6 steel stud, 20 long (port `stud`). It
clamps a part by hand: screwed into a tapped hole, or through a hole into a nut. The class values (spec.md, "Class values") are
design inputs. The M6 thread's limits are derived (spec.md, What it meets: derive.thread, ISO 68-1 / ISO 965-1); the thread form
is not drawn: the stud is a plain cylinder at the nominal Ø6. Every size below is a design choice. No vendor file was opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "knob-knurled", "1.2", "device"
TITLE = "knurled knob, generic, Ø32 x 22, PA black, M6 x 20 male stud"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic knurled knob (ETIM 10.0 EC011970); class values are design inputs (spec.md); the M6 thread "
            "derived (ISO 68-1, ISO 965-1), modelled plain; every size a design choice; no vendor file opened")
ORIGIN = ("the collar's underside (the face that seats on the work) on the knob's axis; the knob toward +z, its top face up, the "
          "stud toward -z")
COMMAND = "KNOBKNURL"
PARAMS = dict()
COLLAR_D, COLLAR_H = 20.0, 6.0   # plain collar under the grip, its underside the seating face: design choice
CORE_D = 30.0                    # the grip's core under the knurl: design choice
TOP = 22.0                       # class value: total height, the seating face to the top face (the stud not included)
RIDGES = 30                      # straight knurl, 30 ridges (12° pitch): design choice (appearance, class C)
RIDGE_IN, RIDGE_OUT = 14.4, 16.0 # each ridge from r 14.4 (inside the core, below its facets' r 14.8) to r 16: Ø32 over the ridges, the class value
RIDGE_W = 1.2                    # ridge width: design choice
RIDGE_Z = (COLLAR_H + 0.5, TOP - 0.5)   # the ridges stop 0.5 short of the grip's faces (no coplanar faces, GEO-050)
STUD_D, STUD_L = 6.0, 20.0       # class values M6, thread length 20. The thread's limits are derived (spec.md, What it meets);
                                 # the form is not drawn: modelled plain at the nominal Ø6

def build():
    P = Prims(); K, Z = "M-BLACK-PA", "M-ZINC"
    P.cyl(K, (0, 0, 0), (0, 0, COLLAR_H), COLLAR_D / 2)                                     # collar, seating face at z = 0
    P.cyl(K, (0, 0, COLLAR_H), (0, 0, TOP), CORE_D / 2)                                     # the grip's core
    for k in range(RIDGES):                                                                  # straight knurl ridges round the grip
        a = 2 * math.pi * k / RIDGES; ex = (math.cos(a), math.sin(a), 0.0); ey = (-math.sin(a), math.cos(a), 0.0)
        o = (RIDGE_IN * ex[0] - RIDGE_W / 2 * ey[0], RIDGE_IN * ex[1] - RIDGE_W / 2 * ey[1], RIDGE_Z[0])
        P.obox(K, o, ex, ey, (0, 0, 1), RIDGE_OUT - RIDGE_IN, RIDGE_W, RIDGE_Z[1] - RIDGE_Z[0])
    P.cyl(f"node:stud|{Z}", (0, 0, -STUD_L), (0, 0, 0), STUD_D / 2)                         # stud M6 x 20 (plain at Ø6), moulded in
    P.pivot("stud", "port", (0, 0, 0), axis=(0, 0, -1), unit="M6", gender="male", thread="M6", length=STUD_L)
    P.collider("body", -RIDGE_OUT, -RIDGE_OUT, 0, 2 * RIDGE_OUT, 2 * RIDGE_OUT, TOP)
    P.collider("stud", -STUD_D / 2, -STUD_D / 2, -STUD_L, STUD_D, STUD_D, STUD_L)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
