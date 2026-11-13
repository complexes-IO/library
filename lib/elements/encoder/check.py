#!/usr/bin/env python3
"""encoder: the contract. Regenerate with `python lib/build.py expect encoder` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("encoder"), dict(primitives=10, extents=((-29.0, -20.0, -29.0), (29.0, 52.0, 29.0)), nodes=['port-x1', 'shaft'], holes=3))
