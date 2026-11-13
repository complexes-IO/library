#!/usr/bin/env python3
"""hyd-filter-return: the contract. Regenerate with `python lib/build.py expect hyd-filter-return` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("hyd-filter-return"), dict(primitives=9, extents=((0.0, -40.0, -158.0), (102.0, 40.0, 34.0)), nodes=['indicator', 'port-in', 'port-out'], holes=0))
