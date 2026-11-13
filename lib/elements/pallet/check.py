#!/usr/bin/env python3
"""pallet: the contract. Regenerate with `python lib/build.py expect pallet` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("pallet"), dict(primitives=38, extents=((0.0, 0.0, 0.0), (1219.0, 1016.0, 144.0)), nodes=[], holes=0))
