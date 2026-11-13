#!/usr/bin/env python3
"""oven-cure: the contract. Regenerate with `python lib/build.py expect oven-cure` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("oven-cure"), dict(primitives=25, extents=((-1200.0, 0.0, 0.0), (1200.0, 3200.0, 3000.0)), nodes=[], holes=2))
