#!/usr/bin/env python3
"""port-pwr-480: the contract. Regenerate with `python lib/build.py expect port-pwr-480` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("port-pwr-480"), dict(primitives=15, extents=((-39.5, -72.7, -39.5), (39.5, 22.2, 40.0)), nodes=['cap', 'self'], holes=4))
