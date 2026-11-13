#!/usr/bin/env python3
"""hook-rack: the contract. Regenerate with `python lib/build.py expect hook-rack` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("hook-rack"), dict(primitives=79, extents=((-400.0, -64.0, -1500.0), (400.0, 64.0, 30.0)), nodes=[], holes=1))
