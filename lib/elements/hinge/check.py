#!/usr/bin/env python3
"""hinge: the contract. Regenerate with `python lib/build.py expect hinge` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("hinge"), dict(primitives=19, extents=((-40.0, 0.0, -40.5), (40.0, 12.0, 40.5)), nodes=['leaf'], holes=7))
