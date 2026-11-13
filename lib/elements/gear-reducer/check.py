#!/usr/bin/env python3
"""gear-reducer: the contract. Regenerate with `python lib/build.py expect gear-reducer` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("gear-reducer"), dict(primitives=19, extents=((-75.0, -92.0, 0.0), (97.0, 65.0, 160.0)), nodes=['input', 'output'], holes=9))
