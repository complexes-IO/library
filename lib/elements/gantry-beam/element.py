#!/usr/bin/env python3
"""gantry-beam: gantry beam carrying the cutting head axis, our own design (OPERATING.md 12, own designs; inventory row
own_design "yes"). The cross beam of the fibre laser, sheet laser and CNC plasma cutters of lib/machines-factory.txt: a
box-section beam 2200 long, 200 deep and 300 high, on a saddle plate at each end (where the machine's side carriages carry it
along the bed), with two flat machined ways along its front face (node `ways`, fixed: the head carriage a BOM puts on the beam
is placed on the ways' front plane and moves along the beam on its own nodes). The body is drawn by its outside: a welded box
section is closed at its ends and its webs and ribs are not seen. Its 2200 length spans bed-slat's 1600 width with the saddles
outside it. Every size is a design choice. No load rating, no stiffness or accuracy claim."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "gantry-beam", "1.1", "furniture"
TITLE = "gantry beam 2200 x 200 x 300 on two end saddles 250 x 400 x 30, two flat front ways 40 high, 1600 long"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; no hole, thread or standard interface; every "
            "size a design choice; no load rating, no stiffness or accuracy claim")
ORIGIN = ("the saddles' underside z = 0 at the beam's centre x = 0, y = 0; the beam's length along x; front (the ways) toward "
          "-y; the ways' front plane (the head carriage's seat) at y = -115")
COMMAND = "GANTRYBEAM"
PARAMS = dict()
BEAM_L, BEAM_D, BEAM_H = 2200.0, 200.0, 300.0   # box beam 2200 long, 200 deep (y), 300 high: design choice
SAD_L, SAD_W, SAD_T = 250.0, 400.0, 30.0        # end saddles 250 along the beam, 400 across it, 30 thick, flush with the beam's ends: design choice
WAY_W, WAY_D = 40.0, 15.0                       # flat ways 40 high, 15 proud of the beam's front face: design choice
WAY_L = 1600.0                                  # the ways run x -800 to 800: design choice (the head's stroke depends on a carriage not on file)
WAY_Z = (80.0, 280.0)                           # way centres at z 80 and 280 (200 apart) on the beam's face z 30 to 330: design choice

def build():
    P = Prims(); S = "M-STEEL-7035"; W = "M-SILVER"                  # the ways: bare machined steel, the library's bright-metal layer
    hl = BEAM_L / 2
    for sx in (-1, 1):                                                                          # end saddles, flush with the beam's ends
        P.box(S, hl - SAD_L if sx > 0 else -hl, -SAD_W / 2, 0, SAD_L, SAD_W, SAD_T)
    P.box(S, -hl, -BEAM_D / 2, SAD_T, BEAM_L, BEAM_D, BEAM_H)                                  # box beam
    for zc in WAY_Z:                                                                            # the two flat ways
        P.box(f"node:ways|{W}", -WAY_L / 2, -BEAM_D / 2 - WAY_D, zc - WAY_W / 2, WAY_L, WAY_D, WAY_W)
    P.pivot("ways", "fixed", (0, -BEAM_D / 2 - WAY_D, sum(WAY_Z) / 2), axis=(0, -1, 0))
    for sx in (-1, 1):
        P.collider(f"saddle-{'b' if sx > 0 else 'a'}", hl - SAD_L if sx > 0 else -hl, -SAD_W / 2, 0, SAD_L, SAD_W, SAD_T)
    P.collider("beam", -hl, -BEAM_D / 2, SAD_T, BEAM_L, BEAM_D, BEAM_H)
    P.collider("ways", -WAY_L / 2, -BEAM_D / 2 - WAY_D, WAY_Z[0] - WAY_W / 2, WAY_L, WAY_D, WAY_Z[1] - WAY_Z[0] + WAY_W)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="front", az=270, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
