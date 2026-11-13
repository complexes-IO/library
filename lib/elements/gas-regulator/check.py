#!/usr/bin/env python3
"""gas-regulator: the contract. Regenerate with `python lib/build.py expect gas-regulator` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("gas-regulator"), dict(primitives=13, extents=((-39.0, 0.0, -25.0), (28.0, 74.0, 156.0)), nodes=['knob', 'port-1', 'port-2', 'port-g'], holes=3))
