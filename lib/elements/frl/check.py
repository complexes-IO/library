#!/usr/bin/env python3
"""frl: the contract. Regenerate with `python lib/build.py expect frl` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("frl"), dict(primitives=22, extents=((0.0, -34.0, -118.0), (118.0, 36.0, 66.0)), nodes=['handle', 'knob', 'port-1', 'port-2', 'port-3', 'port-g'], holes=6))
