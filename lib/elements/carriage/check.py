#!/usr/bin/env python3
"""carriage: the contract. Regenerate with `python lib/build.py expect carriage` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("carriage"), dict(primitives=7, extents=((-200.0, -320.0, -220.0), (200.0, 280.0, 160.0)), nodes=['cross-slide'], holes=0))
