#!/usr/bin/env python3
"""slide-profile-round-belt: the contract. Regenerate with `python lib/build.py expect slide-profile-round-belt` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("slide-profile-round-belt"), dict(primitives=10, extents=((0.0, -31.0, 0.0), (1000.0, 31.0, 18.0)), nodes=[], holes=6))
