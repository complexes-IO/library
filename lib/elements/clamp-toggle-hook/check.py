#!/usr/bin/env python3
"""clamp-toggle-hook: the contract. Regenerate with `python lib/build.py expect clamp-toggle-hook` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("clamp-toggle-hook"), dict(primitives=25, extents=((-30.0, -25.0, 0.0), (110.0, 25.0, 30.0)), nodes=['lever'], holes=12))
