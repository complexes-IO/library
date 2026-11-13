#!/usr/bin/env python3
"""ipc: the contract. Regenerate with `python lib/build.py expect ipc` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("ipc"), dict(primitives=57, extents=((-55.0, -164.0, -120.0), (55.0, 0.0, 120.0)), nodes=['led-pwr', 'led-run', 'x1.s-1', 'x1.s-2', 'x1.s-3', 'x1.t-1', 'x1.t-2', 'x1.t-3', 'x2.c-1', 'x2.c-2', 'x2.c-3', 'x2.c-4', 'x2.c-5', 'x2.c-6', 'x2.c-7', 'x2.c-8', 'x3.c-1', 'x3.c-2', 'x3.c-3', 'x3.c-4', 'x3.c-5', 'x3.c-6', 'x3.c-7', 'x3.c-8'], holes=4))
