#!/usr/bin/env python3
"""coolant-pump: the contract. Regenerate with `python lib/build.py expect coolant-pump` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("coolant-pump"), dict(primitives=12, extents=((-75.0, -75.0, -250.0), (75.0, 117.0, 250.0)), nodes=['port-out', 'pwr'], holes=1))
