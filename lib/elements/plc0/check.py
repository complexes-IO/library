#!/usr/bin/env python3
"""plc0: the contract. Regenerate with `python lib/build.py expect plc0` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("plc0"), dict(primitives=13, extents=((0.0, -60.3, -65.3), (90.0, 7.5, 52.5)), nodes=['led-fault', 'led-run', 'port-eth', 'port-pwr'], holes=0))
