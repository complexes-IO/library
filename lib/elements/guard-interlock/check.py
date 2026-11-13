#!/usr/bin/env python3
"""guard-interlock: the contract. Regenerate with `python lib/build.py expect guard-interlock` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("guard-interlock"), dict(primitives=23, extents=((-20.0, -54.0, 0.0), (20.0, 0.0, 122.0)), nodes=['actuator', 't-11', 't-12', 't-21', 't-22', 't-A1', 't-A2'], holes=5))
