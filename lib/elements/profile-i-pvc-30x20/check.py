#!/usr/bin/env python3
"""profile-i-pvc-30x20: the contract. Regenerate with `python lib/build.py expect profile-i-pvc-30x20` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("profile-i-pvc-30x20"), dict(primitives=6, extents=((0.0, -10.0, 0.0), (1000.0, 10.0, 30.0)), nodes=[], holes=0))
