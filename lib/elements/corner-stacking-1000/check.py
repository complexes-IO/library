#!/usr/bin/env python3
"""corner-stacking-1000: the contract. Regenerate with `python lib/build.py expect corner-stacking-1000` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("corner-stacking-1000"), dict(primitives=12, extents=((-8.0, -8.0, -16.0), (120.0, 120.0, 1016.0)), nodes=[], holes=0))
