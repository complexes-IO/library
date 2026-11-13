#!/usr/bin/env python3
"""hold-down: the contract. Regenerate with `python lib/build.py expect hold-down` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("hold-down"), dict(primitives=12, extents=((-40.0, -40.0, -122.0), (40.0, 40.0, 16.0)), nodes=['plunger', 'port-cap'], holes=5))
