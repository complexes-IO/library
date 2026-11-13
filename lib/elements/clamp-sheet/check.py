#!/usr/bin/env python3
"""clamp-sheet: the contract. Regenerate with `python lib/build.py expect clamp-sheet` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("clamp-sheet"), dict(primitives=9, extents=((-70.0, -25.0, -30.0), (0.0, 25.0, 72.0)), nodes=['jaw', 'port-cap'], holes=2))
