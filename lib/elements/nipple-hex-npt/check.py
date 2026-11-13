#!/usr/bin/env python3
"""nipple-hex-npt: the contract. Regenerate with `python lib/build.py expect nipple-hex-npt` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("nipple-hex-npt"), dict(primitives=10, extents=((-9.52, -10.21, -9.52), (9.52, 18.21, 9.52)), nodes=['port-a', 'port-b'], holes=0))
