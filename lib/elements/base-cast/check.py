#!/usr/bin/env python3
"""base-cast: the contract. Regenerate with `python lib/build.py expect base-cast` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("base-cast"), dict(primitives=24, extents=((-450.0, -1100.0, 0.0), (450.0, 400.0, 270.0)), nodes=['column-seat', 'work-face'], holes=16))
