#!/usr/bin/env python3
"""plug-m12: the contract. Regenerate with `python lib/build.py expect plug-m12` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("plug-m12"), dict(primitives=65, extents=((-7.5, -8.9, -7.5), (7.5, 31.8, 7.5)), nodes=['insert.c1', 'insert.c2', 'insert.c3', 'insert.c4', 'insert.c5', 'nut', 'self'], holes=19))
