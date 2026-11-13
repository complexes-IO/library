#!/usr/bin/env python3
"""bearing-pillow: the contract. Regenerate with `python lib/build.py expect bearing-pillow` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("bearing-pillow"), dict(primitives=6, extents=((-70.0, -20.0, 0.0), (70.0, 20.0, 90.0)), nodes=[], holes=3))
