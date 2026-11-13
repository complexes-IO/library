#!/usr/bin/env python3
"""relay-ice-cube-2co: the contract. Regenerate with `python lib/build.py expect relay-ice-cube-2co` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("relay-ice-cube-2co"), dict(primitives=84, extents=((0.0, -69.71, -39.7), (29.2, 7.5, 39.7)), nodes=['actuator', 'armature', 'btn-test', 'case', 'coil', 'door-lock', 'flag', 'led-coil', 'pole-1', 'pole-2', 'spring-return', 't-1', 't-12', 't-13', 't-14', 't-4', 't-5', 't-8', 't-9'], holes=0))
