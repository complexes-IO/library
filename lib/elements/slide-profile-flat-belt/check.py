#!/usr/bin/env python3
"""slide-profile-flat-belt: the contract. Regenerate with `python lib/build.py expect slide-profile-flat-belt` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("slide-profile-flat-belt"), dict(primitives=10, extents=((0.0, -50.0, 0.0), (1000.0, 50.0, 15.0)), nodes=[], holes=6))
