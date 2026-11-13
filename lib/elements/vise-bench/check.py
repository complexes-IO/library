#!/usr/bin/env python3
"""vise-bench: the contract. Regenerate with `python lib/build.py expect vise-bench` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("vise-bench"), dict(primitives=16, extents=((-130.0, -90.0, 0.0), (100.0, 90.0, 150.0)), nodes=['jaw'], holes=4))
