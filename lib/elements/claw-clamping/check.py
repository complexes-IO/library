#!/usr/bin/env python3
"""claw-clamping: the contract. Regenerate with `python lib/build.py expect claw-clamping` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("claw-clamping"), dict(primitives=8, extents=((-70.0, -16.0, 0.0), (40.0, 16.0, 38.0)), nodes=[], holes=1))
