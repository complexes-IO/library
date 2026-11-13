#!/usr/bin/env python3
"""frame-welded: the contract. Regenerate with `python lib/build.py expect frame-welded` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("frame-welded"), dict(primitives=31, extents=((-650.0, -450.0, 0.0), (650.0, 450.0, 850.0)), nodes=['mount'], holes=4))
