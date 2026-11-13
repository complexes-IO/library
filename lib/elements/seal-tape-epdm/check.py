#!/usr/bin/env python3
"""seal-tape-epdm: the contract. Regenerate with `python lib/build.py expect seal-tape-epdm` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("seal-tape-epdm"), dict(primitives=5, extents=((-100.37, -100.37, 0.0), (100.37, 100.37, 15.0)), nodes=[], holes=2))
