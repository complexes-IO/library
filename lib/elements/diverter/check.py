#!/usr/bin/env python3
"""diverter: the contract. Regenerate with `python lib/build.py expect diverter` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("diverter"), dict(primitives=11, extents=((-420.0, -730.0, 0.0), (-260.0, 150.0, 860.0)), nodes=['arm'], holes=4))
