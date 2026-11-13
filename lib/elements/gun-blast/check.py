#!/usr/bin/env python3
"""gun-blast: the contract. Regenerate with `python lib/build.py expect gun-blast` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("gun-blast"), dict(primitives=7, extents=((-80.0, -18.0, 0.0), (85.0, 18.0, 164.0)), nodes=['port-1'], holes=1))
