#!/usr/bin/env python3
"""relay-aux-2no2nc: the contract. Regenerate with `python lib/build.py expect relay-aux-2no2nc` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("relay-aux-2no2nc"), dict(primitives=40, extents=((0.0, -68.3, -41.0), (45.0, 7.5, 41.0)), nodes=['carrier', 'led-coil', 't-13', 't-14', 't-21', 't-22', 't-31', 't-32', 't-43', 't-44', 't-A1', 't-A2'], holes=0))
