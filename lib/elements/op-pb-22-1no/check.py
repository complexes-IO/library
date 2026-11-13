#!/usr/bin/env python3
"""op-pb-22-1no: the contract. Regenerate with `python lib/build.py expect op-pb-22-1no` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("op-pb-22-1no"), dict(primitives=12, extents=((-15.0, -4.6, -32.5), (15.0, 42.5, 17.5)), nodes=['self'], holes=3))
