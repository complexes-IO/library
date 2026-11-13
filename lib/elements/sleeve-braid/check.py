#!/usr/bin/env python3
"""sleeve-braid: the contract. Regenerate with `python lib/build.py expect sleeve-braid` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("sleeve-braid"), dict(primitives=3, extents=((-4.68, 0.0, -4.68), (4.68, 500.0, 4.68)), nodes=[], holes=1))
