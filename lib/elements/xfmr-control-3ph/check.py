#!/usr/bin/env python3
"""xfmr-control-3ph: the contract. Regenerate with `python lib/build.py expect xfmr-control-3ph` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("xfmr-control-3ph"), dict(primitives=52, extents=((-11.0, -98.2, -10.0), (183.0, 0.0, 202.0)), nodes=['t-1U', 't-1V', 't-1W', 't-2N', 't-2U', 't-2V', 't-2W', 't-PE'], holes=4))
