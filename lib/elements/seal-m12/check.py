#!/usr/bin/env python3
"""seal-m12: the contract. Regenerate with `python lib/build.py expect seal-m12` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("seal-m12"), dict(primitives=3, extents=((-5.46, 0.0, -5.46), (5.46, 0.3, 5.46)), nodes=['self'], holes=1))
