#!/usr/bin/env python3
"""clamp-spring-25: the contract. Regenerate with `python lib/build.py expect clamp-spring-25` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("clamp-spring-25"), dict(primitives=15, extents=((-110.0, -12.0, -34.0), (70.0, 12.0, 34.0)), nodes=['jaw'], holes=3))
