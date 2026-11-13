#!/usr/bin/env python3
"""chuck-zero-point-120: the contract. Regenerate with `python lib/build.py expect chuck-zero-point-120` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("chuck-zero-point-120"), dict(primitives=9, extents=((-60.0, -60.0, 0.0), (60.0, 60.0, 40.0)), nodes=[], holes=5))
