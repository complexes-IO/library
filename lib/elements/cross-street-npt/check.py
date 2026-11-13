#!/usr/bin/env python3
"""cross-street-npt: the contract. Regenerate with `python lib/build.py expect cross-street-npt` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("cross-street-npt"), dict(primitives=12, extents=((-23.2, -14.2, -14.0), (24.21, 14.2, 14.0)), nodes=['port-a', 'port-b', 'port-c', 'port-d'], holes=6))
