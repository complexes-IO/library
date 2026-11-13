#!/usr/bin/env python3
"""rack-bar: the contract. Regenerate with `python lib/build.py expect rack-bar` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("rack-bar"), dict(primitives=37, extents=((-600.0, -300.0, 0.0), (600.0, 300.0, 1270.0)), nodes=[], holes=0))
