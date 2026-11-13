#!/usr/bin/env python3
"""vise-machine: the contract. Regenerate with `python lib/build.py expect vise-machine` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("vise-machine"), dict(primitives=19, extents=((-90.0, -90.0, 0.0), (298.0, 90.0, 110.0)), nodes=['jaw'], holes=4))
