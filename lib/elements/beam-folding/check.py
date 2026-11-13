#!/usr/bin/env python3
"""beam-folding: the contract. Regenerate with `python lib/build.py expect beam-folding` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("beam-folding"), dict(primitives=14, extents=((-620.0, -250.0, -250.0), (620.0, 450.0, 60.0)), nodes=['fold'], holes=0))
