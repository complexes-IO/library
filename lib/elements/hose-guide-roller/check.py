#!/usr/bin/env python3
"""hose-guide-roller: the contract. Regenerate with `python lib/build.py expect hose-guide-roller` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("hose-guide-roller"), dict(primitives=13, extents=((-45.0, -25.0, 0.0), (45.0, 25.0, 60.0)), nodes=['roller'], holes=4))
