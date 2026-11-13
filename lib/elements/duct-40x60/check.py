#!/usr/bin/env python3
"""duct-40x60: the contract. Regenerate with `python lib/build.py expect duct-40x60` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("duct-40x60"), dict(primitives=107, extents=((0.0, -60.1, 0.0), (1000.0, 0.0, 40.0)), nodes=['cover'], holes=0))
