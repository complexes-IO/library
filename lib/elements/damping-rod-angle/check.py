#!/usr/bin/env python3
"""damping-rod-angle: the contract. Regenerate with `python lib/build.py expect damping-rod-angle` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("damping-rod-angle"), dict(primitives=16, extents=((-70.0, -80.0, 0.0), (70.0, 80.0, 80.0)), nodes=[], holes=6))
