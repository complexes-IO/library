#!/usr/bin/env python3
"""strut: the contract. Regenerate with `python lib/build.py expect strut` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("strut"), dict(primitives=28, extents=((0.0, -20.5, 0.0), (1000.0, 20.5, 41.0)), nodes=[], holes=0))
