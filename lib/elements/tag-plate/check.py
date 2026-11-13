#!/usr/bin/env python3
"""tag-plate: the contract. Regenerate with `python lib/build.py expect tag-plate` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("tag-plate"), dict(primitives=11, extents=((0.0, -2.3, 0.0), (120.0, 0.0, 60.0)), nodes=[], holes=4))
