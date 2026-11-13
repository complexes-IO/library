#!/usr/bin/env python3
"""tensioner-chain: the contract. Regenerate with `python lib/build.py expect tensioner-chain` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("tensioner-chain"), dict(primitives=10, extents=((-38.0, -16.0, 0.0), (38.0, 16.0, 94.0)), nodes=['head'], holes=3))
