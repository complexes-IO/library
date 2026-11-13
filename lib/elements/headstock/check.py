#!/usr/bin/env python3
"""headstock: the contract. Regenerate with `python lib/build.py expect headstock` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("headstock"), dict(primitives=6, extents=((-250.0, -220.0, 0.0), (270.0, 220.0, 420.0)), nodes=['spindle-seat'], holes=0))
