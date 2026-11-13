#!/usr/bin/env python3
"""wire: the contract. Regenerate with `python lib/build.py expect wire` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("wire"), dict(primitives=8, extents=((-1.49, -150.02, -5.32), (1.49, 0.0, 1.42)), nodes=['end-a', 'end-b'], holes=0))
