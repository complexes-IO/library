#!/usr/bin/env python3
"""fan-exhaust: the contract. Regenerate with `python lib/build.py expect fan-exhaust` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("fan-exhaust"), dict(primitives=46, extents=((-350.0, -360.0, 0.0), (350.0, 540.0, 875.0)), nodes=['impeller'], holes=17))
