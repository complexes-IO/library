#!/usr/bin/env python3
"""contactor-9a-1no1nc: the contract. Regenerate with `python lib/build.py expect contactor-9a-1no1nc` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("contactor-9a-1no1nc"), dict(primitives=128, extents=((-0.1, -133.0, -39.2), (44.9, 7.5, 39.2)), nodes=['armature', 'aux-13', 'aux-21', 'carrier', 'coil', 'fb-53', 'fb-61', 'fb-slide', 'front-block', 'pole-1', 'pole-2', 'pole-3', 'spring-contact-1', 'spring-contact-2', 'spring-contact-3', 'spring-return', 't-1', 't-13', 't-14', 't-2', 't-21', 't-22', 't-3', 't-4', 't-5', 't-53', 't-54', 't-6', 't-61', 't-62', 't-a1', 't-a2'], holes=20))
