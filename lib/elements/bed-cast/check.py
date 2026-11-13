#!/usr/bin/env python3
"""bed-cast: the contract. Regenerate with `python lib/build.py expect bed-cast` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("bed-cast"), dict(primitives=12, extents=((-1000.0, -330.0, 0.0), (1000.0, 330.0, 430.0)), nodes=['ways'], holes=6))
