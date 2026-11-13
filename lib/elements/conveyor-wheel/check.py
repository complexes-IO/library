#!/usr/bin/env python3
"""conveyor-wheel: the contract. Regenerate with `python lib/build.py expect conveyor-wheel` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("conveyor-wheel"), dict(primitives=71, extents=((-375.0, -750.0, 0.0), (375.0, 750.0, 750.0)), nodes=['wheel-1-1', 'wheel-1-2', 'wheel-1-3', 'wheel-10-1', 'wheel-10-2', 'wheel-11-1', 'wheel-11-2', 'wheel-11-3', 'wheel-12-1', 'wheel-12-2', 'wheel-13-1', 'wheel-13-2', 'wheel-13-3', 'wheel-14-1', 'wheel-14-2', 'wheel-15-1', 'wheel-15-2', 'wheel-15-3', 'wheel-2-1', 'wheel-2-2', 'wheel-3-1', 'wheel-3-2', 'wheel-3-3', 'wheel-4-1', 'wheel-4-2', 'wheel-5-1', 'wheel-5-2', 'wheel-5-3', 'wheel-6-1', 'wheel-6-2', 'wheel-7-1', 'wheel-7-2', 'wheel-7-3', 'wheel-8-1', 'wheel-8-2', 'wheel-9-1', 'wheel-9-2', 'wheel-9-3'], holes=4))
