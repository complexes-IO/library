#!/usr/bin/env python3
"""contact-m12-socket: one female contact of an M12 insert, as its own element (a spread spring or corrosion is a property of this
part, not of the cable). Built in the M12 mating frame (toolkit/m12.py): the mouth at the origin, the bore running toward +y.
Brief: references/measure.md."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, m12
from toolkit.prims import Prims

ID, VERSION, CLASS = "contact-m12-socket", "1.3", "contact"
TITLE = "M12 female contact (socket), gold-plated, for a Ø1.0 (A / D) or Ø1.5 (L) pin, with condition"
TOOLKIT = "1.3"
BASELINE = "own design to the M12 interface (toolkit/m12.py 1.2): mouth 1.0 below the face, cavity Ø1.65 / Ø2.1 (the I/O block's read-back); bore to 7.0 below the face (A cordset drawing: holes 7 deep) or 8.0 (L FE bore); springs an Assumption"
ORIGIN = "the socket mouth on its axis; the bore runs toward +y"
COMMAND = "M12SOCK"
PARAMS = dict(d=1.0, pole="1", condition="ok", tail=1.0, outer=1.65, bottom=6.0, face=1.0)

def build(d=1.0, pole="1", condition="ok", tail=1.0, outer=1.65, bottom=6.0, face=1.0):
    """outer: the cavity it sits in (toolkit/m12.py CAVITY: A / D 1.65, L 2.1; the L FE socket 1.85); bottom: the bore's depth from the
    mouth (SOCKET: A / D 6.0, L 7.0; L FE 8.0); face: how far the insert face stands in front of the mouth (1.0; 0 for the L FE socket,
    whose mouth is the key block's face)"""
    P = Prims(); r = d / 2; s = m12.SOCKET; bottom = float(bottom); ro = outer / 2
    mat = "M-CU-CORRODED" if condition == "corroded" else "M-GOLD"
    rb = r + (0.12 if condition == "spread" else 0.05)                          # a spread spring no longer grips: the bore opens up
    body = P.cyl(f"node:self|{mat}", (0, 0, 0), (0, bottom + 1.0 + tail, 0), ro)
    P.hole("M-GASKET", (0, -1.0, 0), (0, bottom, 0), rb, body)                   # the bore, blind: the pin bottoms at `bottom`
    P.pivot("self", "contact", (0, 0, 0), axis=(0, 1, 0), range=(s["spring"], bottom), unit="mm", pole=str(pole), gender="socket", d=d, wipe=m12.WIPE, r=m12.R_CONTACT, condition=condition,
            face=float(face))                                                  # the insert face, the mouth this far below it
    P.collider("env", -ro, 0, -ro, 2 * ro, bottom + 1.0 + tail, 2 * ro)
    return P

PREVIEWS = [dict(name="socket", az=250, el=30), dict(name="spread", az=250, el=30, params=dict(condition="spread"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
