#!/usr/bin/env python3
"""terminal-plug: the contract. Regenerate with `python lib/build.py expect terminal-plug` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("terminal-plug"), dict(primitives=27, extents=((0.0, -16.0, -6.0), (20.0, 0.0, 9.5)), nodes=['s-1', 's-2', 's-3', 's-4', 't-1', 't-2', 't-3', 't-4'], holes=0))
