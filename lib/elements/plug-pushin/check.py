#!/usr/bin/env python3
"""plug-pushin: the contract. Regenerate with `python lib/build.py expect plug-pushin` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("plug-pushin"), dict(primitives=3, extents=((-5.5, -16.0, -5.5), (5.5, 8.0, 5.5)), nodes=['port-a'], holes=0))
