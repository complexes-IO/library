#!/usr/bin/env python3
"""lubrication-central-air-6: the contract. Regenerate with `python lib/build.py expect lubrication-central-air-6` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("lubrication-central-air-6"), dict(primitives=30, extents=((-100.0, -95.0, 0.0), (100.0, 65.0, 278.7)), nodes=['indicator', 'port-air', 'port-out-1', 'port-out-2', 'port-out-3', 'port-out-4', 'port-out-5', 'port-out-6'], holes=14))
