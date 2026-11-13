#!/usr/bin/env python3
"""hyd-gauge: the contract. Regenerate with `python lib/build.py expect hyd-gauge` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("hyd-gauge"), dict(primitives=16, extents=((-32.0, -14.0, 0.0), (32.0, 13.0, 79.5)), nodes=['pointer', 'port-1'], holes=1))
