#!/usr/bin/env python3
"""foam-tool-tray: the contract. Regenerate with `python lib/build.py expect foam-tool-tray` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("foam-tool-tray"), dict(primitives=4, extents=((0.0, 0.0, 0.0), (865.0, 555.0, 50.0)), nodes=[], holes=0))
