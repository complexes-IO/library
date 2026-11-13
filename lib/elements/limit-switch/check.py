#!/usr/bin/env python3
"""limit-switch: the contract. Regenerate with `python lib/build.py expect limit-switch` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("limit-switch"), dict(primitives=19, extents=((-15.0, -48.0, 0.0), (15.0, 0.0, 111.0)), nodes=['lever', 't-11', 't-12', 't-23', 't-24'], holes=3))
