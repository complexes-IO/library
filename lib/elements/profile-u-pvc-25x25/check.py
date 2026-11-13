#!/usr/bin/env python3
"""profile-u-pvc-25x25: the contract. Regenerate with `python lib/build.py expect profile-u-pvc-25x25` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("profile-u-pvc-25x25"), dict(primitives=5, extents=((0.0, -12.5, 0.0), (1000.0, 12.5, 25.0)), nodes=[], holes=0))
