#!/usr/bin/env python3
"""valve-needle: the contract. Regenerate with `python lib/build.py expect valve-needle` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("valve-needle"), dict(primitives=12, extents=((-0.2, -12.2, -12.0), (40.2, 12.0, 46.0)), nodes=['knob', 'port-1', 'port-2'], holes=4))
