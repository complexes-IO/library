#!/usr/bin/env python3
"""robot-pedestal: the contract. Regenerate with `python lib/build.py expect robot-pedestal` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("robot-pedestal"), dict(primitives=13, extents=((-300.0, -300.0, 0.0), (300.0, 300.0, 700.0)), nodes=['mount'], holes=4))
