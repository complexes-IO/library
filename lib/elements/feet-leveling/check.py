#!/usr/bin/env python3
"""feet-leveling: the contract. Regenerate with `python lib/build.py expect feet-leveling` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("feet-leveling"), dict(primitives=6, extents=((-40.0, -40.0, 0.0), (40.0, 40.0, 110.0)), nodes=['stud'], holes=0))
