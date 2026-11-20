#!/usr/bin/env python3
"""psu-ac-24v-2a5: the contract. Regenerate with `python lib/build.py expect psu-ac-24v-2a5` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("psu-ac-24v-2a5"), dict(primitives=44, extents=((0.0, -86.0, -50.0), (45.0, 7.5, 50.0)), nodes=['led-on', 'x1.s-1', 'x1.s-2', 'x1.s-3', 'x1.t-1', 'x1.t-2', 'x1.t-3', 'x2.s-1', 'x2.s-2', 'x2.t-1', 'x2.t-2'], holes=0))
