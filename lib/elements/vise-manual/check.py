#!/usr/bin/env python3
"""vise-manual: the contract. Regenerate with `python lib/build.py expect vise-manual` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("vise-manual"), dict(primitives=19, extents=((-60.0, -70.0, 0.0), (220.0, 70.0, 65.0)), nodes=['jaw'], holes=4))
