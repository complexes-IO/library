#!/usr/bin/env python3
"""wall-side-shelving-500: the contract. Regenerate with `python lib/build.py expect wall-side-shelving-500` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("wall-side-shelving-500"), dict(primitives=3, extents=((-498.0, 52.0, 22.0), (-478.0, 448.0, 1998.0)), nodes=[], holes=0))
