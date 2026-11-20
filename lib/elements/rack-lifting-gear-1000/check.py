#!/usr/bin/env python3
"""rack-lifting-gear-1000: the contract. Regenerate with `python lib/build.py expect rack-lifting-gear-1000` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("rack-lifting-gear-1000"), dict(primitives=36, extents=((-550.0, -400.0, 0.0), (550.0, 400.0, 1650.0)), nodes=[], holes=0))
