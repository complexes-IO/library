#!/usr/bin/env python3
"""lift-stacker: the contract. Regenerate with `python lib/build.py expect lift-stacker` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("lift-stacker"), dict(primitives=61, extents=((-850.0, -1150.0, 0.0), (850.0, 1150.0, 2700.0)), nodes=['fork-1', 'fork-2', 'table'], holes=20))
