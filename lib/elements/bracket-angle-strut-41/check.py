#!/usr/bin/env python3
"""bracket-angle-strut-41: the contract. Regenerate with `python lib/build.py expect bracket-angle-strut-41` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("bracket-angle-strut-41"), dict(primitives=6, extents=((0.0, -20.5, 0.0), (90.0, 20.5, 90.0)), nodes=[], holes=2))
