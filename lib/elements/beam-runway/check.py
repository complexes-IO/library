#!/usr/bin/env python3
"""beam-runway: the contract. Regenerate with `python lib/build.py expect beam-runway` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("beam-runway"), dict(primitives=16, extents=((-3000.0, -150.0, 0.0), (3000.0, 150.0, 420.0)), nodes=['track'], holes=0))
