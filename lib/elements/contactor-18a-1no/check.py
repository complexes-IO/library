#!/usr/bin/env python3
"""contactor-18a-1no: the contract. Regenerate with `python lib/build.py expect contactor-18a-1no` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("contactor-18a-1no"), dict(primitives=29, extents=((0.0, -84.1, -42.5), (45.0, 7.5, 42.5)), nodes=['carrier', 't-1', 't-13', 't-14', 't-2', 't-3', 't-4', 't-5', 't-6', 't-A1', 't-A2'], holes=0))
