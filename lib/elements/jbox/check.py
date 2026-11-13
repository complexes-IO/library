#!/usr/bin/env python3
"""jbox: the contract. Regenerate with `python lib/build.py expect jbox` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("jbox"), dict(primitives=14, extents=((0.0, -2.0, 0.0), (240.0, 120.0, 240.0)), nodes=['lid'], holes=6))
