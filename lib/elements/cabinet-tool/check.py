#!/usr/bin/env python3
"""cabinet-tool: the contract. Regenerate with `python lib/build.py expect cabinet-tool` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("cabinet-tool"), dict(primitives=52, extents=((0.0, -47.0, 0.0), (900.0, 600.0, 1000.0)), nodes=['drawer-1', 'drawer-2', 'drawer-3', 'drawer-4', 'drawer-5'], holes=0))
