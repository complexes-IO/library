#!/usr/bin/env python3
"""regulator: the contract. Regenerate with `python lib/build.py expect regulator` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("regulator"), dict(primitives=10, extents=((0.0, -34.0, -20.0), (68.0, 20.0, 66.0)), nodes=['knob', 'port-1', 'port-2', 'port-g'], holes=3))
