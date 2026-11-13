#!/usr/bin/env python3
"""column: the contract. Regenerate with `python lib/build.py expect column` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("column"), dict(primitives=15, extents=((-300.0, -300.0, 0.0), (300.0, 300.0, 1600.0)), nodes=['ways'], holes=8))
