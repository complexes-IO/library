#!/usr/bin/env python3
"""arm-radial: the contract. Regenerate with `python lib/build.py expect arm-radial` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("arm-radial"), dict(primitives=7, extents=((-200.0, -1500.0, 0.0), (200.0, 200.0, 550.0)), nodes=['arm'], holes=0))
