#!/usr/bin/env python3
"""receptacle-m23: the contract. Regenerate with `python lib/build.py expect receptacle-m23` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("receptacle-m23"), dict(primitives=14, extents=((-15.0, -15.0, -15.0), (15.0, 18.0, 15.0)), nodes=['c-1', 'c-2', 'c-3', 'c-pe'], holes=5))
