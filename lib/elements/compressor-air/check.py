#!/usr/bin/env python3
"""compressor-air: the contract. Regenerate with `python lib/build.py expect compressor-air` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("compressor-air"), dict(primitives=41, extents=((0.0, -0.2, 0.0), (518.0, 260.0, 540.0)), nodes=['drain', 'lever', 'motor', 'port-2', 'switch'], holes=2))
