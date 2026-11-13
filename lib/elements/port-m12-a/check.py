#!/usr/bin/env python3
"""port-m12-a: the contract. Regenerate with `python lib/build.py expect port-m12-a` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("port-m12-a"), dict(primitives=51, extents=((-9.0, -15.6, -31.68), (9.0, 144.28, 9.81)), nodes=['insert.c1', 'insert.c2', 'insert.c3', 'insert.c4', 'insert.c5', 'seal', 'self'], holes=29))
