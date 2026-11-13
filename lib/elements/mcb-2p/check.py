#!/usr/bin/env python3
"""mcb-2p: the contract. Regenerate with `python lib/build.py expect mcb-2p` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("mcb-2p"), dict(primitives=19, extents=((0.0, -65.5, -52.6), (35.4, 7.5, 52.6)), nodes=['indicator-1', 'indicator-2', 't-1', 't-2', 't-3', 't-4', 'toggle'], holes=0))
