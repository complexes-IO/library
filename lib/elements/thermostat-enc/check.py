#!/usr/bin/env python3
"""thermostat-enc: the contract. Regenerate with `python lib/build.py expect thermostat-enc` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("thermostat-enc"), dict(primitives=16, extents=((0.0, -48.1, -30.0), (35.0, 7.5, 30.0)), nodes=['dial'], holes=0))
