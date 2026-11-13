#!/usr/bin/env python3
"""gas-spring: the contract. Regenerate with `python lib/build.py expect gas-spring` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("gas-spring"), dict(primitives=7, extents=((-12.0, -9.0, -9.0), (268.0, 9.0, 9.0)), nodes=['end-cyl', 'rod'], holes=1))
