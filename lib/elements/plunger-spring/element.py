#!/usr/bin/env python3
"""plunger-spring: generic slotted spring plunger with a thrust pin, our own vendor-neutral design of the ETIM 10.0 class EC011996
(Spring plunger), built unattended (OPERATING.md 12, generic elements). A steel body threaded M8 over its 16 length (node `self`,
the port that screws into the host), slotted at the rear for a screwdriver, with a Ø4 thrust pin (node `pin`) that a spring
inside holds 2 proud of the front face and that presses in flush against it. It locates, detents or ejects a part. The class
values (spec.md, "Class values") are design inputs. The M8 thread is derived (derive.thread, ISO 68-1 / ISO 965-1; spec.md, "What
it meets"); the body is modelled plain at the nominal Ø8. One fit is NOT ON FILE (B): the slot's fit to a screwdriver blade
(modelled at a design size). Every size below is a design choice. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "plunger-spring", "1.1", "device"
TITLE = "spring plunger, generic, M8 x 16, slotted, thrust pin Ø4, travel 2, 10 to 30 N"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic spring plunger (ETIM 10.0 EC011996); class values are design inputs (spec.md); the M8 thread "
            "derived (ISO 68-1, ISO 965-1), modelled plain; the slot's screwdriver fit NOT ON FILE (B); every size a design choice; no vendor file opened")
ORIGIN = ("the front face (the face the pin stands out of) on the plunger's axis; the pin toward +z, the threaded body toward -z, "
          "its slotted rear face at z = -16")
COMMAND = "SPRPLUNGER"
PARAMS = dict()
BODY_D = 8.0                     # class value M8. The thread is derived (derive.thread(8.0, 1.25), spec.md): modelled plain at the nominal Ø8
BODY_L = 16.0                    # class value: length, the threaded body from its rear face to its front face
PIN_D = 4.0                      # class value: diameter, the thrust pin
PIN_OUT = 2.0                    # the pin stands 2 proud of the front face at rest and presses in flush: its travel, design choice
PIN_L = 8.0                      # pin length, 6 of it inside the body at rest: design choice
BORE_D, BORE_DEPTH = 4.2, 9.0    # the pin's bore, 0.1 radial clearance, 9 deep from the front face (features.csv): design choice
SLOT_W, SLOT_DEPTH = 1.2, 2.0    # rear slot across the full Ø8. Its fit to a screwdriver blade NOT ON FILE (B): a design size

def build():
    P = Prims(); Z = "M-ZINC"
    body = P.cyl(f"node:self|{Z}", (0, 0, -BODY_L), (0, 0, 0), BODY_D / 2)                    # threaded body M8 x 16 (plain at Ø8)
    P.hole(Z, (0, 0, 1), (0, 0, -BORE_DEPTH), BORE_D / 2, body)                               # the pin's bore, from the front face
    P.cutbox(Z, -BODY_D / 2 - 1, -SLOT_W / 2, -BODY_L - 1, BODY_D + 2, SLOT_W, SLOT_DEPTH + 1, body)   # screwdriver slot in the rear face
    P.pivot("self", "port", (0, 0, 0), axis=(0, 0, -1), unit="M8", gender="male", thread="M8", length=BODY_L)
    P.cyl(f"node:pin|{Z}", (0, 0, PIN_OUT - PIN_L), (0, 0, PIN_OUT), PIN_D / 2)               # thrust pin Ø4, z -6 to 2 at rest
    P.pivot("pin", "translate", (0, 0, PIN_OUT), axis=(0, 0, -1), range=(0, PIN_OUT))          # pressed in, flush at 2
    P.collider("self", -BODY_D / 2, -BODY_D / 2, -BODY_L, BODY_D, BODY_D, BODY_L)
    P.collider("pin", -PIN_D / 2, -PIN_D / 2, 0, PIN_D, PIN_D, PIN_OUT)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="slotted rear", az=230, el=-35)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
