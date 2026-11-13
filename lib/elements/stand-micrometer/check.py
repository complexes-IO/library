#!/usr/bin/env python3
"""stand-micrometer: the contract. Regenerate with `python lib/build.py expect stand-micrometer` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("stand-micrometer"), dict(primitives=11, extents=((-60.0, -45.0, 0.0), (60.0, 45.0, 228.0)), nodes=['head'], holes=0))
