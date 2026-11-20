#!/usr/bin/env python3
"""flow-meter: the contract. Regenerate with `python lib/build.py expect flow-meter` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("flow-meter"), dict(primitives=20, extents=((-0.2, -18.6, -16.0), (70.2, 18.0, 76.0)), nodes=['port-1', 'port-2', 't-1', 't-2'], holes=5))
