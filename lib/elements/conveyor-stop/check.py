#!/usr/bin/env python3
"""conveyor-stop: the contract. Regenerate with `python lib/build.py expect conveyor-stop` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("conveyor-stop"), dict(primitives=12, extents=((-35.0, -45.0, -100.0), (35.0, 45.0, 60.0)), nodes=['port-rod', 'rod'], holes=5))
