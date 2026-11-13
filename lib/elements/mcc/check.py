#!/usr/bin/env python3
"""mcc: the contract. Regenerate with `python lib/build.py expect mcc` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("mcc"), dict(primitives=74, extents=((0.0, -18.0, 0.0), (600.0, 500.0, 2300.0)), nodes=['bus-l1', 'bus-l2', 'bus-l3', 'door-1', 'door-2', 'door-3', 'door-4', 'door-ww', 'pe-bus'], holes=0))
