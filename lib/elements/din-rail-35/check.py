#!/usr/bin/env python3
"""din-rail-35: the contract. Regenerate with `python lib/build.py expect din-rail-35` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("din-rail-35"), dict(primitives=57, extents=((-12.5, -14.0, -17.5), (987.5, 0.0, 20.0)), nodes=[], holes=0))
