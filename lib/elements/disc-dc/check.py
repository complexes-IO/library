#!/usr/bin/env python3
"""disc-dc: the contract. Regenerate with `python lib/build.py expect disc-dc` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("disc-dc"), dict(primitives=22, extents=((0.0, -75.2, -45.0), (36.0, 7.5, 45.0)), nodes=['handle', 't-1', 't-2', 't-3', 't-4'], holes=0))
