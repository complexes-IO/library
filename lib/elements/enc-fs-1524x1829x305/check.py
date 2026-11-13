#!/usr/bin/env python3
"""enc-fs-1524x1829x305: the contract. Regenerate with `python lib/build.py expect enc-fs-1524x1829x305` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("enc-fs-1524x1829x305"), dict(primitives=126, extents=((-1.0, -67.0, 0.0), (1525.0, 365.0, 2182.0)), nodes=['back-panel', 'btn-reset', 'door-l', 'door-r', 'estop-door', 'gland-plate', 'handle-1', 'hinge-l', 'hinge-r', 'lamp-power', 'pe-body', 'pe-door-l', 'pe-door-r'], holes=18))
