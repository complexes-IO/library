#!/usr/bin/env python3
"""joystick-22: the contract. Regenerate with `python lib/build.py expect joystick-22` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("joystick-22"), dict(primitives=27, extents=((-15.0, -54.0, -38.5), (15.0, 42.5, 17.5)), nodes=['self', 't-13', 't-14', 't-23', 't-24'], holes=2))
