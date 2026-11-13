#!/usr/bin/env python3
"""valve-sol-32nc-sr: the contract. Regenerate with `python lib/build.py expect valve-sol-32nc-sr` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("valve-sol-32nc-sr"), dict(primitives=18, extents=((-48.0, -30.5, -22.0), (54.0, 0.0, 22.2)), nodes=['coil-12', 'led-12', 'ovr-12', 'port-1', 'port-2', 'port-3'], holes=8))
