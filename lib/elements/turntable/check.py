#!/usr/bin/env python3
"""turntable: the contract. Regenerate with `python lib/build.py expect turntable` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("turntable"), dict(primitives=45, extents=((-475.0, -500.0, 0.0), (475.0, 500.0, 760.0)), nodes=['deck', 'roller-1', 'roller-2', 'roller-3', 'roller-4', 'roller-5', 'roller-6'], holes=4))
