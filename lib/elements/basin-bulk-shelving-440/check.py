#!/usr/bin/env python3
"""basin-bulk-shelving-440: the contract. Regenerate with `python lib/build.py expect basin-bulk-shelving-440` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("basin-bulk-shelving-440"), dict(primitives=4, extents=((-445.0, 10.0, 150.0), (-5.0, 490.0, 400.0)), nodes=[], holes=0))
