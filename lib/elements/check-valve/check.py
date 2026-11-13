#!/usr/bin/env python3
"""check-valve: the contract. Regenerate with `python lib/build.py expect check-valve` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("check-valve"), dict(primitives=18, extents=((-14.0, -26.0, -14.0), (14.0, 26.0, 14.0)), nodes=['port-1', 'port-2'], holes=2))
