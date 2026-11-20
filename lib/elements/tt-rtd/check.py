#!/usr/bin/env python3
"""tt-rtd: the contract. Regenerate with `python lib/build.py expect tt-rtd` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("tt-rtd"), dict(primitives=21, extents=((-20.0, -18.6, -100.0), (20.0, 18.0, 76.0)), nodes=['port-1', 't-1', 't-2'], holes=1))
