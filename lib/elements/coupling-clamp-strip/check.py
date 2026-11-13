#!/usr/bin/env python3
"""coupling-clamp-strip: the contract. Regenerate with `python lib/build.py expect coupling-clamp-strip` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("coupling-clamp-strip"), dict(primitives=11, extents=((-20.0, -13.86, -13.86), (20.0, 13.86, 23.36)), nodes=[], holes=6))
