#!/usr/bin/env python3
"""table-brush: the contract. Regenerate with `python lib/build.py expect table-brush` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("table-brush"), dict(primitives=52, extents=((-1000.0, -625.0, 0.0), (1000.0, 625.0, 920.0)), nodes=[], holes=0))
