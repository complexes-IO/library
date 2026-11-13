#!/usr/bin/env python3
"""clamp-beam: the contract. Regenerate with `python lib/build.py expect clamp-beam` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("clamp-beam"), dict(primitives=10, extents=((-600.0, -50.0, 0.0), (600.0, 400.0, 820.0)), nodes=['clamp'], holes=0))
