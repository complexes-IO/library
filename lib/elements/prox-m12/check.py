#!/usr/bin/env python3
"""prox-m12: the contract. Regenerate with `python lib/build.py expect prox-m12` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("prox-m12"), dict(primitives=7, extents=((-5.99, 0.0, -5.99), (5.99, 53.0, 5.99)), nodes=['led-out', 'port-x1'], holes=0))
