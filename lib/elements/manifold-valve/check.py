#!/usr/bin/env python3
"""manifold-valve: the contract. Regenerate with `python lib/build.py expect manifold-valve` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("manifold-valve"), dict(primitives=20, extents=((-28.0, -58.0, -8.2), (28.2, 0.0, 36.2)), nodes=['knob-bleed', 'knob-block', 'port-1', 'port-2', 'port-cal'], holes=8))
