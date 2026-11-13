#!/usr/bin/env python3
"""damping-rod: the contract. Regenerate with `python lib/build.py expect damping-rod` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("damping-rod"), dict(primitives=11, extents=((-55.0, -100.0, 0.0), (55.0, 100.0, 55.0)), nodes=[], holes=6))
