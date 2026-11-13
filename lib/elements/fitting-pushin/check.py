#!/usr/bin/env python3
"""fitting-pushin: the contract. Regenerate with `python lib/build.py expect fitting-pushin` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("fitting-pushin"), dict(primitives=11, extents=((-7.84, -6.7, -7.84), (7.84, 23.5, 7.84)), nodes=['port-thread', 'port-tube'], holes=0))
