#!/usr/bin/env python3
"""tensioner-belt: the contract. Regenerate with `python lib/build.py expect tensioner-belt` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("tensioner-belt"), dict(primitives=17, extents=((-45.0, -25.0, 0.0), (78.0, 25.0, 76.0)), nodes=['arm', 'roll'], holes=4))
