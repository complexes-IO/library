#!/usr/bin/env python3
"""hyd-flow-control: the contract. Regenerate with `python lib/build.py expect hyd-flow-control` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("hyd-flow-control"), dict(primitives=8, extents=((0.0, -20.0, -20.0), (72.0, 20.0, 52.0)), nodes=['knob', 'port-1', 'port-2'], holes=0))
