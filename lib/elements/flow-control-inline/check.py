#!/usr/bin/env python3
"""flow-control-inline: the contract. Regenerate with `python lib/build.py expect flow-control-inline` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("flow-control-inline"), dict(primitives=13, extents=((-0.2, -12.2, -12.0), (44.2, 12.0, 41.0)), nodes=['knob', 'port-1', 'port-2'], holes=4))
