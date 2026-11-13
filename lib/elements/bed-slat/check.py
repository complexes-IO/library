#!/usr/bin/env python3
"""bed-slat: the contract. Regenerate with `python lib/build.py expect bed-slat` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("bed-slat"), dict(primitives=41, extents=((-1550.0, -800.0, 0.0), (1550.0, 800.0, 200.0)), nodes=['slats'], holes=0))
