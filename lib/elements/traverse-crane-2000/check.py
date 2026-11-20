#!/usr/bin/env python3
"""traverse-crane-2000: the contract. Regenerate with `python lib/build.py expect traverse-crane-2000` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("traverse-crane-2000"), dict(primitives=20, extents=((-1000.0, -50.0, -120.0), (1000.0, 50.0, 320.0)), nodes=[], holes=3))
