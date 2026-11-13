#!/usr/bin/env python3
"""accumulator: the contract. Regenerate with `python lib/build.py expect accumulator` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("accumulator"), dict(primitives=8, extents=((-57.0, -57.0, 0.0), (57.0, 57.0, 251.0)), nodes=['port-oil'], holes=0))
