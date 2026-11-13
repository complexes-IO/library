#!/usr/bin/env python3
"""conveyor-roller: the contract. Regenerate with `python lib/build.py expect conveyor-roller` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("conveyor-roller"), dict(primitives=53, extents=((-375.0, -750.0, 0.0), (375.0, 750.0, 750.0)), nodes=['roller-1', 'roller-10', 'roller-11', 'roller-12', 'roller-13', 'roller-14', 'roller-15', 'roller-16', 'roller-17', 'roller-18', 'roller-19', 'roller-2', 'roller-20', 'roller-3', 'roller-4', 'roller-5', 'roller-6', 'roller-7', 'roller-8', 'roller-9'], holes=4))
