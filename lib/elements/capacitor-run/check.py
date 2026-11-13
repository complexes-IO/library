#!/usr/bin/env python3
"""capacitor-run: the contract. Regenerate with `python lib/build.py expect capacitor-run` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("capacitor-run"), dict(primitives=17, extents=((-8.0, -50.0, -47.5), (72.0, 0.0, 62.0)), nodes=['t-1', 't-2'], holes=3))
