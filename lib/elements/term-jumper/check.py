#!/usr/bin/env python3
"""term-jumper: the contract. Regenerate with `python lib/build.py expect term-jumper` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("term-jumper"), dict(primitives=12, extents=((-2.75, -8.0, -4.0), (20.75, 11.5, 4.0)), nodes=['p-1', 'p-2', 'p-3', 'p-4'], holes=0))
