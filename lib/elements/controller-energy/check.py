#!/usr/bin/env python3
"""controller-energy: the contract. Regenerate with `python lib/build.py expect controller-energy` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("controller-energy"), dict(primitives=64, extents=((0.0, -86.0, -50.0), (45.0, 7.5, 50.0)), nodes=['led-err', 'led-run', 'x1.s-1', 'x1.s-2', 'x1.s-3', 'x1.t-1', 'x1.t-2', 'x1.t-3', 'x2.s-1', 'x2.s-2', 'x2.s-3', 'x2.t-1', 'x2.t-2', 'x2.t-3', 'x3.c-1', 'x3.c-2', 'x3.c-3', 'x3.c-4', 'x3.c-5', 'x3.c-6', 'x3.c-7', 'x3.c-8'], holes=0))
