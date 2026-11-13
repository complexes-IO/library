#!/usr/bin/env python3
"""table-slotted: the contract. Regenerate with `python lib/build.py expect table-slotted` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("table-slotted"), dict(primitives=11, extents=((-250.0, -600.0, 0.0), (250.0, 600.0, 100.0)), nodes=[], holes=0))
