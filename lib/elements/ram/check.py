#!/usr/bin/env python3
"""ram: the contract. Regenerate with `python lib/build.py expect ram` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("ram"), dict(primitives=8, extents=((-1300.0, -60.0, 0.0), (1300.0, 60.0, 450.0)), nodes=['tool-seat'], holes=0))
