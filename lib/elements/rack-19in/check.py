#!/usr/bin/env python3
"""rack-19in: the contract. Regenerate with `python lib/build.py expect rack-19in` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("rack-19in"), dict(primitives=31, extents=((0.0, -47.0, 0.0), (600.0, 800.0, 2000.0)), nodes=['door-front'], holes=0))
