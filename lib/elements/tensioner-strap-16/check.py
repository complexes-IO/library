#!/usr/bin/env python3
"""tensioner-strap-16: the contract. Regenerate with `python lib/build.py expect tensioner-strap-16` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("tensioner-strap-16"), dict(primitives=15, extents=((-200.0, -20.0, 0.0), (50.0, 20.0, 40.0)), nodes=['lever'], holes=4))
