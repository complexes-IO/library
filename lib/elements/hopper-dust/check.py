#!/usr/bin/env python3
"""hopper-dust: the contract. Regenerate with `python lib/build.py expect hopper-dust` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("hopper-dust"), dict(primitives=26, extents=((-500.0, -400.0, -856.0), (500.0, 400.0, 0.0)), nodes=[], holes=3))
