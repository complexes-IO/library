#!/usr/bin/env python3
"""threaded-sleeve-m8: the contract. Regenerate with `python lib/build.py expect threaded-sleeve-m8` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("threaded-sleeve-m8"), dict(primitives=3, extents=((-7.0, -7.0, 0.0), (7.0, 7.0, 20.0)), nodes=[], holes=1))
