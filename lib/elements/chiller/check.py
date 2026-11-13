#!/usr/bin/env python3
"""chiller: the contract. Regenerate with `python lib/build.py expect chiller` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("chiller"), dict(primitives=15, extents=((-250.0, -310.0, 0.0), (250.0, 314.0, 990.0)), nodes=['port-return', 'port-supply', 'pwr'], holes=2))
