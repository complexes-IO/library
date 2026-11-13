#!/usr/bin/env python3
"""cable-tray: the contract. Regenerate with `python lib/build.py expect cable-tray` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("cable-tray"), dict(primitives=104, extents=((0.0, -150.0, 0.0), (3000.0, 150.0, 100.0)), nodes=[], holes=8))
