#!/usr/bin/env python3
"""tslot-nut: slide nut for tslot-40's T-slot, our own vendor-neutral design of the ETIM 10.0 class EC000096 (Slide nut), built
unattended (OPERATING.md 12, generic elements; lib/inventory.csv row "tslot-nut", own_design generic, etim EC000096, "T-slot nut for
40 mm profile", a common part). The nut a bracket, a panel or a part is screwed to anywhere along a tslot-40 profile: slid in from
the profile's cut end along the slot, an M8 screw through the host's part drawn into it pulls its body up against the slot's lips.
A body under the lips (in the undercut) and a neck in the slot's opening that keeps it from turning, one M8 thread through both.
Every figure it meets is read from tslot-40 (library.load), so the slot and the nut cannot drift apart. The internal thread's
figures are derived (ISO 68-1, ISO 965-1); it is drawn as a plain bore at its minor diameter. The class values (spec.md, "Class
values") are design inputs; every other size is a design choice. No load, torque or slip claim. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "tslot-nut", "1.0", "connector-part"
TITLE = "slide nut M8 for tslot-40's T-slot, generic, 20 long, body 14 x 3 under the lips, neck 9 x 3 in the opening"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic slide nut (ETIM 10.0 EC000096) for tslot-40 1.0's T-slot (figures read with library.load); "
            "class values are design inputs (spec.md); M8 internal thread 6H derived (ISO 68-1 / ISO 965-1), drawn plain at its "
            "minor diameter; every other size a design choice; no load or torque claim; no vendor file opened")
ORIGIN = ("the nut's bearing face (the body's top, which the M8 screw draws up against the slot's lips) on the thread's axis; x along "
          "the slot, +z out of the slot toward the profile's face (the neck)")
COMMAND = "TSLOTNUT"
PARAMS = dict()

TS = library.load("tslot-40")                # tslot-40 1.0: the profile whose slot this nut runs in (one home for the slot's figures)
CLEAR = 0.5                                  # side clearance in the slot, each side: design choice (the nut slides in from a cut end)
BODY_W = TS.UNDER_W - 2 * CLEAR              # 14: the body across the slot, in the 15 undercut
NECK_W = TS.THROAT - 2 * CLEAR               # 9: the neck across the slot, in the 10 opening
BODY_T = 3.0                                 # the body's height under the lips: design choice (3.0, so its short edges are under the gate's 3 mm minimum, mech-r101)
NECK_T = TS.LIP - 1.0                        # 3: the neck stops 1.0 under the profile's face, so the host's part clamps on the face, not on the nut
LENGTH = 20.0                                # along the slot: design choice (class value Length)
THREAD_D1 = 6.6468                           # M8 internal 6H, D1 min: derived: derive.thread(8.0, 1.25) (ISO 68-1; ISO 965-1 clause 10); the thread itself is not drawn
MAT = "M-ZINC"                               # steel, zinc-plated

assert BODY_W < TS.UNDER_W and NECK_W < TS.THROAT and BODY_W > TS.THROAT       # the body can't pull through the opening: it bears on the lips
assert BODY_T <= TS.UNDER_H - CLEAR and NECK_T < TS.LIP                         # the body fits under the lips with room below; the neck stays under the face
assert (BODY_W - TS.THROAT) / 2 >= 2.0                                          # 2.0 of bearing on each lip
assert (NECK_W - THREAD_D1) / 2 >= 1.0                                          # the neck's walls beside the thread


def build():
    P = Prims()
    body = P.box(MAT, -LENGTH / 2, -BODY_W / 2, -BODY_T, LENGTH, BODY_W, BODY_T)          # under the lips, z -3..0
    neck = P.box(MAT, -LENGTH / 2, -NECK_W / 2, 0.0, LENGTH, NECK_W, NECK_T)               # in the slot's opening, z 0..3
    P.hole(MAT, (0, 0, -BODY_T - 1.0), (0, 0, 0.5), THREAD_D1 / 2, body)                  # M8 through the body, plain at D1
    P.hole(MAT, (0, 0, -0.5), (0, 0, NECK_T + 1.0), THREAD_D1 / 2, neck)                  # and through the neck (one hole cuts one solid)
    P.collider("nut", -LENGTH / 2, -BODY_W / 2, -BODY_T, LENGTH, BODY_W, BODY_T + NECK_T)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="end", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
