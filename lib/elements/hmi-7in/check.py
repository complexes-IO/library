#!/usr/bin/env python3
"""hmi-7in: the contract. Regenerate with `python lib/build.py expect hmi-7in` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("hmi-7in"), dict(primitives=47, extents=((-100.0, -8.5, -75.0), (100.0, 66.0, 75.0)), nodes=['led-run', 'screen', 'x1.s-1', 'x1.s-2', 'x1.s-3', 'x1.t-1', 'x1.t-2', 'x1.t-3'], holes=4))
