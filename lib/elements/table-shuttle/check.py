#!/usr/bin/env python3
"""table-shuttle: the contract. Regenerate with `python lib/build.py expect table-shuttle` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("table-shuttle"), dict(primitives=29, extents=((-1600.0, -850.0, 0.0), (4900.0, 850.0, 700.0)), nodes=['pallet'], holes=0))
