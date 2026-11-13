#!/usr/bin/env python3
"""seal-tape-ptfe: a roll of PTFE thread-seal tape, the sealant wound onto a tapered male thread before it is made up (toolkit/pneu.py
D1: every NPT air port is sealed on the thread with sealant on the male). Generic (OPERATING.md 12, EM 2026-11-07): our own
vendor-neutral design of ETIM 10.0 EC010670 "PTFE sealing tape" (its synonyms: gas tape, PTFE tape, sealing tape, water tape); the
class values it is designed to are in spec.md "## Class values". Whether a standard shapes a consumable tape (A-A-58092, EN 751-3)
is EM's ruling (spec.md "Why it may be generic"); until then its width, its thickness and its length on the roll are design choices, the roll's outside diameter is calculated from them (the wound tape's
area, spec.md Dimensions), and the spool is a design choice too. seal-strip-eptfe 1.0's roll pattern (pneu-r101). The roll lies
flat, its axis on z. Nothing moves and nothing connects: no port, no node. No vendor file was opened (pneu-r102)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "seal-tape-ptfe", "1.1", "connector-part"
TITLE = "generic PTFE thread-seal tape, 12 wide, 15 m roll"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic PTFE sealing tape (ETIM 10.0 EC010670), a thread-seal tape wound on a plastic spool; the "
            "tape's width, thickness and length on the roll and the spool are design choices, the roll's outside diameter calculated "
            "from them")
ORIGIN = "the centre of the roll's underside (z = 0) on its axis; the roll lies flat, its axis along +z, the tape's width along z"
COMMAND = "SEAL-TAPE-PTFE"
PARAMS = dict(width="12", length=15000.0)

WIDTHS = {"12": 12.0, "19": 19.0, "25": 25.0}   # design choices: the tape's width, mm (the trade's 1/2, 3/4 and 1 in widths, rounded)
THICK = 0.1                          # design choice: the tape's thickness before it is stretched onto the thread, mm
SPOOL_ID = 25.0                      # design choice: the spool's bore
SPOOL_WALL = 8.0                     # design choice: the spool's wall; >= 8 so every edge passes the AutoCAD fillet pre-flight
SPOOL_OD = SPOOL_ID + 2 * SPOOL_WALL # 41: the tape's first turn sits on it
WOUND_MIN = 8.0                      # design choice: the wound tape's radial wall is at least 8 (the fillet pre-flight, as the spool)
LENGTH_MIN, LENGTH_MAX = 15000.0, 50000.0   # design choices: the tape on one roll, 15 m (WOUND_MIN's floor, asserted) to 50 m
OD_MAX = 100.0                       # design choice: the largest roll built
MAT_TAPE = "M-WHITE-PVC"             # class value: PTFE, white (the closest material on file to its look)
MAT_SPOOL = "M-BROWN"                # design choice: the spool's colour (a plastic spool, no material claimed)

for _w in WIDTHS.values():
    assert _w >= 8.0                 # the roll's height is the tape's width: >= 8 for the fillet pre-flight (envelope edges)


def outside_d(length=15000.0):
    """the roll's outside diameter: the wound tape's end area length x thickness fills the annulus from the spool's OD,
    pi / 4 x (D^2 - SPOOL_OD^2) = length x thickness (59.92 for 15 m of 0.1 tape); the width does not enter it"""
    return math.sqrt(SPOOL_OD ** 2 + 4.0 * float(length) * THICK / math.pi)


assert (outside_d(LENGTH_MIN) - SPOOL_OD) / 2.0 >= WOUND_MIN   # the shortest roll still has 8 of wound tape (9.46 at 15 m)
assert outside_d(LENGTH_MAX) <= OD_MAX                         # the longest roll fits the largest built (89.71 at 50 m)


def build(width="12", length=15000.0):
    width = str(width)
    if width not in WIDTHS: raise ValueError(f"width {width}: one of {', '.join(WIDTHS)} (mm)")
    length = float(length)
    if not LENGTH_MIN <= length <= LENGTH_MAX: raise ValueError(f"length {length:g}: {LENGTH_MIN:g} to {LENGTH_MAX:g} mm")
    w = WIDTHS[width]; od = outside_d(length)
    P = Prims()
    roll = P.cyl(MAT_TAPE, (0, 0, 0), (0, 0, w), od / 2.0)                               # the wound tape
    P.hole(MAT_TAPE, (0, 0, -1.0), (0, 0, w + 1.0), SPOOL_OD / 2.0, roll)               # its bore, on the spool
    spool = P.cyl(MAT_SPOOL, (0, 0, 0), (0, 0, w), SPOOL_OD / 2.0)                       # the spool, face to face in the bore
    P.hole(MAT_SPOOL, (0, 0, -1.0), (0, 0, w + 1.0), SPOOL_ID / 2.0, spool)             # the spool's bore
    r = od / 2.0
    P.collider("env", -r, -r, 0, 2 * r, 2 * r, w)
    return P


PREVIEWS = [dict(name="three-quarter, 12 wide, 15 m", az=250, el=35), dict(name="side", az=200, el=5),
            dict(name="19 wide, 30 m", az=250, el=35, params=dict(width="19", length=30000.0)),
            dict(name="25 wide, 50 m", az=250, el=35, params=dict(width="25", length=50000.0))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
