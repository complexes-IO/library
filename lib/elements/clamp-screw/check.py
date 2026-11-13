#!/usr/bin/env python3
"""clamp-screw: the contract. Regenerate with `python lib/build.py expect clamp-screw` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("clamp-screw"), dict(primitives=6, extents=((-2.55, 0.0, -9.4), (2.55, 7.5, 4.0)), nodes=['screw', 'self'], holes=1))
