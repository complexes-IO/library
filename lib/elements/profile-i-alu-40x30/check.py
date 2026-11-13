#!/usr/bin/env python3
"""profile-i-alu-40x30: the contract. Regenerate with `python lib/build.py expect profile-i-alu-40x30` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("profile-i-alu-40x30"), dict(primitives=6, extents=((0.0, -15.0, 0.0), (1000.0, 15.0, 40.0)), nodes=[], holes=0))
