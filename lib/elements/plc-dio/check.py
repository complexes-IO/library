#!/usr/bin/env python3
"""plc-dio: the contract. Regenerate with `python lib/build.py expect plc-dio` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("plc-dio"), dict(primitives=157, extents=((0.0, -86.0, -50.0), (60.0, 7.5, 50.0)), nodes=['led-di0', 'led-di1', 'led-di2', 'led-di3', 'led-di4', 'led-di5', 'led-di6', 'led-di7', 'led-do0', 'led-do1', 'led-do2', 'led-do3', 'led-do4', 'led-do5', 'led-do6', 'led-do7', 'led-err', 'led-run', 'x1.s-1', 'x1.s-10', 'x1.s-11', 'x1.s-2', 'x1.s-3', 'x1.s-4', 'x1.s-5', 'x1.s-6', 'x1.s-7', 'x1.s-8', 'x1.s-9', 'x1.t-1', 'x1.t-10', 'x1.t-11', 'x1.t-2', 'x1.t-3', 'x1.t-4', 'x1.t-5', 'x1.t-6', 'x1.t-7', 'x1.t-8', 'x1.t-9', 'x2.s-1', 'x2.s-10', 'x2.s-2', 'x2.s-3', 'x2.s-4', 'x2.s-5', 'x2.s-6', 'x2.s-7', 'x2.s-8', 'x2.s-9', 'x2.t-1', 'x2.t-10', 'x2.t-2', 'x2.t-3', 'x2.t-4', 'x2.t-5', 'x2.t-6', 'x2.t-7', 'x2.t-8', 'x2.t-9'], holes=0))
