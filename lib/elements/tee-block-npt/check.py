#!/usr/bin/env python3
"""tee-block-npt: the contract. Regenerate with `python lib/build.py expect tee-block-npt` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("tee-block-npt"), dict(primitives=11, extents=((-23.2, -11.0, -11.0), (23.2, 11.2, 11.0)), nodes=['port-a', 'port-b', 'port-c'], holes=6))
