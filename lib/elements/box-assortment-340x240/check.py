#!/usr/bin/env python3
"""box-assortment-340x240: the contract. Regenerate with `python lib/build.py expect box-assortment-340x240` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("box-assortment-340x240"), dict(primitives=16, extents=((0.0, 0.0, 0.0), (340.0, 240.0, 52.0)), nodes=['lid'], holes=0))
