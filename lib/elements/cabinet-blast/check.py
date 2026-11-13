#!/usr/bin/env python3
"""cabinet-blast: the contract. Regenerate with `python lib/build.py expect cabinet-blast` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("cabinet-blast"), dict(primitives=30, extents=((-500.0, 0.0, 0.0), (549.0, 800.0, 1650.0)), nodes=['door'], holes=3))
