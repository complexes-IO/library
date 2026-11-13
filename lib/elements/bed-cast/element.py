#!/usr/bin/env python3
"""bed-cast: machine bed, our own design (OPERATING.md 12, own designs; inventory row own_design "yes"). A box-section bed
2000 long on a 25 base plate with six M12 floor-anchor holes, ISO 273 medium (lib/standards/holes.csv), and two flat machined
ways on its top face (node `ways`, fixed: the carriage, table or headstock a BOM puts on the bed is placed on the ways' top
plane). The body is drawn by its outside: a cast or welded box section is closed at its ends and its cores are not seen. Ribs,
cores and the scraping of the ways are not drawn. Every size is a design choice. No load rating, no accuracy claim."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "bed-cast", "1.0", "furniture"
TITLE = "machine bed 2000 x 660 x 430, box section, two flat ways 80 wide, 6 x M12 floor anchors"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; floor anchors M12 in ISO 273 medium holes; "
            "every size a design choice; no load rating, no accuracy claim")
ORIGIN = ("floor plane z = 0 at the bed's centre x = 0, y = 0; the bed's length along x; front toward -y; the ways' top plane "
          "(the carriage's seat) at z = 430")
COMMAND = "BEDCAST"
PARAMS = dict()
L = 2000.0                              # bed length: design choice
BASE_W, BASE_T = 660.0, 25.0            # base plate 2000 x 660 x 25 (the anchor flanges, 80 each side of the body): design choice
BODY_W, BODY_TOP = 500.0, 400.0         # box body 500 wide, its top face 400 above the floor: design choice
WAY_W, WAY_H = 80.0, 30.0               # flat ways 80 wide, 30 proud of the body's top: design choice
WAY_Y = 170.0                           # way centres at y +-170 (340 apart): design choice
WAY_END = 20.0                          # the ways stop 20 short of each end of the body: design choice
ANCHOR_D = 13.5                         # M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv)
ANCHOR_X = (-900.0, 0.0, 900.0)         # three anchors a side: design choice
ANCHOR_Y = 290.0                        # anchor centres at y +-290, mid-flange (40 from the body, 40 from the plate's edge)

def build():
    P = Prims(); S = "M-STEEL-7035"; W = "M-SILVER"                  # the ways: bare machined steel, the library's bright-metal layer
    base = P.box(S, -L / 2, -BASE_W / 2, 0, L, BASE_W, BASE_T)                                  # base plate, anchor flanges
    for sy in (-1, 1):
        for x in ANCHOR_X:
            P.hole(S, (x, sy * ANCHOR_Y, -1), (x, sy * ANCHOR_Y, BASE_T + 1), ANCHOR_D / 2, base)  # floor anchor M12
    P.box(S, -L / 2, -BODY_W / 2, BASE_T, L, BODY_W, BODY_TOP - BASE_T)                        # box body
    wl = L - 2 * WAY_END
    for sy in (-1, 1):                                                                          # the two flat ways
        P.box(f"node:ways|{W}", -wl / 2, sy * WAY_Y - WAY_W / 2, BODY_TOP, wl, WAY_W, WAY_H)
    P.pivot("ways", "fixed", (0, 0, BODY_TOP + WAY_H), axis=(0, 0, 1))
    P.collider("body", -L / 2, -BASE_W / 2, 0, L, BASE_W, BODY_TOP)
    P.collider("ways", -wl / 2, -WAY_Y - WAY_W / 2, BODY_TOP, wl, 2 * WAY_Y + WAY_W, WAY_H)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="end", az=270, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
