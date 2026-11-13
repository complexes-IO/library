#!/usr/bin/env python3
"""servo-drive: the contract. Regenerate with `python lib/build.py expect servo-drive` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("servo-drive"), dict(primitives=145, extents=((0.0, -136.0, -75.0), (65.0, 7.5, 75.0)), nodes=['led-flt', 'led-rdy', 't-L1', 't-L2', 't-L3', 't-PE', 't-PE-m', 't-U', 't-V', 't-W', 'x1.s-1', 'x1.s-2', 'x1.s-3', 'x1.s-4', 'x1.s-5', 'x1.s-6', 'x1.s-7', 'x1.s-8', 'x1.t-1', 'x1.t-2', 'x1.t-3', 'x1.t-4', 'x1.t-5', 'x1.t-6', 'x1.t-7', 'x1.t-8', 'x2.s-1', 'x2.s-2', 'x2.t-1', 'x2.t-2', 'x3.s-1', 'x3.s-2', 'x3.s-3', 'x3.s-4', 'x3.s-5', 'x3.s-6', 'x3.t-1', 'x3.t-2', 'x3.t-3', 'x3.t-4', 'x3.t-5', 'x3.t-6'], holes=0))
