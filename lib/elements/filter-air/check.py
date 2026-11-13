#!/usr/bin/env python3
"""filter-air: the contract. Regenerate with `python lib/build.py expect filter-air` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("filter-air"), dict(primitives=14, extents=((-0.2, -20.2, -84.0), (40.2, 20.0, 16.2)), nodes=['drain', 'port-1', 'port-2'], holes=5))
