#!/usr/bin/env python3
"""receptacle-m12: the contract. Regenerate with `python lib/build.py expect receptacle-m12` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("receptacle-m12"), dict(primitives=46, extents=((-6.75, 0.0, -6.75), (6.75, 13.0, 6.75)), nodes=['insert.c1', 'insert.c2', 'insert.c3', 'insert.c4', 'insert.c5', 'seal', 'self'], holes=29))
