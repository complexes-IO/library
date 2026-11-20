#!/usr/bin/env python3
"""gl-xr-1: the contract. Regenerate with `python lib/build.py expect gl-xr-1` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("gl-xr-1"), dict(primitives=54, extents=((-71.36, -0.0, -22.7), (71.36, 140.07, 24.26)), nodes=['dial-l', 'dial-r', 'display-l', 'display-r', 'frame', 'lens-l', 'lens-r', 'temple-l', 'temple-r'], holes=0))
