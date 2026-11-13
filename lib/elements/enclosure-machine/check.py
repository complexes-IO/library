#!/usr/bin/env python3
"""enclosure-machine: the contract. Regenerate with `python lib/build.py expect enclosure-machine` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("enclosure-machine"), dict(primitives=42, extents=((-1200.0, -67.0, 0.0), (1200.0, 2000.0, 2200.0)), nodes=['door-l', 'door-r'], holes=4))
