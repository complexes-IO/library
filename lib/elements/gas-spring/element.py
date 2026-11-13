#!/usr/bin/env python3
"""gas-spring: generic gas compression spring, our own vendor-neutral design of the ETIM 10.0 class EC012096 (Gas spring), built
unattended (OPERATING.md 12, generic elements). A steel tube Ø18 x 150 with a Ø8 piston rod, stroke 100, extended length 280 over an
M8 male stud at each end. The rod (node `rod`) slides into the tube by its stroke; the cylinder-end stud is the port `end-cyl`.
The class values (spec.md, "Class values") are design inputs. The M8 thread's limits are derived (spec.md, What it meets:
derive.thread, ISO 68-1 / ISO 965-1); the thread form is not drawn: both studs are plain cylinders at the nominal Ø8. Every size
below is a design choice. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "gas-spring", "1.2", "actuator"
TITLE = "gas spring, generic, rod Ø8, tube Ø18, stroke 100, 280 extended, M8 male both ends"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic gas spring (ETIM 10.0 EC012096); class values are design inputs (spec.md); the M8 thread "
            "derived (ISO 68-1, ISO 965-1), modelled plain; every size a design choice; no vendor file opened")
ORIGIN = ("the cylinder end's shoulder (the face its end fitting seats on) on the spring's axis; the axis along +x, the tube toward +x, "
          "the cylinder-end stud toward -x, the rod out toward +x")
COMMAND = "GASSPRING"
PARAMS = dict()
ROD_D, TUBE_D = 8.0, 18.0        # class values: outer diameter piston rod, outer diameter cylinder (spec.md)
TUBE_L = 150.0                   # class value: cylinder length, the tube from the shoulder at x = 0 to its rod-end face
STROKE = 100.0                   # class value: stroke
THREAD_L = 12.0                  # M8 stud length at each end: design choice. The thread's limits are derived (spec.md, What it meets);
                                 # the form is not drawn: modelled plain at the nominal Ø8
ROD_OUT = 118.0                  # rod out of the tube, extended, thread included: design choice (stroke 100 + 6 clear + the 12 stud)
ROD_IN = 20.0                    # rod inside the tube at full extension (guide and piston, not modelled): design choice
BORE_D = 8.4                     # the rod's bore in the tube: Ø8 + 0.2 radial clearance, design choice (features.csv)
BORE_END = TUBE_L - ROD_IN - STROKE - 10.0    # bore bottom at x = 20: 10 beyond the rod's inner end at full stroke

def build():
    P = Prims(); T, R = "M-STEEL-7035", "M-ZINC"
    tube = P.cyl(T, (0, 0, 0), (TUBE_L, 0, 0), TUBE_D / 2)                                  # the tube (cylinder), shoulder at x = 0
    P.hole(R, (TUBE_L + 1, 0, 0), (BORE_END, 0, 0), BORE_D / 2, tube)                       # the rod's bore, from the rod-end face
    P.cyl(f"node:end-cyl|{R}", (-THREAD_L, 0, 0), (0, 0, 0), ROD_D / 2)                    # cylinder-end stud M8 x 12 (plain at Ø8)
    P.pivot("end-cyl", "port", (0, 0, 0), axis=(-1, 0, 0), unit="M8", gender="male", thread="M8", length=THREAD_L)
    x0, x1 = TUBE_L - ROD_IN, TUBE_L + ROD_OUT                                              # the rod: 130 to 268 at rest (extended)
    P.cyl(f"node:rod|{R}", (x0, 0, 0), (x1, 0, 0), ROD_D / 2)                               # rod Ø8; its last 12 is the M8 stud (plain at Ø8)
    P.pivot("rod", "translate", (x1 - THREAD_L, 0, 0), axis=(-1, 0, 0), range=(0, STROKE),  # compresses into the tube by its stroke
            end="rod", gender="male", thread="M8", length=THREAD_L)
    P.collider("body", 0, -TUBE_D / 2, -TUBE_D / 2, TUBE_L, TUBE_D, TUBE_D)
    P.collider("end-cyl", -THREAD_L, -ROD_D / 2, -ROD_D / 2, THREAD_L, ROD_D, ROD_D)
    P.collider("rod", TUBE_L, -ROD_D / 2, -ROD_D / 2, ROD_OUT, ROD_D, ROD_D)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="rod end", az=330, el=15)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
