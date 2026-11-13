#!/usr/bin/env python3
"""desk-pc: the contract. Regenerate with `python lib/build.py expect desk-pc` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("desk-pc"), dict(primitives=37, extents=((0.0, -47.0, 0.0), (1400.0, 700.0, 740.0)), nodes=['drawer'], holes=0))
