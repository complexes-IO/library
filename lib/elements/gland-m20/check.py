#!/usr/bin/env python3
"""gland-m20: the contract. Regenerate with `python lib/build.py expect gland-m20` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("gland-m20"), dict(primitives=17, extents=((-14.86, -27.9, -14.86), (14.86, 10.2, 14.86)), nodes=['self'], holes=0))
