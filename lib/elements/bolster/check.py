#!/usr/bin/env python3
"""bolster: the contract. Regenerate with `python lib/build.py expect bolster` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("bolster"), dict(primitives=9, extents=((-500.0, -350.0, 0.0), (500.0, 350.0, 80.0)), nodes=[], holes=7))
