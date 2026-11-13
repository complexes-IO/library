#!/usr/bin/env python3
"""head-rivet-c-hyd: the contract. Regenerate with `python lib/build.py expect head-rivet-c-hyd` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("head-rivet-c-hyd"), dict(primitives=26, extents=((-110.0, -50.0, 0.0), (60.0, 50.0, 651.5)), nodes=['cyl.port-cap', 'cyl.port-rod', 'cyl.rod'], holes=4))
