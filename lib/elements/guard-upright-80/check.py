#!/usr/bin/env python3
"""guard-upright-80: the contract. Regenerate with `python lib/build.py expect guard-upright-80` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("guard-upright-80"), dict(primitives=10, extents=((-98.0, -158.0, 0.0), (98.0, 40.0, 400.0)), nodes=[], holes=2))
