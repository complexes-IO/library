#!/usr/bin/env python3
"""motor-iec71-370w: the contract. Regenerate with `python lib/build.py expect motor-iec71-370w` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("motor-iec71-370w"), dict(primitives=38, extents=((-13.0, -110.0, 0.0), (125.0, 140.5, 175.5)), nodes=['fan', 'pwr', 'shaft'], holes=13))
