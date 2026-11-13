#!/usr/bin/env python3
"""contact-m12-pin: the contract. Regenerate with `python lib/build.py expect contact-m12-pin` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("contact-m12-pin"), dict(primitives=5, extents=((-0.75, 0.0, -0.75), (0.75, 12.5, 0.75)), nodes=['self'], holes=0))
