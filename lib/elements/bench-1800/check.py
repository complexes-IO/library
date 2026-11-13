#!/usr/bin/env python3
"""bench-1800: the contract. Regenerate with `python lib/build.py expect bench-1800` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("bench-1800"), dict(primitives=24, extents=((0.0, -49.2, 0.0), (1872.4, 712.8, 1250.9)), nodes=['backboard', 'pe'], holes=4))
