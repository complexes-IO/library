#!/usr/bin/env python3
"""gauge-p: the contract. Regenerate with `python lib/build.py expect gauge-p` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("gauge-p"), dict(primitives=17, extents=((-32.0, -14.0, -10.21), (32.0, 13.0, 79.5)), nodes=['pointer', 'port-1'], holes=1))
