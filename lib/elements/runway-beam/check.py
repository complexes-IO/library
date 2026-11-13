#!/usr/bin/env python3
"""runway-beam: the contract. Regenerate with `python lib/build.py expect runway-beam` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("runway-beam"), dict(primitives=14, extents=((-6000.0, -250.0, 0.0), (6000.0, 250.0, 880.0)), nodes=['rail'], holes=0))
