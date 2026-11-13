#!/usr/bin/env python3
"""profile-z-alu-30x40x3: the contract. Regenerate with `python lib/build.py expect profile-z-alu-30x40x3` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("profile-z-alu-30x40x3"), dict(primitives=6, extents=((0.0, -28.5, 0.0), (1000.0, 28.5, 40.0)), nodes=[], holes=0))
