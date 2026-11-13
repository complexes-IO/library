#!/usr/bin/env python3
"""nut-m12: the contract. Regenerate with `python lib/build.py expect nut-m12` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("nut-m12"), dict(primitives=15, extents=((-7.5, -8.9, -7.5), (7.5, 6.4, 7.5)), nodes=['self'], holes=4))
