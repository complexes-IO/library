#!/usr/bin/env python3
"""actuator-valve: the contract. Regenerate with `python lib/build.py expect actuator-valve` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("actuator-valve"), dict(primitives=11, extents=((-85.5, -49.0, 0.0), (85.5, 37.0, 99.5)), nodes=['port-2', 'port-4', 'shaft'], holes=2))
