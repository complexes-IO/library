#!/usr/bin/env python3
"""op-pilot-22: the contract. Regenerate with `python lib/build.py expect op-pilot-22` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("op-pilot-22"), dict(primitives=11, extents=((-15.0, -10.0, -32.5), (15.0, 42.5, 17.5)), nodes=['self'], holes=2))
