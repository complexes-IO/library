#!/usr/bin/env python3
"""pbs-6h-22: the contract. Regenerate with `python lib/build.py expect pbs-6h-22` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("pbs-6h-22"), dict(primitives=367, extents=((-34.5, -103.5, -26.0), (354.5, 0.0, 81.5)), nodes=['btn-reset', 'btn-start', 'btn-stop', 'estop-1', 'lamp-fault', 'lamp-run', 'lid-1', 's-es', 's-es.insert.c1', 's-es.insert.c2', 's-es.insert.c3', 's-es.insert.c4', 's-es.insert.c5', 's-x1', 's-x1.insert.c1', 's-x1.insert.c2', 's-x1.insert.c3', 's-x1.insert.c4', 's-x1.insert.c5', 's-x2', 's-x2.insert.c1', 's-x2.insert.c2', 's-x2.insert.c3', 's-x2.insert.c4', 's-x2.insert.c5', 's-x3', 's-x3.insert.c1', 's-x3.insert.c2', 's-x3.insert.c3', 's-x3.insert.c4', 's-x3.insert.c5', 's-x5', 's-x5.insert.c1', 's-x5.insert.c2', 's-x5.insert.c3', 's-x5.insert.c4', 's-x5.insert.c5'], holes=115))
