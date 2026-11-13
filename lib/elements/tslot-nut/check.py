#!/usr/bin/env python3
"""tslot-nut: the contract. Regenerate with `python lib/build.py expect tslot-nut` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("tslot-nut"), dict(primitives=5, extents=((-10.0, -7.0, -3.0), (10.0, 7.0, 3.0)), nodes=[], holes=2))
