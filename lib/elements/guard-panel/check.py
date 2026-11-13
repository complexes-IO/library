#!/usr/bin/env python3
"""guard-panel: the contract. Regenerate with `python lib/build.py expect guard-panel` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("guard-panel"), dict(primitives=14, extents=((-540.0, -30.0, 0.0), (540.0, 0.0, 800.0)), nodes=[], holes=4))
