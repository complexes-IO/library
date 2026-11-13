#!/usr/bin/env python3
"""receiver-air: the contract. Regenerate with `python lib/build.py expect receiver-air` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("receiver-air"), dict(primitives=18, extents=((-188.0, -188.0, 0.0), (188.0, 188.0, 1014.0)), nodes=['port-1', 'port-2', 'port-drain', 'port-g', 'port-relief'], holes=5))
