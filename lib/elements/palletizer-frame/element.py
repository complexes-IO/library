#!/usr/bin/env python3
"""palletizer-frame: the frame of a robot palletizing cell, our own design (OPERATING.md 12, own designs; inventory row
palletizer-frame, own_design "yes": "palletizer gantry frame around robot-arm (our own build)", the conveyor family, EM 2026-11-08).
Four posts on anchored foot plates carry a top frame over a floor area 2900 x 2300 between them: the robot's half at -x, where
the infeed conveyor comes in through the open -x end, and the pallet station at +x, where a pallet is set down against a back
stop and two side guides and leaves through the open +x end. Two floor ties along x join the foot plates and carry the stop and
the guides, so the frame is one body. The pallet's footprint is pallet 1.2's, read with library.load (an Assumption (B) there,
ISO 6780 not on file), so the stop and guides cannot drift from it.
Not drawn, placed in a later version once their elements are on file (OPERATING.md 12: a host doesn't model holes for a part it
places later): the robot (robot-arm is not built) and its pedestal, the infeed conveyor section (conveyor-seg), the guarding, the
light curtain or safety scanner at the open ends, and the controls. Every size is a design choice; the anchor holes ISO 273. No
load, reach, cycle or safety claim. No vendor file was opened (the folder's record says there is none)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "palletizer-frame", "1.1", "furniture"
TITLE = "robot palletizing cell frame, own design, four posts 3300 x 2700 x 2500 with a top frame, floor ties, pallet back stop and side guides sized to pallet 1.2, 16 x M12 anchor holes"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; anchor holes ISO 273 medium for M12; the pallet "
            "station's stop and guides from pallet 1.2's footprint (library.load; an Assumption (B) there, inherited); every other "
            "size a design choice; no load, reach, cycle or safety claim; the robot, its pedestal, the infeed conveyor, the guarding "
            "and the light curtains placed in a later version; no vendor file opened")
ORIGIN = ("the floor plane z = 0 at the centre of the cell between the four posts: x along the flow, from the infeed end (-x, the "
          "robot's half) to the pallet end (+x); y across it")
COMMAND = "PALLETIZERFRAME"
PARAMS = dict()
FILLET_R = 0.5                                   # the gate's radius, set per primitive below (P.radii): the furniture class's 1.0 reads short edges short (mech-r106)
PAL = library.load("pallet")                     # pallet 1.2: its footprint (one home for the figure)
PX, PY = PAL.LX, PAL.LY                          # 1219 along x, 1016 along y: Assumption (B) there (ISO 6780 not on file)
POST, POST_X, POST_Y = 100.0, 1500.0, 1200.0     # 4 posts 100 x 100 on centres x +-1500, y +-1200: design choice
FOOT, FOOT_T = 300.0, 20.0                       # foot plates 300 x 300 x 20 under each post: design choice
TOP_Z, TOP_H = 2400.0, 100.0                     # the posts' tops; the top frame 100 x 100 on them: design choice
TIE_W = 100.0                                    # 2 floor ties 100 wide x 20 along x, foot plate to foot plate, on the posts' line y +-1200: design choice
PCX = 700.0                                      # the pallet station's centre at x 700, y 0: design choice
GAP = 10.0                                       # the stop's and guides' faces 10 clear of the pallet's footprint: design choice
STOP_B, STOP_T, STOP_H = 80.0, 20.0, 100.0       # back stop: a floor bar 80 wide across the cell, an upright 20 x 100 at its face, 1200 long: design choice
STOP_L = 1200.0
GUIDE_L, GUIDE_T, GUIDE_H = 600.0, 20.0, 100.0   # side guides: floor plates 600 long from the pallet's side to the tie, uprights 20 x 100 at their inner edges: design choice
HOLE = 110.0                                     # 4 x M12 per foot plate at 220 x 220 about the post: design choice
M12_D = 13.5                                     # M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv)

def build():
    P = Prims(); S = "M-STEEL-7035"; Y = "M-YELLOW"
    for i, (sx, sy) in enumerate(((-1, -1), (1, -1), (1, 1), (-1, 1)), 1):
        cx, cy = sx * POST_X, sy * POST_Y
        fp = P.box(S, cx - FOOT / 2, cy - FOOT / 2, 0, FOOT, FOOT, FOOT_T)                             # foot plate on the floor
        for hx in (-1, 1):
            for hy in (-1, 1):
                P.hole(S, (cx + hx * HOLE, cy + hy * HOLE, -1), (cx + hx * HOLE, cy + hy * HOLE, FOOT_T + 1), M12_D / 2, fp)   # M12 anchor hole
        P.box(S, cx - POST / 2, cy - POST / 2, FOOT_T, POST, POST, TOP_Z - FOOT_T)                     # post, foot plate to the top frame
        P.collider(f"post-{i}", cx - POST / 2, cy - POST / 2, 0, POST, POST, TOP_Z)
    for sy in (-1, 1):                                                                                  # top frame: two beams along x over the posts...
        P.box(S, -POST_X - POST / 2, sy * POST_Y - POST / 2, TOP_Z, 2 * POST_X + POST, POST, TOP_H)
    for sx in (-1, 1):                                                                                  # ...and two along y between them
        P.box(S, sx * POST_X - POST / 2, -POST_Y + POST / 2, TOP_Z, POST, 2 * POST_Y - POST, TOP_H)
    P.collider("top", -POST_X - POST / 2, -POST_Y - POST / 2, TOP_Z, 2 * POST_X + POST, 2 * POST_Y + POST, TOP_H)
    xt = POST_X - FOOT / 2                        # 1350: the ties run between the foot plates' inner edges
    yt = POST_Y - TIE_W / 2                       # 1150: the ties' inner faces
    for i, sy in enumerate((-1, 1), 1):           # floor ties along x, on the posts' line
        P.box(S, -xt, yt if sy > 0 else -yt - TIE_W, 0, 2 * xt, TIE_W, FOOT_T)
        P.collider(f"tie-{i}", -xt, yt if sy > 0 else -yt - TIE_W, 0, 2 * xt, TIE_W, FOOT_T)
    xs = PCX - PX / 2 - GAP                       # 80.5: the back stop's face, 10 behind the pallet's -x end
    P.box(Y, xs - STOP_B, -yt, 0, STOP_B, 2 * yt, FOOT_T)                                               # back stop's floor bar, tie to tie
    P.box(Y, xs - STOP_T, -STOP_L / 2, FOOT_T, STOP_T, STOP_L, STOP_H)                                  # back stop's upright, at the bar's face
    P.collider("stop", xs - STOP_B, -yt, 0, STOP_B, 2 * yt, FOOT_T + STOP_H)
    yg = PY / 2 + GAP                             # 518: the side guides' faces, 10 beside the pallet's sides
    for i, sy in enumerate((-1, 1), 1):
        P.box(Y, PCX - GUIDE_L / 2, yg if sy > 0 else -yt, 0, GUIDE_L, yt - yg, FOOT_T)                 # guide's floor plate, the pallet's side to the tie
        P.box(Y, PCX - GUIDE_L / 2, yg if sy > 0 else -yg - GUIDE_T, FOOT_T, GUIDE_L, GUIDE_T, GUIDE_H) # guide's upright, at the plate's inner edge
        P.collider(f"guide-{i}", PCX - GUIDE_L / 2, yg if sy > 0 else -yt, 0, GUIDE_L, yt - yg, FOOT_T + GUIDE_H)
    for i in range(len(P)): P.radii[i] = FILLET_R                       # the gate reads each primitive's radius (fillet._radii), not FILLET_R (mech-r106)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=20), dict(name="front", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
