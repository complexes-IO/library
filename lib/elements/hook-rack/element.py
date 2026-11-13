#!/usr/bin/env python3
"""hook-rack: a hanging rack for powder coating parts, our own design (OPERATING.md 12, own designs; inventory row own_design
"yes": "hanging rack for powder coating parts"; lib/machines-factory.txt line 69, powder-coating-system, places it with booth-powder,
oven-cure and conveyor-overhead). A vertical spine bar with a hang eye at its top, four cross-bars along it, and on each cross-bar
four L-shaped pins out of each face (an arm straight out, a tip turned up), so a part with a hole hangs on a pin and can't slide
off. It hangs from the overhead conveyor's hook by the eye; conveyor-overhead is not built, so how the eye fits its hook is checked
when that element is on file. One fixed body, no node. Every size is a design choice. No load rating, no earthing or safety claim.
No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "hook-rack", "1.0", "furniture"
TITLE = "hanging rack for powder coating, spine 1530 with a Ø18 hang eye, four cross-bars 800 wide, 32 L-pins Ø8"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; every size a design choice; no load rating, "
            "no earthing or safety claim; no vendor file opened")
ORIGIN = ("the hang point: the centre of the hang eye x = 0, y = 0, z = 0; the rack hangs toward -z; the cross-bars run along x; "
          "the pins stand out toward -y and +y")
COMMAND = "HOOKRACK"
PARAMS = dict()
SPINE_W, SPINE_T = 50.0, 20.0                     # spine bar 50 (x) by 20 (y): design choice
SPINE_TOP, SPINE_BOT = 30.0, -1500.0              # spine from z 30 (21 of bar above the eye) down to z -1500: design choice
EYE_D = 18.0                                      # hang eye Ø18 through the spine along y at z 0: design choice
BAR_L, BAR_H = 400.0, 40.0                        # cross-bars reach x +-400, 40 deep, as thick as the spine (20): design choice
LEVELS = (-350.0, -700.0, -1050.0, -1400.0)       # the cross-bars' centre heights: design choice
PIN_X = (-300.0, -100.0, 100.0, 300.0)            # four pins out of each face of each cross-bar, 200 apart: design choice
PIN_R = 4.0                                       # pins Ø8 rod: design choice
PIN_IN = 2.0                                      # each arm starts 2 inside the bar's face (one body, no gap)
PIN_OUT = 50.0                                    # the tip's axis 50 out from the bar's face (axis y +-60, the tip's outside +-64): design choice
TIP_UP = 20.0                                     # the tip stands 20 above the arm's axis: design choice

def build():
    P = Prims(); S = "M-SILVER"
    w2, t2 = SPINE_W / 2, SPINE_T / 2
    spine = P.box(S, -w2, -t2, SPINE_BOT, SPINE_W, SPINE_T, SPINE_TOP - SPINE_BOT)          # spine, x +-25, y +-10
    P.hole(S, (0, -t2 - 1, 0), (0, t2 + 1, 0), EYE_D / 2, spine)                            # hang eye Ø18 along y
    for zc in LEVELS:
        for sx in (-1, 1):
            x0 = w2 if sx > 0 else -BAR_L
            P.box(S, x0, -t2, zc - BAR_H / 2, BAR_L - w2, SPINE_T, BAR_H)                   # cross-bar half, its inner end abutting the spine
        for sy in (-1, 1):
            y_in = sy * (t2 - PIN_IN); y_tip = sy * (t2 + PIN_OUT)
            for x in PIN_X:
                P.cyl(S, (x, y_in, zc), (x, y_tip, zc), PIN_R)                              # arm, straight out of the bar's face
                P.cyl(S, (x, y_tip, zc - PIN_R), (x, y_tip, zc + TIP_UP), PIN_R)            # tip, turned up; the arm ends on its axis
    P.collider("spine", -w2, -t2, SPINE_BOT, SPINE_W, SPINE_T, SPINE_TOP - SPINE_BOT)
    reach = t2 + PIN_OUT + PIN_R
    for i, zc in enumerate(LEVELS, 1):
        P.collider(f"bar-{i}", -BAR_L, -reach, zc - BAR_H / 2, 2 * BAR_L, 2 * reach, BAR_H)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
