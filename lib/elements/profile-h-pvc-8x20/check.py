#!/usr/bin/env python3
"""profile-h-pvc-8x20: the contract. Regenerate with `python lib/build.py expect profile-h-pvc-8x20` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("profile-h-pvc-8x20"), dict(primitives=6, extents=((0.0, -4.0, 0.0), (1000.0, 4.0, 20.0)), nodes=[], holes=0))
