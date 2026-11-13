#!/usr/bin/env python3
"""pt: the contract. Regenerate with `python lib/build.py expect pt` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("pt"), dict(primitives=20, extents=((-20.0, -18.6, 0.0), (20.0, 18.0, 96.0)), nodes=['port-p', 't-1', 't-2'], holes=1))
