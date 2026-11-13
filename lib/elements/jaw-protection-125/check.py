#!/usr/bin/env python3
"""jaw-protection-125: the contract. Regenerate with `python lib/build.py expect jaw-protection-125` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("jaw-protection-125"), dict(primitives=4, extents=((-15.0, -62.5, 0.0), (0.0, 62.5, 53.0)), nodes=[], holes=0))
