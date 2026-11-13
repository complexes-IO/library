#!/usr/bin/env python3
"""conveyor-slat: the contract. Regenerate with `python lib/build.py expect conveyor-slat` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("conveyor-slat"), dict(primitives=62, extents=((-375.0, -750.0, 0.0), (375.0, 750.0, 750.0)), nodes=['shaft-head', 'shaft-tail'], holes=4))
