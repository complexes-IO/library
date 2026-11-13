#!/usr/bin/env python3
"""palletizer-frame: the contract. Regenerate with `python lib/build.py expect palletizer-frame` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("palletizer-frame"), dict(primitives=46, extents=((-1650.0, -1350.0, 0.0), (1650.0, 1350.0, 2500.0)), nodes=[], holes=16))
