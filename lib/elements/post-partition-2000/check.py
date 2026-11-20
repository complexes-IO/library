#!/usr/bin/env python3
"""post-partition-2000: the contract. Regenerate with `python lib/build.py expect post-partition-2000` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("post-partition-2000"), dict(primitives=23, extents=((-75.0, -75.0, 0.0), (75.0, 75.0, 2000.0)), nodes=[], holes=10))
