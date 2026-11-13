#!/usr/bin/env python3
"""water-table: the contract. Regenerate with `python lib/build.py expect water-table` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("water-table"), dict(primitives=11, extents=((-1595.0, -845.0, 0.0), (1595.0, 845.0, 550.0)), nodes=[], holes=0))
