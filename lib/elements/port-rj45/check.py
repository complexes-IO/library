#!/usr/bin/env python3
"""port-rj45: the contract. Regenerate with `python lib/build.py expect port-rj45` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("port-rj45"), dict(primitives=12, extents=((-8.0, 0.0, -7.0), (8.0, 21.0, 7.0)), nodes=['c-1', 'c-2', 'c-3', 'c-4', 'c-5', 'c-6', 'c-7', 'c-8'], holes=0))
