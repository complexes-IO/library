#!/usr/bin/env python3
"""bracket-monitor: the contract. Regenerate with `python lib/build.py expect bracket-monitor` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("bracket-monitor"), dict(primitives=18, extents=((-75.0, -224.0, -75.0), (75.0, 0.0, 75.0)), nodes=['tilt'], holes=8))
