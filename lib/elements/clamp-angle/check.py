#!/usr/bin/env python3
"""clamp-angle: the contract. Regenerate with `python lib/build.py expect clamp-angle` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("clamp-angle"), dict(primitives=18, extents=((-20.0, -20.0, 0.0), (100.0, 100.0, 50.0)), nodes=['pad-a', 'pad-b'], holes=2))
