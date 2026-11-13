#!/usr/bin/env python3
"""jack-screw: the contract. Regenerate with `python lib/build.py expect jack-screw` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("jack-screw"), dict(primitives=8, extents=((-25.0, -25.0, 0.0), (25.0, 25.0, 92.0)), nodes=['screw'], holes=1))
