#!/usr/bin/env python3
"""stack-light: the contract. Regenerate with `python lib/build.py expect stack-light` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("stack-light"), dict(primitives=21, extents=((-50.0, -30.6, 0.0), (50.0, 30.0, 176.0)), nodes=['lamp-green', 'lamp-red', 'lamp-yellow', 't-1', 't-2', 't-3', 't-C'], holes=3))
