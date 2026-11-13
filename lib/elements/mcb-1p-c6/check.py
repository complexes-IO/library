#!/usr/bin/env python3
"""mcb-1p-c6: the contract. Regenerate with `python lib/build.py expect mcb-1p-c6` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("mcb-1p-c6"), dict(primitives=13, extents=((0.0, -65.5, -52.6), (17.7, 7.5, 52.6)), nodes=['indicator-1', 't-1-line', 't-1-load', 'toggle'], holes=0))
