#!/usr/bin/env python3
"""switch-cam-22: the contract. Regenerate with `python lib/build.py expect switch-cam-22` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("switch-cam-22"), dict(primitives=33, extents=((-24.0, -19.2, -24.0), (24.0, 41.0, 24.0)), nodes=['self', 't-1', 't-2', 't-3', 't-4', 't-5', 't-6', 't-7', 't-8'], holes=0))
