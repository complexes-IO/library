#!/usr/bin/env python3
"""term-4mm: the contract. Regenerate with `python lib/build.py expect term-4mm` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("term-4mm"), dict(primitives=22, extents=((0.0, -44.9, -23.5), (6.0, 0.0, 23.5)), nodes=['clamp-1', 'clamp-1.screw', 'clamp-2', 'clamp-2.screw'], holes=4))
