#!/usr/bin/env python3
"""insert-m12: the contract. Regenerate with `python lib/build.py expect insert-m12` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("insert-m12"), dict(primitives=39, extents=((-5.46, 0.0, -5.46), (5.46, 10.0, 5.46)), nodes=['c1', 'c2', 'c3', 'c4', 'c5'], holes=26))
