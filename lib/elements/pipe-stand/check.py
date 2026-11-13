#!/usr/bin/env python3
"""pipe-stand: the contract. Regenerate with `python lib/build.py expect pipe-stand` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("pipe-stand"), dict(primitives=14, extents=((-300.0, -200.0, 0.0), (300.0, 200.0, 820.0)), nodes=['roller-1', 'roller-2'], holes=0))
