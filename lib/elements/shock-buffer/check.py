#!/usr/bin/env python3
"""shock-buffer: the contract. Regenerate with `python lib/build.py expect shock-buffer` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("shock-buffer"), dict(primitives=6, extents=((-20.0, -20.0, -20.0), (20.0, 20.0, 34.0)), nodes=['pad', 'stud'], holes=0))
