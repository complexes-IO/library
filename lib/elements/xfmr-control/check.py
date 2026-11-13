#!/usr/bin/env python3
"""xfmr-control: the contract. Regenerate with `python lib/build.py expect xfmr-control` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("xfmr-control"), dict(primitives=50, extents=((-8.0, -108.0, -10.0), (108.0, 0.0, 120.0)), nodes=['t-1U', 't-1V', 't-PE', 'x2.s-1', 'x2.s-2', 'x2.t-1', 'x2.t-2'], holes=4))
