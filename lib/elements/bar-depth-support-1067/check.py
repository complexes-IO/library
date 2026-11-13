#!/usr/bin/env python3
"""bar-depth-support-1067: the contract. Regenerate with `python lib/build.py expect bar-depth-support-1067` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("bar-depth-support-1067"), dict(primitives=7, extents=((-20.0, -10.0, -60.0), (20.0, 1077.0, 30.0)), nodes=[], holes=0))
