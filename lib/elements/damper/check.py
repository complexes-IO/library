#!/usr/bin/env python3
"""damper: the contract. Regenerate with `python lib/build.py expect damper` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("damper"), dict(primitives=26, extents=((-130.0, -145.0, 0.0), (130.0, 145.0, 150.0)), nodes=['blade-1', 'blade-2', 'blade-3'], holes=11))
