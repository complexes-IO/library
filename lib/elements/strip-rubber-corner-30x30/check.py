#!/usr/bin/env python3
"""strip-rubber-corner-30x30: the contract. Regenerate with `python lib/build.py expect strip-rubber-corner-30x30` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("strip-rubber-corner-30x30"), dict(primitives=6, extents=((0.0, -30.0, -30.0), (1000.0, 14.0, 14.0)), nodes=[], holes=0))
