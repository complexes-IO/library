#!/usr/bin/env python3
"""plinth-shelving-1000: the contract. Regenerate with `python lib/build.py expect plinth-shelving-1000` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("plinth-shelving-1000"), dict(primitives=3, extents=((-448.0, 2.0, 0.0), (448.0, 42.0, 108.0)), nodes=[], holes=0))
