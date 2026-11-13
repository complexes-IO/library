#!/usr/bin/env python3
"""panel-operator: the contract. Regenerate with `python lib/build.py expect panel-operator` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("panel-operator"), dict(primitives=20, extents=((0.0, -0.89, 0.0), (300.0, 200.0, 161.79)), nodes=['door'], holes=10))
