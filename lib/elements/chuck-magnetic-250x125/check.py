#!/usr/bin/env python3
"""chuck-magnetic-250x125: the contract. Regenerate with `python lib/build.py expect chuck-magnetic-250x125` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("chuck-magnetic-250x125"), dict(primitives=10, extents=((-125.0, -77.5, 0.0), (156.0, 80.0, 75.0)), nodes=['lever'], holes=1))
