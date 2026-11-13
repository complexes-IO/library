#!/usr/bin/env python3
"""hpu-0.37kw: the contract. Regenerate with `python lib/build.py expect hpu-0.37kw` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("hpu-0.37kw"), dict(primitives=21, extents=((-178.0, -128.0, 0.0), (178.0, 128.0, 559.5)), nodes=['port-gauge', 'port-pressure', 'port-return', 'pwr'], holes=0))
