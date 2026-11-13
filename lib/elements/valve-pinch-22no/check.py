#!/usr/bin/env python3
"""valve-pinch-22no: the contract. Regenerate with `python lib/build.py expect valve-pinch-22no` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("valve-pinch-22no"), dict(primitives=9, extents=((0.0, -28.2, -28.0), (112.0, 28.0, 38.0)), nodes=['port-10', 'port-in', 'port-out'], holes=3))
