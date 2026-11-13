#!/usr/bin/env python3
"""footswitch: the contract. Regenerate with `python lib/build.py expect footswitch` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("footswitch"), dict(primitives=16, extents=((-50.0, -200.0, 0.0), (50.0, 0.0, 130.6)), nodes=['pedal', 't-11', 't-12', 't-23', 't-24'], holes=1))
