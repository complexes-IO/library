#!/usr/bin/env python3
"""gripper: the contract. Regenerate with `python lib/build.py expect gripper` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("gripper"), dict(primitives=21, extents=((-32.0, -30.0, 0.0), (32.0, 20.0, 106.0)), nodes=['jaw-l', 'jaw-r', 'port-close', 'port-open'], holes=10))
