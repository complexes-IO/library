#!/usr/bin/env python3
"""hx-shell-tube: the contract. Regenerate with `python lib/build.py expect hx` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("hx-shell-tube"), dict(primitives=14, extents=((-256.0, -60.0, 0.0), (240.0, 60.0, 160.0)), nodes=['port-shell-in', 'port-shell-out', 'port-tube-in', 'port-tube-out'], holes=4))
