#!/usr/bin/env python3
"""pressure-washer-skid: the contract. Regenerate with `python lib/build.py expect pressure-washer-skid` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("pressure-washer-skid"), dict(primitives=21, extents=((-280.0, -150.0, 0.0), (280.0, 150.0, 268.0)), nodes=['port-in', 'port-out'], holes=4))
