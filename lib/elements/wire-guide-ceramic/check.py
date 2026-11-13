#!/usr/bin/env python3
"""wire-guide-ceramic: the contract. Regenerate with `python lib/build.py expect wire-guide-ceramic` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("wire-guide-ceramic"), dict(primitives=5, extents=((-12.0, -12.0, -8.0), (12.0, 12.0, 4.0)), nodes=[], holes=2))
