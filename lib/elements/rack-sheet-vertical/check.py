#!/usr/bin/env python3
"""rack-sheet-vertical: the contract. Regenerate with `python lib/build.py expect rack-sheet-vertical` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("rack-sheet-vertical"), dict(primitives=51, extents=((-800.0, -600.0, 0.0), (800.0, 600.0, 1500.0)), nodes=[], holes=0))
