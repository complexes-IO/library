#!/usr/bin/env python3
"""enc-wm: the contract. Regenerate with `python lib/build.py expect enc-wm` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("enc-wm"), dict(primitives=31, extents=((0.0, -2.0, 0.0), (600.0, 250.0, 800.0)), nodes=['back-panel', 'door', 'pe-body', 'pe-door', 'pe-plate'], holes=10))
