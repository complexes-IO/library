#!/usr/bin/env python3
"""silencer: the contract. Regenerate with `python lib/build.py expect silencer` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("silencer"), dict(primitives=11, extents=((-9.52, -9.52, -10.21), (9.52, 9.52, 31.0)), nodes=['port-1'], holes=0))
