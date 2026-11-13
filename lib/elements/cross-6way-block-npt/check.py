#!/usr/bin/env python3
"""cross-6way-block-npt: the contract. Regenerate with `python lib/build.py expect cross-6way-block-npt` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("cross-6way-block-npt"), dict(primitives=20, extents=((-23.2, -14.2, -23.2), (23.2, 14.2, 23.2)), nodes=['port-a', 'port-b', 'port-c', 'port-d', 'port-e', 'port-f'], holes=12))
