#!/usr/bin/env python3
"""cable-pwr-480: the contract. Regenerate with `python lib/build.py expect cable-pwr-480` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("cable-pwr-480"), dict(primitives=29, extents=((-24.0, -4063.0, -161.96), (24.0, 0.0, 24.0)), nodes=['core-l1.end-a', 'core-l1.end-b', 'core-l2.end-a', 'core-l2.end-b', 'core-l3.end-a', 'core-l3.end-b', 'core-pe.end-a', 'core-pe.end-b', 'port-a', 'port-b'], holes=0))
