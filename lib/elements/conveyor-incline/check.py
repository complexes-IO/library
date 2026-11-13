#!/usr/bin/env python3
"""conveyor-incline: the contract. Regenerate with `python lib/build.py expect conveyor-incline` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("conveyor-incline"), dict(primitives=62, extents=((-375.0, -750.0, 0.0), (375.0, 750.0, 1558.3)), nodes=['pulley-head', 'pulley-tail'], holes=4))
