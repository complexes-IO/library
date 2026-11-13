#!/usr/bin/env python3
"""panel-plc-training: the contract. Regenerate with `python lib/build.py expect panel-plc-training` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("panel-plc-training"), dict(primitives=22, extents=((0.0, -150.0, 0.0), (600.0, 150.0, 482.0)), nodes=[], holes=16))
