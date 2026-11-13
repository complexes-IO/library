#!/usr/bin/env python3
"""cap-nut-af13: the contract. Regenerate with `python lib/build.py expect cap-nut-af13` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("cap-nut-af13"), dict(primitives=3, extents=((-10.0, -10.0, 0.0), (10.0, 10.0, 16.0)), nodes=[], holes=1))
