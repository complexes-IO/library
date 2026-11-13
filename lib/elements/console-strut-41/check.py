#!/usr/bin/env python3
"""console-strut-41: the contract. Regenerate with `python lib/build.py expect console-strut-41` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("console-strut-41"), dict(primitives=8, extents=((0.0, -40.0, -120.0), (308.0, 40.0, 40.0)), nodes=[], holes=2))
