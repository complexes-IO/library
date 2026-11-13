#!/usr/bin/env python3
"""control-valve: the contract. Regenerate with `python lib/build.py expect control-valve` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("control-valve"), dict(primitives=12, extents=((0.0, -40.0, -22.0), (88.0, 40.0, 115.5)), nodes=['port-12', 'port-in', 'port-out', 'stem'], holes=3))
