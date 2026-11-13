#!/usr/bin/env python3
"""conveyor-ball-transfer: the contract. Regenerate with `python lib/build.py expect conveyor-ball-transfer` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("conveyor-ball-transfer"), dict(primitives=131, extents=((-375.0, -500.0, 0.0), (375.0, 500.0, 750.0)), nodes=['ball-1-1', 'ball-1-2', 'ball-1-3', 'ball-1-4', 'ball-2-1', 'ball-2-2', 'ball-2-3', 'ball-2-4', 'ball-3-1', 'ball-3-2', 'ball-3-3', 'ball-3-4', 'ball-4-1', 'ball-4-2', 'ball-4-3', 'ball-4-4', 'ball-5-1', 'ball-5-2', 'ball-5-3', 'ball-5-4', 'ball-6-1', 'ball-6-2', 'ball-6-3', 'ball-6-4', 'ball-7-1', 'ball-7-2', 'ball-7-3', 'ball-7-4', 'ball-8-1', 'ball-8-2', 'ball-8-3', 'ball-8-4'], holes=36))
