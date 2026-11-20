#!/usr/bin/env python3
"""diode-rail-3a: the contract. Regenerate with `python lib/build.py expect diode-rail-3a` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("diode-rail-3a"), dict(primitives=22, extents=((0.0, -76.0, -40.0), (18.0, 7.5, 40.0)), nodes=['x1.s-1', 'x1.s-2', 'x1.t-1', 'x1.t-2'], holes=0))
