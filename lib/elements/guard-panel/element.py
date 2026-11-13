#!/usr/bin/env python3
"""guard-panel: fixed guard panel for a machine frame, our own design (OPERATING.md 12, own designs: guards; inventory row
own_design "yes"). A rectangular frame of 30 x 30 square tube with a plain 1.5 sheet infill (no openings), and four fixing lugs
welded to the frame's sides, flush with its back face, each with one M8 clearance hole, ISO 273 medium (lib/standards/holes.csv).
The panel bolts with its back face against the machine frame it guards. The tubes are drawn by their outside: every tube end is
welded shut against another tube, so no bore shows. The welds are not drawn. Every size is a design choice. Where the panel stands
relative to the hazard is the assembly's placement; the element makes no safety claim of its own."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "guard-panel", "1.0", "furniture"
TITLE = "fixed guard panel 1000 x 800, square tube 30 frame, plain sheet infill 1.5, 4 x M8 fixing lugs"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; fixing holes M8 in ISO 273 medium; every size a "
            "design choice; no safety claim")
ORIGIN = ("the mounting face y = 0 (the back faces of the frame and the lugs, against the machine frame); x = 0 at the panel's "
          "centre; z = 0 at its lower edge; the panel's front toward -y")
COMMAND = "GRDPNL"
PARAMS = dict()
W, H = 1000.0, 800.0                   # outside of the frame: design choice
FR = 30.0                              # frame: square tube 30 x 30, drawn by its outside: design choice
SHEET_T = 1.5                          # infill sheet, centred in the frame's depth: design choice
LUG_W, LUG_T, LUG_H = 40.0, 10.0, 50.0  # fixing lugs 40 out from the frame's side, 10 thick, 50 tall: design choice
LUG_Z = (100.0, 700.0)                 # lug centres above the lower edge: design choice
HOLE_D = 9.0                           # M8 clearance, ISO 273 medium H13 (lib/standards/holes.csv)

def build():
    P = Prims(); F = "M-YELLOW"; S = "M-STEEL-7035"
    x0 = W / 2                                                   # the frame's outer sides at x +-500
    for sx in (-1, 1):                                           # uprights, full height
        P.box(F, x0 - FR if sx > 0 else -x0, -FR, 0, FR, FR, H)
    for z in (0.0, H - FR):                                      # top and bottom rails, between the uprights
        P.box(F, -x0 + FR, -FR, z, W - 2 * FR, FR, FR)
    P.box(S, -x0 + FR, -FR / 2 - SHEET_T / 2, FR, W - 2 * FR, SHEET_T, H - 2 * FR)   # infill sheet, plain
    for sx in (-1, 1):
        lx = x0 if sx > 0 else -x0 - LUG_W                      # the lug's inner edge on the upright's outer face
        hx = sx * (x0 + LUG_W / 2)                               # hole centre x +-520
        for zc in LUG_Z:
            lug = P.box(F, lx, -LUG_T, zc - LUG_H / 2, LUG_W, LUG_T, LUG_H)
            P.hole(F, (hx, -LUG_T - 1, zc), (hx, 1, zc), HOLE_D / 2, lug)                  # M8 fixing hole
    P.collider("panel", -x0, -FR, 0, W, FR, H)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="back, the fixing lugs", az=40, el=15)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
