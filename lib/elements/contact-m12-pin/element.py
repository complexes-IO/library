#!/usr/bin/env python3
"""contact-m12-pin: one male contact of an M12 insert, as its own element so it can be bent, pushed back, broken or corroded, and so the
joint's state comes from where it actually is. Built in the M12 mating frame (toolkit/m12.py): tip at the origin, the pin pointing
toward -y (out of the carrier face, which is at y = protrude), its root toward +y. Brief: references/measure.md."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, m12
from toolkit.prims import Prims

ID, VERSION, CLASS = "contact-m12-pin", "1.2", "contact"
TITLE = "M12 male contact (pin), gold-plated, Ø1.0 (A / D) or Ø1.5 (L), with condition"
TOOLKIT = "1.3"
BASELINE = "own design to the M12 interface (toolkit/m12.py 1.2): Ø1.0 protruding 6.45 + a 0.45 rounded tip (A / D cordset drawing), Ø1.5 x 4.8 (L drawing); collar and tail an Assumption"
ORIGIN = "the pin tip on the pin axis; the pin points toward -y, the carrier face at y = protrude"
COMMAND = "M12PIN"
PARAMS = dict(d=1.0, pole="1", condition="ok", recess=4.7, tail=3.0, protrude=6.9, lead=0.45)
BEND = 12.0                                    # deg: a bent pin (condition) leans this far toward +z

def build(d=1.0, pole="1", condition="ok", recess=4.7, tail=3.0, protrude=6.9, lead=0.45):
    """protrude, lead: toolkit/m12.py PIN for the coding (A / D 6.9, 0.45; L 4.8, 0.4). recess: how far a pushed-back pin sits back
    (4.7 leaves an A / D pin only marginal at the seat)"""
    P = Prims(); r = d / 2; L = float(protrude); ch = float(lead)
    mat = "M-CU-CORRODED" if condition == "corroded" else "M-GOLD"
    y0 = recess if condition == "pushed-back" else 0.0                     # a pin pushed back into its carrier: the tip sits behind
    if condition == "bent":
        th = math.radians(BEND); a = (0.0, -math.cos(th), math.sin(th))      # the exposed shank leans about the carrier face
        base = (0.0, L, 0.0); tip = tuple(base[i] + a[i] * L for i in range(3))
        P.cyl(f"node:self|{mat}", base, tuple(base[i] + a[i] * (L - ch) for i in range(3)), r)
        P.cyl(f"node:self|{mat}", tuple(base[i] + a[i] * (L - ch) for i in range(3)), tip, r * 0.7)
        origin, axis = tip, a
    elif condition == "broken":
        stub = 0.6
        P.cyl(f"node:self|{mat}", (0, L, 0), (0, L - stub, 0), r)            # what is left above the carrier face
        origin, axis = (0.0, L - stub, 0.0), (0.0, -1.0, 0.0)
    else:
        P.cyl(f"node:self|{mat}", (0, y0 + ch, 0), (0, y0, 0), r * 0.7)        # lead-in
        P.cyl(f"node:self|{mat}", (0, y0 + L + 2.0, 0), (0, y0 + ch, 0), r)    # shank (the contact zone) on into the carrier
        origin, axis = (0.0, y0, 0.0), (0.0, -1.0, 0.0)
    y1 = (y0 if condition == "pushed-back" else 0.0) + L
    if condition == "pushed-back": tail = max(0.1, tail - recess)           # the pin slid back: its tail no further back than before
    if condition in ("bent", "broken"): P.cyl(f"node:self|{mat}", (0, y1 + 2.0, 0), (0, y1, 0), r)   # in the carrier
    P.cyl(f"node:self|{mat}", (0, y1 + 2.6, 0), (0, y1 + 2.0, 0), r + 0.25)    # retention collar
    P.cyl(f"node:self|{mat}", (0, y1 + 2.6 + tail, 0), (0, y1 + 2.6, 0), r + 0.15)            # solder / crimp tail
    P.pivot("self", "contact", origin, axis=axis, range=(ch, L), unit="mm", pole=str(pole), gender="pin", d=d, wipe=m12.WIPE, r=m12.R_CONTACT, condition=condition)
    P.collider("env", -r - 0.3, min(0.0, y0) - 0.1, -r - 0.3, d + 0.6, y1 + 2.6 + tail + 0.1, d + 0.6 + (L * math.sin(math.radians(BEND)) if condition == "bent" else 0))
    return P

PREVIEWS = [dict(name="pin", az=250, el=20), dict(name="bent", az=200, el=10, params=dict(condition="bent")),
            dict(name="pushed back", az=250, el=20, params=dict(condition="pushed-back"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
