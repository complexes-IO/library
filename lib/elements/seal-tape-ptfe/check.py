#!/usr/bin/env python3
"""seal-tape-ptfe: the contract. Regenerate with `python lib/build.py expect seal-tape-ptfe` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("seal-tape-ptfe"), dict(primitives=5, extents=((-29.96, -29.96, 0.0), (29.96, 29.96, 12.0)), nodes=[], holes=2))
