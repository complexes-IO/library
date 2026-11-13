#!/usr/bin/env python3
"""cable-tray: perforated sheet-steel cable tray, one straight length, flanged sides, 300 wide x 100 high. Our own design (EM r4
rule): every size is a design choice. What it meets: M6 splice screws (clearance Ø6.6, ISO 273 medium H13, lib/standards/holes.csv).
The folder's acquisition record (metadata.json, references/source.txt) describes a catalogue wire-basket tray; this element is not
built from it. No load rating."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "cable-tray", "1.0", "furniture"
TITLE = "perforated cable tray 300 x 100, flanged sides, cut to length"
TOOLKIT = "1.3"
BASELINE = "our own design (EM r4 rule, 2026-11-05): no product matched; every size a design choice; mates M6 splice screws, clearance ISO 273"
ORIGIN = "run start x = 0, tray centre line y = 0, underside of the bottom z = 0; the run along +x, open side up (+z)"
COMMAND = "CTRAY"
PARAMS = dict(length=3000.0)
W, H, T = 300.0, 100.0, 1.5          # outside width, outside height, sheet: design choices
LIP = 20.0                           # inward return flange at the top of each side, from the outer face: design choice
SLOT_L, SLOT_W = 50.0, 10.0          # bottom slots (along x, across y): design choice
SLOT_PITCH = 100.0                   # slot rows along the run: design choice
SLOT_Y = (-90.0, 0.0, 90.0)          # slot centres across the bottom: design choice
SPLICE_X = (25.0, 75.0)              # splice holes from each end, both sides: design choice
SPLICE_Z = 50.0                      # splice-hole height above the underside: design choice, mid-side
SPLICE_D = 6.6                       # M6 clearance, ISO 273 medium (H13), lib/standards/holes.csv
MAT = "M-GALV"

def build(length=3000.0):
    P = Prims(); L = float(length)
    b = P.box(MAT, 0, -W / 2, 0, L, W, T)                                               # bottom
    rows = int((L - SLOT_PITCH) // SLOT_PITCH) + 1 if L >= SLOT_PITCH else 0
    x0 = (L - (rows - 1) * SLOT_PITCH) / 2 if rows else 0.0                             # rows centred on the length
    for k in range(rows):
        cx = x0 + k * SLOT_PITCH
        for cy in SLOT_Y:
            P.cutbox(MAT, cx - SLOT_L / 2, cy - SLOT_W / 2, -1.0, SLOT_L, SLOT_W, T + 2.0, b)
    for y0, yn in ((-W / 2, -1.0), (W / 2 - T, 1.0)):                                   # sides, outer face at y = -W/2 and +W/2
        s = P.box(MAT, 0, y0, T, L, T, H - 2 * T)
        ly = -W / 2 if yn < 0 else W / 2 - LIP
        P.box(MAT, 0, ly, H - T, L, LIP, T)                                               # top return flange, inward
        for x in [*SPLICE_X, *(L - v for v in SPLICE_X)]:
            P.hole(MAT, (x, y0 - 1.0, SPLICE_Z), (x, y0 + T + 1.0, SPLICE_Z), SPLICE_D / 2, s)
    P.collider("body", 0, -W / 2, 0, L, W, H)
    return P

PREVIEWS = [dict(name="three-quarter 3000", az=230, el=30), dict(name="end and splice holes", az=200, el=20, center=(0, 0, 50), height=200)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
