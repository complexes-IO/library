#!/usr/bin/env python3
"""servo-motor: the contract. Regenerate with `python lib/build.py expect servo-motor` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("servo-motor"), dict(primitives=17, extents=((-40.0, -35.0, -40.0), (40.0, 175.0, 56.0)), nodes=['port-enc', 'port-pwr', 'shaft'], holes=4))
