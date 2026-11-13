#!/usr/bin/env python3
"""girder-bridge: the contract. Regenerate with `python lib/build.py expect girder-bridge` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("girder-bridge"), dict(primitives=12, extents=((-4000.0, -350.0, 0.0), (4000.0, 350.0, 880.0)), nodes=['rail'], holes=0))
