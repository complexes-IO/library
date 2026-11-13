#!/usr/bin/env python3
"""cap-hex-npt: the contract. Regenerate with `python lib/build.py expect cap-hex-npt` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("cap-hex-npt"), dict(primitives=11, extents=((-11.13, 0.0, -11.13), (11.13, 16.41, 11.13)), nodes=['port-a'], holes=2))
