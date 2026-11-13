#!/usr/bin/env python3
"""nipple-bulkhead-npt: the contract. Regenerate with `python lib/build.py expect nipple-bulkhead-npt` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("nipple-bulkhead-npt"), dict(primitives=19, extents=((-11.55, -18.21, -11.55), (11.55, 29.21, 11.55)), nodes=['port-a', 'port-b'], holes=0))
