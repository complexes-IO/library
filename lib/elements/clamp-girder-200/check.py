#!/usr/bin/env python3
"""clamp-girder-200: the contract. Regenerate with `python lib/build.py expect clamp-girder-200` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("clamp-girder-200"), dict(primitives=14, extents=((-40.0, -134.0, -120.0), (40.0, 184.0, 36.0)), nodes=['jaw'], holes=4))
