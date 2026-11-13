#!/usr/bin/env python3
"""manifold-pneu: the contract. Regenerate with `python lib/build.py expect manifold-pneu` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("manifold-pneu"), dict(primitives=20, extents=((-0.2, -36.0, -0.2), (140.2, 0.0, 50.2)), nodes=['port-1', 'port-3', 'port-5', 'st1-port-2', 'st1-port-4', 'st2-port-2', 'st2-port-4', 'st3-port-2', 'st3-port-4', 'st4-port-2', 'st4-port-4'], holes=2))
