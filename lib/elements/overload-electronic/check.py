#!/usr/bin/env python3
"""overload-electronic: the contract. Regenerate with `python lib/build.py expect overload-electronic` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("overload-electronic"), dict(primitives=43, extents=((0.0, -77.3, -45.0), (45.0, 7.5, 45.0)), nodes=['btn-reset', 'dial-ir', 'ind-trip', 't-95', 't-96', 't-97', 't-98', 't-L1', 't-L2', 't-L3', 't-T1', 't-T2', 't-T3'], holes=0))
