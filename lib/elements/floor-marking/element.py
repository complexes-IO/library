#!/usr/bin/env python3
"""floor-marking: floor marking tape, one straight strip, our own vendor-neutral design of the ETIM 10.0 class EC001496 (Warning
tape), built unattended (OPERATING.md 12, generic elements; lib/inventory.csv row "floor-marking", own_design yes, etim EC001496,
systems safety-equipment, storage-steel). A 50 wide, 1 thick, 1000 long self-adhesive PVC strip laid on the floor to mark an aisle,
a storage bay or a keep-clear zone; strips chain end to end from the origin at one end. Plain, one colour, no print: the class value
Colour is "not stated" (which colour a marking carries is the placing system's choice under its colour code; OSHA 1910.144 is in
lib/standards/sources.csv as free to read, its figures to be recorded attended), and the layer M-YELLOW is the model's appearance
only. Corner and T pieces are later versions. One fixed body, no moving node, no terminal. The class values (spec.md, "Class
values") are design inputs; every size is a design choice. No safety claim; no vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "floor-marking", "1.0", "plate"
TITLE = "floor marking tape, generic, one straight strip 50 wide x 1 thick x 1000 long, self-adhesive PVC, one colour, no print"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic warning tape (ETIM 10.0 EC001496), one straight floor marking strip 50 x 1 x 1000, self-adhesive "
            "PVC, plain; class values are design inputs (spec.md); every size a design choice; no colour code, symbol or safety "
            "message claimed; no vendor file opened")
ORIGIN = ("the floor plane (z = 0) at the strip's start end, on its centre line: the strip runs along +x (x 0 to 1000), y +-25, "
          "z 0 to 1 (+z up, off the floor); the next strip is placed at x 1000")
COMMAND = "FLOORTAPE"
PARAMS = dict()
WIDTH, THICK, LENGTH = 50.0, 1.0, 1000.0       # class values Width 50 mm and Length 1 m; 1.0 thick with its adhesive (design choices)

def build():
    P = Prims(); Y = "M-YELLOW"
    P.box(Y, 0, -WIDTH / 2, 0, LENGTH, WIDTH, THICK)                                                  # the strip, x 0..1000, y +-25, z 0..1
    P.collider("strip", 0, -WIDTH / 2, 0, LENGTH, WIDTH, THICK)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="end", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
