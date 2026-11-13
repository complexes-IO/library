#!/usr/bin/env python3
"""separator-oil-water: the contract. Regenerate with `python lib/build.py expect separator-oil-water` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("separator-oil-water"), dict(primitives=15, extents=((-260.0, -230.0, 0.0), (260.0, 160.0, 716.0)), nodes=['port-in-1', 'port-in-2', 'port-out'], holes=4))
