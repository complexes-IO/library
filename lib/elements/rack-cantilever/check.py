#!/usr/bin/env python3
"""rack-cantilever: the contract. Regenerate with `python lib/build.py expect rack-cantilever` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("rack-cantilever"), dict(primitives=42, extents=((-890.0, -1100.0, 0.0), (890.0, 200.0, 2400.0)), nodes=[], holes=4))
