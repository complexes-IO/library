#!/usr/bin/env python3
"""psu-acdc-24v-1a25: the contract. Regenerate with `python lib/build.py expect psu-acdc-24v-1a25` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("psu-acdc-24v-1a25"), dict(primitives=60, extents=((0.0, -86.0, -50.0), (45.0, 7.5, 50.0)), nodes=['led-ac', 'led-dc', 'x1.s-1', 'x1.s-2', 'x1.s-3', 'x1.t-1', 'x1.t-2', 'x1.t-3', 'x2.s-1', 'x2.s-2', 'x2.t-1', 'x2.t-2', 'x3.s-1', 'x3.s-2', 'x3.t-1', 'x3.t-2'], holes=0))
