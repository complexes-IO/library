#!/usr/bin/env python3
"""cap-strut-41: the contract. Regenerate with `python lib/build.py expect cap-strut-41` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("cap-strut-41"), dict(primitives=4, extents=((-2.0, -20.5, 0.0), (12.0, 20.5, 41.0)), nodes=[], holes=0))
