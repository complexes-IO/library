#!/usr/bin/env python3
"""saddle: the contract. Regenerate with `python lib/build.py expect saddle` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("saddle"), dict(primitives=7, extents=((-300.0, -350.0, 0.0), (300.0, 350.0, 270.0)), nodes=['ways'], holes=0))
