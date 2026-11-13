#!/usr/bin/env python3
"""head-plate-strut-41: the contract. Regenerate with `python lib/build.py expect head-plate-strut-41` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("head-plate-strut-41"), dict(primitives=9, extents=((-8.0, -60.0, -39.5), (75.0, 60.0, 80.5)), nodes=[], holes=4))
