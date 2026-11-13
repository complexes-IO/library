#!/usr/bin/env python3
"""gauge-t: the contract. Regenerate with `python lib/build.py expect gauge-t` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("gauge-t"), dict(primitives=18, extents=((-32.0, -32.0, -100.0), (32.0, 32.0, 39.0)), nodes=['pointer', 'port-1'], holes=1))
