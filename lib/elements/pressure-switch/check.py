#!/usr/bin/env python3
"""pressure-switch: the contract. Regenerate with `python lib/build.py expect pressure-switch` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("pressure-switch"), dict(primitives=22, extents=((-22.0, -20.6, 0.0), (22.0, 20.0, 86.0)), nodes=['port-p', 't-11', 't-12', 't-14'], holes=1))
