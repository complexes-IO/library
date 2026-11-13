#!/usr/bin/env python3
"""booth-powder: the contract. Regenerate with `python lib/build.py expect booth-powder` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("booth-powder"), dict(primitives=18, extents=((-1000.0, 0.0, 0.0), (1000.0, 1600.0, 2200.0)), nodes=[], holes=2))
