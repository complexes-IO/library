#!/usr/bin/env python3
"""photoeye-m18: the contract. Regenerate with `python lib/build.py expect photoeye-m18` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("photoeye-m18"), dict(primitives=7, extents=((-8.99, -1.0, -8.99), (8.99, 62.0, 8.99)), nodes=['led-out', 'led-pwr', 'port-x1'], holes=0))
