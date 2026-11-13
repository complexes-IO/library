#!/usr/bin/env python3
"""panel-light: the contract. Regenerate with `python lib/build.py expect panel-light` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("panel-light"), dict(primitives=18, extents=((-15.0, -25.0, -28.0), (285.0, 32.0, 12.0)), nodes=['door-switch', 'lamp'], holes=12))
