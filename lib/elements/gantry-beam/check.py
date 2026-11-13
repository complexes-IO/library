#!/usr/bin/env python3
"""gantry-beam: the contract. Regenerate with `python lib/build.py expect gantry-beam` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("gantry-beam"), dict(primitives=9, extents=((-1100.0, -200.0, 0.0), (1100.0, 200.0, 330.0)), nodes=['ways'], holes=0))
