#!/usr/bin/env python3
"""valve-ball-32: the contract. Regenerate with `python lib/build.py expect valve-ball-32` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("valve-ball-32"), dict(primitives=16, extents=((-25.2, -60.0, -15.0), (25.2, 25.2, 30.0)), nodes=['lever', 'port-1', 'port-2', 'port-3'], holes=6))
