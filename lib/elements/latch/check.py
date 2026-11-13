#!/usr/bin/env python3
"""latch: the contract. Regenerate with `python lib/build.py expect latch` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("latch"), dict(primitives=45, extents=((-20.0, -9.99, -20.0), (20.0, 9.99, 9.0)), nodes=['stud'], holes=6))
