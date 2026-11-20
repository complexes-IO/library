#!/usr/bin/env python3
"""ramp-loading-150: the contract. Regenerate with `python lib/build.py expect ramp-loading-150` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("ramp-loading-150"), dict(primitives=14, extents=((0.0, 0.0, 0.0), (1500.0, 1000.0, 150.0)), nodes=[], holes=0))
