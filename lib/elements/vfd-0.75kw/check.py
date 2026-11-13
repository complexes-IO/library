#!/usr/bin/env python3
"""vfd-0.75kw: the contract. Regenerate with `python lib/build.py expect vfd-0.75kw` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("vfd-0.75kw"), dict(primitives=100, extents=((0.0, -136.0, -70.0), (72.0, 7.5, 70.0)), nodes=['led-flt', 'led-rdy', 't-L1', 't-L2', 't-L3', 't-PE', 't-PE-m', 't-U', 't-V', 't-W', 'x1.s-1', 'x1.s-2', 'x1.s-3', 'x1.s-4', 'x1.s-5', 'x1.s-6', 'x1.s-7', 'x1.t-1', 'x1.t-2', 'x1.t-3', 'x1.t-4', 'x1.t-5', 'x1.t-6', 'x1.t-7', 'x2.s-1', 'x2.s-2', 'x2.t-1', 'x2.t-2'], holes=0))
