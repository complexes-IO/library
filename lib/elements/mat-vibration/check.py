#!/usr/bin/env python3
"""mat-vibration: the contract. Regenerate with `python lib/build.py expect mat-vibration` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("mat-vibration"), dict(primitives=42, extents=((-250.0, -250.0, 0.0), (250.0, 250.0, 16.0)), nodes=[], holes=0))
