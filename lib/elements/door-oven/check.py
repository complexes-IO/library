#!/usr/bin/env python3
"""door-oven: the contract. Regenerate with `python lib/build.py expect door-oven` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("door-oven"), dict(primitives=16, extents=((-1000.0, -210.0, 0.0), (1000.0, 0.0, 2200.0)), nodes=['door-l', 'door-r'], holes=0))
