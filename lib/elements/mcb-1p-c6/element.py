#!/usr/bin/env python3
"""mcb-1p-c6: miniature circuit breaker, 1-pole C6: the family's pole body once. Brief: references/measure.md (derived from the 3-pole drawing).
Maker and part number only in references/source.txt (OPERATING.md 6, DOC-006).
1.4 (elec-r30): follows mcb-3p-c10 1.4: the terminal screws are port nodes t-1-line / t-1-load (the core's pin-nodes note of
2026-11-11); nodes added, none moved: a minor.
1.5 (elec-r37; review mcb-1p-c6-1.4 findings 1, 2, 3, 5): the family body is pinned (mcb-3p-c10 1.5, whose 1.5 is text only, so the
geometry is 1.4's); spec.md lists the inherited open figures with their classes and says which width governs."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims
from toolkit.library import load

ID, VERSION, CLASS = "mcb-1p-c6", "1.5", "device"
FAMILY = "1.5"                                                       # mcb-3p-c10's version this element builds (pinned: review mcb-1p-c6-1.4 finding 2)
TITLE = "miniature circuit breaker, 1-pole 6 A C-curve, 35 mm rail"
TOOLKIT = "1.3"
BASELINE = "maker's datasheet (references/measure.md, references/source.txt): figures derived from the 3-pole family drawing on file under mcb-3p-c10 (17.7 pitch, 105 x 73) per the 2026-11-03 ruling"
ORIGIN = "rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward -y"
COMMAND = "MCB1"
PARAMS = {}

def build():
    return load("mcb-3p-c10", FAMILY).build(poles=1, rating="C6")          # same family body, one module: the one allowed cross-import (a family, not a carried part)

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="rear rail clip", az=60, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
