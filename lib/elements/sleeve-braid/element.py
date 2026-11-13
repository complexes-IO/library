#!/usr/bin/env python3
"""sleeve-braid: a straight length of braided protective sleeve, pulled over an air tube to guard it against abrasion where it
runs over an edge or rubs in a bundle. Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0
EC011215 "Braiding for hose", the first class of the Hoses group (EG015510) that builds after the Fittings group closed
(pneu-r116); the class values it is designed to are in spec.md "## Class values". Its bore is the OD of the tube it covers, read
from the contract's tube series (toolkit/pneu.py D2, TUBES_IN: 5/32, 1/4 and 3/8 in), so tube-pneu sits in it face to face; its
wall and its length range are design choices. The braid's strands are not drawn: one solid annulus, the sleeve's envelope. It lies
along +y, as tube-pneu does. Nothing moves and nothing connects: no port, no node. No vendor file was opened (pneu-r116)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "sleeve-braid", "1.0", "connector-part"
TITLE = "generic braided protective sleeve, polyester, for 1/4 in tube, 500 long"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic braiding for hose (ETIM 10.0 EC011215), a polyester braided protective sleeve; its bore is "
            "the tube OD of toolkit/pneu.py D2 (TUBES_IN, inch 5/32, 1/4, 3/8) it is pulled over; its wall and length are design "
            "choices")
ORIGIN = "the centre of the sleeve's end face a (y = 0) on its axis; the sleeve along +y to end b at y = length, z up"
COMMAND = "SLEEVE-BRAID"
PARAMS = dict(tube="1/4", length=500.0)

WALL = 1.5                           # design choice: the braid's radial wall as drawn; >= 1.25 (2.5 x the gate's 0.5 fillet, fillet.py)
LENGTH_MIN, LENGTH_MAX = 50.0, 10000.0   # design choices: the shortest guard built, and one cut from a reel (longer runs are two)
MAT = "M-GREY-PA"                    # class value: polyester (PET) monofilament, grey; the grey plastic on file closest to its look

assert WALL >= 2.5 * 0.5             # every edge of the annulus passes the AutoCAD gate's fillet pre-flight


def bore_d(tube="1/4"):
    """the sleeve's bore: the OD of the tube it covers (pneu.TUBES_IN, D2), so the tube sits in it face to face"""
    if tube not in pneu.TUBES_IN: raise ValueError(f"tube {tube}: one of {', '.join(pneu.TUBES_IN)} (pneu.TUBES_IN, D2)")
    return pneu.TUBES_IN[tube]


def build(tube="1/4", length=500.0):
    d = bore_d(tube); length = float(length)
    if not LENGTH_MIN <= length <= LENGTH_MAX: raise ValueError(f"length {length:g}: {LENGTH_MIN:g} to {LENGTH_MAX:g} mm")
    r = d / 2.0 + WALL
    P = Prims()
    body = P.cyl(MAT, (0, 0, 0), (0, length, 0), r)                       # the braid, as one solid annulus
    P.hole(MAT, (0, -1.0, 0), (0, length + 1.0, 0), d / 2.0, body)        # its bore, the tube's OD, through
    P.collider("env", -r, 0, -r, 2 * r, length, 2 * r)
    return P


PREVIEWS = [dict(name="three-quarter", az=250, el=25), dict(name="end", az=180, el=10),
            dict(name="tube-5-32", az=250, el=25, params=dict(tube="5/32", length=200.0)),
            dict(name="tube-3-8", az=250, el=25, params=dict(tube="3/8", length=200.0))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
