#!/usr/bin/env python3
"""cross-side-block-npt: the contract. Regenerate with `python lib/build.py expect cross-side-block-npt` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("cross-side-block-npt"), dict(primitives=17, extents=((-23.2, -14.2, -14.0), (23.2, 14.2, 23.2)), nodes=['port-a', 'port-b', 'port-c', 'port-d', 'port-e'], holes=10))
