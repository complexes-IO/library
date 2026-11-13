#!/usr/bin/env python3
"""seal-m12: the face seal of an M12 joint. NOT ON FILE: no file on hand shows a seal (round 4), so it is modelled where the parts on
file leave room for one: a flat ring on the female's bore floor round the insert, pressed by the male sleeve's front at the seat
(toolkit/m12.py 1.3). That, and the nut's torque, is what makes the joint IP67 (toolkit/contact.py). A compress pivot: the binder
squeezes it as the plug comes home. Built in the M12 mating frame: the face the sleeve presses at y = 0, the ring toward +y.
Brief: references/measure.md."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, m12
from toolkit.prims import Prims

ID, VERSION, CLASS = "seal-m12", "1.2", "connector-part"
TITLE = "M12 face seal ring, FKM / NBR class, on the female's bore floor, pressed by the male sleeve"
TOOLKIT = "1.3"
BASELINE = "own design (toolkit/m12.py 1.3): NOT ON FILE in any file on hand; Ø8.2 to Ø10.92, as thick as the gap the male sleeve leaves to the bore floor plus a 0.2 squeeze: Assumption"
ORIGIN = "the pressed face on the ring axis; the ring toward +y"
COMMAND = "M12SEAL"
PARAMS = dict(r_in=m12.INSERT_R["A"], r_out=m12.THREAD_R, thick=m12.seal_thick("A"))

def build(r_in=m12.INSERT_R["A"], r_out=m12.THREAD_R, thick=m12.seal_thick("A")):
    P = Prims(); t = float(thick)
    ring = P.cyl("node:self|M-GASKET", (0, 0, 0), (0, t, 0), r_out)
    P.hole("M-GASKET", (0, -1.0, 0), (0, t + 1.0, 0), r_in, ring)
    P.pivot("self", "compress", (0, t, 0), axis=(0, -1, 0), range=(0, m12.SEAL["squeeze"]), unit="mm")
    P.collider("env", -r_out, 0, -r_out, 2 * r_out, t, 2 * r_out)
    return P

PREVIEWS = [dict(name="seal", az=250, el=35)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
