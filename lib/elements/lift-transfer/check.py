#!/usr/bin/env python3
"""lift-transfer: the contract. Regenerate with `python lib/build.py expect lift-transfer` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("lift-transfer"), dict(primitives=15, extents=((-240.0, -120.0, 0.0), (240.0, 120.0, 745.0)), nodes=['lift'], holes=4))
