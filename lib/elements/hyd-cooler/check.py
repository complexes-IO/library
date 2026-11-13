#!/usr/bin/env python3
"""hyd-cooler: the contract. Regenerate with `python lib/build.py expect hyd-cooler` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("hyd-cooler"), dict(primitives=14, extents=((-256.0, -60.0, 0.0), (240.0, 60.0, 153.0)), nodes=['port-oil-in', 'port-oil-out', 'port-water-in', 'port-water-out'], holes=2))
