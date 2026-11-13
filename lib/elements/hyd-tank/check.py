#!/usr/bin/env python3
"""hyd-tank: the contract. Regenerate with `python lib/build.py expect hyd-tank` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("hyd-tank"), dict(primitives=15, extents=((-266.0, -185.0, 0.0), (260.0, 185.0, 448.0)), nodes=['port-drain', 'port-return', 'port-suction'], holes=1))
