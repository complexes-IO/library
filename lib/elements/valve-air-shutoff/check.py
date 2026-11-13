#!/usr/bin/env python3
"""valve-air-shutoff: the contract. Regenerate with `python lib/build.py expect valve-air-shutoff` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("valve-air-shutoff"), dict(primitives=13, extents=((-0.2, -50.0, -13.0), (44.2, 13.0, 28.0)), nodes=['lever', 'port-1', 'port-2'], holes=4))
