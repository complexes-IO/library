#!/usr/bin/env python3
"""teach-pendant: the contract. Regenerate with `python lib/build.py expect teach-pendant` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("teach-pendant"), dict(primitives=43, extents=((-122.0, -85.0, -150.0), (120.0, 0.0, 150.0)), nodes=['enable', 'estop', 'key-1', 'key-10', 'key-11', 'key-12', 'key-13', 'key-14', 'key-15', 'key-16', 'key-2', 'key-3', 'key-4', 'key-5', 'key-6', 'key-7', 'key-8', 'key-9', 'screen'], holes=2))
