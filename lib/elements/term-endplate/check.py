#!/usr/bin/env python3
"""term-endplate: the contract. Regenerate with `python lib/build.py expect term-endplate` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("term-endplate"), dict(primitives=2, extents=((0.0, -44.5, -23.5), (2.0, 0.0, 23.5)), nodes=[], holes=0))
