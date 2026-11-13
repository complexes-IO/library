#!/usr/bin/env python3
"""handle: the contract. Regenerate with `python lib/build.py expect handle` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("handle"), dict(primitives=6, extents=((-68.0, 0.0, -6.0), (68.0, 42.0, 6.0)), nodes=[], holes=2))
