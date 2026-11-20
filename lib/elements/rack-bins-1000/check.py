#!/usr/bin/env python3
"""rack-bins-1000: the contract. Regenerate with `python lib/build.py expect rack-bins-1000` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("rack-bins-1000"), dict(primitives=54, extents=((-500.0, -400.0, 0.0), (500.0, 250.0, 1800.0)), nodes=[], holes=0))
