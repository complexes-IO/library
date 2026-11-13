#!/usr/bin/env python3
"""door-shelving-1000: the contract. Regenerate with `python lib/build.py expect door-shelving-1000` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("door-shelving-1000"), dict(primitives=14, extents=((-500.0, -42.0, 0.0), (500.0, 0.0, 2000.0)), nodes=['door-l', 'door-r'], holes=0))
