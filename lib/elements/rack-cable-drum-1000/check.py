#!/usr/bin/env python3
"""rack-cable-drum-1000: the contract. Regenerate with `python lib/build.py expect rack-cable-drum-1000` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("rack-cable-drum-1000"), dict(primitives=26, extents=((-590.0, -350.0, 0.0), (590.0, 350.0, 1650.0)), nodes=[], holes=4))
