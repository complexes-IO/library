#!/usr/bin/env python3
"""reactor-line-3p-4a: the contract. Regenerate with `python lib/build.py expect reactor-line-3p-4a` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("reactor-line-3p-4a"), dict(primitives=49, extents=((-8.0, -73.2, -10.0), (104.0, 0.0, 124.0)), nodes=['t-1U1', 't-1U2', 't-1V1', 't-1V2', 't-1W1', 't-1W2', 't-PE'], holes=4))
