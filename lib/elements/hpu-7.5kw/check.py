#!/usr/bin/env python3
"""hpu-7.5kw: the contract. Regenerate with `python lib/build.py expect hpu-7.5kw` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("hpu-7.5kw"), dict(primitives=21, extents=((-360.0, -235.0, 0.0), (360.0, 235.0, 1067.5)), nodes=['port-g', 'port-p', 'port-t', 'pwr'], holes=0))
