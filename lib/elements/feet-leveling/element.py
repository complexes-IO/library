#!/usr/bin/env python3
"""feet-leveling: levelling foot, our own design (OPERATING.md 12, own designs; lib/inventory.csv marks feet-leveling own_design
"yes"), built unattended. A fixed (non-swivel) machine levelling foot: a rubber anti-slip pad Ø76 x 6 bonded under a steel base
disc Ø80 x 10, a hub Ø30 x 14 on the base, and an M12 steel stud 80 long (port `stud`) that screws into a tapped hole or a nut in the
host's foot. Turning the stud in the host sets the host's height. The M12 thread's limits are derived (spec.md, What it meets:
derive.thread, ISO 68-1 / ISO 965-1); the thread form is not drawn: the stud is a plain cylinder at the nominal Ø12. Every size
below is a design choice; none is taken from the catalogue record that came with the element's folder (references/source.txt), and
no vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "feet-leveling", "1.2", "device"
TITLE = "levelling foot, fixed base Ø80, rubber pad, M12 x 80 male stud"
TOOLKIT = "1.3"
BASELINE = ("our own design: fixed levelling foot, no product matched; the M12 thread derived (ISO 68-1, ISO 965-1), modelled plain; every size a design "
            "choice; no vendor file opened")
ORIGIN = ("the pad's underside (the face that stands on the floor) on the foot's axis; the foot toward +z, the stud up, its tip at "
          "z = 110")
COMMAND = "FEETLEVEL"
PARAMS = dict()
PAD_D, PAD_T = 76.0, 6.0         # rubber anti-slip pad, 2 inside the base's rim (no flush side faces, GEO-050): design choice
BASE_D, BASE_T = 80.0, 10.0      # steel base disc: design choice
HUB_D, HUB_H = 30.0, 14.0        # hub on the base that carries the stud: design choice
STUD_D, STUD_L = 12.0, 80.0      # M12 (designation), 80 long: design choice. The thread's limits are derived (spec.md, What it
                                 # meets); the form is not drawn: modelled plain at the nominal Ø12
Z_BASE = PAD_T                   # 6: the base's underside
Z_HUB = PAD_T + BASE_T           # 16: the base's top face, the hub's underside
Z_STUD = Z_HUB + HUB_H           # 30: the hub's top face, the stud's root (the port)

def build():
    P = Prims(); Z, R = "M-ZINC", "M-GASKET"
    P.cyl(R, (0, 0, 0), (0, 0, PAD_T), PAD_D / 2)                                            # pad, stands on the floor at z = 0
    P.cyl(Z, (0, 0, Z_BASE), (0, 0, Z_HUB), BASE_D / 2)                                      # base disc
    P.cyl(Z, (0, 0, Z_HUB), (0, 0, Z_STUD), HUB_D / 2)                                       # hub
    P.cyl(f"node:stud|{Z}", (0, 0, Z_STUD), (0, 0, Z_STUD + STUD_L), STUD_D / 2)            # stud M12 x 80 (plain at Ø12)
    P.pivot("stud", "port", (0, 0, Z_STUD), axis=(0, 0, 1), unit="M12", gender="male", thread="M12", length=STUD_L)
    P.collider("body", -BASE_D / 2, -BASE_D / 2, 0, BASE_D, BASE_D, Z_STUD)
    P.collider("stud", -STUD_D / 2, -STUD_D / 2, Z_STUD, STUD_D, STUD_D, STUD_L)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
