#!/usr/bin/env python3
"""hanger-vibration: the contract. Regenerate with `python lib/build.py expect hanger-vibration` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("hanger-vibration"), dict(primitives=11, extents=((-30.0, -20.0, -90.0), (30.0, 20.0, 0.0)), nodes=[], holes=4))
