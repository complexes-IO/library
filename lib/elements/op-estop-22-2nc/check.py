#!/usr/bin/env python3
"""op-estop-22-2nc: the contract. Regenerate with `python lib/build.py expect op-estop-22-2nc` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("op-estop-22-2nc"), dict(primitives=14, extents=((-30.0, -31.5, -38.5), (30.0, 42.5, 30.0)), nodes=['self'], holes=2))
