#!/usr/bin/env python3
"""valve-sol-52-sr: the contract. Regenerate with `python lib/build.py expect valve-sol-52-sr` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("valve-sol-52-sr"), dict(primitives=25, extents=((-48.0, -30.5, -22.0), (80.0, 0.0, 22.2)), nodes=['coil-14', 'led-14', 'ovr-14', 'port-1', 'port-2', 'port-3', 'port-4', 'port-5'], holes=12))
