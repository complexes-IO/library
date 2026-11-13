#!/usr/bin/env python3
"""bed-slat: slat bed for thermal cutting, our own design (OPERATING.md 12, own designs; inventory row own_design "yes"). A
drop-in tray for the fibre laser, sheet laser and CNC plasma cutters of lib/machines-factory.txt: a welded frame 3100 x 1600 x
150 of flat-bar rails round a 3000 x 1500 opening (a 3000 x 1500 sheet), a support ledge inside each long rail, and 30
replaceable flat slats 2.5 thick and 100 high at a 100 pitch standing on the ledges (node `slats`, fixed: the sheet is placed on
the slats' top plane; a worn slat is lifted out and a new one dropped in). The slats' top edge is plain (no teeth). Every size is
a design choice. No load rating, no claim about the cutting process."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "bed-slat", "1.1", "furniture"
TITLE = "slat bed 3100 x 1600 x 200 for a 3000 x 1500 sheet, 30 replaceable flat slats 2.5 x 100 at a 100 pitch"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; no hole, thread or standard interface; every "
            "size a design choice; no load rating, no cutting-process claim")
ORIGIN = ("the frame's underside z = 0 at the bed's centre x = 0, y = 0; the bed's length along x; the slats run across it "
          "along y; the slats' top plane (the sheet's seat) at z = 200")
COMMAND = "BEDSLAT"
PARAMS = dict()
IN_X, IN_Y = 3000.0, 1500.0             # inner opening 3000 x 1500 (a 3000 x 1500 sheet): design choice
RAIL_T, RAIL_H = 50.0, 150.0            # frame rails 50 thick, 150 high: design choice
LEDGE_W, LEDGE_T = 40.0, 10.0           # support ledge 40 wide, 10 thick, inside each long rail: design choice
LEDGE_TOP = 100.0                       # the ledges' top (the slats' seat) 100 above the frame's underside: design choice
SLAT_T, SLAT_H = 2.5, 100.0             # slats 2.5 thick, 100 high: design choice
SLAT_N, SLAT_P = 30, 100.0              # 30 slats at a 100 pitch, the first and last 50 from the end rails: design choice
SLAT_GAP = 2.0                          # 2 clear between each slat end and the long rail's inner face (drop-in fit): design choice

def build():
    P = Prims(); S = "M-STEEL-7035"; W = "M-SILVER"                  # the slats: bare steel, the library's bright-metal layer
    ox, oy = IN_X / 2 + RAIL_T, IN_Y / 2 + RAIL_T                    # outer half-sizes 1550, 800
    for sy in (-1, 1):                                                                          # long rails, full length
        P.box(S, -ox, oy - RAIL_T if sy > 0 else -oy, 0, 2 * ox, RAIL_T, RAIL_H)
    for sx in (-1, 1):                                                                          # end rails, between the long rails
        P.box(S, IN_X / 2 if sx > 0 else -ox, -IN_Y / 2, 0, RAIL_T, IN_Y, RAIL_H)
    for sy in (-1, 1):                                                                          # support ledges on the long rails
        P.box(S, -IN_X / 2, IN_Y / 2 - LEDGE_W if sy > 0 else -IN_Y / 2, LEDGE_TOP - LEDGE_T, IN_X, LEDGE_W, LEDGE_T)
    sl = IN_Y - 2 * SLAT_GAP
    x0 = -(SLAT_N - 1) * SLAT_P / 2
    for i in range(SLAT_N):                                                                     # the slats
        x = x0 + i * SLAT_P
        P.box(f"node:slats|{W}", x - SLAT_T / 2, -sl / 2, LEDGE_TOP, SLAT_T, sl, SLAT_H)
    P.pivot("slats", "fixed", (0, 0, LEDGE_TOP + SLAT_H), axis=(0, 0, 1))
    for sy in (-1, 1):
        P.collider(f"rail-{'b' if sy > 0 else 'a'}", -ox, oy - RAIL_T if sy > 0 else -oy, 0, 2 * ox, RAIL_T, RAIL_H)
    for sx in (-1, 1):
        P.collider(f"end-{'b' if sx > 0 else 'a'}", IN_X / 2 if sx > 0 else -ox, -IN_Y / 2, 0, RAIL_T, IN_Y, RAIL_H)
    P.collider("slats", x0 - SLAT_T / 2, -sl / 2, LEDGE_TOP, (SLAT_N - 1) * SLAT_P + SLAT_T, sl, SLAT_H)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="end", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
