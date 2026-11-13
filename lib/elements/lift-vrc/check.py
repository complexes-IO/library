#!/usr/bin/env python3
"""lift-vrc: the contract. Regenerate with `python lib/build.py expect lift-vrc` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("lift-vrc"), dict(primitives=22, extents=((-635.0, -800.0, 0.0), (635.0, 800.0, 4600.0)), nodes=['carriage'], holes=8))
