#!/usr/bin/env python3
"""floor-marking: the contract. Regenerate with `python lib/build.py expect floor-marking` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("floor-marking"), dict(primitives=2, extents=((0.0, -25.0, 0.0), (1000.0, 25.0, 1.0)), nodes=[], holes=0))
