#!/usr/bin/env python3
"""drag-chain: the contract. Regenerate with `python lib/build.py expect drag-chain` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("drag-chain"), dict(primitives=62, extents=((-667.5, -45.0, 0.0), (40.0, 45.0, 235.0)), nodes=['moving-end'], holes=4))
