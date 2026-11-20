#!/usr/bin/env python3
"""rail-suspension-shelving-1000: the contract. Regenerate with `python lib/build.py expect rail-suspension-shelving-1000` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("rail-suspension-shelving-1000"), dict(primitives=9, extents=((-450.0, 455.0, 300.0), (450.0, 495.0, 380.0)), nodes=[], holes=0))
