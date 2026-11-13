#!/usr/bin/env python3
"""valve-counterbalance: the contract. Regenerate with `python lib/build.py expect valve-counterbalance` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("valve-counterbalance"), dict(primitives=9, extents=((0.0, -20.0, -21.0), (82.0, 20.0, 60.0)), nodes=['port-1', 'port-12', 'port-2', 'screw'], holes=0))
