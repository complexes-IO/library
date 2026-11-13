#!/usr/bin/env python3
"""booth-paint: the contract. Regenerate with `python lib/build.py expect booth-paint` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("booth-paint"), dict(primitives=39, extents=((-1500.0, 0.0, 0.0), (1500.0, 3000.0, 2650.0)), nodes=[], holes=2))
