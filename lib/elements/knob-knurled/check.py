#!/usr/bin/env python3
"""knob-knurled: the contract. Regenerate with `python lib/build.py expect knob-knurled` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("knob-knurled"), dict(primitives=35, extents=((-16.0, -15.98, -20.0), (16.0, 15.98, 22.0)), nodes=['stud'], holes=0))
