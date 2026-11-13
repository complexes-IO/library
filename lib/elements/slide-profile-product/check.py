#!/usr/bin/env python3
"""slide-profile-product: the contract. Regenerate with `python lib/build.py expect slide-profile-product` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("slide-profile-product"), dict(primitives=8, extents=((0.0, -12.0, 0.0), (1000.0, 50.0, 60.0)), nodes=[], holes=3))
