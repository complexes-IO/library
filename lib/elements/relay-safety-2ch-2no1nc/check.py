#!/usr/bin/env python3
"""relay-safety-2ch-2no1nc: the contract. Regenerate with `python lib/build.py expect relay-safety-2ch-2no1nc` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("relay-safety-2ch-2no1nc"), dict(primitives=48, extents=((0.0, -107.1, -59.57), (22.5, 7.5, 59.57)), nodes=['led-in1', 'led-in2', 'led-logic', 'led-out', 'led-pwr', 'sw-mode'], holes=0))
