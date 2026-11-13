#!/usr/bin/env python3
"""spring-plate-qt-6: the contract. Regenerate with `python lib/build.py expect spring-plate-qt-6` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("spring-plate-qt-6"), dict(primitives=10, extents=((-26.0, -7.0, -10.2), (26.0, 7.0, 0.0)), nodes=[], holes=3))
