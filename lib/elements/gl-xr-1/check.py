#!/usr/bin/env python3
"""gl-xr-1: the contract. Regenerate with `python lib/build.py expect gl-xr-1` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("gl-xr-1"), dict(primitives=25, extents=((-74.0, -2.25, -24.13), (74.0, 153.68, 28.0)), nodes=['dial-l', 'dial-r', 'frame', 'lens-l', 'lens-r', 'temple-l', 'temple-r'], holes=0))
