#!/usr/bin/env python3
"""gun-spray: the contract. Regenerate with `python lib/build.py expect gun-spray` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("gun-spray"), dict(primitives=12, extents=((-58.0, -47.0, 0.0), (95.0, 47.0, 293.0)), nodes=['port-1', 'trigger'], holes=1))
