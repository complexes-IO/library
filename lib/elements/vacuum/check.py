#!/usr/bin/env python3
"""vacuum: the contract. Regenerate with `python lib/build.py expect vacuum` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("vacuum"), dict(primitives=14, extents=((-0.2, -16.0, -29.0), (64.2, 16.0, 14.2)), nodes=['port-1', 'port-3', 'port-blow'], holes=6))
