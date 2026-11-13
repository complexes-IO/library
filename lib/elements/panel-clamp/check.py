#!/usr/bin/env python3
"""panel-clamp: the contract. Regenerate with `python lib/build.py expect panel-clamp` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("panel-clamp"), dict(primitives=4, extents=((-2.5, -6.0, 0.0), (8.0, 6.0, 22.0)), nodes=[], holes=1))
