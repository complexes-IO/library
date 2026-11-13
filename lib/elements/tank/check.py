#!/usr/bin/env python3
"""tank: the contract. Regenerate with `python lib/build.py expect tank` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("tank"), dict(primitives=15, extents=((-210.0, -135.0, 0.0), (210.0, 135.0, 278.0)), nodes=['port-drain', 'port-out', 'port-return'], holes=6))
