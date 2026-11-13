#!/usr/bin/env python3
"""shelving-steel: generic steel shelving bay, our own vendor-neutral design of the ETIM 10.0 class EC004064 (Shelf rack), built
unattended (OPERATING.md 12, generic elements; inventory row own_design "generic": "steel shelving"). One bay for boxed and loose
goods put in and taken out by hand (lib/machines-factory.txt line 121, racks-storage): four uprights at the corners of a
1000 x 500 footprint, 2000 high, five plain shelves 900 x 500 between them, and four anchor plates inside the footprint with one
M12 clearance hole each (ISO 273 medium). One fixed body, no node. The class values (spec.md, "Class values") are design inputs;
every size below is a design choice. No load rating, no safety claim. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "shelving-steel", "1.0", "furniture"
TITLE = "steel shelving bay, generic, 1000 x 500 x 2000, 5 shelves 900 x 500, 4 x M12 anchor holes"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic steel shelving bay (ETIM 10.0 EC004064); class values are design inputs (spec.md); anchor holes "
            "ISO 273 medium for M12; every size a design choice; no load rating, no safety claim; no vendor file opened")
ORIGIN = ("floor plane z = 0, the middle of the bay's width x = 0, the front uprights' front faces y = 0; the bay's depth toward "
          "+y, its back at y = 500; goods go in and out at the front, from -y")
COMMAND = "SHELVSTEEL"
PARAMS = dict()
W, D, H = 1000.0, 500.0, 2000.0                   # the bay over its uprights: width (x), depth (y), height: class values (design inputs)
UP = 50.0                                         # uprights 50 x 50, one at each corner of the footprint, floor to top: design choice
SH_T = 40.0                                       # shelves 40 deep (a folded panel's edge height, modelled solid): design choice
SH_TOPS = (150.0, 600.0, 1050.0, 1500.0, 1950.0)  # the shelves' top faces, five levels 450 apart: class value 5, heights a design choice
PL_W, PL_L, PL_T = 50.0, 100.0, 20.0              # anchor plates 50 (x, the upright's width) by 100 (y), 20 thick: design choice
M12_D = 13.5                                      # M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv)

def build():
    P = Prims(); S = "M-STEEL-7035"
    for sx, kx in ((-1, "l"), (1, "r")):
        x0 = -W / 2 if sx < 0 else W / 2 - UP                                                # the upright's low x
        for y0, ky in ((0.0, "f"), (D - UP, "b")):
            P.box(S, x0, y0, 0, UP, UP, H)                                                   # upright, floor to top
            P.collider(f"upright-{kx}{ky}", x0, y0, 0, UP, UP, H)
            py = UP if ky == "f" else D - UP - PL_L                                          # anchor plate, behind the front upright or
            pl = P.box(S, x0, py, 0, PL_W, PL_L, PL_T)                                       # in front of the rear one, inside the footprint
            cx, cy = x0 + PL_W / 2, py + PL_L / 2
            P.hole(S, (cx, cy, -1), (cx, cy, PL_T + 1), M12_D / 2, pl)                       # M12 anchor hole
            P.collider(f"anchor-{kx}{ky}", x0, py, 0, PL_W, PL_L, PL_T)
    for i, top in enumerate(SH_TOPS, 1):
        P.box(S, -W / 2 + UP, 0, top - SH_T, W - 2 * UP, D, SH_T)                            # shelf, between the uprights' inner faces
        P.collider(f"shelf-{i}", -W / 2 + UP, 0, top - SH_T, W - 2 * UP, D, SH_T)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="front", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
