#!/usr/bin/env python3
"""dryer-air: the contract. Regenerate with `python lib/build.py expect dryer-air` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("dryer-air"), dict(primitives=13, extents=((-0.2, -24.2, -126.0), (48.2, 24.0, 16.2)), nodes=['desiccant', 'port-1', 'port-2'], holes=5))
