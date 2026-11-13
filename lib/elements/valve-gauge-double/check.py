#!/usr/bin/env python3
"""valve-gauge-double: the contract. Regenerate with `python lib/build.py expect valve-gauge-double` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("valve-gauge-double"), dict(primitives=16, extents=((-12.0, -35.0, -10.21), (12.0, 11.0, 70.2)), nodes=['knob-2', 'knob-4', 'port-1', 'port-2', 'port-4'], holes=4))
