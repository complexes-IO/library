#!/usr/bin/env python3
"""fan-cooling: the contract. Regenerate with `python lib/build.py expect fan-cooling` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("fan-cooling"), dict(primitives=22, extents=((-30.6, 0.0, -30.0), (38.7, 25.0, 30.0)), nodes=['impeller', 't-1', 't-2'], holes=5))
