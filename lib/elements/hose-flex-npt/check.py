#!/usr/bin/env python3
"""hose-flex-npt: the contract. Regenerate with `python lib/build.py expect hose-flex-npt` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("hose-flex-npt"), dict(primitives=20, extents=((-9.01, -10.21, -9.01), (9.01, 310.21, 9.01)), nodes=['port-a', 'port-b'], holes=0))
