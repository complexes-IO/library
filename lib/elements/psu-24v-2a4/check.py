#!/usr/bin/env python3
"""psu-24v-2a4: the contract. Regenerate with `python lib/build.py expect psu-24v-2a4` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("psu-24v-2a4"), dict(primitives=33, extents=((0.0, -102.7, -48.0), (32.0, 7.5, 45.3)), nodes=['led-dclow', 'led-dcok', 't-l', 't-n', 't-pe', 't-vn', 't-vn2', 't-vp', 't-vp2', 'vadj'], holes=0))
