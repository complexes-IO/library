#!/usr/bin/env python3
"""receptacle-clip-qt-6: the contract. Regenerate with `python lib/build.py expect receptacle-clip-qt-6` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("receptacle-clip-qt-6"), dict(primitives=11, extents=((-20.0, -7.0, -10.2), (20.0, 7.0, 0.0)), nodes=[], holes=4))
