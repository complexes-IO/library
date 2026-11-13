#!/usr/bin/env python3
"""conveyor-guard: the contract. Regenerate with `python lib/build.py expect conveyor-guard` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("conveyor-guard"), dict(primitives=16, extents=((-500.0, -322.0, 0.0), (500.0, 322.0, 400.0)), nodes=[], holes=6))
