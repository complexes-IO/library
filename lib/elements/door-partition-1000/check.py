#!/usr/bin/env python3
"""door-partition-1000: the contract. Regenerate with `python lib/build.py expect door-partition-1000` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("door-partition-1000"), dict(primitives=60, extents=((-465.0, -10.0, 100.0), (465.0, 10.0, 1950.0)), nodes=['door'], holes=6))
