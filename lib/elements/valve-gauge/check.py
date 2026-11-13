#!/usr/bin/env python3
"""valve-gauge: the contract. Regenerate with `python lib/build.py expect valve-gauge` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("valve-gauge"), dict(primitives=10, extents=((-12.0, -35.0, -10.21), (12.0, 11.0, 40.2)), nodes=['knob', 'port-1', 'port-2'], holes=2))
