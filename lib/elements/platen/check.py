#!/usr/bin/env python3
"""platen: the contract. Regenerate with `python lib/build.py expect platen` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("platen"), dict(primitives=7, extents=((-65.0, -50.0, -125.0), (65.0, 0.0, 125.0)), nodes=[], holes=2))
