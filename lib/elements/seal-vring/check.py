#!/usr/bin/env python3
"""seal-vring: the contract. Regenerate with `python lib/build.py expect seal-vring` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("seal-vring"), dict(primitives=7, extents=((-27.0, -27.0, 0.0), (27.0, 27.0, 11.0)), nodes=[], holes=3))
