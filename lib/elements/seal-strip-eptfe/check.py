#!/usr/bin/env python3
"""seal-strip-eptfe: the contract. Regenerate with `python lib/build.py expect seal-strip-eptfe` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("seal-strip-eptfe"), dict(primitives=5, extents=((-108.01, -108.01, 0.0), (108.01, 108.01, 10.0)), nodes=[], holes=2))
