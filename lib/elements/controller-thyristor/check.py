#!/usr/bin/env python3
"""controller-thyristor: the contract. Regenerate with `python lib/build.py expect controller-thyristor` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("controller-thyristor"), dict(primitives=61, extents=((0.0, -99.0, -75.0), (90.0, 7.5, 75.0)), nodes=['led-fault', 'led-l1', 'led-l2', 'led-l3', 'led-on', 't-0V', 't-13', 't-14', 't-24V', 't-AI', 't-EN', 't-L1', 't-L2', 't-L3', 't-PE', 't-T1', 't-T2', 't-T3'], holes=0))
