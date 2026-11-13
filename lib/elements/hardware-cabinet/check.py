#!/usr/bin/env python3
"""hardware-cabinet: the contract. Regenerate with `python lib/build.py expect hardware-cabinet` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("hardware-cabinet"), dict(primitives=39, extents=((0.0, -47.0, 0.0), (600.0, 300.0, 700.0)), nodes=['door-l', 'door-r'], holes=4))
