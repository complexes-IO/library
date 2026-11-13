#!/usr/bin/env python3
"""stand-magnetic: the contract. Regenerate with `python lib/build.py expect stand-magnetic` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("stand-magnetic"), dict(primitives=12, extents=((-45.0, -30.0, 0.0), (185.0, 30.0, 280.0)), nodes=['arm', 'switch'], holes=1))
