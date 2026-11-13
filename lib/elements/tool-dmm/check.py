#!/usr/bin/env python3
"""tool-dmm: the contract. Regenerate with `python lib/build.py expect tool-dmm` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("tool-dmm"), dict(primitives=23, extents=((-57.0, -50.6, -90.0), (57.0, 0.0, 90.0)), nodes=['dial', 'display', 'probe-black', 'probe-red'], holes=4))
