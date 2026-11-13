#!/usr/bin/env python3
"""valve-needle-3way: the contract. Regenerate with `python lib/build.py expect valve-needle-3way` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("valve-needle-3way"), dict(primitives=15, extents=((-0.2, -12.2, -12.0), (64.2, 12.2, 46.0)), nodes=['knob', 'port-1', 'port-2', 'port-g'], holes=6))
