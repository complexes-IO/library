#!/usr/bin/env python3
"""sign-iso7010: the contract. Regenerate with `python lib/build.py expect sign-iso7010` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("sign-iso7010"), dict(primitives=8, extents=((-100.0, -2.1, -150.0), (100.0, 0.0, 150.0)), nodes=[], holes=4))
