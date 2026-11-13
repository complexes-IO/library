#!/usr/bin/env python3
"""caster: the contract. Regenerate with `python lib/build.py expect caster` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("caster"), dict(primitives=19, extents=((-50.0, -42.5, -140.0), (75.0, 42.5, 0.0)), nodes=['swivel', 'wheel'], holes=8))
