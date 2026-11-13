#!/usr/bin/env python3
"""hose-reel-single-npt: the contract. Regenerate with `python lib/build.py expect hose-reel-single-npt` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("hose-reel-single-npt"), dict(primitives=22, extents=((-110.0, -160.0, 0.0), (171.0, 160.0, 336.0)), nodes=['drum', 'port-1'], holes=8))
