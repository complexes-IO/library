#!/usr/bin/env python3
"""seal-tape-epdm: a roll of closed-cell EPDM sponge sealing tape, self-adhesive on one face, the joint seal stuck along a cover's,
a guard panel's, a door's or a duct's joint face and pressed when the joint is closed, keeping dust and splash out (no pressure
seal). Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC003185 "Sealing tape" (its synonyms
include elasto cell band, joint sealing tape, sealing adhesive tape, sealing strip); the class values it is designed to are in
spec.md "## Class values". No dimensional standard on file shapes the tape: its section and its length on the roll are design
choices, the roll's outside diameter is calculated from them (the wound tape's area, spec.md Dimensions), and the core is a design
choice too. seal-strip-eptfe 1.0's roll pattern (pneu-r101). The roll lies flat, its axis on z. Nothing moves and nothing
connects: no port, no node. No vendor file was opened (pneu-r103)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "seal-tape-epdm", "1.0", "connector-part"
TITLE = "generic EPDM sponge sealing tape, self-adhesive, 15 x 5, 5 m roll"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic sealing tape (ETIM 10.0 EC003185), a closed-cell EPDM sponge tape, self-adhesive on one face, "
            "wound on a cardboard core; the tape's section, its length on the roll and the core are design choices, the roll's "
            "outside diameter calculated from them")
ORIGIN = "the centre of the roll's underside (z = 0) on its axis; the roll lies flat, its axis along +z, the tape's width along z"
COMMAND = "SEAL-TAPE-EPDM"
PARAMS = dict(size="15x5", length=5000.0)

TAPES = {"10x3": (10.0, 3.0), "15x5": (15.0, 5.0), "20x10": (20.0, 10.0)}   # design choices: (width, thickness) of the tape, mm
CORE_ID = 76.0                       # design choice: the core's bore (a 3 in core, seal-strip-eptfe's)
CORE_WALL = 8.0                      # design choice: the core's wall; >= 8 so every edge passes the AutoCAD fillet pre-flight
CORE_OD = CORE_ID + 2 * CORE_WALL    # 92: the tape's first turn sits on it
WOUND_MIN = 8.0                      # design choice: the wound tape's radial wall is at least 8 (the fillet pre-flight, as the core)
LENGTH_MIN, LENGTH_MAX = 1000.0, 25000.0   # design choices: the tape on one roll, 1 m to 25 m
OD_MAX = 400.0                       # design choice: the largest roll built
MAT_TAPE = "M-GASKET"                # class value: EPDM sponge, black (the black rubber material on file)
MAT_CORE = "M-BROWN"                 # design choice: a cardboard core


def outside_d(size="15x5", length=5000.0):
    """the roll's outside diameter: the wound tape's end area length x thickness fills the annulus from the core's OD,
    pi / 4 x (D^2 - CORE_OD^2) = length x thickness (200.74 for 5 m of 15 x 5); the release liner is not counted"""
    return math.sqrt(CORE_OD ** 2 + 4.0 * float(length) * TAPES[size][1] / math.pi)


for _s, (_w, _t) in TAPES.items():
    assert _w >= 8.0                 # the roll's height is the tape's width: >= 8 for the fillet pre-flight (envelope edges)
    assert _t < _w                   # a tape, stuck flat on the joint face, is wider than it is thick
    assert (outside_d(_s, LENGTH_MIN) - CORE_OD) / 2.0 >= WOUND_MIN   # the shortest roll still has 8 of wound tape (9.42 for 10 x 3)


def build(size="15x5", length=5000.0):
    if size not in TAPES: raise ValueError(f"size {size}: one of {', '.join(TAPES)} (width x thickness, mm)")
    length = float(length)
    if not LENGTH_MIN <= length <= LENGTH_MAX: raise ValueError(f"length {length:g}: {LENGTH_MIN:g} to {LENGTH_MAX:g} mm")
    w = TAPES[size][0]; od = outside_d(size, length)
    if od > OD_MAX: raise ValueError(f"size {size} x {length:g} mm makes a roll of {od:.1f} mm, over {OD_MAX:g}")
    P = Prims()
    roll = P.cyl(MAT_TAPE, (0, 0, 0), (0, 0, w), od / 2.0)                               # the wound tape
    P.hole(MAT_TAPE, (0, 0, -1.0), (0, 0, w + 1.0), CORE_OD / 2.0, roll)                # its bore, on the core
    core = P.cyl(MAT_CORE, (0, 0, 0), (0, 0, w), CORE_OD / 2.0)                          # the core, face to face in the bore
    P.hole(MAT_CORE, (0, 0, -1.0), (0, 0, w + 1.0), CORE_ID / 2.0, core)                # the core's bore
    r = od / 2.0
    P.collider("env", -r, -r, 0, 2 * r, 2 * r, w)
    return P


PREVIEWS = [dict(name="three-quarter, 15 x 5, 5 m", az=250, el=35), dict(name="side", az=200, el=5),
            dict(name="10 x 3, 10 m", az=250, el=35, params=dict(size="10x3", length=10000.0)),
            dict(name="20 x 10, 3 m", az=250, el=35, params=dict(size="20x10", length=3000.0))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
