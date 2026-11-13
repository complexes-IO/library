#!/usr/bin/env python3
"""pallet: four-way block pallet 1219 x 1016 x 144. Our own design (EM r4 rule). The footprint 1219 x 1016 is an Assumption (B)
(spec.md): the rack, conveyor and AMR dock meet it, and ISO 6780, the standard that fixes pallet footprints, is not on file
(lib/standards/sources.csv iso-6780 "to get"); lib/inventory.csv only names the size. Every other size is a design choice. No load
rating is claimed. 1.1 (review pallet-1.0 findings 1 and 2): the footprint and the fork fit marked open; the part unchanged.
1.2 (review pallet-1.1 finding 1): the one `deck` collider (z 104 to 144) split into three stringer colliders (z 104 to 124) and the
deck collider (z 124 to 144), so the twin's x-entry opening is the part's 106 above the bottom boards; the part unchanged."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "pallet", "1.2", "furniture"
TITLE = "four-way block pallet 1219 x 1016 x 144"
TOOLKIT = "1.3"
BASELINE = "our own design (EM r4 rule, 2026-11-05): footprint 1219 x 1016 an Assumption (ISO 6780 not on file); the rest are design choices"
ORIGIN = "floor corner: floor plane z = 0, the corner of the footprint at x = 0, y = 0; the 1219 length along +x, the 1016 width along +y"
COMMAND = "PALLET"
PARAMS = dict()
LX, LY = 1219.0, 1016.0          # footprint: Assumption (B), ISO 6780 not on file (spec.md); the size inventory.csv names
BOT, BLK, STR, DECK = 18.0, 86.0, 20.0, 20.0   # bottom boards, blocks, stringer boards, deck boards: design choices (144 overall)
B = 145.0                        # block footprint 145 x 145: design choice
DECK_N, DECK_W = 7, 120.0        # deck boards along y, across the stringers: design choice (gaps 63.2)
BOT_W = 145.0                    # bottom boards along y under each block column

def _at(n, size, span):
    """n positions of a part `size` wide spread from 0 to span (first at 0, last flush with the far edge)"""
    return [i * (span - size) / (n - 1) for i in range(n)]

def build():
    P = Prims()
    xs, ys = _at(3, B, LX), _at(3, B, LY)
    for x in xs:
        P.box("M-BROWN", x, 0, 0, BOT_W, LY, BOT)                                     # bottom boards (along y, under each block column)
        P.collider(f"base-{int(x)}", x, 0, 0, BOT_W, LY, BOT)
        for y in ys:
            P.box("M-BROWN", x, y, BOT, B, B, BLK)                                    # blocks
            P.collider(f"block-{int(x)}-{int(y)}", x, y, BOT, B, B, BLK)
    for y in ys:
        P.box("M-BROWN", 0, y, BOT + BLK, LX, B, STR)                                 # stringer boards (along x, over each block row)
        P.collider(f"stringer-{int(y)}", 0, y, BOT + BLK, LX, B, STR)                # 1.2: one collider per stringer board, so the
    for x in _at(DECK_N, DECK_W, LX):                                                 # twin's x-entry opening is the part's (106)
        P.box("M-BROWN", x, 0, BOT + BLK + STR, DECK_W, LY, DECK)                     # deck boards (along y, across the stringer boards)
    P.collider("deck", 0, 0, BOT + BLK + STR, LX, LY, DECK)                           # 1.2: the deck boards only, z 124 to 144
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="fork entry, x end", az=270, el=8)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
