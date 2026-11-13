#!/usr/bin/env python3
"""hose-coolant-seg-npt: the contract. Regenerate with `python lib/build.py expect hose-coolant-seg-npt` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("hose-coolant-seg-npt"), dict(primitives=44, extents=((-9.01, -10.21, -9.01), (9.01, 288.0, 9.01)), nodes=['port-a'], holes=0))
