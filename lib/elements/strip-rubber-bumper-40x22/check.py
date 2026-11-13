#!/usr/bin/env python3
"""strip-rubber-bumper-40x22: the contract. Regenerate with `python lib/build.py expect strip-rubber-bumper-40x22` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("strip-rubber-bumper-40x22"), dict(primitives=4, extents=((0.0, -20.0, 0.0), (1000.0, 20.0, 22.0)), nodes=[], holes=0))
