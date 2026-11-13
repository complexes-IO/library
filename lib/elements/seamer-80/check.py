#!/usr/bin/env python3
"""seamer-80: the contract. Regenerate with `python lib/build.py expect seamer-80` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("seamer-80"), dict(primitives=17, extents=((-200.0, -40.0, -26.0), (50.0, 40.0, 26.0)), nodes=['jaw'], holes=3))
