#!/usr/bin/env python3
"""cordset-m12: the contract. Regenerate with `python lib/build.py expect cordset-m12` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("cordset-m12"), dict(primitives=115, extents=((-7.5, -1000.0, -30.41), (7.5, 8.9, 7.5)), nodes=['port-a', 'port-a.insert.c1', 'port-a.insert.c2', 'port-a.insert.c3', 'port-a.insert.c4', 'port-a.insert.c5', 'port-a.nut', 'port-b', 'port-b.insert.c1', 'port-b.insert.c2', 'port-b.insert.c3', 'port-b.insert.c4', 'port-b.insert.c5', 'port-b.nut', 'port-b.seal'], holes=47))
