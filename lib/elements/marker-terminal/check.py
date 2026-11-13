#!/usr/bin/env python3
"""marker-terminal: the contract. Regenerate with `python lib/build.py expect marker-terminal` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("marker-terminal"), dict(primitives=2, extents=((0.15, -46.5, -5.0), (5.85, -44.5, 5.0)), nodes=[], holes=0))
