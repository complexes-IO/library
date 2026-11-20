#!/usr/bin/env python3
"""reel-cable-630: the contract. Regenerate with `python lib/build.py expect reel-cable-630` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("reel-cable-630"), dict(primitives=9, extents=((-250.0, -315.0, -315.0), (250.0, 315.0, 315.0)), nodes=[], holes=5))
