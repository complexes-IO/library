#!/usr/bin/env python3
"""hyd-pump: the contract. Regenerate with `python lib/build.py expect hyd-pump` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("hyd-pump"), dict(primitives=10, extents=((-36.0, -58.0, -50.0), (86.0, 58.0, 30.0)), nodes=['port-p', 'port-s', 'shaft'], holes=2))
