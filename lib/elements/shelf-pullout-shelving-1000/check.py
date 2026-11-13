#!/usr/bin/env python3
"""shelf-pullout-shelving-1000: the contract. Regenerate with `python lib/build.py expect shelf-pullout-shelving-1000` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("shelf-pullout-shelving-1000"), dict(primitives=14, extents=((-449.0, 20.0, 0.0), (449.0, 480.0, 65.0)), nodes=['tray'], holes=0))
