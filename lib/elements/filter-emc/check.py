#!/usr/bin/env python3
"""filter-emc: the contract. Regenerate with `python lib/build.py expect filter-emc` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("filter-emc"), dict(primitives=36, extents=((-10.0, -71.2, -10.0), (50.0, 0.0, 220.0)), nodes=['t-L1', 't-L1-load', 't-L2', 't-L2-load', 't-L3', 't-L3-load', 't-PE', 't-PE-load'], holes=4))
