#!/usr/bin/env python3
"""tube-pneu: the contract. Regenerate with `python lib/build.py expect tube-pneu` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("tube-pneu"), dict(primitives=4, extents=((-3.18, 0.0, -3.18), (3.18, 500.0, 3.18)), nodes=['port-a', 'port-b'], holes=0))
