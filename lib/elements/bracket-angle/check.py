#!/usr/bin/env python3
"""bracket-angle: the contract. Regenerate with `python lib/build.py expect bracket-angle` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("bracket-angle"), dict(primitives=5, extents=((0.0, -18.0, 0.0), (40.0, 18.0, 40.0)), nodes=[], holes=2))
