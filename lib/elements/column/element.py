#!/usr/bin/env python3
"""column: machine column, our own design (OPERATING.md 12, own designs; inventory row own_design "yes"). A box-section column
400 x 400, 1600 high, on a 600 x 600 x 25 base flange with eight M12 holes, ISO 273 medium (lib/standards/holes.csv), and two
flat machined ways on its front face (node `ways`, fixed: the head, knee or saddle a BOM puts on the column is placed on the ways'
front plane and moves on its own nodes). The body is drawn by its outside: a cast or welded box section is closed at its ends
and its cores are not seen. Ribs, cores, scraping of the ways, the counterweight and its chain are not drawn. Every size is a
design choice. No load rating, no accuracy claim."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "column", "1.1", "furniture"
TITLE = "machine column 400 x 400 x 1600 on a 600 x 600 base flange, two flat front ways 60 wide, 8 x M12"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; base flange holes M12 in ISO 273 medium; "
            "every size a design choice; no load rating, no accuracy claim")
ORIGIN = ("the base flange's underside z = 0 at the column's centre x = 0, y = 0; the column's height along z; front (the ways) "
          "toward -y; the ways' front plane (the head's seat) at y = -225")
COMMAND = "MCOLUMN"
PARAMS = dict()
FL_W, FL_T = 600.0, 25.0                # base flange 600 x 600 x 25 (100 each side of the body): design choice
BODY_W, BODY_TOP = 400.0, 1600.0        # box body 400 x 400, its top face 1600 above the flange's underside: design choice
WAY_W, WAY_D = 60.0, 25.0               # flat ways 60 wide, 25 proud of the body's front face: design choice
WAY_X = 130.0                           # way centres at x +-130 (260 apart): design choice
WAY_Z0, WAY_Z1 = 400.0, 1560.0          # the ways run from z 400 to z 1560 (40 short of the top): design choice
BOLT_D = 13.5                           # M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv)
BOLT_C = 250.0                          # bolt centres on a 500 x 500 square, corners and mid-sides (mid-flange): design choice

def build():
    P = Prims(); S = "M-STEEL-7035"; W = "M-SILVER"                  # the ways: bare machined steel, the library's bright-metal layer
    fl = P.box(S, -FL_W / 2, -FL_W / 2, 0, FL_W, FL_W, FL_T)                                    # base flange
    for x in (-BOLT_C, 0.0, BOLT_C):
        for y in (-BOLT_C, 0.0, BOLT_C):
            if x == 0.0 and y == 0.0:
                continue                                                                        # the centre is under the body
            P.hole(S, (x, y, -1), (x, y, FL_T + 1), BOLT_D / 2, fl)                             # M12 base bolt
    P.box(S, -BODY_W / 2, -BODY_W / 2, FL_T, BODY_W, BODY_W, BODY_TOP - FL_T)                   # box body
    for sx in (-1, 1):                                                                          # the two flat ways
        P.box(f"node:ways|{W}", sx * WAY_X - WAY_W / 2, -BODY_W / 2 - WAY_D, WAY_Z0, WAY_W, WAY_D, WAY_Z1 - WAY_Z0)
    P.pivot("ways", "fixed", (0, -BODY_W / 2 - WAY_D, (WAY_Z0 + WAY_Z1) / 2), axis=(0, -1, 0))
    P.collider("base", -FL_W / 2, -FL_W / 2, 0, FL_W, FL_W, FL_T)
    P.collider("body", -BODY_W / 2, -BODY_W / 2, FL_T, BODY_W, BODY_W, BODY_TOP - FL_T)
    P.collider("ways", -WAY_X - WAY_W / 2, -BODY_W / 2 - WAY_D, WAY_Z0, 2 * WAY_X + WAY_W, WAY_D, WAY_Z1 - WAY_Z0)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="front", az=270, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
