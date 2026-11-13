#!/usr/bin/env python3
"""seal-strip-eptfe: a roll of expanded PTFE sealing strip, the soft joint sealant laid on a flange face or a cover's joint and
pressed flat when the joint is bolted up (a tank's or a reservoir's cover, a housing's split face, an unmachined flange). Generic
(OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC010669 "Expanded PTFE sealing strip" (its synonyms
include PTFE cord, sealing band, sealing strip); the class values it is designed to are in spec.md "## Class values". No dimensional
standard on file or off it shapes the strip: its section and its length on the roll are design choices, the roll's outside diameter
is calculated from them (the wound strip's area, spec.md Dimensions), and the core is a design choice too. The roll lies flat, its
axis on z. Nothing moves and nothing connects: no port, no node. No vendor file was opened (pneu-r101)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "seal-strip-eptfe", "1.0", "connector-part"
TITLE = "generic expanded PTFE sealing strip, 10 x 3, 10 m roll"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic expanded PTFE sealing strip (ETIM 10.0 EC010669), a strip wound on a cardboard core; the "
            "strip's section, its length on the roll and the core are design choices, the roll's outside diameter calculated from them")
ORIGIN = "the centre of the roll's underside (z = 0) on its axis; the roll lies flat, its axis along +z, the strip's width along z"
COMMAND = "SEAL-STRIP-EPTFE"
PARAMS = dict(size="10x3", length=10000.0)

STRIPS = {"10x3": (10.0, 3.0), "14x5": (14.0, 5.0), "20x7": (20.0, 7.0)}   # design choices: (width, thickness) of the strip, mm
CORE_ID = 76.0                       # design choice: the core's bore (a 3 in core, a common winding core)
CORE_WALL = 8.0                      # design choice: the core's wall; >= 8 so every edge passes the AutoCAD fillet pre-flight
CORE_OD = CORE_ID + 2 * CORE_WALL    # 92: the strip's first turn sits on it
LENGTH_MIN, LENGTH_MAX = 1000.0, 25000.0   # design choices: the strip on one roll, 1 m to 25 m
OD_MAX = 400.0                       # design choice: the largest roll built
MAT_STRIP = "M-WHITE-PVC"            # class value: expanded PTFE, white (the closest material on file to its look)
MAT_CORE = "M-BROWN"                 # design choice: a cardboard core

for _s, (_w, _t) in STRIPS.items():
    assert _w >= 8.0                 # the roll's height is the strip's width: >= 8 for the fillet pre-flight (envelope edges)
    assert _t < _w                   # a strip, laid flat on the joint, is wider than it is thick


def outside_d(size="10x3", length=10000.0):
    """the roll's outside diameter: the wound strip's end area length x thickness fills the annulus from the core's OD,
    pi / 4 x (D^2 - CORE_OD^2) = length x thickness (216.01 for 10 m of 10 x 3)"""
    return math.sqrt(CORE_OD ** 2 + 4.0 * float(length) * STRIPS[size][1] / math.pi)


def build(size="10x3", length=10000.0):
    if size not in STRIPS: raise ValueError(f"size {size}: one of {', '.join(STRIPS)} (width x thickness, mm)")
    length = float(length)
    if not LENGTH_MIN <= length <= LENGTH_MAX: raise ValueError(f"length {length:g}: {LENGTH_MIN:g} to {LENGTH_MAX:g} mm")
    w = STRIPS[size][0]; od = outside_d(size, length)
    if od > OD_MAX: raise ValueError(f"size {size} x {length:g} mm makes a roll of {od:.1f} mm, over {OD_MAX:g}")
    P = Prims()
    roll = P.cyl(MAT_STRIP, (0, 0, 0), (0, 0, w), od / 2.0)                              # the wound strip
    P.hole(MAT_STRIP, (0, 0, -1.0), (0, 0, w + 1.0), CORE_OD / 2.0, roll)               # its bore, on the core
    core = P.cyl(MAT_CORE, (0, 0, 0), (0, 0, w), CORE_OD / 2.0)                          # the core, face to face in the bore
    P.hole(MAT_CORE, (0, 0, -1.0), (0, 0, w + 1.0), CORE_ID / 2.0, core)                # the core's bore
    r = od / 2.0
    P.collider("env", -r, -r, 0, 2 * r, 2 * r, w)
    return P


PREVIEWS = [dict(name="three-quarter, 10 x 3, 10 m", az=250, el=35), dict(name="side", az=200, el=5),
            dict(name="14 x 5, 5 m", az=250, el=35, params=dict(size="14x5", length=5000.0)),
            dict(name="20 x 7, 5 m", az=250, el=35, params=dict(size="20x7", length=5000.0))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
