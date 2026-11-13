#!/usr/bin/env python3
"""strip-rubber-rect-30x10: the contract. Regenerate with `python lib/build.py expect strip-rubber-rect-30x10` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("strip-rubber-rect-30x10"), dict(primitives=2, extents=((0.0, -15.0, 0.0), (1000.0, 15.0, 10.0)), nodes=[], holes=0))
