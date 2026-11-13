#!/usr/bin/env python3
"""contact-m12-socket: the contract. Regenerate with `python lib/build.py expect contact-m12-socket` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("contact-m12-socket"), dict(primitives=3, extents=((-0.82, 0.0, -0.82), (0.82, 8.0, 0.82)), nodes=['self'], holes=1))
