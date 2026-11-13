#!/usr/bin/env python3
"""compensator-ring-qt-6: the contract. Regenerate with `python lib/build.py expect compensator-ring-qt-6` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("compensator-ring-qt-6"), dict(primitives=5, extents=((-20.0, -20.0, -1.0), (20.0, 20.0, 0.0)), nodes=[], holes=3))
