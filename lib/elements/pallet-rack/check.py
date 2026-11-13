#!/usr/bin/env python3
"""pallet-rack: the contract. Regenerate with `python lib/build.py expect pallet-rack` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("pallet-rack"), dict(primitives=38, extents=((-35.0, -35.0, 0.0), (2527.0, 1102.0, 2500.0)), nodes=[], holes=8))
