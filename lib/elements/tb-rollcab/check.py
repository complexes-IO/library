#!/usr/bin/env python3
"""tb-rollcab: the contract. Regenerate with `python lib/build.py expect tb-rollcab` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("tb-rollcab"), dict(primitives=76, extents=((0.0, -47.0, 0.0), (707.0, 460.0, 800.0)), nodes=['drawer-1', 'drawer-2', 'drawer-3', 'drawer-4', 'drawer-5'], holes=16))
