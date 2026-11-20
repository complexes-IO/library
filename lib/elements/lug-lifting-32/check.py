#!/usr/bin/env python3
"""lug-lifting-32: the contract. Regenerate with `python lib/build.py expect lug-lifting-32` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("lug-lifting-32"), dict(primitives=5, extents=((-60.0, -10.0, 0.0), (60.0, 10.0, 120.0)), nodes=[], holes=1))
