#!/usr/bin/env python3
"""shelving-steel: the contract. Regenerate with `python lib/build.py expect shelving-steel` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("shelving-steel"), dict(primitives=30, extents=((-500.0, 0.0, 0.0), (500.0, 500.0, 2000.0)), nodes=[], holes=4))
