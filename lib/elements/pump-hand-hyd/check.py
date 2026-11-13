#!/usr/bin/env python3
"""pump-hand-hyd: the contract. Regenerate with `python lib/build.py expect pump-hand-hyd` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("pump-hand-hyd"), dict(primitives=18, extents=((-14.0, -70.0, 0.0), (560.0, 70.0, 175.0)), nodes=['knob', 'lever', 'port-p'], holes=4))
