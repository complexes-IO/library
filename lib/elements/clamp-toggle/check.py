#!/usr/bin/env python3
"""clamp-toggle: the contract. Regenerate with `python lib/build.py expect clamp-toggle` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("clamp-toggle"), dict(primitives=20, extents=((-32.0, -22.0, 0.0), (62.0, 22.0, 102.0)), nodes=['arm'], holes=6))
