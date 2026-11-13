#!/usr/bin/env python3
"""hyd-cylinder-da-40: the contract. Regenerate with `python lib/build.py expect hyd-cylinder-da-40` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("hyd-cylinder-da-40"), dict(primitives=16, extents=((0.0, -30.0, -30.0), (340.0, 30.0, 31.0)), nodes=['port-cap', 'port-rod', 'rod'], holes=3))
