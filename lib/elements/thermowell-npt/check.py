#!/usr/bin/env python3
"""thermowell-npt: the contract. Regenerate with `python lib/build.py expect thermowell-npt` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("thermowell-npt"), dict(primitives=15, extents=((-11.55, -11.55, -92.8), (11.55, 11.55, 13.2)), nodes=['port-a', 'port-b'], holes=4))
