#!/usr/bin/env python3
"""disc-3p-30a: the contract. Regenerate with `python lib/build.py expect disc-3p-30a` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("disc-3p-30a"), dict(primitives=26, extents=((-34.55, -22.0, -35.55), (34.55, 64.3, 48.0)), nodes=['door-unit', 'handle', 't-1-line', 't-1-load', 't-2-line', 't-2-load', 't-3-line', 't-3-load'], holes=0))
