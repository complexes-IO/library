#!/usr/bin/env python3
"""term-dist-12a-1p: the contract. Regenerate with `python lib/build.py expect term-dist-12a-1p` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("term-dist-12a-1p"), dict(primitives=46, extents=((0.0, -76.0, -40.0), (36.0, 7.5, 40.0)), nodes=['x1.s-1', 'x1.s-2', 'x1.s-3', 'x1.s-4', 'x1.s-5', 'x1.s-6', 'x1.t-1', 'x1.t-2', 'x1.t-3', 'x1.t-4', 'x1.t-5', 'x1.t-6'], holes=0))
