#!/usr/bin/env python3
"""plunger-spring: the contract. Regenerate with `python lib/build.py expect plunger-spring` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("plunger-spring"), dict(primitives=6, extents=((-4.0, -4.0, -16.0), (4.0, 4.0, 2.0)), nodes=['pin', 'self'], holes=1))
