#!/usr/bin/env python3
"""threaded-sleeve-m8: generic threaded sleeve with an M8 internal thread, our own vendor-neutral design of the ETIM 10.0 class
EC002350 (Threaded sleeve; the class's synonyms name the adapter, the distance holder, the sleeve and the spacer sleeve), built
unattended (OPERATING.md 12, generic elements; group EG021006 Accessories/components for fasteners and anchoring systems, by name after
spacer-sleeve-m8, mech-r145's list). A plain round steel sleeve tapped M8 right through, set between two parts to hold them a fixed
distance apart, an M8 screw driven into each end: Ø14 outside (spacer-sleeve-m8's, so the two stand on the same ring), the M8 x 1.25
thread drawn at its minor diameter D1 6.6468 (derived: derive.thread(8.0, 1.25): ISO 68-1 basic profile, ISO 965-1 clause 10, 6H D1
min; ISO 261 pitch), the thread itself not drawn; cut to length by the `length` parameter (default 20; a parameter stays out of the id,
OPERATING.md 6). The class is tier 2: its features are not in lib/standards/etim/class-features.csv, so its class values are written
under plain names as design values (the core's answers mech-8 and mech-9). Every size but the thread is a design choice. No load,
torque or temperature claim. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "threaded-sleeve-m8", "1.0", "connector-part"
TITLE = "threaded sleeve, generic, steel zinc plated, round D14 tapped M8 through (thread drawn at its minor diameter), cut to length (default 20)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic threaded sleeve (ETIM 10.0 EC002350), steel, zinc plated, round D14, tapped M8 x 1.25 right "
            "through, drawn at the minor diameter D1 6.6468 (derived: derive.thread(8.0, 1.25), ISO 68-1, ISO 965-1 6H), length a "
            "parameter, default 20; class values are design inputs under plain names (spec.md; the class's features not on file); "
            "every other size a design choice; no load, torque or temperature claim; no vendor file opened")
ORIGIN = ("one end face (its seat on the lower part) z = 0 on the sleeve's axis; the axis along +z; the other end face at "
          "z = length (default 20)")
COMMAND = "THRDSLV"
PARAMS = dict(length=20.0)

OD = 14.0                                    # outside diameter: design choice, spacer-sleeve-m8's (the same Ø14 ring on a host's face)
TAP_D1 = 6.6468                              # M8 x 1.25 internal thread drawn at its minor diameter D1 (6H min): derived:
                                             # derive.thread(8.0, 1.25) (ISO 68-1; ISO 965-1 clause 10; ISO 261 pitch 1.25)
NOMINAL = 8.0                                # the thread's nominal diameter (ISO 261)
WALL_AT_D = (OD - NOMINAL) / 2.0             # 3.0: the wall left outside the thread's major diameter
MAT = "M-ZINC"                               # steel, zinc plated (render layer M-ZINC, not a printed layer)
L_MIN, L_MAX = 16.0, 200.0                   # design choice: at least one nominal diameter (8) of thread for the screw at each end

assert abs(WALL_AT_D - 3.0) < 1e-9 and TAP_D1 < NOMINAL < OD


def build(length=20.0):
    L = float(length)
    assert L_MIN <= L <= L_MAX, f"length {L} outside {L_MIN} to {L_MAX}"
    assert L / 2.0 >= NOMINAL                                                                     # 8 of engagement a screw, each end
    P = Prims()
    sleeve = P.cyl(MAT, (0, 0, 0), (0, 0, L), OD / 2.0)                                         # the sleeve, Ø14 x length
    P.hole(MAT, (0, 0, -1.0), (0, 0, L + 1.0), TAP_D1 / 2.0, sleeve)                            # M8 tapped through, at D1 6.6468
    P.collider("sleeve", -OD / 2.0, -OD / 2.0, 0, OD, OD, L)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
