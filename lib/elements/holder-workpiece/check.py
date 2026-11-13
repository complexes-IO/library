#!/usr/bin/env python3
"""holder-workpiece: the contract. Regenerate with `python lib/build.py expect holder-workpiece` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("holder-workpiece"), dict(primitives=14, extents=((-75.0, -100.0, 0.0), (80.0, 100.0, 190.0)), nodes=['arm-left', 'arm-right'], holes=3))
