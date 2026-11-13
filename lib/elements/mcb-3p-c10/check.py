#!/usr/bin/env python3
"""mcb-3p-c10: the contract. Regenerate with `python lib/build.py expect mcb-3p-c10` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("mcb-3p-c10"), dict(primitives=25, extents=((0.0, -65.5, -52.6), (53.1, 7.5, 52.6)), nodes=['indicator-1', 'indicator-2', 'indicator-3', 't-1-line', 't-1-load', 't-2-line', 't-2-load', 't-3-line', 't-3-load', 'toggle'], holes=0))
