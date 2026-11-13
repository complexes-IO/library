#!/usr/bin/env python3
"""drain-auto: the contract. Regenerate with `python lib/build.py expect drain-auto` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("drain-auto"), dict(primitives=6, extents=((-25.0, -25.0, -130.0), (25.0, 25.0, 0.0)), nodes=['port-1', 'port-drain'], holes=2))
