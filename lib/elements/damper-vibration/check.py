#!/usr/bin/env python3
"""damper-vibration: the contract. Regenerate with `python lib/build.py expect damper-vibration` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("damper-vibration"), dict(primitives=9, extents=((-25.0, -25.0, -25.0), (25.0, 25.0, 65.0)), nodes=['rubber', 'stud', 'top'], holes=0))
